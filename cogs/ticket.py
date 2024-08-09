import discord
from discord.ext import commands
from discord import app_commands
import json
import os
import io

TICKET_FILE = 'tickets.json'

def load_ticket_data():
    if os.path.exists(TICKET_FILE):
        with open(TICKET_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_ticket_data(data):
    with open(TICKET_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# loading everything is not a good way to handle it

ticket_data = load_ticket_data()

class TicketUI(discord.ui.View):
    def __init__(self, client):
        super().__init__(timeout=None)
        self.client = client

    @discord.ui.button(label="Create ticket",custom_id="mainpannel", style=discord.ButtonStyle.secondary, emoji="📩")
    async def mainpannel(self, interaction: discord.Interaction, button: discord.ui.Button):
        user_id = str(interaction.user.id)
        guild_id = str(interaction.guild.id)

        if guild_id in ticket_data and user_id in ticket_data[guild_id]:
            channel_id = ticket_data[guild_id][user_id]
            channel = self.client.get_channel(int(channel_id))
            if channel:
                await interaction.response.send_message(f"{interaction.user.mention} You already have a ticket open: {channel.mention}", ephemeral=True)
                return

        category = discord.utils.get(interaction.guild.categories, name="Tickets")
        if not category:
            await interaction.response.send_message("Ticket category not found.", ephemeral=True)
            return

        overwrites = {
            interaction.user: discord.PermissionOverwrite(
                view_channel=True,
                send_messages=True,
                attach_files=True,
                embed_links=True,
                external_emojis=True,
                external_stickers=True,
                read_message_history=True
            ),
            interaction.guild.default_role: discord.PermissionOverwrite(
                view_channel=False,
                send_messages=False,
                read_message_history=False
            )
        }
        channel = await interaction.guild.create_text_channel(
            name=f"Ticket-{interaction.user.id}",
            category=category,
            overwrites=overwrites
        )

        if guild_id not in ticket_data:
            ticket_data[guild_id] = {}
        ticket_data[guild_id][user_id] = str(channel.id)
        save_ticket_data(ticket_data)

        embed = discord.Embed(
            color=interaction.user.color,
        )
        embed.add_field(name="", value="Support will be here shortly.\nTo close this ticket react with :lock:")


        await channel.send(f"{interaction.user.mention}, your ticket has been created.", view=TicketManger(self.client), embed=embed)


        await interaction.response.send_message(f"Ticket created: {channel.mention}", ephemeral=True)

class TicketManger(discord.ui.View):
    def __init__(self, client):
        super().__init__(timeout=None)
        self.client = client
    
    async def create_ticket_transcript(self, channel):
        messages = [message async for message in channel.history(limit=1000)]
        transcript_content = "\n".join([f"{msg.author}: {msg.content}" for msg in messages])

        transcript_file = discord.File(io.StringIO(transcript_content), filename=f"{channel.name}_transcript.txt")
        return transcript_file



    @discord.ui.button(label="Close Ticket", custom_id="closeticket", style=discord.ButtonStyle.secondary, emoji="🔒")
    async def close_ticket_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        log_channel = discord.utils.get(guild.text_channels, name="ticketlog")

        if not log_channel:
            await interaction.response.send_message("Ticket log channel (`#ticketlog`) does not exist.", ephemeral=True)
            return

        transcript = await self.create_ticket_transcript(interaction.channel)
        
        if transcript:
            await log_channel.send(f"Transcript for {interaction.channel.name}:", file=transcript)
            await interaction.response.send_message("Ticket closed and transcript sent to the log channel.", ephemeral=True)
        else:
            await interaction.response.send_message("Failed to generate transcript.", ephemeral=True)

        await interaction.channel.delete()

class ticketCog(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    @app_commands.command(name="ticket_pannel", description="Ticket creation Terminal")
    @app_commands.guild_only()
    @app_commands.default_permissions(manage_channels=True)
    async def ticket_pannel(self, interaction: discord.Interaction, headline: str):
        embed = discord.Embed(
            title=headline,
            color=discord.Color.green(),
            description="To create a ticket react with :envelope_with_arrow:"
        )
        await interaction.response.send_message(embed=embed, view=TicketUI(self.client))
        await interaction.channel.set_permissions(
            interaction.guild.default_role,
            send_messages=False,
            read_messages=True,
            add_reactions=False,
            embed_links=False,
            attach_files=False,
            read_message_history=True,
            external_emojis=False,
            manage_messages=False
        )


    #We have to remove it from the tickets.json
    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        guild_id = str(channel.guild.id)
        for user_id, chan_id in ticket_data.get(guild_id, {}).items():
            if chan_id == str(channel.id):
                del ticket_data[guild_id][user_id]
                save_ticket_data(ticket_data)
                break


    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_channels=True)
    async def close(self, ctx):
        channel = ctx.channel
        guild_id = str(channel.guild.id)
        for user_id, chan_id in ticket_data.get(guild_id, {}).items():
            if chan_id == str(channel.id):
                await channel.delete()
                del ticket_data[guild_id][user_id]
                save_ticket_data(ticket_data)
                await ctx.send(f"Ticket closed and channel {channel.name} deleted.")
                break
    
    @commands.command()
    @commands.guild_only()
    async def ticket(self, ctx):
        embed = discord.Embed(
            title="prefix before every command",
            color = discord.Color.magenta()
        )
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/443208943213477889/601699371221909504/imagesfidosfhdis.jpg?width=598&height=585")
        embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
        embed.add_field(name=":ticket:`/ticket_pannel <name>`", value="Set a channel for creating tickets", inline=True)
        embed.add_field(name=":card_box:`close`", value="Force close the ticket", inline=True)
        embed.set_footer(text="Help Box for the House Keeper Bot")

        await ctx.send(embed = embed)





async def setup(bot):
    await bot.add_cog(ticketCog(bot))
