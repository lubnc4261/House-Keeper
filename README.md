<h1 align="center">
  Discord Bot - House Keeper
</h1>

<h4 align="center">Moderation, Management, Logging and Utilities.</h4>

<p align="center">
  <a href="https://github.com/lubnc4261/House-Keeper">
     <img alt="status" src="https://img.shields.io/badge/status-working-green">
  </a>
  <a href="https://www.python.org/downloads/">
    <img alt="Python Version" src="https://img.shields.io/badge/python-3.12.4-blue.svg">
  </a>
  <a href="https://github.com/Rapptz/discord.py/">
     <img src="https://img.shields.io/badge/discord-py-blue.svg" alt="discord.py">
  </a>
</p>


<p align="center">
  <a href="https://github.com/lubnc4261/House-Keeper?tab=readme-ov-file#preface">Preface</a>
  •
  <a href="https://github.com/lubnc4261/House-Keeper?tab=readme-ov-file#overview">Overview</a>
  •
  <a href="https://github.com/lubnc4261/House-Keeper?tab=readme-ov-file#installation">Installation</a>
  •
  <a href="https://github.com/lubnc4261/House-Keeper?tab=readme-ov-file#developer">Developer</a>
  •
  <a href="https://github.com/lubnc4261/House-Keeper?tab=readme-ov-file#featured-commands">Commands</a>
  •
  <a href="https://github.com/lubnc4261/House-Keeper?tab=readme-ov-file#tickets">Tickets</a>
  •
  <a href="https://github.com/lubnc4261/House-Keeper?tab=readme-ov-file#logging">Logging</a>
</p>

# Preface
**Feel free to skip this section**

