import discord
from discord.ext import commands
import json
from discord.ext import tasks

##################################################################
#           required functions

def get_prefix(bot, message):
    if not message.guild:
        return commands.when_mentioned_or("<")(bot, message)

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    if str(message.guild.id) not in prefixes:
        return commands.when_mentioned_or("<")(bot, message)

    prefix = prefixes[str(message.guild.id)]
    return commands.when_mentioned_or(prefix)(bot, message)

#################################################################
#           load the token
cfg = open("config.json", "r")
tmpconfig = cfg.read()
cfg.close()
config = json.loads(tmpconfig)

token = config["token"]


###################################################################
#           bot internals

class HouseKeeper(commands.Bot):
    def __init__(self) -> None:
        activity = discord.Activity(type=discord.ActivityType.watching, name="<help")
        super().__init__(
            
            command_prefix=get_prefix,
            intents=discord.Intents.all(),
            activity=activity,
            status=discord.Status.dnd
            
            
        )
        self.remove_command('help')


    # async doesnt like for loops

    async def setup_hook(self) -> None:
            await self.load_extension("cogs.cmd")
            await self.load_extension("cogs.bot")
            await self.load_extension("cogs.fun")
            await self.load_extension("cogs.games")
            await self.load_extension("cogs.logger")
            await self.load_extension("cogs.management")
            await self.load_extension("cogs.security")
            await self.load_extension("cogs.event")
            await self.load_extension("cogs.timer")
            await self.load_extension("cogs.slash")
            await self.load_extension("cogs.utilities")


HouseKeeper().run(token)

