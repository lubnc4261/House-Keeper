import discord
import json
import os
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

from discord_slash import SlashCommand
from discord_slash import SlashCommandOptionType
from discord_slash.utils import manage_commands

##############################################

def get_prefix(bot, message):
    if not message.guild:
        return commands.when_mentioned_or("<")(bot, message)

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    if str(message.guild.id) not in prefixes:
        return commands.when_mentioned_or("<")(bot, message)

    prefix = prefixes[str(message.guild.id)]
    return commands.when_mentioned_or(prefix)(bot, message)

bot = commands.Bot(command_prefix=get_prefix)




slash = SlashCommand(bot, sync_commands=True)
#############################################
#
# This took me a lot fo nerves to create, since its a new feature :kekw:
#
############################################


class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="ban", description="Bans the given user from the guild")
    async def _removeuser(self, ctx: SlashContext, member: discord.Member, *, reason=None):
        try:
            if ctx.author.guild_permissions.ban_members == True:

                if reason == None:

                    await member.ban(reason=reason)

                    embed = discord.Embed(
                        title="User got banned",
                        color = discord.Color.green()
                    )
                    embed.add_field(name=":green_square:", value=f"User {member} got banned")
                    embed.add_field(name="Reason", value="No reason set")
                
                    await ctx.send(embed=embed)

                else:
                    await member.ban(reason=reason)

                    embed = discord.Embed(
                        title="User got banned",
                        color = discord.Color.green()
                    )
                    embed.add_field(name=":green_square:", value=f"User {member} got banned")
                    embed.add_field(name="Reason", value=reason)

                    await ctx.send(embed=embed)
            
            else:
                await ctx.send("You don't have the ban memeber permission")

        except discord.Forbidden:
            await ctx.channel.send(f"Bot doesn't have enough permission to ban someone. Upgrade the Permissions")

    
    @cog_ext.cog_slash(name="lock", description="locks a channel for the default server role (manage channels permission for you needed)", options=[manage_commands.create_option("channel", "The channel you want to lock.", SlashCommandOptionType.CHANNEL, True), manage_commands.create_option("reason", "the reason for locking the channel", SlashCommandOptionType.STRING, True)])
    async def _lock(self, ctx, channel, reason=None):
        try:

            if ctx.author.guild_permissions.manage_channels == True:

                if reason == None:

                    await ctx.channel.set_permissions(
                    ctx.guild.default_role, send_messages=False)
                    embed = discord.Embed(title=":warning: Channel has been locked!",description="Moderation action")
                    embed.add_field(
                    name=(f"{ctx.author} has locked this channel!"),
                    value=(f"{reason}"))
                    await ctx.send(embeds=[embed])

                else:
                    await ctx.channel.set_permissions(
                    ctx.guild.default_role, send_messages=False)
                    embed = discord.Embed(title=":warning: Channel has been locked!",description="Moderation action")
                    embed.add_field(
                    name=(f"{ctx.author} has locked this channel!"),
                    value=("-"))
                    await ctx.send(embeds=[embed])

            else:
                await ctx.send("You aren't an administrator!")

        except discord.Forbidden:
            await ctx.channel.send("Bot doesn't have enough permissions to lock the channel. Upgrade the Permissions")


    @cog_ext.cog_slash(name="unlock", description="unlocks the channel back again (manage channels permission for you needed)", options=[manage_commands.create_option("channel", "The channel you want to unlock.", SlashCommandOptionType.CHANNEL, True), manage_commands.create_option("reason", "the reason for unlocking the channel", SlashCommandOptionType.STRING, True)])
    async def _unlock(self, ctx, channel, reason):
        try:

            if ctx.author.guild_permissions.manage_channels == True:
                await ctx.channel.set_permissions(
                ctx.guild.default_role, send_messages=True)
                embed = discord.Embed(title=":white_check_mark: Channel has been unlocked!",description="Moderation action")
                embed.add_field(
                name=(f"{ctx.author} has unlocked this channel!"),
                value=(f"{reason}"))
                await ctx.send(embeds=[embed])
            else:
                await ctx.send("You aren't an administrator!")

        except discord.Forbidden:
            await ctx.channel.send("Bot doesn't have enough permissions to unlock the channel. Upgrade the Permissions")


    @cog_ext.cog_slash(name="nick", description="nick the given user (manage nicknames permission for you needed", options=[manage_commands.create_option("user", "The user you want to nick.", SlashCommandOptionType.USER, True), manage_commands.create_option("nick", "now the new nick for the user", SlashCommandOptionType.STRING, True)])
    async def _nick(self, ctx, member:discord.Member, nick):
        try:

            if ctx.author.guild_permissions.manage_nicknames == True:
                await member.edit(nick=nick)

                embed = discord.Embed(
                    title="User got nicked",
                    color=discord.Color.green()
                )

                embed.add_field(name=":green_square:", value=f"Nickname got changed to {member.mention}")
                await ctx.send(embed=embed)

            else:
                await ctx.send("You miss the manage nicknames Permissio")

        
        except discord.Forbidden:
            await ctx.send("Bot doesn't have enough permissions to nick the member. Upgrade the Permissions")


        await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="prefix", description="Change the prefix if you forgott it (administrator permissions are needed)", options=[manage_commands.create_option("prefix", "The new prefix", SlashCommandOptionType.STRING, True)])
    async def _prefix(self, ctx: SlashCommand, pre):

        if ctx.author.guild_permissions.administrator == True:

        
            with open ("prefixes.json", "r") as f:
                prefixes = json.load(f)

            prefixes[str(ctx.guild.id)] = pre
            await ctx.send(f"New prefix is `{pre}`")

            with open ("prefixes.json", "w") as f:
                json.dump(prefixes, f, indent=4)

        else:
            await ctx.send("You miss the administrator permission")



def setup(bot):
    bot.add_cog(Slash(bot))