What began as a simple, fun idea a few years ago has developed into a fully-fledged, powerful Discord bot, thanks to the time and interest poured into this long-term project. Originally created as a modest experiment, this bot has undergone numerous transformations, evolving significantly with each iteration. By using the features [discord.py v2+](https://github.com/Rapptz/discord.py) has to offer, it has matured into a robust and reliable tool that enhances the Discord experience. This journey of development, innovation, and improvement showcases the potential of combining creativity with technical expertise, resulting in a bot that is both functional and easy to interact with. Beyond the enjoyment of the process, this project has been an invaluable learning experience, significantly enhancing my coding skills and deepening my understanding of software development. While it is primarily designed for self-hosting on a [Raspberry PI4](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/), there are no restrictions on the platform you choose for hosting. Whether you prefer a different single-board computer, a personal server, or even a cloud-based solution, this bot offers the flexibility to adapt to your preferred setup.

# To-Do List

- ✔️ Rewrite to v2
- ✅ Add slash-comamnds
- ✅ Create Ticket support
- ❌ Implement music-feature
- ❌ Add an Economy System

# Overview

This bot is a versatile tool designed for a range of uses, including management, utility features, and more. I am committed to keeping the bot up-to-date and continuously adding new features. If you explore the code and have any questions, suggestions, or encounter any bugs, please feel free to submit a pull request or open an issue.

- The bot is initialized with a default prefix of `<` and changeable via `<prefix !`

- Custom responses for various scenarios a command might encounter during execution, such as, but not limited to:
  - Attempting to ban a user with higher permissions than the bot
  - Trying to unban a user who is not currently banned
 
- An effort to address the most common daily functions


# Installation

To set up and run the Discord bot, you'll need Python 3, a Bot Token and the required dependencies listed in the `requirements.txt` file. Follow these steps to get everything you need:

## Python
> [!TIP]
> Type `python --version` in a Terminal to check your version

- Download [Python3](https://www.python.org/downloads/) on your machine or alternatively on your Linux server. Here are some websites that could help you:
[itheo.nl](https://itheo.nl/install-python-3-9-on-raspberry-pi) and [raspberry-valley](https://raspberry-valley.azurewebsites.net/Python-Default-Version/)

After you confirmed that Python3 is successfully installed, open a Terminal in the Project's root directory and execute:  `pip install -r requirements.txt`

## Bot Token

- Visit the [Discord Developer Portal](https://discord.com/developers/) and create a new Application
- Generate a Token in the Bot Section
- Create a invite URL in the OAuth Section

> [!NOTE]
> Make sure to set the **Scopes** to `bot` and **Bot Permissions** to `Administrator`

## Discord Bot
- Download [this Project](https://github.com/lubnc4261/House-Keeper/archive/refs/heads/main.zip) directly or use git in case you have it installed.
- Insert your previously generated Token into the [config.json](https://github.com/lubnc4261/House-Keeper/blob/08ec95a6ff2ba505fcb417d91509d969cc79ceb8/config.json) file
- You can now start the bot by executing the following command  `python main.py`

# Logging


- If the server has a channel named `hk-logging`, all events will be logged there. If such a channel does not exist, you can use the command `<setuplog` to automatically create one for you
- Examples of events that are logged include channel edits, voice channel activities, deleted messages, role updates, and more.


# Developer

## Adding own plugins

If you need to add your own commands or cogs, here's a brief guide to help you get started:
- create a file myownextension.py inside the [/cogs](https://github.com/lubnc4261/House-Keeper/tree/08ec95a6ff2ba505fcb417d91509d969cc79ceb8/cogs) folder
- The extension must adhere to the following structure:
  
```python
class myownextensionCog(commands.Cog):
    def __init__(self, bot):
        self.client = bot

  @commands.command()
  ...

async def setup(bot):
    await bot.add_cog(myownextensionCog(bot))

  ```

- Add the following one-liner into the main.py [setup_hook function](https://github.com/lubnc4261/House-Keeper/blob/08ec95a6ff2ba505fcb417d91509d969cc79ceb8/main.py#L52)
   - ```python
     await self.load_extension("cogs.myownextension")
     ```

> [!NOTE]
> Replace all instances of `myownextension` with the filename

## Catching Events

All error events that may occur during the bot's runtime are handled within the [event.py](https://github.com/lubnc4261/House-Keeper/blob/08ec95a6ff2ba505fcb417d91509d969cc79ceb8/cogs/event.py#L601) cog. This cog is specifically designed to capture and manage any exceptions or issues that arise, ensuring that errors are properly logged and addressed without disrupting the bot’s functionality.

# Tickets

The bot also includes a basic ticketing system. To set it up, you'll need to designate a channel as the anchor for ticket creation. You can create this anchor channel by using the command `/ticket_panel <title>`.

> [!NOTE]
> - The bot will automatically configure the channel to be write-only.  
> - A category named "Tickets" is required to exist for proper functionality.  
> - Ticket logs will be saved in **#ticketlog**, provided the channel exists.

The channel name is designed as ticket-<userid> instead of the traditional #number format.  
When a user or admin closes the ticket using the provided button, the log is automatically saved.

# Featured Commands

The following list includes all currently available commands, organized into subcategories based on their respective cogs.

- The account that I use in the examples, `test` is entirely fictional and has no connection or association with any real individual or this Project


### bot ###

Command and Alias | Description | Usage | Info
---------------|-------------|----------|---------
`bot` | Shows all bot related commands | `bot` |
`status` | Basic status about host | `status` |
`about` | Infos about the bot | `info` |
`botinvite` | Send you an invite link | `botinvite` |
`ping` | bot latency and api ping | `ping` |

## cmd ##

Command and Alias | Description | Usage | Info
----------------|-------------|---------|--------
`help` | List all possible help commands | `help` | 
`mod`, `management` | help bot for mod commands | `mod`, `management` |
`security` | Security command help | `security`| 
`utilities` | Usefull commands | `utilities` |
`fun` | fun commands | `fun` |
`games` | game commands | `games` |
`slash` | slash supported commands | `slash` |
`bot` | bot related help  | `bot` |


## fun ##

Command and Alias | Description | Usage | Info
---------------|---------------|--------|-------
`8ball` | get a random answer to a question | `8ball can i code ?` | 
`youtube` | perform a search on youtube | `youtube python tutorial` | 
`coinflip` `flip` `coin` | flip the coin | `flip` |
`f` | pay respect | `f` | 
`reverse` | reverse the message | `reverse` | 
`rate` | gives you a rate about sth. | `rate java` | 
`meow` | cat image | `meow` | uses api
`dog` | dog image | `dog` | uses api
`duck` | duck image | `duck` | uses api
`fox` | fow image | `fox` | uses api

## games ## 

Command and Alias | Description | Usage | Info
---------------|---------------|--------|-------
`hangman` | play hangman with the bot | `hangman` | change words in gams/hangman.py
`minesweeper` | play minesweeper | `minesweeper` or `minesweeper <columns> <rows> <bombs>` | it cant make a score just a basic play
`rps` | play rock paper scissors | `rps` | will react with emojis
`teams` | creates team with users in voice channel | `teams 5` | will send teams in the text channel
`ttt` | play tic tac toe | `ttt` |

## management ##

Command and Alias | Description | Usage | Info
---------------|---------------|--------|-------
`clear` | clears the chat, if amount not given then 13 | `clear 4` |
`kick` | kicks a user | `kick test` |
`ban` | bans a user w.reason | `ban test uncool` |
`softban` | softban a user | `softban test` | 
`unban` | unbanns a user | `unban test` | enter manually since user don't "exists"
`nick` | nick a user | `nick test nownicked` |
`give` | give a user a role | `give test admin` | can't give role higher than you or bot
`rmrank` | removes a role from user | `rmrank test supporter` | mention user **manually** with tag
`moverole` | moves the role on server hierarchy | `moverole kek 4` | 4 from bottom
`name` | renames the server | `name SuperCoolDiscord` |
`log` | logs messages from the chat | `log 55` | logs messages in .txt then send it to the channel as attachement
`savemembers` | logs all users in server to File | `savemembers` | log get send in channel
`delcat` | delete a category w.reason | `delcat Channels useless` | 
`setuplog` | create a "hk-logging" channel | `setuplog` | events will be logged here

## security ##


Command and Alias | Description | Usage | Info
---------------|---------------|--------|-------
`block` | stop a user from sending messages | `block test` | channel only
`unblock` | allow user sending messages | `unblock test` | channel only

## utilities ##


Command and Alias | Description | Usage | Info
---------------|---------------|--------|-------
`userinfo` | see all infos about a user | `userinfo test` | 
`permissions` | list all permissions a user has | `permissions test` |
`avatar` | bot send user avatar in channel | `avatar test` |
`serverinfo` | bot provides server infos | `serverinfo` |
`channelstats` | provides channel infos | `channelstats` |
`hierarchy` | list all roles in hierarchy order | `hierarchy` |
`chknsfw` | check if the channel is nsfw | `chknsfw`|
`myid` | shows you you'r id | `myid`
`ip` | make a ip info lookup | `ip 8.8.8.8` | uses api, no you are not a hacker
`games` | list all current played games on the server | `games` |
`emoji` | extract emojis as image | `emoji pogchamp` | only the id not the emoji itself
`timer` | creates a timer that will remind you in the channel | `timer "buy toilet paper" 1s` or `1m` or `1h` |

## slash ##

I want to keep this balanced and avoid overdoing it

Command and Alias | Description | Usage | info
---------------|---------------|--------|-------
`ban` | ban a user | `ban @test` | 
`userinfo` | show userinfo | `userinfo @test` | 
`permissions` | show user permissions | `permissions @test` |
`avatar` | return a user's avatar | `avatar @test` |
`youtube` | get a fitting video | `youtube python` |
`lock` | lockdown a whole channel | `lock #general stop` | slash only
`unlock` | unlock a channel | `unlock #general thanks` | slash only

## ticket ##

Command and Alias | Description | Usage | Info
---------------|---------------|--------|-------
`/ticket_pannel <name>` | Create a Ticket ancor | `/ticket_pannel help` | slash only
`close` | Close the current viewed Ticket | `close` | Be in the Ticket Channel

