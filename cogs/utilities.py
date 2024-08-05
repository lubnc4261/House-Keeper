import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions, BadArgument, MissingRequiredArgument, CommandInvokeError, CommandOnCooldown
import aiohttp
from datetime import datetime
import os
from collections import Counter
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


class utilitiesCog(commands.Cog):
    def __init__(self, bot):
        self.client = bot


    @commands.command()
    @commands.guild_only()
    async def utilities(self, ctx):
        embed = discord.Embed(
            title="Every command needs the prefix before",
            color = discord.Color.magenta()
        )

        embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
        embed.add_field(name=":ticket: `userinfo <@mention>`", value="Shows user related information", inline=True)
        embed.add_field(name=":spy: `permissions <@mention>", value="List all permissions a user has", inline=True)
        embed.add_field(name=":no_mouth: `avatar <@mention>`", value="Profile Picture of the User in PNG", inline=True)
        embed.add_field(name=":book: `serverinfo`", value="Shows Server related information", inline=True)
        embed.add_field(name=":bar_chart: `channelstats`", value="See Channel stats", inline=True)
        embed.add_field(name=":dividers: `hierarchy`", value="Shows Hierarchy system", inline=True)
        embed.add_field(name=":orange_book: `chknsfw`", value="Checks if channel is nsfw", inline=True)
        embed.add_field(name=":tickets: `myid`", value="Shows own discord ID", inline=True)
        embed.add_field(name=":memo: `ip <query>`", value="Perform an ip lookup", inline=True)
        embed.add_field(name=":clipboard: `games`", value="See what games are played on this server", inline=True)
        embed.add_field(name=":label: `emoji <onlyname>`", value="Emoji as png **ONLY** the name **NO** :abc", inline=True)
        embed.add_field(name=":clock11: `timer <time> <task>`", value="Set a Timer that reminds you", inline=True)
        embed.set_footer(text="Help Box fot the House Keeper Bot")
        await ctx.reply(embed = embed,mention_author=False)


    @commands.command()
    @commands.guild_only()
    async def userinfo(self, ctx, member: discord.Member=None):
        try:
            prefix = get_prefix(self.client, message=ctx.message)

            if member == None:
                member = ctx.author

            embed = discord.Embed(
                color= member.color
            )
            perms = member.guild_permissions
            perm_list = [perm for perm, value in perms if value]  # Listet alle Berechtigungen auf, die auf True gesetzt sind
            perm_string = ", ".join(perm_list)

            embed.set_author(name=f"User Info for {member.display_name}", icon_url=member.display_avatar.url)
            embed.set_thumbnail(url=member.display_avatar.url)
            embed.set_footer(text=f"Requested from {ctx.message.author} | {ctx.message.author.id}")

            embed.add_field(name="User", value=f"{member.mention}")
            embed.add_field(name="ID", value=member.id)
            embed.add_field(name="Permissions", value=f"Use `{prefix[2]}permissions`")
            if member.bot == False:
                embed.add_field(name="Bot ?", value="No")
            else:
                embed.add_field(name="Bot ?", value="Yes")

            embed.add_field(name="Account Created at", value=member.created_at.strftime('%Y-%m-%d %H:%M:%S'))
            embed.add_field(name="Server joined at", value=member.joined_at.strftime('%Y-%m-%d %H:%M:%S'))
            if member.premium_since == None:
                embed.add_field(name="Booster since", value="Never")
            else:

                embed.add_field(name="Booster since", value=member.premium_since.strftime('%Y-%m-%d %H:%M:%S'))


            await ctx.reply(embed=embed,mention_author=False)

        except discord.errors.HTTPException:
            pass

    @commands.command()
    @commands.guild_only()
    async def permissions(self, ctx, member: discord.Member=None):
        try:

            if member == None:
                member = ctx.author

            embed = discord.Embed(
                color= member.color
            )
            perms = member.guild_permissions
            perm_list = [perm for perm, value in perms if value]  # Listet alle Berechtigungen auf, die auf True gesetzt sind
            perm_string = ", ".join(perm_list)
            try:

                embed.set_author(name=f"Permission info for {member.display_name}", icon_url=member.display_avatar.url)
            except AttributeError:
                pass
            
            embed.set_thumbnail(url=member.display_avatar.url)
            embed.set_footer(text=f"Requested from {ctx.message.author} | {ctx.message.author.id}")

            embed.add_field(name="Permissions", value=perm_string)

            await ctx.reply(embed=embed,mention_author=False)
        except discord.errors.HTTPException:
            pass


    
    @commands.command()
    @commands.guild_only()
    async def avatar(self, ctx, member: discord.Member=None):
        if member == ctx.author:
            embed = discord.Embed(
            title=f"Here is your avatar, {ctx.author}",
            color=member.color
        )
            embed.set_footer(text=f"Requested by {ctx.author}")
            embed.set_image(url=f"{ctx.author.avatar.url}")
            try:
                embed.set_author(name=f"{member.guild}", icon_url=f"{member.guild.icon.url}")
            except AttributeError:
                pass

        if member == ctx.me:
            embed = discord.Embed(
            title=f"Here is my avatar, {ctx.author}",
            color=member.color
            )
            embed.set_footer(text=f"Requested by {ctx.author}")
            embed.set_image(url=f"{member.avatar.url}")
            try:
                embed.set_author(name=f"{member.guild}", icon_url=f"{member.guild.icon.url}")
            except AttributeError:
                pass

        else:
            embed = discord.Embed(
            title=f"Here is the avatar of, {member}",
            color=member.color
            )
            embed.set_footer(text=f"Requested by {ctx.author}")
            embed.set_image(url=f"{member.avatar.url}")
            try:
                embed.set_author(name=f"{member.guild}", icon_url=f"{member.guild.icon.url}")
            except AttributeError:
                pass

        await ctx.reply(embed=embed,mention_author=False)
    

    @commands.command()
    @commands.guild_only()
    async def serverinfo(self, ctx):
        embed = discord.Embed(
            title=f"Serverinfo for {ctx.guild.name}",
            color=discord.Color.blue()
        )
        try:

            embed.set_author(name=f"{ctx.guild.name}", icon_url=ctx.guild.icon.url)
        except AttributeError:
            pass
        embed.set_footer(text=f"Servername: {ctx.guild.name} | ServerID: {ctx.guild.id}")
        try:

            embed.set_thumbnail(url=ctx.guild.icon.url)
        except AttributeError:
            pass

        embed.add_field(name="Created at", value=ctx.guild.created_at.strftime('%Y-%m-%d %H:%M:%S'), inline=True)
        embed.add_field(name="Roles", value=len(ctx.guild.roles), inline=True)
        embed.add_field(name="Owner", value=ctx.guild.owner.mention, inline=True)

        total_members = len(ctx.guild.members)
        bots = sum(1 for member in ctx.guild.members if member.bot)
        online_members = sum(1 for member in ctx.guild.members if str(member.status) == 'online')
        real_users = total_members - bots
        
        embed.add_field(name="Member", value=f"Total: {total_members}\n Bots: {bots}\n Online: {online_members}\n Real users : {real_users}")
        
        total_channels = len(ctx.guild.channels)
        text_channels = len([channel for channel in ctx.guild.channels if isinstance(channel, discord.TextChannel)])
        voice_channels = len([channel for channel in ctx.guild.channels if isinstance(channel, discord.VoiceChannel)])
        categories = len([channel for channel in ctx.guild.channels if isinstance(channel, discord.CategoryChannel)])


        embed.add_field(name="Channels", value=f"Total: {total_channels}\n Text: {text_channels}\n Voice: {voice_channels}\n Categories: {categories}")


        embed.add_field(name="AFK channel", value=ctx.guild.afk_channel)
        embed.add_field(name="AFK timeout", value=ctx.guild.afk_timeout)
        embed.add_field(name="Bitrate limit", value=ctx.guild.bitrate_limit)
    
        embed.add_field(name="MFA required", value=ctx.guild.mfa_level)

        embed.add_field(name="Booster count", value=ctx.guild.premium_subscription_count, inline=False)

        await ctx.reply(embed=embed,mention_author=False)


    @commands.command()
    @commands.guild_only()
    async def chknsfw(self, ctx):
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title="NSFW Check",
                color = discord.Color.red(),
                description = "This is a NSFW Channel"
            )

            await ctx.reply(embed=embed,mention_author=False)

        else:
            embed = discord.Embed(
                title="NSFW Check",
                color = discord.Color.green(),
                description ="This is not a NSFW Channel"
            )
            await ctx.reply(embed=embed,mention_author=False)


    @commands.command(pass_context=True)
    @commands.guild_only()
    async def myid(self, ctx):
        embed = discord.Embed(
            title=f"{ctx.author}"+" ID:",
            color=discord.Color.green()
        )
        embed.add_field(name="{} ".format(ctx.message.author.id), value=":keyboard:")

        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
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



    @commands.command()
    @commands.guild_only()
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


        await ctx.reply(msg,mention_author=False)



    @commands.command()
    @commands.guild_only()
    async def emoji(self, ctx, emojiname: str):
        emoji = discord.utils.find(lambda e: e.name.lower() == emojiname.lower(), self.client.emojis)
        if emoji:
            tempEmojiFile = 'temp_emoji.png'
            async with aiohttp.ClientSession() as cs:
                async with cs.get(str(emoji.url)) as img:
                    # will this cause problems when a lot of people use it at the same time ???
                    with open(tempEmojiFile, 'wb') as f:
                        f.write(await img.read())
                f = discord.File(tempEmojiFile)
                await ctx.reply(file=f, mention_author=False)
                os.remove(tempEmojiFile)
        else:
            embed = discord.Embed(
                title=":x: unknown emoji",
                color = discord.Color.magenta()
            )
            embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
            embed.set_image(url="https://media.discordapp.net/attachments/1268538785340063755/1268926384810491915/idk.gif?ex=66af84c9&is=66ae3349&hm=581e779a5d56acd46d3db76ec0992b8cd07bb81fc9322688a0e11cb1416f283a&=")
            embed.set_footer(text="House Keeper emoji extractor")
            await ctx.reply(embed=embed,mention_author=False)

    @commands.command(aliases=['activities'])
    @commands.guild_only()
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
        
    @commands.command()
    @commands.guild_only()
    async def channelstats(self, ctx):
        channel = ctx.channel

        embed = discord.Embed(
            title=f"Stats for **{channel.name}**",
            description=f"{'Category: {}'.format(channel.category.name) if channel.category else 'This channel is not in a category'}",
            color=discord.Colour.purple(),
        )
        embed.add_field(name="Channel Guild", value=ctx.guild.name, inline=True)
        embed.add_field(name="Channel Id", value=channel.id, inline=True)
        embed.add_field(name="Channel Topic",value=f"{channel.topic if channel.topic else 'No topic.'}",inline=True)
        embed.add_field(name="Channel Position", value=channel.position, inline=True)
        embed.add_field(name="Channel Slowmode Delay", value=channel.slowmode_delay, inline=True)
        embed.add_field(name="Channel is nsfw?", value=channel.is_nsfw(), inline=True)
        embed.add_field(name="Channel is news?", value=channel.is_news(), inline=True)
        embed.add_field(name="Channel Creation Time", value=channel.created_at, inline=True)
        embed.add_field(name="Channel Permissions Synced",value=channel.permissions_synced,inline=True)
        embed.add_field(name="Channel Hash", value=hash(channel), inline=True)

        await ctx.reply(embed=embed,mention_author=False)
        



async def setup(bot):
    await bot.add_cog(utilitiesCog(bot))
