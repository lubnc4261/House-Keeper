import random
import asyncio

import discord
from discord.ext import commands
from games import hangman, minesweeper, tictactoe, wumpus

class Game(commands.Cog):

    def __init__(self, bot):
        self.bot = bot



    @commands.command()
    async def game(self, ctx):
        embed = discord.Embed(
            title="prefix before every command",
            color = discord.Color.gold()
        )

        embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
        embed.add_field(name=":knot: `hangman`", value="Play hangman in the chat", inline=True)
        embed.add_field(name=":bomb: `minesweeper <colm> <row> <bomb>`", value="Play minesweeper", inline=True)
        embed.add_field(name=":scissors: `rps`", value="Play rock paper scissors", inline=True)
        embed.add_field(name=":family: `teams <ammount>`", value="Create a team for the **voice channel**", inline=True)
        embed.add_field(name=":jigsaw: `ttt`", value="Play tic tac toe", inline=True)
        embed.set_footer(text="Help Box for the House Keeper Bot")

        await ctx.send(embed=embed)


    @commands.command(name='hangman', aliases=['hang'])
    async def hangman(self, ctx):
        """Play Hangman"""
        await hangman.play(self.bot, ctx)

    @commands.command(name='minesweeper', aliases=['ms'])
    async def minesweeper(self, ctx, columns = None, rows = None, bombs = None):
        """Play Minesweeper"""
        await minesweeper.play(ctx, columns, rows, bombs)


    @commands.command(name='rps', aliases=['rockpaperscissors'])
    async def rps(self, ctx):
        """Play Rock, Paper, Scissors game"""
        def check_win(p, b):
            if p=='🌑':
                return False if b=='📄' else True
            if p=='📄':
                return False if b=='✂' else True
            # p=='✂'
            return False if b=='🌑' else True

        async with ctx.typing():
            reactions = ['🌑', '📄', '✂']
            game_message = await ctx.send("**Rock Paper Scissors**\nChoose your shape:", delete_after=15.0)
            for reaction in reactions:
                await game_message.add_reaction(reaction)
            bot_emoji = random.choice(reactions)

        def check(reaction, user):
            return user != self.bot.user and user == ctx.author and (str(reaction.emoji) == '🌑' or '📄' or '✂')
        try:
            reaction, _ = await self.bot.wait_for('reaction_add', timeout=10.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send("Time's Up! :stopwatch:")
        else:
            await ctx.send(f"**:man_in_tuxedo_tone1:\t{reaction.emoji}\n:robot:\t{bot_emoji}**")
            # if conds
            if str(reaction.emoji) == bot_emoji:
                await ctx.send("**It's a Tie :ribbon:**")
            elif check_win(str(reaction.emoji), bot_emoji):
                await ctx.send("**You win :sparkles:**")
            else:
                await ctx.send("**I win :robot:**")


    @commands.command(name='teams', aliases=['team'])
    async def teams(self, ctx, num=2):
        """Makes random teams with specified number(def. 2)"""
        if not ctx.author.voice:
            return await ctx.send("You are not connected to a voice channel :mute:")
        members = ctx.author.voice.channel.members
        memnames = []
        for member in members:
            memnames.append(member.name)

        remaining = memnames
        if len(memnames)>=num:
            for i in range(num):
                team = random.sample(remaining,len(memnames)//num)
                remaining = [x for x in remaining if x not in team]
                await ctx.send(f"Team {chr(65+i)}\n" + "```CSS\n" + '\n'.join(team) + "\n```")
        if len(remaining)> 0:
            await ctx.send("Remaining\n```diff\n- " + '\n- '.join(remaining) + "\n```")


    @commands.command(name='tictactoe', aliases=['ttt'])
    async def ttt(self, ctx):
        """Play Tic-Tac-Toe"""
        await tictactoe.play_game(self.bot, ctx, chance_for_error=0.2)


    @commands.command(name='wumpus')
    async def _wumpus(self, ctx):
        """Play Wumpus game"""
        await wumpus.play(self.bot, ctx)


def setup(bot):
    bot.add_cog(Game(bot))