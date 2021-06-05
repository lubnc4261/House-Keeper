import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions, BadArgument, MissingRequiredArgument, CommandInvokeError, CommandOnCooldown
import urllib.request
import aiohttp
from datetime import datetime
import os
from collections import Counter


class utilitiesCog(commands.Cog):
    def __init__(self, bot):
        self.client = bot


    @commands.command()
    async def utilities(self, ctx):
        embed = discord.Embed(
            title="Every command needs the prefix before",
            color = discord.Color.magenta()
        )

        embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
        embed.add_field(name=":ticket: `userinfo <@mention>`", value="Shows user related information", inline=True)
        embed.add_field(name=":no_mouth: `avatar <@mention>`", value="Profile Picture of the User in PNG", inline=True)
        embed.add_field(name=":book: `serverinfo`", value="Shows Server related information", inline=True)
        embed.add_field(name=":dividers: `hierarchy`", value="Shows Hierarchy system", inline=True)
        embed.add_field(name=":orange_book: `chknsfw`", value="Checks if channel is nsfw", inline=True)
        embed.add_field(name=":tickets: `myid`", value="Shows own discord ID", inline=True)
        embed.add_field(name=":abacus: `poll <question> <option1> <option2>`", value="Create a basic poll", inline=True)
        embed.add_field(name=":memo: `ip <query>`", value="Perform an ip lookup", inline=True)
        embed.add_field(name=":page_with_curl:`lyrics <query>`", value="Search the lyrics for a song", inline=True)
        embed.add_field(name=":clipboard: `games`", value="See what games are played on this server", inline=True)
        embed.add_field(name=":label: `emoji <onlyname>`", value="Emoji as png **ONLY** the name **NO** :abc", inline=True)
        embed.add_field(name=":clock11: `timer <time> <task>`", value="Set a Timer that reminds you", inline=True)
        embed.set_footer(text="Help Box fot the House Keeper Bot")
        await ctx.send(embed = embed)


    @commands.command()
    async def userinfo(self, ctx, member: discord.Member = None):
        try:

            member = ctx.author if not member else member
            roles = [role for role in member.roles]

            embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

            embed.set_author(name=f"User Info for {member}")
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(text=f"Requested from {ctx.author}")

            embed.add_field(name="ID", value=member.id)
            embed.add_field(name="Server name:", value=member.display_name)

            embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
            embed.add_field(name="Joined at", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

            embed.add_field(name=F"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
            embed.add_field(name="Best Role:", value=member.top_role.mention)

            embed.add_field(name="Bot ?", value=member.bot)

            await ctx.send(embed=embed)

        except discord.errors.HTTPException:

            member = ctx.author if not member else member
            roles = [role for role in member.roles]

            embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

            embed.set_author(name=f"User Info for {member}")
            embed.set_thumbnail(url=member.avatar_url)
            #embed.set_footer(text=f"Requested from {ctx.author}")

            embed.add_field(name="ID", value=member.id)
            #embed.add_field(name="Server name:", value=member.display_name)

            embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
            embed.add_field(name="Joined at", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

            #embed.add_field(name=F"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
            embed.add_field(name="Best Role:", value=member.top_role.mention)

            embed.add_field(name="Bot ?", value=member.bot)
            embed.add_field(name=":red_square:", value="Cannot send more Informations due too much context")

            await ctx.send(embed=embed)



    
    @commands.command()
    async def avatar(self, ctx, member: discord.Member):
        await ctx.send('{}'. format(member.avatar_url))


    

    @commands.command()
    async def serverinfo(self, ctx):

        guild = ctx.message.guild

        role_count = len(ctx.guild.roles)
        list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]

        text = len(guild.text_channels)
        voice = len(guild.voice_channels)
        total = text + voice
        
        embed2 = discord.Embed(timestamp=ctx.message.created_at, color=ctx.author.color)
        embed2.add_field(name='Name', value=f"{ctx.guild.name}", inline=False)
        embed2.add_field(name='Owner', value=f"{ctx.guild.owner}", inline=False)
        embed2.add_field(name='Verification Level', value=str(ctx.guild.verification_level), inline=False)
        embed2.add_field(name='Highest role', value=ctx.guild.roles[-2], inline=False)
        if ctx.guild.system_channel:
            embed2.add_field(name='Standard Channel', value=f'#{ctx.guild.system_channel}', inline=True)



        embed2.add_field(name='AFK Voice Timeout', value=f'{int(ctx.guild.afk_timeout / 60)} min', inline=True)
        embed2.add_field(name='Guild Shard', value=ctx.guild.shard_id, inline=True)
        embed2.add_field(name='Roles', value=str(role_count), inline=True)
        embed2.add_field(name='Members', value=ctx.guild.member_count, inline=True)
        embed2.add_field(name="Text Channels", value=f"{text}", inline=True)
        embed2.add_field(name="Voice Channels", value=f"{voice}", inline=True)
        embed2.add_field(name="Total Channles", value=f"{total}", inline=True)
        embed2.add_field(name='Bots:', value=(', '.join(list_of_bots)))
        embed2.add_field(name='Created At', value=ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=False)
        embed2.set_thumbnail(url=ctx.guild.icon_url)

        author = ctx.message.author
        pfp = author.avatar_url

        embed2.set_author(name=f"Requested by {ctx.author}", icon_url=pfp)
        embed2.set_footer(text="Serverinfo")
        await ctx.send(embed=embed2)


    @commands.command()
    async def chknsfw(self, ctx):
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title="NSFW Check",
                color = discord.Color.red(),
                description = "This is a NSFW Channel"
            )

            await ctx.send(embed = embed)

        else:
            embed = discord.Embed(
                title="NSFW Check",
                color = discord.Color.green(),
                description ="This is not a NSFW Channel"
            )
            await ctx.send(embed = embed)


    @commands.command(pass_context=True)
    async def myid(self, ctx):
        embed = discord.Embed(
            title=f"{ctx.author}"+" ID:",
            color=discord.Color.green()
        )
        embed.add_field(name="{} ".format(ctx.message.author.id), value=":keyboard:")

        await ctx.send(embed=embed)

    @commands.command()
    async def poll(self, ctx, question, option1=None, option2=None):
        if option1==None and option2==None:
            await ctx.channel.purge(limit=1)
            message = await ctx.send(f"```New poll: \n{question}```\n**✅ = Yes**\n**❎ = No**")
            await message.add_reaction('❎')
            await message.add_reaction('✅')
        elif option1==None:
            await ctx.channel.purge(limit=1)
            message = await ctx.send(f"```New poll: \n{question}```\n**✅ = {option1}**\n**❎ = No**")
            await message.add_reaction('❎')
            await message.add_reaction('✅')
        elif option2==None:
            await ctx.channel.purge(limit=1)
            message = await ctx.send(f"```New poll: \n{question}```\n**✅ = Yes**\n**❎ = {option2}**")
            await message.add_reaction('❎')
            await message.add_reaction('✅')
        else:
            await ctx.channel.purge(limit=1)
            message = await ctx.send(f"```New poll: \n{question}```\n**✅ = {option1}**\n**❎ = {option2}**")
            await message.add_reaction('❎')
            await message.add_reaction('✅')

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def ip(self, ctx, query):

        
        async with aiohttp.ClientSession() as session:
            request = await session.get("http://ip-api.com/json/"+query+"?fields=62648319")
            stuff = await request.json()

        embed = discord.Embed(
                title=f"IP: {query}",
                color=discord.Color.purple()
        )

        embed.set_author(name="House Keeper")
        #embed.add_field(name="status", value=stuff["status"], inline=False)
        embed.add_field(name="continent", value=stuff["continent"], inline=False)
        #embed.add_field(name="continetCode", value=stuff["continentCode"], inline=False)
        embed.add_field(name="country", value=stuff["country"], inline=False)
        #embed.add_field(name="countryCode", value=stuff["countryCode"], inline=False)
        embed.add_field(name="region", value=stuff["region"], inline=True)
        #embed.add_field(name="regionName", value=stuff["regionName"], inline=False)
        embed.add_field(name="city", value=stuff["city"], inline=True)
        #embed.add_field(name="district", value=stuff["district"], inline=False)
        embed.add_field(name="zip", value=stuff["zip"], inline=False)
        embed.add_field(name="lat", value=stuff["lat"], inline=False)
        embed.add_field(name="lon", value=stuff["lon"], inline=True)
        embed.add_field(name="timezone", value=stuff["timezone"], inline=True)
        #embed.add_field(name="offset", value=stuff["offset"])
        embed.add_field(name="currency", value=stuff["currency"], inline=False)
        embed.add_field(name="isp", value=stuff["isp"], inline=False)
        #embed.add_field(name="org", value=stuff["org"])
        #embed.add_field(name="as", value=stuff["as"])
        #embed.add_field(name="mobile", value=stuff["mobile"])
        embed.add_field(name="proxy", value=stuff["proxy"], inline=True)
        #embed.add_field(name="hosting", value=stuff["hosting"])
        embed.set_footer(text=stuff["query"]+" lookup by the House Keeper Bot")

        await ctx.send(embed=embed)

    @ip.error
    async def ip_error(self, ctx, error):
        if isinstance(error, CommandOnCooldown):

            embed = discord.Embed(
                title="Not so fast",
                color = discord.Color.red()
            )

            embed.add_field(name=":clock1:", value="This command got a 2 second cooldown")
            embed.set_footer(text="Due API limitations")

            await ctx.send(embed=embed)

    @commands.command(aliases=['lyrc']) # adding a aliase to the command so we can use !lyrc or !lyrics
    async def lyrics(self, ctx, *, search=None):
    
        if not search: # if user hasnt typed anything, throw a error
            embed = discord.Embed(title="No search argument!", description="You havent entered anything, so i couldnt find lyrics!")
            await ctx.reply(embed=embed)
        
        # ctx.reply is available only on discord.py 1.6.0!
        
        song = search.replace(' ', '%20') # replace spaces with "%20"
    
        async with aiohttp.ClientSession() as lyricsSession: # define session
            async with lyricsSession.get(f'https://some-random-api.ml/lyrics?title={song}') as jsondata: # define json data
                if not (300 > jsondata.status >= 200):
                    await ctx.send(f'Recieved Poor Status code of {jsondata.status}.')
                else:
                    lyricsData = await jsondata.json() # load json data
            songLyrics = lyricsData['lyrics'] # the lyrics
            songArtist = lyricsData['author'] # the authors name
            songTitle = lyricsData['title'] # the songs title
        
            try:
                for chunk in [songLyrics[i:i+2000] for i in range(0, len(songLyrics), 2000)]: # if the lyrics extend the discord character limit (2000): split the embed
                    embed = discord.Embed(title=f'{songTitle} by {songArtist}', description=chunk, color=discord.Color.blurple())
                    embed.timestamp = datetime.utcnow()
                
                    await lyricsSession.close() # closing the session
                
                    await ctx.reply(embed=embed)
                
            except discord.HTTPException:
                embed = discord.Embed(title=f'{songTitle} by {songArtist}', description=chunk, color=discord.Color.blurple())
                embed.timestamp = datetime.utcnow()
            
                await lyricsSession.close() # closing the session
            
                await ctx.reply(embed=embed)



    @commands.command()
    async def hierarchy(self, ctx):
        msg = f'Hierarchy system for this Server **{ctx.guild}**:\n\n'
        roleDict = {}

        for role in ctx.guild.roles:
            if role.is_default():
                roleDict[role.position] = 'everyone'
            else:
                roleDict[role.position] = role.name

        for role in sorted(roleDict.items(), reverse=True):
            msg += role[1] + '\n'
        await ctx.send(msg)

    @commands.command()
    async def emoji(self, ctx, emojiname: str):
        emoji = discord.utils.find(lambda e: e.name.lower() == emojiname.lower(), self.client.emojis)
        if emoji:
            tempEmojiFile = 'temp_emoji.png'
            async with aiohttp.ClientSession() as cs:
                async with cs.get(str(emoji.url)) as img:
                    with open(tempEmojiFile, 'wb') as f:
                        f.write(await img.read())
                f = discord.File(tempEmojiFile)
                await ctx.send(file=f)
                os.remove(tempEmojiFile)
        else:
            await ctx.send(":x: I Couldn't find that emoji :(")

    @commands.command(aliases=['activities'])
    async def games(self, ctx, *scope):
        games = Counter()
        for member in ctx.guild.members:
            for activity in member.activities:
                if isinstance(activity, discord.Game):
                    games[str(activity)] += 1
                elif isinstance(activity, discord.Activity):
                    games[activity.name] += 1
        msg = ':bar_chart: Current played games on this server\n'
        msg += '```js\n'
        msg += '{!s:40s}: {!s:>3s}\n'.format('Name', 'Count')
        chart = sorted(games.items(), key=lambda t: t[1], reverse=True)
        for index, (name, amount) in enumerate(chart):
            if len(msg) < 1950:
                msg += '{!s:40s}: {!s:>3s}\n'.format(name, amount)
            else:
                amount = len(chart) - index
                msg += f'+ {amount} others'
                break
        msg += '```'
        await ctx.send(msg)
        



def setup(bot):
    bot.add_cog(utilitiesCog(bot))