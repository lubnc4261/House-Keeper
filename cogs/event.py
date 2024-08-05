import discord
from discord import Member
from discord.ext import commands
import re
import datetime
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

class eventCog(commands.Cog):
	def __init__(self, bot):
		self.client = bot

	@commands.Cog.listener()
	async def on_message(self, message):
		urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',message.content.lower())
		if urls and str(message.channel.id) in open ("idstuff/links/deny.py").read():
			await message.delete()
			await message.channel.send("Link detected and deleted")

	@commands.Cog.listener()
	@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
	async def on_message(self, message):
		# avoid a infinite reply spam
		if message.author.bot:
			return
		
		if self.client.user.mention in message.mentions:
			prefix = get_prefix(self.client, message=message)
			emoji = '<:haarglatzfall:1268212705055998004>'
			rec = f"My current prefix is {prefix[2]}"
			await message.reply(rec,mention_author=False)
			await message.add_reaction(emoji)


			



	@commands.Cog.listener()
	async def on_message_delete(self, message):

		if message.author == self.client.user:
			return

		try:
			execution_time = datetime.datetime.now()
			channel = discord.utils.get(message.guild.channels, name="hk-logging")
			embed = discord.Embed(
				title=f":wastebasket: Message got deleted in `{message.channel}` from `{message.author}`",
				color = discord.Color.purple(),
				
			)
			try:
				# if the guild has no icon an embed wouldnt be send because of this error
				embed.set_author(name=f"{channel.guild}", icon_url=f"{channel.guild.icon.url}")

			except AttributeError:
				pass
			embed.add_field(name="**Message**", value=message.content)
			embed.set_footer(text=execution_time)
			embed.timestamp = datetime.datetime.now()	
			await channel.send(embed=embed)

		
		except AttributeError:     # makes us ignore an exception that occures when the channel doesn't get found
			pass

		except discord.Forbidden:  # stop the console from spams because if the bot get's removed from a guild it could still process sth. that would raise this exception
			pass
		
		except discord.HTTPException: # if an embed itself get deleted, we do not care, embed content cannot be embeded
			pass



	@commands.Cog.listener()
	async def on_message_edit(self, before, after):

		# catching the possibility that an embed update results in a blank edit embed
		# happens on for e.g image insertions into an embed

		if before.author == self.client.user:
			return
		try:
			channel = discord.utils.get(before.guild.channels, name="hk-logging")
			embed = discord.Embed(
				title=f":clipboard: Message got edited in `{before.channel}` by {after.author}",
				color = discord.Color.blue(),
				
			)
			try:
				# if the guild has no icon an embed wouldnt be send because of this error
				embed.set_author(name=f"{channel.guild}", icon_url=f"{channel.guild.icon.url}")

			except AttributeError:
				pass
			embed.add_field(name="**Before**", value=before.content)
			embed.add_field(name="**after**", value=after.content)
			embed.timestamp = datetime.datetime.now()	
			await channel.send(embed=embed)

		except AttributeError:
			pass

		except discord.Forbidden:
			pass
		
		except discord.HTTPException:
			pass

	@commands.Cog.listener()
	async def on_guild_channel_create(self, channel):
		try:

			chann = discord.utils.get(channel.guild.channels, name="hk-logging")

			embed = discord.Embed(
				title=f":new: Channel got created",
				color = discord.Color.green(),
			)
			try:
				# if the guild has no icon an embed wouldnt be send because of this error
				embed.set_author(name=f"{channel.guild}", icon_url=f"{channel.guild.icon.url}")

			except AttributeError:
				pass
			embed.add_field(name="Channel:", value=f"**{channel.mention}**")
			embed.add_field(name="ID: ", value=channel.id)
			embed.timestamp = datetime.datetime.now()	


			await chann.send(embed=embed)

		except AttributeError:
			pass

		except discord.Forbidden:
			pass


	@commands.Cog.listener()
	async def on_guild_channel_delete(self, channel):
		try:

			chann = discord.utils.get(channel.guild.channels, name="hk-logging")

			embed = discord.Embed(
				title=":wastebasket: Channel got deleted",
				color = discord.Color.red(),
			)
			try:
				# if the guild has no icon an embed wouldnt be send because of this error
				embed.set_author(name=f"{channel.guild}", icon_url=f"{channel.guild.icon.url}")

			except AttributeError:
				pass

			embed.add_field(name="Channel:", value=f"**{channel}**")
			embed.timestamp = datetime.datetime.now()	

			await chann.send(embed=embed)

		except AttributeError:
			pass

		except discord.Forbidden:
			pass



	@commands.Cog.listener()
	async def on_guild_channel_update(self, before, after):
		# Voice channel updates
		if isinstance(before, discord.VoiceChannel) and isinstance(after, discord.VoiceChannel):
			chann = discord.utils.get(before.guild.channels, name="hk-logging")
			
			embed = discord.Embed(
				description=f":ear: Voice Channel {before.mention} got updated",
				title=f"Channel id: {before.id}",
				color=discord.Color.green()
			)
			try:
				# if the guild has no icon an embed wouldnt be send because of this error
				embed.set_author(name=f"{before.guild}", icon_url=f"{before.guild.icon.url}")

			except AttributeError:
				pass
			embed.timestamp = datetime.datetime.now()
			if before.name != after.name:
				embed.add_field(name="Name change", value=f"{before.name} -> {after.name}")
			if before.category != after.category:
				embed.add_field(name="Category change", value=f"{before.category} -> {after.category}")
			if before.bitrate != after.bitrate:
				embed.add_field(name="Bitrate change", value=f"{before.bitrate} -> {after.bitrate}")
			if before.nsfw != after.nsfw:
				embed.add_field(name="NSFW change", value=f"{before.nsfw} -> {after.nsfw}")
			if before.position != after.position:
				embed.add_field(name="Position change", value=f"{before.position} -> {after.position}")
			if before.rtc_region != after.rtc_region:
				embed.add_field(name="RTC-region change", value=f"{before.rtc_region} -> {after.rtc_region}")
			if before.slowmode_delay != after.slowmode_delay:
				embed.add_field(name="Slowmode delay change", value=f"{before.slowmode_delay} -> {after.slowmode_delay}")
			if before.user_limit != after.user_limit:
				embed.add_field(name="Userlimit change", value=f"{before.user_limit} -> {after.user_limit}")

			await chann.send(embed=embed)

		elif isinstance(before, discord.TextChannel) and isinstance(after, discord.TextChannel):
			chann = discord.utils.get(before.guild.channels, name="hk-logging")
			embed = discord.Embed(
				description=f":map: Text Channel {before.mention} got updated",
				title=f"Channel id: {before.id}",
				color=discord.Color.green()
			)
			try:
				# if the guild has no icon an embed wouldnt be send because of this error
				embed.set_author(name=f"{before.guild}", icon_url=f"{before.guild.icon.url}")

			except AttributeError:
				pass
			if before.name != after.name:
				embed.add_field(name="Name change", value=f"{before.name} -> {after.name}")
			if before.category != after.category:
				embed.add_field(name="Category change", value=f"{before.category} -> {after.category}")
			if before.nsfw != after.nsfw:
				embed.add_field(name="NSFW change", value=f"{before.nsfw} -> {after.nsfw}")
			if before.position != after.position:
				embed.add_field(name="Position change", value=f"{before.position} -> {after.position}")
			if before.slowmode_delay != after.slowmode_delay:
				embed.add_field(name="Slowmode delay change", value=f"{before.slowmode_delay} -> {after.slowmode_delay}")
			if before.topic != after.topic:
				embed.add_field(name="Topic change", value=f"{before.topic} -> {after.topic}")
			if before.default_thread_slowmode_delay != after.default_thread_slowmode_delay:
				embed.add_field(name="Thread delay change", value=f"{before.default_thread_slowmode_delay} -> {after.default_thread_slowmode_delay}")
			if before.default_auto_archive_duration != after.default_auto_archive_duration:
				embed.add_field(name="Archive thread duration", value=f"{before.default_auto_archive_duration} -> {after.default_auto_archive_duration}")
			if before.changed_roles != after.changed_roles:
				embed.add_field(name="Roles change", value=f"{before.default_auto_archive_duration} -> {after.default_auto_archive_duration}")
			
			await chann.send(embed=embed)

		elif isinstance(before, discord.CategoryChannel) and isinstance(after, discord.CategoryChannel):
			chann = discord.utils.get(before.guild.channels, name="hk-logging")
			embed = discord.Embed(
				description=f":map: Category Channel {before.mention} got updated",
				title=f"Channel id: {before.id}",
				color=discord.Color.green()
			)
			try:
				# if the guild has no icon an embed wouldnt be send because of this error
				embed.set_author(name=f"{before.guild}", icon_url=f"{before.guild.icon.url}")

			except AttributeError:
				pass
			if before.name != after.name:
				embed.add_field(name="Name change", value=f"{before.name} -> {after.name}")
			if before.category != after.category:
				embed.add_field(name="Category change", value=f"{before.category} -> {after.category}")
			if before.nsfw != after.nsfw:
				embed.add_field(name="NSFW change", value=f"{before.nsfw} -> {after.nsfw}")
			if before.changed_roles != after.changed_roles:
				embed.add_field(name="Roles change", value=f"{before.changed_roles} -> {after.changed_roles}")
			if before.text_channels != after.text_channels:
				embed.add_field(name="Channels change", value=f"{before.text_channels} -> {after.text_channels}")

			await chann.send(embed=embed)

	@commands.Cog.listener()
	async def on_member_update(self, before, after):
		try:

			chann = discord.utils.get(before.guild.channels, name="hk-logging")
			if before.nick != after.nick:
				embed = discord.Embed(
				#title=f":pencil: nickname got changed",
				color = discord.Color.purple()
				)
				embed.set_author(name=f"{after.name}", icon_url=after.display_avatar.url)
				embed.set_thumbnail(url=after.display_avatar.url)
				embed.add_field(name="	", value=f":pencil: {after.mention} **nickname update**", inline=False)
				embed.add_field(name="**old nickname**", value=f"`{before.nick}`", inline=True)
				embed.add_field(name="**new nickname**", value=f"`{after.nick}`", inline=True)
				embed.timestamp = datetime.datetime.now()

				await chann.send(embed=embed)

			elif before.roles != after.roles:
				embed = discord.Embed(
					#title=f":white_check_mark: Role update",
					color = discord.Color.yellow(),
				)

				before_roles = [r for r in before.roles if r != before.guild.default_role]
				after_roles = [r for r in after.roles if r != after.guild.default_role]

				fields = [("before", ", ".join([r.mention for r in before_roles]), False),
						("after", ", ".join([r.mention for r in after_roles]), False)]

				embed.set_author(name=f"{after.name}", icon_url=after.display_avatar.url)
				embed.set_thumbnail(url=after.display_avatar.url)
				#embed.add_field(name="User: ", value=f"{after.mention}")
				embed.timestamp = datetime.datetime.now()	
				embed.add_field(name="	", value=f":white_check_mark: {after.mention} **role update**", inline=False)
				for name, value, inline in fields:
					embed.add_field(name=name, value=value, inline=inline)



				await chann.send(embed=embed)


		except AttributeError:
			pass

		except discord.Forbidden:
			pass
	


	@commands.Cog.listener()
	async def on_guild_role_create(self, role):
		try:
			chann = discord.utils.get(role.guild.channels, name="hk-logging")
			embed = discord.Embed(
				title="Role got created",
				color = discord.Color.green(),
				
			)
			embed.timestamp = datetime.datetime.now()

			embed.add_field(name="Role", value=f"{role}")
		
			await chann.send(embed=embed)

		except AttributeError:
			pass

		except discord.Forbidden:
			pass

	@commands.Cog.listener()
	async def on_guild_role_delete(self, role):
		try:

			chann = discord.utils.get(role.guild.channels, name="hk-logging")
			embed = discord.Embed(
				title="Role got deleted",
				color = discord.Color.red(),
				timestamp = datetime.utcnow()
			)

			embed.add_field(name="Role", value=f"{role}")

			await chann.send(embed=embed)

		except AttributeError:
			pass

		except discord.Forbidden:
			pass


	@commands.Cog.listener()
	async def on_member_ban(self, guild, user):
		try:

			chann = discord.utils.get(guild.channels, name="hk-logging")

			embed = discord.Embed(
			title="User ban",
			color = discord.Color.red(),
			timestamp = datetime.utcnow()
			)

			embed.add_field(name="\u200b", value=f"{user.mention} got banned") #\u200b makes empty field

			await chann.send(embed=embed)

		except AttributeError:
			pass

		except discord.Forbidden:
			pass

	@commands.Cog.listener()
	async def on_member_unban(self, guild, user):
		try:

			chann = discord.utils.get(guild.channels, name="hk-logging")

			embed = discord.Embed(
			title="User unban",
			color = discord.Color.green(),
			timestamp = datetime.utcnow()
			)

			embed.add_field(name="\u200b", value=f"{user.mention} got unbanned")

			await chann.send(embed=embed)

		except AttributeError:
			pass

		except discord.Forbidden:
			pass


	@commands.Cog.listener()
	async def on_guild_join(self, guild):

		if guild.system_channel:
			message = f"Thanks for adding me to {guild.name}\n``-``Use ``<help`` to view all my commands\n``-``You can change my prefix from ``<`` by using ``<prefix <new prefix>``\nI support moderation commands as well as other commands. To provide that all my commands work properly, you can additionally give me Administrator permissions\nI also have a logging function so if you run ``<setuplog`` i will log events in it\nCurrent logging cases"
			await guild.system_channel.send(message)

		else:
			pass

		# No process_commands needed /shrug

	@commands.Cog.listener()
	async def on_guild_remove(self, guild):
		print(f"Removed from {guild}")



	@commands.Cog.listener()
	async def on_member_join(self, member):
		try:

			channel = discord.utils.get(member.guild.channels, name="hk-logging")
			await channel.send(f"{member.mention} has joined")

		except AttributeError:
			pass

		except discord.Forbidden:
			pass



	@commands.Cog.listener()
	async def on_member_remove(self, member):
		try:

			channel = discord.utils.get(member.guild.channels, name="hk-logging")
			await channel.send(f"{member.mention} has left")

		except AttributeError:
			pass

		except discord.Forbidden:
			pass

	@commands.Cog.listener()
	async def on_voice_state_update(self, member, before, after):
		if member.bot:
			return
		# Voice join
		
		if not before.channel:
			embed = discord.Embed(
				description=f":inbox_tray: {member.mention} **joined voice channel** ``{after.channel.name}``",
				color = discord.Color.blue()
			)
			embed.timestamp = datetime.datetime.now()
			embed.set_author(name=f"{member.name}", icon_url=f'{member.display_avatar.url}')
			try:
				channel = discord.utils.get(member.guild.channels, name="hk-logging")
				await channel.send(embed=embed)
			except AttributeError:  
				pass
			except discord.Forbidden: 
				pass
			except discord.HTTPException: 
				pass
		# Voice leave

		if before.channel and not after.channel:
			embed = discord.Embed(
				description=f":outbox_tray: {member.mention} **left voice channel** ``{before.channel.name}``",
				color = discord.Color.blue()
			)
			embed.timestamp = datetime.datetime.now()
			embed.set_author(name=f"{member.name}", icon_url=f'{member.display_avatar.url}')
			try:
				channel = discord.utils.get(member.guild.channels, name="hk-logging")
				await channel.send(embed=embed)
			except AttributeError:  
				pass
			except discord.Forbidden: 
				pass
			except discord.HTTPException: 
				pass

		if before.channel and after.channel:
			# stream starting
			if after.self_stream:
				embed = discord.Embed(
				description=f":movie_camera: {member.mention} **started a stream** ``{before.channel.name}``",
				color = discord.Color.blue()
				)
				embed.timestamp = datetime.datetime.now()
				embed.set_author(name=f"{member.name}", icon_url=f'{member.display_avatar.url}')
				try:
					channel = discord.utils.get(member.guild.channels, name="hk-logging")
					await channel.send(embed=embed)
				except AttributeError:  
					pass
				except discord.Forbidden: 
					pass
				except discord.HTTPException: 
					pass
			
			# stream ending
			else:
				embed = discord.Embed(
					description=f":vhs: {member.mention} **endet a stream** ``{before.channel.name}``",
					color = discord.Color.orange()
				)
				embed.timestamp = datetime.datetime.now()
				embed.set_author(name=f"{member.name}", icon_url=f'{member.display_avatar.url}')
				try:
					channel = discord.utils.get(member.guild.channels, name="hk-logging")
					await channel.send(embed=embed)
				except AttributeError:  
					pass
				except discord.Forbidden: 
					pass
				except discord.HTTPException: 
					pass





	@commands.Cog.listener()
	async def on_invite_create(self, invite):
		embed = discord.Embed(
				description=f":calling: {invite.inviter.mention} **created the invite** ``{invite.url}``",
				color = discord.Color.orange()
		)
		embed.timestamp = datetime.datetime.now()
		embed.set_author(name=f"{invite.inviter.name}", icon_url=f'{invite.inviter.display_avatar.url}')
		embed.add_field(name="Target channel", value=f"{invite.channel}")
		embed.add_field(name="Expires at", value=f"{invite.expires_at}")
		try:
			channel = discord.utils.get(invite.guild.channels, name="hk-logging")
			await channel.send(embed=embed)
		except AttributeError:  
			pass
		except discord.Forbidden: 
			pass
		except discord.HTTPException: 
			pass

	@commands.Cog.listener()
	async def on_typing(self, channel, user, when):
		pass

	@commands.Cog.listener()
	async def on_webhook_update(self, channel):
		try:
			channel = discord.utils.get(channel.guild.channels, name="hk-logging")
			embed = discord.Embed(
				description=f":ear: Webhook in {channel.mention} got updated",
				title=f"Channel id: {channel.id}",
				color=discord.Color.green()
			)
			embed.timestamp = datetime.datetime.now()

			try:
				embed.set_author(name=f"{channel.guild}", icon_url=f"{channel.guild.icon.url}")
			except AttributeError:
				pass
			await channel.send(embed=embed)

		except AttributeError:
			pass

		except discord.Forbidden:
			pass
	
	
	# Bot-wide error handling section


	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		if isinstance(error, commands.CommandNotFound):
			pass

		elif isinstance(error, discord.Forbidden):
			await ctx.reply("I dont have enought Permissions to perform that action")

		if isinstance(error, commands.MissingPermissions):
			cross = '❌'
			await ctx.message.add_reaction(cross)

		elif isinstance(error, commands.CommandOnCooldown):
			cooldown = '<cooldown:1269595377795993672>'
			await ctx.message.add_reaction(cooldown)
			return

		elif isinstance(error, commands.DisabledCommand):
			await ctx.send("This command is disabled")

		elif isinstance(error, commands.NoPrivateMessage):
			await ctx.send("This cannot be used in DM's")

		elif isinstance(error, commands.MissingRequiredArgument):
			embed = discord.Embed(
				title="Specify a user",
				color=discord.Color.yellow()
			)
			embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
			embed.set_image(url="https://media.discordapp.net/attachments/1268177354614640661/1269605379537637376/image.png?ex=66b0aba6&is=66af5a26&hm=4c1e8c1a19c71f39f9ac5ec9b3b5732aeebdb1aba0ba735ca3445b22471047d1&=&format=webp&quality=lossless")
			embed.set_footer(text="Missing Required Argument")


			await ctx.reply(embed=embed, mention_author=False)

		elif isinstance(error, commands.MissingAnyRole):
			await ctx.send("Missing any Role")

		else:
			pass





async def setup(bot):
    await bot.add_cog(eventCog(bot))
