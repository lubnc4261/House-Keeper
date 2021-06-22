import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions, BadArgument, MissingRequiredArgument, CommandInvokeError, has_permissions
import json
import re
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
				
			)

			embed.set_author(name=f"{message.author}", icon_url=message.author.avatar_url)
			embed.add_field(name="Content:", value=f"{message.content}", inline=True)
			embed.add_field(name="Channel:", value=f"{message.channel.mention}", inline=True)
			embed.add_field(name="At:", value=time, inline=False)
			embed.add_field(name="User / Nick:", value=f"{message.author.mention}", inline=False)

			#await channel.send(f'message: ``{message.content}`` by **{message.author.mention}** was deleted in **{message.channel.mention}** at: ' +time)

			await channel.send(embed=embed)
			await client.process_commands(message)
		
		except Exception as e:
			print(str(e))


	@commands.Cog.listener()
	async def on_message_edit(self, before, after):
		pass





	@commands.Cog.listener()
	async def on_guild_join(self, guild):

		if guild.system_channel:
			await guild.system_channel.send(f"Thanks for inviting me to {guild.name} ! \nYou can see all my commands by typing §§help\nYou can change the prefix any time by using ``<prefix>prefix<new_prefix>`` \nTo make sure every command will work you can additionally give me Admin permissions\nI need to have all Permissions from the 0Auth Scope to work properly")
		
		else:
			pass

		# No process_commands needed /shrug

	@commands.Cog.listener()
	async def on_guild_remove(self, guild):
		print("removed from {guild}")

	@commands.Cog.listener()
	async def on_member_join(self, member):
		pass

	@commands.Cog.listener()
	async def on_member_remove(self, member):
		try:

			channel = discord.utils.get(member.guild.channels, name="hk-logging")
			await channel.send(f"{member.mention} has left")

		except Exception as a:
			print(a)




def setup(bot):
	bot.add_cog(eventCog(bot))
