import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions, BadArgument, MissingRequiredArgument, CommandInvokeError, CommandOnCooldown
from random import choice
import random
import aiohttp
import io

class funCog(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    @commands.command()
    async def fun(self, ctx):
        embed = discord.Embed(
            title="prefix before every command",
            color = discord.Color.magenta()
        )

        embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
        embed.add_field(name=":8ball: `8ball <question>`", value="Random answer generator", inline=True)
        embed.add_field(name=":drop_of_blood: `kill <@mention>`", value="'Kills' a random user", inline=True)
        embed.add_field(name=":love_letter: `hug <@mention>`", value="'hugs' a user", inline=True)
        embed.add_field(name=":cat: `horny <@mention>`", value="Give someone a horny id", inline=True)
        embed.add_field(name=":angry: `triggered <@mention>`", value="Triggered overlay on user", inline=True)
        embed.add_field(name=":computer: `youtube <search>`", value="Search something on youtube", inline=True)
        embed.add_field(name=":rewind: `say <text>`", value="Bot say's <text>", inline=True)
        embed.add_field(name="<:dank_meme:848973798526812212>`dankmeme`", value="Random Reddit Dank Meme", inline=True)
        embed.add_field(name="<:meme:848973488185933844>`meme`", value="Response with a meme", inline=True)
        embed.add_field(name=":cat: `meow`", value="Get random cat image", inline=True)
        embed.add_field(name=":dog: `dog`", value="Random dog quote / image", inline=True)
        embed.add_field(name=":duck: `duck`", value="Cute ducks !", inline=True)
        embed.add_field(name=":panda_face: `panda`", value="Pandas! uwu", inline=True)
        embed.add_field(name=":fox: `fox`", value="Fox pictures !", inline=True)
        embed.set_footer(text="Help Box for the House Keeper Bot")

        await ctx.send(embed=embed)
    
    
    @commands.command(aliases=['8ball', 'rate'])
    async def _8ball(self, ctx, *, question):
        responses = ["Yes",
                    "sure",
                    "obviously",
                    "dont annoy me with this shit",
                    "leave me alone",
                    "go away from me",
                    "no",
                    'yeah']
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


    
    @commands.command()
    async def kill(self, ctx, member):
        embed = discord.Embed(
            title="Whoops !",
            color=discord.Color.dark_red()
        )

        embed.add_field(name=":drop_of_blood:", value=f' {member} got killed')

        await ctx.send(embed=embed)


    @commands.command()
    async def hug(self, ctx, *, something):
        async with aiohttp.ClientSession() as session:
            request = await session.get("https://some-random-api.ml/animu/hug")
            hug = await request.json()

        embed = discord.Embed(
            colour=discord.Colour.dark_purple(),
            description=f'{ctx.message.author.mention} hugs {something} :smiling_face_with_3_hearts: !'
        )
        embed.set_image(url=hug["link"])

        await ctx.send(embed=embed)

    @commands.command()
    async def youtube(self, ctx, *, search):
        try:
            from urllib import parse, request
            import re

        except ModuleNotFoundError as e:
            print(e)

        try:


            query_string = parse.urlencode({'search_query': search})
            html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
            search_results = re.findall( r"watch\?v=(\S{11})", html_content.read().decode())
            await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

        except Exception as e:
            await ctx.send(e)

    @hug.error
    async def hug_error(self, ctx, error):
        if isinstance(error, BadArgument):
            embed = discord.Embed(
                title="Command Error",
                color=discord.Color.red()
            )

            embed.add_field(name=":thinking:", value="Who do you want to share love with ?")

            await ctx.send(embed=embed)

    
    @commands.command()
    async def say(self, ctx, *, something):
        embed = discord.Embed(
            color=discord.Color.purple(),
            description=f"{ctx.message.author.mention} says: **{something}**"
        )

        await ctx.send(embed=embed)


    
    @commands.command()
    async def dankmeme(self, ctx):
        embed = discord.Embed(title="meme", description="Yes memes")
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)


    @commands.command()
    async def meow(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get('http://aws.random.cat/meow') as r:
                if r.status == 200:
                    js = await r.json()
                    #await ctx.send(js['file'])
                    embed = discord.Embed(
                        title="Kitties!",
                        color = discord.Color.purple()
                    )

                    embed.set_image(url=js["file"])

                    await ctx.send(embed=embed)

                else:
                    embed = discord.Embed(
                        title="API Error",
                        color=discord.Color.red()
                    )

                    embed.add_field(name=":red_square:", value="API seems to be down")
                    
                    await ctx.send(embed=embed)

    @commands.command()
    async def dog(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get("https://some-random-api.ml/img/dog")
            dogjson = await request.json()

            request2 = await session.get("https://some-random-api.ml/facts/dog")
            factjson = await request2.json()

        embed = discord.Embed(
            title="Doggo!",
            color=discord.Color.purple()
        )
        embed.set_image(url=dogjson["link"])
        embed.set_footer(text=factjson["fact"])

        await ctx.send(embed=embed)

    @commands.command()
    async def duck(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get("https://random-d.uk/api/v1/random")
            duck = await request.json()

        embed = discord.Embed(
            title="Duck!",
            color=discord.Color.purple()
        )

        embed.set_image(url=duck["url"])

        await ctx.send(embed=embed)

    @commands.command()
    async def panda(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get("https://some-random-api.ml/img/panda")
            dogjson = await request.json()

            request2 = await session.get("https://some-random-api.ml/facts/panda")
            factjson = await request2.json()

        embed = discord.Embed(
            title="Panda!",
            color=discord.Color.purple()
        )
        embed.set_image(url=dogjson["link"])
        embed.set_footer(text=factjson["fact"])

        await ctx.send(embed=embed)

    @commands.command()
    async def meme(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get("https://some-random-api.ml/meme")
            requestjson= await request.json()

        embed = discord.Embed(
            title="memes",
            color=discord.Color.magenta()
        )
        embed.set_author(name=requestjson["category"])
        embed.set_image(url=requestjson["image"])
        embed.set_footer(text=requestjson["caption"])

        await ctx.send(embed=embed)

    @commands.command()
    async def fox(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get("https://some-random-api.ml/img/fox")
            foxjson = await request.json()

            request2 = await session.get("https://some-random-api.ml/facts/fox")
            factjson = await request2.json()

        embed = discord.Embed(
            title="Fox!",
            color=discord.Color.purple()
        )
        embed.set_image(url=foxjson["link"])
        embed.set_footer(text=factjson["fact"])

        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def triggered(self, ctx, member: discord.Member=None):
        if not member: # if no member is mentioned
            member = ctx.author # the user who ran the command will be the member
        
        async with aiohttp.ClientSession() as wastedSession:
            async with wastedSession.get(f'https://some-random-api.ml/canvas/triggered?avatar={member.avatar_url_as(format="png", size=1024)}') as wastedImage: # get users avatar as png with 1024 size
                imageData = io.BytesIO(await wastedImage.read()) # read the image/bytes
            
                await wastedSession.close() # closing the session and;
            
                await ctx.reply(file=discord.File(imageData, 'triggered.gif'))


    @triggered.error
    async def triggered_error(self, ctx, error):
        if isinstance(error, CommandOnCooldown):

            embed = discord.Embed(
                title="Not so fast",
                color = discord.Color.red()
            )

            embed.add_field(name=":clock1:", value="This command got a 5 second cooldown")
            embed.set_footer(text="Due API limitations")

            await ctx.send(embed=embed)



    @commands.command()
    async def horny(self, ctx, member: discord.Member = None):
        '''Horny license just for u'''
        member = member or ctx.author
        await ctx.trigger_typing()
        async with aiohttp.ClientSession() as session:
         async with session.get(
            f'https://some-random-api.ml/canvas/horny?avatar={member.avatar_url_as(format="png")}'
        ) as af:
            if 300 > af.status >= 200:
                fp = io.BytesIO(await af.read())
                file = discord.File(fp, "horny.png")
                em = discord.Embed(
                    title="bonk",
                    color=0xf1f1f1,
                )
                em.set_image(url="attachment://horny.png")
                await ctx.send(embed=em, file=file)
            else:
                await ctx.send('No horny :(')
            await session.close()


    




def setup(bot):
    bot.add_cog(funCog(bot))