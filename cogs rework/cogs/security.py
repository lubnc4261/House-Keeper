import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions, BadArgument, MissingRequiredArgument, CommandInvokeError


class securityCog(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    @commands.command()
    async def security(self, ctx):
        embed = discord.Embed(
            title="prefix before every command",
            color = discord.Color.red()
        )
        embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
        embed.add_field(name=":red_square: `block <@mention>`", value="Blocks a user send permission for the chanenl", inline=True)
        embed.add_field(name=":green_square: `unblock <@mention>`", value="Unblock the User from all consequenses", inline=True)
        embed.add_field(name=":bookmark_tabs: `denylinks <channel_id>`", value="If a links gets send, it gets deleted", inline=True)
        embed.add_field(name=":incoming_envelope: `allowlinks <channel_id>`", value="Allow links back again", inline=True)
        embed.set_footer(text="Server Security from the House Keeper Bot")

        await ctx.send(embed=embed)


    @commands.command()
    @commands.has_permissions(manage_roles=True, manage_channels=True, administrator=True)
    async def block(self, ctx, member: discord.Member):
        perms = ctx.channel.overwrites_for(member)
        try:
            await ctx.channel.set_permissions(member, read_messages=True,
                                                    send_messages=False)

            embed = discord.Embed(
                title="Successfully",
                color = discord.Color.green()
            )
            embed.add_field(name=":white_check_mark:", value=f"Successfully blocked {member.name} send permission")

            await ctx.send(embed = embed)

        except Exception:
            embed = discord.Embed(
                title="Block Error",
                color = discord.Color.red()
            )
            embed.add_field(name=":question:", value=f"Something went wrong with user {member.name}")

            await ctx.send(embed=embed)

    @block.error
    async def block_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            embed = discord.Embed(
            title="Command Error",
            color = discord.Color.red()
            )

            embed.add_field(name=":thinking:", value="You miss the manage roles or manage channels permission")

            await ctx.send(embed = embed)


    @commands.command()
    @commands.has_permissions(manage_roles=True, manage_channels=True, administrator=True)
    async def unblock(self, ctx, member: discord.Member):
        perms = ctx.channel.overwrites_for(member)
        try:
            await ctx.channel.set_permissions(member, read_messages=True,
                                                    send_messages=True)

            embed = discord.Embed(
            title="Successfully",
            color = discord.Color.green()
            )
            embed.add_field(name=":white_check_mark:", value=f"Successfully unblocked {member.name} ")

            await ctx.send(embed = embed)
    
        except Exception:
            embed = discord.Embed(
            title="Block Error",
            color = discord.Color.red()
            )
            embed.add_field(name=":question:", value=f"Something went wrong with unblocking user {member.name}")

            await ctx.send(embed=embed)


    @unblock.error
    async def unblock_error(self, ctx, error):
        if isinstance(error, MissingPermissions):

            embed = discord.Embed(
            title="Command Error",
            color = discord.Color.red()
            )

            embed.add_field(name=":thinking:", value="You miss the manage roles or manage channels permission")

            await ctx.send(embed = embed)


    @commands.command()
    @commands.has_permissions(manage_guild=True, administrator=True, manage_channels=True)
    async def denylinks(self, ctx, id):
        try:

            if id in open ("idstuff/links/deny.py").read():
                await ctx.send("Links are already blocked")

            else:

                f = open("idstuff/links/deny.py", "a")
                f.write("\n"+id)
                await ctx.send("Added " +id+ " to the List")
                f.close

        except MissingRequiredArgument:
            await ctx.send("Specify the Channel ID")

    @commands.command()
    @commands.has_permissions(manage_guild=True, administrator=True, manage_channels=True)
    async def allowlinks(self, ctx, id):
        if id not in open ("idstuff/links/deny.py").read():
            await ctx.send("Links are already allowed")

        if id in open ("idstuff/links/deny.py").read():
            a_file = open("idstuff/links/deny.py", "r")
            lines = a_file.readlines()
            a_file.close()

            new_file = open("idstuff/links/deny.py", "w")
            for line in lines:
                if line.strip("\n") != id:

                    new_file.write(line)

            new_file.close

            await ctx.send("Links are now allowed")



def setup(bot):
    bot.add_cog(securityCog(bot))