import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions, BadArgument, MissingRequiredArgument, CommandInvokeError, CommandOnCooldown
from random import choice
import random
import aiohttp
import io
import json

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
        embed.add_field(name=":computer: `youtube <search>`", value="Search something on youtube", inline=True)
        embed.add_field(name="🔁 `reverse <text>`", value="Reverse the message", inline=True)
        embed.add_field(name=":8ball: `rate <thing>`", value="Gives you a rate", inline=True)
        embed.add_field(name=":coin: `coinflip`", value="Flip a coin", inline=True)
        embed.add_field(name=":skull: `f`", value="Pay respect", inline=True)
        embed.add_field(name=":cat: `meow`", value="Get random cat image", inline=True)
        embed.add_field(name=":dog: `dog`", value="Random dog quote / image", inline=True)
        embed.add_field(name=":duck: `duck`", value="Cute ducks !", inline=True)
        embed.add_field(name=":fox: `fox`", value="Fox pictures !", inline=True)
        embed.set_footer(text="Help Box for the House Keeper Bot")

        await ctx.send(embed=embed)
    
    
    @commands.command(aliases=['8ball'])
    @commands.guild_only()
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
    @commands.guild_only()
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



    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def meow(self, ctx):

        embed = discord.Embed(
                        title=":cat: cat !",
                        color = discord.Color.purple()
                    )

        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.thecatapi.com/v1/images/search") as r:
                data = await r.json()
                url = data[0]['url']

        embed.set_image(url=url)
        embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
        embed.set_footer(text=f"cat requested by {ctx.message.author}")

        await ctx.send(embed=embed)


    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def dog(self, ctx):
        embed = discord.Embed(
                        title=":dog: dog !",
                        color = discord.Color.purple()
                    )

        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.thedogapi.com/v1/images/search") as r:
                data = await r.json()
                url = data[0]['url']

        embed.set_image(url=url)
        embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
        embed.set_footer(text=f"dog requested by {ctx.message.author}")

        await ctx.send(embed=embed)


    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def duck(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get("https://random-d.uk/api/v2/random")
            duck = await request.json()

        embed = discord.Embed(
            title=":duck: duck !",
            color=discord.Color.purple()
        )
        embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
        embed.set_footer(text=f"duck requested by {ctx.message.author}")
        embed.set_image(url=duck["url"])

        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def fox(self, ctx):
        embed = discord.Embed(
                        title=":fox: fox !",
                        color = discord.Color.purple()
                    )

        async with aiohttp.ClientSession() as session:
            async with session.get("https://randomfox.ca/floof/") as r:
                data = await r.json()
                url = data['image']

        embed.set_image(url=url)
        embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
        embed.set_footer(text=f"fox requested by {ctx.message.author}")

        await ctx.send(embed=embed)

       
    @commands.command(aliases=["flip", "coin"])
    async def coinflip(self, ctx):
        results = ["Heads", "Tails"]
        await ctx.send(f"**{ctx.author.name}** flipped a coin and got **{random.choice(results)}**!")


    @commands.command()
    async def f(self, ctx, *, text: commands.clean_content = None):
        """ Press F to pay respect """
        hearts = ["❤", "💛", "💚", "💙", "💜"]
        reason = f"for **{text}** " if text else ""
        await ctx.send(f"**{ctx.author.name}** has paid their respect {reason}{random.choice(hearts)}")

    @commands.command()
    async def reverse(self, ctx, *, text: str):
        """ !poow ,ffuts esreveR
        Everything you type after reverse will of course, be reversed
        """
        t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
        await ctx.send(f"🔁 {t_rev}")


        
    @commands.command()
    async def rate(self, ctx, *, thing: commands.clean_content):
        rate_amount = random.uniform(0.0, 100.0)
        await ctx.send(f"I would give `{thing}` a **{round(rate_amount, 4)}** out of  **100**")


    




async def setup(bot):
    await bot.add_cog(funCog(bot))
