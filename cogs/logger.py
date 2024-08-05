from discord.ext import commands
import discord
from discord.ext.commands import MissingPermissions, BadArgument, MissingRequiredArgument, CommandInvokeError, CommandOnCooldown
import os


class loggerCog(commands.Cog):
    def __init__(self, bot):
        self.client = bot


        # HELP IN MANAGEMENT


    @commands.command(aliases=['archive'])
    @commands.guild_only()
    @commands.cooldown(1, 20, commands.cooldowns.BucketType.channel)
    @commands.has_permissions(manage_messages=True)
    async def log(self, ctx, *limit: int):
        if not limit:
            limit = 20
        else:
            limit = limit[0]
        logFile = f'{ctx.channel}.log'
        counter = 0
        with open(logFile, 'w', encoding='UTF-8') as f:
            f.write(f'Archived messages from: {ctx.channel} at {ctx.message.created_at.strftime("%d.%m.%Y %H:%M:%S")}\n')
            async for message in ctx.channel.history(limit=limit, before=ctx.message):
                try:
                    attachment = '[Attached Data: {}]'.format(message.attachments[0].url)
                except IndexError:
                    attachment = ''
                f.write('{} {!s:20s}: {} {}\r\n'.format(message.created_at.strftime('%d.%m.%Y %H:%M:%S'), message.author, message.clean_content, attachment))
                counter += 1
        msg = f':ok: {counter} Message got archived!'
        f = discord.File(logFile)
        await ctx.send(file=f, content=msg)
        os.remove(logFile)

    @log.error
    async def log_error(self, error, ctx):
        if isinstance(error, commands.errors.CommandOnCooldown):
            seconds = str(error)[34:]
            await ctx.send(f':alarm_clock: Cooldown! Try in {seconds} again')

        if isinstance(error, MissingPermissions):
            cross = '❌'
            await ctx.message.add_reaction(cross)
            
    @commands.command()
    @commands.cooldown(1, 15, commands.cooldowns.BucketType.channel)
    @commands.has_permissions(manage_messages=True)
    async def savemembers(self, ctx):
        safeFile = f"{ctx.guild} users.log"
        with open(safeFile,'w', encoding="UTF-8") as f:
            async for member in ctx.guild.fetch_members(limit=None):
                print("{},{}".format(member,member.id), file=f)
        msg = f":ok: Users got archived"
        f = discord.File(safeFile)
        await ctx.send(file = f, content=msg)
        os.remove(safeFile)

    @savemembers.error
    async def savemembers_error(self, error, ctx):
        if isinstance(error, commands.errors.CommandOnCooldown):
            seconds = str(error)[34:]
            await ctx.send(f':alarm_clock: Cooldown! Try in {seconds} again')

        if isinstance(error, commands.MissingPermissions):
            cross = '❌'
            await ctx.message.add_reaction(cross)





async def setup(bot):
    await bot.add_cog(loggerCog(bot))
