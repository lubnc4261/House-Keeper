import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions, BadArgument, MissingRequiredArgument, CommandInvokeError
import platform
import inspect
import os
import datetime
import psutil
import json


def get_prefix(bot, message):
    if not message.guild:
        return commands.when_mentioned_or("<")(bot, message)

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    if str(message.guild.id) not in prefixes:
        return commands.when_mentioned_or("<")(bot, message)

    prefix = prefixes[str(message.guild.id)]
    return commands.when_mentioned_or(prefix)(bot, message)

client = commands.Bot(command_prefix=get_prefix)

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


svmem = psutil.virtual_memory()

totalram = get_size(svmem.total)
ramusage = get_size(svmem.used)




class botCog(commands.Cog):
    def __init__(self, bot):
        self.client = bot


    @commands.command()
    async def bot(self, ctx):
        embed = discord.Embed(
            title="prefix before every command",
            color = discord.Color.magenta()
        )

        embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
        embed.add_field(name=":floppy_disk: `info`", value="Shows Bot related informations", inline=True)
        embed.add_field(name=":key: `permission`", value="Will list a permission overview", inline=True)
        embed.add_field(name=":round_pushpin:`ping`", value="Shows Bot and Discord Ping", inline=True)
        embed.add_field(name=":card_box:`botinvite`", value="Invite link for the Bot", inline=True)
        embed.add_field(name=":health_worker: `status`", value="Technical data", inline=True)
        embed.set_footer(text="Help Box for the House Keeper Bot")

        await ctx.send(embed = embed)


    @commands.command()
    async def status(self, ctx):


        uname = platform.system()

        rel = platform.release()

        embed = discord.Embed(
            title="Status",
            color = discord.Color.magenta()
        )       

        embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
        embed.add_field(name="**Python Version**", value=platform.python_version(), inline=True)
        embed.add_field(name="**Platform**", value=uname, inline=True)
        embed.add_field(name="**Release**", value=rel, inline=True)
        embed.add_field(name="**Ram**", value=str(ramusage) + "/" + str(totalram), inline=True)
        
        await ctx.send(embed=embed)
        



    @commands.command()
    async def about(self, ctx):

        embed = discord.Embed(
            title="Infos about the bot",
            color = discord.Color.magenta()
        )

        embed.set_author(name="House Keeper Info", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
        embed.add_field(name="Bot ID", value="735221653998534688", inline=True)
        embed.add_field(name="Bot created at", value="21.7.2020 at 21:48:22", inline=True)
        embed.add_field(name="Language", value="Python", inline=True)
        embed.add_field(name="Libraries", value="**discord.py rewrite** use `modules` for list", inline=True)
        embed.add_field(name="Programmed from", value="`Militär Staubsauger#0668`", inline=True)
        embed.add_field(name="Contact", value="For questions etc. DM the Programmer", inline=True)
        embed.add_field(name="Source code", value="https://github.com/lubnc4261/House-Keeper", inline=True)
        embed.add_field(name="Tip", value="Keep Parameters in 'quotes' to avoid errors", inline=True)
        embed.add_field(name="Log events", value="Name a channel **hk-logging** for logs", inline=True)
        embed.set_footer(text="Infobox for the House Keeper bot")

        await ctx.send(embed=embed)

    @commands.command()
    async def modules(self, ctx):

        embed = discord.Embed(
            title="List of **all** modules used",
            description="This also includes preinstalled",
            color = discord.Color.gold()
        )

        embed.add_field(name="Modules: ", value="discord-py-slash-command==1.2.0, discord.py==1.7.1, psutil==5.8.0, PyNaCl==1.4.0, youtube-dl==2021.5.16, aiohttp==3.7.4.post0, async-timeout==3.0.1, asyncpg==0.23.0, Pillow==8.2.0, platform, os, sys, json, datetime, time, inspect, random, asyncio, collections, urllib, functools, math, itertools, textwrap", inline=False)


        await ctx.send(embed=embed)


    @commands.command()
    async def botinvite(self, ctx):
        await ctx.send("Invite link for the bot \nhttps://discord.com/api/oauth2/authorize?client_id=735221653998534688&permissions=4260883703&scope=bot%20applications.commands")



    @commands.command()          
    async def botplatform(self, ctx):
        try:
            await ctx.send("The bot is currently running on: ```" + str(platform.platform()) + "```")
        except Exception as e:
            await ctx.send(e)

    

    @commands.command()
    async def ping(self, ctx):
        ping = ctx.message
        pong = await ctx.send('**:ping_pong:** Pong!')
        delta = pong.created_at - ping.created_at
        delta = int(delta.total_seconds() * 1000)
        await pong.edit(content=f':ping_pong: Pong! ({delta} ms)\nDiscord WebSocket Latenz: {round(self.client.latency, 5)} ms')

    @commands.command()
    async def permissions(self, ctx):
        permissions = ctx.channel.permissions_for(ctx.me)

        embed = discord.Embed(title=':customs:  Permissions', color=0x3498db)
        embed.add_field(name='Server', value=ctx.guild)
        embed.add_field(name='Channel', value=ctx.channel, inline=False)

        for item, valueBool in permissions:
            if valueBool == True:
                value = ':white_check_mark:'
            else:
                value = ':x:'
            embed.add_field(name=item, value=value)

        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)


    



def setup(bot):
    bot.add_cog(botCog(bot))
