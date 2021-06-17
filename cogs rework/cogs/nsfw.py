import discord
import json
import random, requests, aiohttp
from discord.ext import commands

# this part is not really needed

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

class nsfwCog(commands.Cog):
    def __init__(self, bot):
        self.client = bot


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.NSFWChannelRequired):
            await ctx.send("https://i.imgur.com/oe4iK5i.gif")  #stolen from dank memer heheheh

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send("command on 3 sec cooldown")

    # you can add try: except: to every command but it isnt really needed


    @commands.command()
    async def neko(self, ctx):

        embed = discord.Embed(
            title="Neko commands (hentai)",
            description="Channel has to be NSFW",
            color = discord.Color.purple()
        )
        embed.add_field(name="**Info**:", value="Commands have a 3 sec cooldown", inline=False)
        embed.add_field(name="NSFW Commands", value="``feet``, ``anal``, ``lewd``, ``pussy``, ``kiss``, ``blowjob``, ``boobs``, ``feed``, ``cum``, ``holo``, ``spank``, ``poke``, ``cuddle``, ``classic``, ``les``, ``ero``, ``smallboobs``, ``kuni``, ``tits``", inline=True)


        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_nsfw()
    @commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
    async def feet(self, ctx):
        async with aiohttp.ClientSession() as session:
            randomfoot = ["feet", "feetg"]
            async with session.get(f"https://nekos.life/api/v2/img/{random.choice(randomfoot)}")as r:
                if r.status == 200:

                    js = await r.json()

                    embed = discord.Embed(
                        title="feets",
                        color = discord.Color.purple()
                        )

                    embed.set_image(url=js["url"])

                    await ctx.send(embed=embed)

                else:
                    await ctx.send("API seems to have issues")

    @commands.command()
    @commands.is_nsfw()
    @commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
    async def anal(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://nekos.life/api/v2/img/anal")as r:
                if r.status == 200:

                    js = await r.json()

                    embed = discord.Embed(
                        title="anal",
                        color = discord.Color.purple()
                        )

                    embed.set_image(url=js["url"])

                    await ctx.send(embed=embed)

                else:
                    await ctx.send("API seems to have issues")

    @commands.command()
    @commands.is_nsfw()
    @commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
    async def lewd(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://nekos.life/api/v2/img/lewd")as r:
                if r.status == 200:

                    js = await r.json()

                    embed = discord.Embed(
                        title="lewd",
                        color = discord.Color.purple()
                        )

                    embed.set_image(url=js["url"])

                    await ctx.send(embed=embed)

                else:
                    await ctx.send("API seems to have issues")

    @commands.command()
    @commands.is_nsfw()
    @commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
    async def pussy(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://nekos.life/api/v2/img/pussy")as r:
                if r.status == 200:

                    js = await r.json()

                    embed = discord.Embed(
                        title="pussy",
                        color = discord.Color.purple()
                        )

                    embed.set_image(url=js["url"])

                    await ctx.send(embed=embed)

                else:
                    await ctx.send("API seems to have issues")

    @commands.command()
    @commands.is_nsfw()
    @commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
    async def kiss(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://nekos.life/api/v2/img/kiss")as r:
                if r.status == 200:

                    js = await r.json()

                    embed = discord.Embed(
                        title="kissing",
                        color = discord.Color.purple()
                        )

                    embed.set_image(url=js["url"])

                    await ctx.send(embed=embed)

                else:
                    await ctx.send("API seems to have issues")

    @commands.command()
    @commands.is_nsfw()
    @commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
    async def blowjob(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://nekos.life/api/v2/img/blowjob")as r:
                if r.status == 200:

                    js = await r.json()

                    embed = discord.Embed(
                        title="blowjob",
                        color = discord.Color.purple()
                        )

                    embed.set_image(url=js["url"])

                    await ctx.send(embed=embed)

                else:
                    await ctx.send("API seems to have issues")

    @commands.command()
    @commands.is_nsfw()
    @commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
    async def boobs(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://nekos.life/api/v2/img/boobs")as r:
                if r.status == 200:

                    js = await r.json()

                    embed = discord.Embed(
                        title="boobs",
                        color = discord.Color.purple()
                        )

                    embed.set_image(url=js["url"])

                    await ctx.send(embed=embed)

                else:
                    await ctx.send("API seems to have issues")

    @commands.command()
    @commands.is_nsfw()
    @commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
    async def feed(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://nekos.life/api/v2/img/feed")as r:
                if r.status == 200:

                    js = await r.json()

                    embed = discord.Embed(
                        title="feed",
                        color = discord.Color.purple()
                        )

                    embed.set_image(url=js["url"])

                    await ctx.send(embed=embed)

                else:
                    await ctx.send("API seems to have issues")

    @commands.command()
    @commands.is_nsfw()
    @commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
    async def cum(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://nekos.life/api/v2/img/cum")as r:
                if r.status == 200:

                    js = await r.json()

                    embed = discord.Embed(
                        title="cum",
                        color = discord.Color.purple()
                        )

                    embed.set_image(url=js["url"])

                    await ctx.send(embed=embed)

                else:
                    await ctx.send("API seems to have issues")

    @commands.command()
    @commands.is_nsfw()
    @commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
    async def holo(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://nekos.life/api/v2/img/holo")as r:
                if r.status == 200:

                    js = await r.json()

                    embed = discord.Embed(
                        title="holo",
                        color = discord.Color.purple()
                        )

                    embed.set_image(url=js["url"])

                    await ctx.send(embed=embed)

                else:
                    await ctx.send("API seems to have issues")

    @commands.command()
    @commands.is_nsfw()
    @commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
    async def spank(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://nekos.life/api/v2/img/spank")as r:
                if r.status == 200:

                    js = await r.json()

                    embed = discord.Embed(
                        title="spanking",
                        color = discord.Color.purple()
                        )

                    embed.set_image(url=js["url"])

                    await ctx.send(embed=embed)

                else:
                    await ctx.send("API seems to have issues")

    @commands.command()
    @commands.is_nsfw()
    @commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
    async def poke(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://nekos.life/api/v2/img/poke")as r:
                if r.status == 200:

                    js = await r.json()

                    embed = discord.Embed(
                        title="poke",
                        color = discord.Color.purple()
                        )

                    embed.set_image(url=js["url"])

                    await ctx.send(embed=embed)

                else:
                    await ctx.send("API seems to have issues")

    @commands.command()
    @commands.is_nsfw()
    @commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
    async def cuddle(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://nekos.life/api/v2/img/cuddle")as r:
                if r.status == 200:

                    js = await r.json()

                    embed = discord.Embed(
                        title="cuddle",
                        color = discord.Color.purple()
                        )

                    embed.set_image(url=js["url"])

                    await ctx.send(embed=embed)

                else:
                    await ctx.send("API seems to have issues")


    @commands.command()
    @commands.is_nsfw()
    @commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
    async def classic(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://nekos.life/api/v2/img/classic")as r:
                if r.status == 200:

                    js = await r.json()

                    embed = discord.Embed(
                        title="classic",
                        color = discord.Color.purple()
                        )

                    embed.set_image(url=js["url"])

                    await ctx.send(embed=embed)

                else:
                    await ctx.send("API seems to have issues")

    @commands.command()
    @commands.is_nsfw()
    @commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
    async def les(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://nekos.life/api/v2/img/les")as r:
                if r.status == 200:

                    js = await r.json()

                    embed = discord.Embed(
                        title="les",
                        color = discord.Color.purple()
                        )

                    embed.set_image(url=js["url"])

                    await ctx.send(embed=embed)

                else:
                    await ctx.send("API seems to have issues")

    @commands.command()
    @commands.is_nsfw()
    @commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
    async def ero(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://nekos.life/api/v2/img/ero")as r:
                if r.status == 200:

                    js = await r.json()

                    embed = discord.Embed(
                        title="ero",
                        color = discord.Color.purple()
                        )

                    embed.set_image(url=js["url"])

                    await ctx.send(embed=embed)

                else:
                    await ctx.send("API seems to have issues")

    @commands.command()
    @commands.is_nsfw()
    @commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
    async def smallboobs(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://nekos.life/api/v2/img/smallboobs")as r:
                if r.status == 200:

                    js = await r.json()

                    embed = discord.Embed(
                        title="small boobs",
                        color = discord.Color.purple()
                        )

                    embed.set_image(url=js["url"])

                    await ctx.send(embed=embed)

                else:
                    await ctx.send("API seems to have issues")

    @commands.command()
    @commands.is_nsfw()
    @commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
    async def kuni(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://nekos.life/api/v2/img/kuni")as r:
                if r.status == 200:

                    js = await r.json()

                    embed = discord.Embed(
                        title="kuni",
                        color = discord.Color.purple()
                        )

                    embed.set_image(url=js["url"])

                    await ctx.send(embed=embed)

                else:
                    await ctx.send("API seems to have issues")

    @commands.command()
    @commands.is_nsfw()
    @commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
    async def tits(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://nekos.life/api/v2/img/tits")as r:
                if r.status == 200:

                    js = await r.json()

                    embed = discord.Embed(
                        title="tits",
                        color = discord.Color.purple()
                        )

                    embed.set_image(url=js["url"])

                    await ctx.send(embed=embed)

                else:
                    await ctx.send("API seems to have issues")

def setup(bot):
    bot.add_cog(nsfwCog(bot))