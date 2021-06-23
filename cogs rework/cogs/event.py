import discord
from discord import Member
from discord.ext import commands
from discord.ext.commands import MissingPermissions, BadArgument, MissingRequiredArgument, CommandInvokeError, has_permissions
import json
import re
import os
from datetime import datetime
from time import gmtime, strftime



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
	async def on_message(self, message):
		attach = message.attachments
		if len(attach) > 0:
			for attachment in attach:
				if attachment.filename.endswith(".exe"):
					await message.channel.send(":exclamation: EXE located, possible danger level [HIGH] \n Don't trust random files !")

				if attachment.filename.endswith(".dll"):
					await message.channel.send(":exclamation: EXE located, possible danger level [HIGH] \n Don't trust random files !")

				if attachment.filename.endswith(".py"):
					await message.channel.send(":exclamation: PYTHON located, possible danger level [HIGH] \n Don't trust random files !")

				if attachment.filename.endswith(".jar"):
					await message.channel.send(":exclamation: JAR located, possible danger level [HIGH] \n Don't trust random files !")

				if attachment.filename.endswith(".bat"):
					await message.channel.send(":exclamation: BAT located, possible danger level [HIGH] \n Don't trust random files !")

				if attachment.filename.endswith(".ps1"):
					await message.channel.send(":exclamation: PS located, possible danger level [HIGH] \n Don't trust random files !")

				if attachment.filename.endswith(".vbs"):
					await message.channel.send(":exclamation: VBS located, possible danger level [HIGH] \n Don't trust random files !")

				else:
					pass

			



	@commands.Cog.listener()
	async def on_message_delete(self, message):
		try:
			channel = discord.utils.get(message.guild.channels, name="hk-logging")
			time = strftime("%Y-%m-%d %H:%M:%S", gmtime())

			embed = discord.Embed(
				title=f"Message got deleted",
				color = discord.Color.purple(),
				timestamp = datetime.utcnow()
				
			)

			embed.set_author(name=f"{message.author}", icon_url=message.author.avatar_url)
			embed.add_field(name="Content:", value=f"{message.content}", inline=True)
			embed.add_field(name="Channel:", value=f"{message.channel.mention}", inline=True)
			embed.add_field(name="At:", value=time, inline=False)
			embed.add_field(name="User / Nick:", value=f"{message.author.mention}", inline=False)

			#await channel.send(f'message: ``{message.content}`` by **{message.author.mention}** was deleted in **{message.channel.mention}** at: ' +time)

			await channel.send(embed=embed)
			await client.process_commands(message)


		
		except AttributeError:     # makes us ignore an exception that occures when the channel doesn't get found
			pass

		except discord.Forbidden:  # stop the console from spams because if the bot get's removed from a guild it could still process sth. that would raise this exception
			pass



	@commands.Cog.listener()
	async def on_message_edit(self, before, after):
		pass

	@commands.Cog.listener()
	async def on_guild_channel_create(self, channel):
		try:

			chann = discord.utils.get(channel.guild.channels, name="hk-logging")
			time = strftime("%Y-%m-%d %H:%M:%S", gmtime())

			embed = discord.Embed(
				title="Channel got created",
				color = discord.Color.green(),
				timestamp = datetime.utcnow()
			)

			embed.add_field(name="Channel:", value=f"**{channel}**")


			await chann.send(embed=embed)

		except AttributeError:
			pass

		except discord.Forbidden:
			pass


	@commands.Cog.listener()
	async def on_guild_channel_delete(self, channel):
		try:

			chann = discord.utils.get(channel.guild.channels, name="hk-logging")
			time = strftime("%Y-%m-%d %H:%M:%S", gmtime())

			embed = discord.Embed(
				title="Channel got deleted",
				color = discord.Color.red(),
				timestamp = datetime.utcnow()
			)

			embed.add_field(name="Channel:", value=f"**{channel}**")
	

			await chann.send(embed=embed)

		except AttributeError:
			pass

		except discord.Forbidden:
			pass

	@commands.Cog.listener()
	async def on_member_update(self, before: Member, after: Member):
		try:

			chann = discord.utils.get(before.guild.channels, name="hk-logging")
			if before.display_name != after.display_name:
				embed = discord.Embed(
				title="Nickname update occured",
				color = discord.Color.purple(),
				timestamp = datetime.utcnow()
				)

				embed.add_field(name="before", value=f"{before.display_name}")
				embed.add_field(name="after", value=f"{before.display_name}")

				await chann.send(embed=embed)

			elif before.roles != after.roles:
				embed = discord.Embed(
					title="Role update",
					color = discord.Color.red(),
					timestamp = datetime.utcnow()
				)

				fields = [("before", ", ".join([r.mention for r in before.roles]), False),
						("after", ", ".join([r.mention for r in after.roles]), False)]

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
			timestamp = datetime.utcnow()
			)

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
			message = f"Thanks for adding me to {guild.name}\n``-``Use ``<help`` to view all my commands\n``-``You can change my prefix from ``<`` by using ``<prefix <new prefix>``\n``-``If you need more help, you can visit my support server at\nhttps://www.discord.gg/gJaZbKCmE7\n▬▬▬▬▬▬▬▬▬▬▬▬▬\nI support moderation commands as well as other commands. To provide that all my commands work properly, you can additionally give me Administrator permissions\nI also have a logging function so if you run ``<setuplog`` i will log events in it\nCurrent logging cases are:\n**-** deleteed messages\n**-** channel creation\n**-** channel delete\n**-** nickname update\n**-** role update\n**-** role creation\n**-** role delete\n**-** member ban\n**-** member unban\n**-** member join\n**-** member remove."
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
	async def on_command_error(self, ctx, error):
		if isinstance(error, commands.CommandNotFound):
			pass

		elif isinstance(error, commands.DisabledCommand):
			await ctx.send("This command is disabled")

		elif isinstance(error, commands.NoPrivateMessage):
			await ctx.send("This cannot be used in DM's")

		elif isinstance(error, commands.MissingRequiredArgument):
			await ctx.send("Missing Argument")

		elif isinstance(error, commands.MissingAnyRole):
			await ctx.send("Missing any Role")

		else:
			pass





def setup(bot):
	bot.add_cog(eventCog(bot))
