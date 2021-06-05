import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions, BadArgument, MissingRequiredArgument, CommandInvokeError, has_permissions
import json
import os
import sys

class randomshitCog(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    @commands.command()
    async def juan(self, ctx):
        await ctx.send(file=discord.File('Images/juan.png'))

    @commands.command()
    async def sus(self, ctx):
        await ctx.send(file=discord.File('Images/sus.jpg'))





def setup(bot):
    bot.add_cog(randomshitCog(bot))