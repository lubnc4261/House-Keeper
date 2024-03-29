# House-Keeper
[![status](https://img.shields.io/badge/status-working-green)](https://github.com/lubnc4261/House-Keeper)
[![Python3](https://img.shields.io/badge/python-3.7-blue.svg)](https://github.com/lubnc4261/House-Keeper)
[![Python3](https://img.shields.io/badge/python-3.9-blue.svg)](https://github.com/lubnc4261/House-Keeper)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)]

**ATTENTION: I made this bot by using the new rewrite version of [discord.py v1.7+](https://github.com/Rapptz/discord.py), and the [discord-py-slash-command v1.2.2](https://github.com/LordOfPolls/discord-py-slash-command) lib. I am currently self hosting this bot on an [Raspberry PI4](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/) but you can take a look on the code and implement it the way you want it.**

To upgrade your python to 3 on the PI i used this:

[itheo.nl](https://itheo.nl/install-python-3-9-on-raspberry-pi)
[raspberry-valley](https://raspberry-valley.azurewebsites.net/Python-Default-Version/)

If you want to also use the music function you have to add the needed lib's down below, as well as add [FFmpeg](https://www.ffmpeg.org/download.html) to your **PATH** on Windows its quiet easy so just search it up:
- install .exe
- get path of the /bin exe's
- go to windows path settings and add new variable down below
- add the path of the 3 exe's

[Usefull video](https://youtu.be/r1AtmY-RMyQ)

On linux its quiet harder some usefull links that I used are:
[pimylifeup.com](https://pimylifeup.com/compiling-ffmpeg-raspberry-pi/)





This bot is an all arounder so you can use it for management, music, and other things. I will keep commiting new changes since its the project i am currently working on (im working alone on it). If you are exploring my code and got any questions, suggestions or bug reports, don't hesitate to contact me on discord, my tag is: `Militär Staubsauger#0921` or join my [community server](https://discord.gg/gJaZbKCmE7)

When i am including examples for commands, you can of course change the numbers since they are just examples, same goes for Strings, ints, etc.

Tips: 
- Mention users for interaction, only do it different if the Info says so
- keep multiple words form 1 argument in  " " quotes to avoid errors and skipped arguments

Modules that are used are:

`pip install discord.py` (rewrite, v1.7+)
`pip install discord-py-slash-command` (v1.2.2)
`pip install youtube_dl` (v2021.5.16, since the bot also works as a music bot)
`pip install pynacl` (v1.4.0)
`pip install request` (if you dont have it already installed)
`pip install psutil` (for the status command)

The account that I use in the examples `test#1111` is just a fictive creation and got no connection or associations to the owner of this account in any way.

Command List
------------
**Info:** The preset prefix is `<` but you can change it via the command `<current_prefix>prefix<new_prefix>`

## passive interactions ##
**Info:** The bot can log events in a channel that is called **hk-logging** but only if it exists
Other events are:
  - if file with [listed extension](https://github.com/lubnc4261/House-Keeper/blob/59850f756122ee55189e0770aa12c05fd451d8bb/cogs%20rework/cogs/event.py#L43) get detected, the bot will send a warn message
  - logging events that are [supported](https://github.com/lubnc4261/House-Keeper/blob/1ea9f63870e379787296bc097811fd603e184d0b/cogs%20rework/cogs/event.py#L31)
  

### Bot ###

Command and Alias | Description | Usage | Info
---------------|-------------|----------|---------
`bot` | Shows all bot related commands | `bot` |
`status` | Basic status about host | `status` |
`info` | Infos about the bot | `info` |
`botinvite` | Send you an invite link | `botinvite` |
`botplatform` | platform info | `botplatform` | 
`ping` | bot latency and api ping | `ping` |
`permission` | lists current given permissions | `permissions` |

## help ##

Command and Alias | Description | Usage | Info
----------------|-------------|---------|--------
`help` | List all possible help commands | `help` | 
`mod`, `management` | help bot for mod commands | `mod`, `management` |
`security` | Security command help | `security`| 
`utilities` | Usefull commands | `utilities` |
`fun` | fun commands | `fun` |
`games` | game commands | `games` |
`music` | music bot commands | `music` |
`bot` | bot related help  | `bot` |
`dev` | commands for whitelisted ppl | `dev` | check idstuff folder

## dev ##

Command and Alias | Description | Usage | Info
---------------|--------------|---------|--------
`developer` | List **force** commands | `developer` | check idstuff folder
`owner` | commands only for the bot owner | `owner` | check idstuff folder
`DBCheck` | add users to certain idstuff file | `DBCheck` | check idstuff folder

## developer ## 

This section is own for whitelisted user, commands work like expected but without user permission check
so its an "exploit" or "breach". Was added long time ago for griefing, but why shouldn't i keep it xd.
The command send will be deleted if possible, if it didn't worked user get a DM with the error.

Command and Alias | Description | Usage | Info
---------------|---------------|--------|-------
`forceunban` | force unban user | `forceunban test#1111` | need to be whitelisted
`forceclear` | forces to clear the chat | `forceclear 5` | need to be whitelisted
`forceban` | forces to ban a user | `forceban test#1111` | need to be whitelisted
`forcekick` | forces to kick a user | `forcekick test#1111` | need to be whitelisted
`forcenick` | forces to nick a user | `forcenick test#1111 nickednowuwu` | need to be whitelisted
`forcegive` | forces to give a user the role | `forcegive test#1111 admin` | need to be whitelisted , bot cant give a role that is higher than him
`role` | creates blank role with admin perms. | `role exploitrole` | need to be whitelisted, get it with `forcegive`

## DBCheck ##

You have to manually add the first owner id in the file idstuff/owner.py since it checks for your existence in there.
After id parameter you can add a comment with **#** since its a py file thats why i choose this design.

Command and Alias | Description | Usage | Info
---------------|---------------|--------|-------
`DBbypass`| force users whitelist | `DBbypass_read` or `_add <id>`| **force commands** and **dev commands**
`DBnukers` | users that can "nuke" | `DBnukers_read` or `_add <id>` | **nuker commands**
`DBsens` | users that can access sensetive informations | `DBsens_read` or `_add <id>` |
`DBblacklistcomms` | Servers on that `force` doesn't work | `DBblacklistcomms_read` or `_add <id>` |
`DBblacklistedserver` | Servers that can't get `nuked` | `DBblacklistedserver_read` or `_add <id>` |
`DBdenylinks` | See what channels dont allow links | `DBdenylinks_read` | channels that got added with `denylinks`
`owner` | add users to be "owner" | `owner_read` or `_add` | owner can add, use all DB commands


## fun ##

Command and Alias | Description | Usage | Info
---------------|---------------|--------|-------
`8ball` | get a random answer to a question | `8ball can i code ?` | 
`kill` | "kills" the user | `kill test#1111` | uses api to get the image
`hug` | "hugs" the user | `hug test#1111` | uses api to get the image
`horny` | creates a horny pass | `horny test#1111` | uses api
`triggered` | triggered image overlay | `triggered test#1111` | uses api to get overlay
`youtube` | perform a search on youtube | `youtube linus sex tips` | 
`say` | bot repeats content | `say fortnite is bad` |
`coinflip` `flip` `coin` | flip the coin | `flip` |
`f` | pay respect | `f` | 
`reverse` | reverse the message | `reverse` | 
`hotcalc` `howhot` `hot` | see how hot the user is | `hot test#1111` | 
`rate` | gives you a rate about sth. | `rate java` | 
`dankmeme` | random r/dankmeme | `dankmeme` | emoji is from extra server
`meme` | random meme | `meme` | emoji is from extra server
`meow` | cat image w. quote | `meow` | uses api
`dog` | dog image w.quote | `dog` | uses api
`duck` | duck image w.quote | `duck` | uses api
`panda` | panda image w. quote | `panda`| uses api
`fox` | fow image w.quote | `fox` | uses api

## games ## 

Command and Alias | Description | Usage | Info
---------------|---------------|--------|-------
`hangman` | play hangman with the bot | `hangman` | change words in gams/hangman.py
`minesweeper` | play minesweeper | `minesweeper` or `minesweeper <columns> <rows> <bombs>` | it cant make a score just a basic play
`rps` | play rock paper scissors | `rps` | will react with emojis
`teams` | creates team with users in voice channel | `teams 5` | will send teams in the text channel
`ttt` | play tic tac toe | `ttt` |

## management ##

You better mention the user, dont write it manually

Command and Alias | Description | Usage | Info
---------------|---------------|--------|-------
`clear` | clears the chat, if amount not given then 13 | `clear 4` |
`kick` | kicks a user | `kick test#1111` |
`ban` | bans a user w.reason | `ban test#1111 uncool` |
`softban` | softban a user | `softban test#1111` | 
`unban` | unbanns a user | `unban <name>#<discriminator>` | enter manually since user don't "exists"
`getbans` | get all active bans | `getbans` |
`bans` | get all bans w. reason | `bans` |
`nick` | nick a user | `nick test#1111 nownicked` |
`give` | give a user a role | `give test#1111 admin` | can't give role higher than you or bot
`rmrank` | removes a role from user | `rmrank test#1111 supporter` | mention user **manually** with tag
`moverole` | moves the role on server hierarchy | `moverole kek 4` | 4 from bottom
`name` | renames the server | `name SuperCoolDiscord` |
`poll` | create a basic poll | `poll "python or java" "python" "java" "html"` | keep text in " " quotes
`log` | logs messages from the chat | `log 55` | logs messages in .txt then send it to the channel as attachement
`savemembers` | logs all users in server to File | `savemembers` | log get send in channel
`delcat` | delete a category w.reason | `delcat Channels useless` | 
`setuplog` | create a "hk-logging" channel | `setuplog` | events will be logged here

## music ##

needs, youtube-dll, pynacl, ffmpeg

Command and Alias | Description | Usage | Info
---------------|---------------|--------|-------
`join` | makes bot join your channel | `join` | you have to be in a channel
`play` | search a song | `play rasputin` |
`leave` | bot leaves channel | `leave` |
`now` | see what is playing now | `now` |

## nuker ##

Command and Alias | Description | Usage | Info
---------------|---------------|--------|-------
`nuker` | show help in DM | `nuker` | be in idstuff/allowednuker.py
`chnuker` | spam channels | `chnuke 5 griefed` | 
`rlnuke` | spam blank roles | `rlnuke 5 hello` |
`vcnuke` | spam voice channels | `vcnuke 20 no` |

## owner ##

Command and Alias | Description | Usage | Info
---------------|---------------|--------|-------
`logout` | shutdown the bot | `shutdown` | 
`rename` | rename the bot | `rename Kouse Heeper` |

## security ##


Command and Alias | Description | Usage | Info
---------------|---------------|--------|-------
`block` | stop a user from sending messages | `block test#111` |
`unblock` | allow user sending messages | `unblock test#1111` |
`denylinks` | deny links in channel | `denylinks 345870938981ß3` | **channel id needed**
`allowlinks` | allow links back again | `allowlinks 345870938981ß3` | **channe id needed**

## utilities ##


Command and Alias | Description | Usage | Info
---------------|---------------|--------|-------
`userinfo` | see all infos about a user | `userinfo test#1111` | If user has to many roles the get cut off
`avatar` | bot send user avatar in channel | `avatar test#1111` |
`serverinfo` | bot provides server infos | `serverinfo` |
`channelstats` | provides channel infos | `channelstats` |
`hierarchy` | list all roles in hierarchy order | `hierarchy` |
`chknsfw` | check if the channel is nsfw | `chknsfw`|
`myid` | shows you you'r id | `myid`
`ip` | make a ip info lookup | `ip 8.8.8.8` | uses api, no you are not a hacker
`lyrics` | shows you the song lyrics | `lyrics rasputin` | uses api
`games` | list all current played games on the server | `games` |
`emoji` | extract emojis as image | `emoji pogchamp` | only the id not the emoji itself
`timer` | creates a timer that will remind you in the channel | `timer "buy toilet paper" 1s` or `1m` or `1h` |

## nsfw ##

using nekos nsfw api to get hentai images
the structure of all nsfw commands is nearly the same due the usage of the same API

Command and Alias | Description | Usage | Info
---------------|--------------|---------|--------
`feet` | feet content | `feet` |
`anal` | anal content | `anal` | 
`lewd` | lewd content | `lewd` |
`pussy` | pussy content | `pussy` |
`kiss` | kiss content | `kiss` | 
`blowjob` | blowjob content | `blowjob` |
`boobs` | boobs content | `boobs` |
`feed` | feed content | `feed` | 
`cum` | cum content | `cum` |
`holo` | holo content | `holo` |
`spank` | spank content | `spank` |
`poke` | poke content | `poke` |
`cuddle` | cuddle content | `cuddle` |
`classic` | classic content | `classic` |
`les` | les content | `les` |
`ero` | ero content | `ero` |
`smallboobs` | smallboobs | `smallboobs` | 
`kuni` | kuni content | `kuni` |
`tits` | tits content | `tits`



## slash commands ##

since the slash commands are quiet new, im still figuring out how to work best with them

**currently supported are:**

Command and Alias | Description | Usage | Info
---------------|---------------|--------|-------
`/ban` | ban the user as regual | `/ban test#1111 "playing fortnite"`| in source code marked as  "_removeuser_" but that doesnt matter
`/lock` | locks the channel for default role | `/lock "stop spamming guys"` | 
`/unlock` | unlock the channel back again | `/unlock "now another try"` | 
`/nick` | nicks the user | `/nick test#111 noob` | 
`/prefix` | change prefix if forgotten | `/prefix <new_prefi>` | **not working**
