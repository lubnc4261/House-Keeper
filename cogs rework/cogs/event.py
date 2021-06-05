import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions, BadArgument, MissingRequiredArgument, CommandInvokeError, has_permissions
import json
import re

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
	async def on_message_delete(self, message):
		#await message.channel.send("A message was deleted here")
		pass
		#await client.process_commands(message)


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
		pass

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