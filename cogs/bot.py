import discord
from discord.ext import commands
import platform
import psutil

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
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/443208943213477889/601699371221909504/imagesfidosfhdis.jpg?width=598&height=585")
        embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
        embed.add_field(name=":round_pushpin:`ping`", value="Shows Bot and Discord Ping", inline=True)
        embed.add_field(name=":card_box:`botinvite`", value="Invite link for the Bot", inline=True)
        embed.add_field(name=":health_worker: `status`", value="Technical data", inline=True)
        embed.add_field(name=":office_worker: `about`", value="Shows the Bot credits", inline=True)
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
        embed.add_field(name="Libraries", value="**discord.py v2**", inline=True)
        embed.add_field(name="Programmed by", value="`dauersteven`", inline=True)
        embed.add_field(name="Contact", value="For questions etc. DM the Programmer", inline=True)
        embed.add_field(name="Source code", value="https://github.com/lubnc4261/House-Keeper", inline=True)
        embed.add_field(name="Tip", value="Keep Parameters in 'quotes' to avoid errors", inline=True)
        embed.add_field(name="Log events", value="Name a channel **hk-logging** for logs", inline=True)
        embed.set_footer(text="Infobox for the House Keeper bot")

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
        await pong.edit(content=f':ping_pong: Pong! ({delta} ms)\nDiscord WebSocket Latecy: {round(self.client.latency, 5)} ms')


    



async def setup(bot):
    await bot.add_cog(botCog(bot))
