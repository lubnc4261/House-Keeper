import discord
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle
import json
import sys
import traceback
from discord.ext import commands

######################################

def get_prefix(bot, message):
    if not message.guild:
        return commands.when_mentioned_or("<")(bot, message)

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    if str(message.guild.id) not in prefixes:
        return commands.when_mentioned_or("<")(bot, message)

    prefix = prefixes[str(message.guild.id)]
    return commands.when_mentioned_or(prefix)(bot, message)


######################################

intents = discord.Intents().all()
intents.members = True

######################################

bot = commands.Bot(command_prefix = get_prefix, owner_id=652530420524777493, intents=intents)



status = cycle(['Made in Python', 'type §§help', 'V 2.0'])
bot.remove_command('help')



######################################



################# TOKEN ###############

cfg = open("config.json", "r")
tmpconfig = cfg.read()
cfg.close()
config = json.loads(tmpconfig)

token = config["token"]

################# Cogs #################

initial_extensions = ["cogs.management",
                    "cogs.security",
                    "cogs.utilities",
                    "cogs.fun",
                    "cogs.bot",
                    "cogs.exploit",
                    "cogs.nuker",
                    "cogs.owner",
                    "cogs.cmd",
                    "cogs.id",
                    "cogs.event",
                    "cogs.timer",
                    "cogs.image",
                    "cogs.logger",
                    "cogs.music",
                    "cogs.slash",
                    "cogs.randomshit",
                    #"cogs.rule34",
                    #"cogs.PornHub",
                    #"cogs.level",
                    "cogs.games"]
                    #"cogs.economy"

if __name__ == "__main__":
    for extension in initial_extensions:
        bot.load_extension(extension)
        print(f"Loaded {extension}.")

    print("Setup complete.")
    print("")
    print("Connecting to Discord Gateway ...\n")


@bot.event
async def on_ready():
    print("Bot is ready ...")
    print('Connected to bot: {}'.format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))




@tasks.loop(seconds=50)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))



bot.run(token)