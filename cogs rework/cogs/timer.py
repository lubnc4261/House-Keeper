import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions, BadArgument, MissingRequiredArgument, CommandInvokeError, has_permissions
import time
import datetime
import asyncio
from datetime import datetime, timedelta
import os
import platform
import re
import inspect
import textwrap
from collections import Counter


class TimeParser:
    def __init__(self, argument):
        compiled = re.compile(r"(?:(?P<hours>[0-9]{1,5})h)?(?:(?P<minutes>[0-9]{1,5})m)?(?:(?P<seconds>[0-9]{1,5})s)?$")
        self.original = argument
        try:
            self.seconds = int(argument)
        except ValueError as e:
            match = compiled.match(argument)
            if match is None or not match.group(0):
                raise commands.BadArgument('Wrong time allowed are eg. `4h`, `3m` oder `2s`') from e

            self.seconds = 0
            hours = match.group('hours')
            if hours is not None:
                self.seconds += int(hours) * 3600
            minutes = match.group('minutes')
            if minutes is not None:
                self.seconds += int(minutes) * 60
            seconds = match.group('seconds')
            if seconds is not None:
                self.seconds += int(seconds)

        if self.seconds <= 0:
            raise commands.BadArgument('Zu wenig Zeit angegeben, gültig sind z.B. `4h`, `3m` oder `2s`')

        if self.seconds > 604800: # 7 days
            raise commands.BadArgument('7 Tage sind ne lange Zeit, denkste du nicht auch?')

    @staticmethod
    def human_timedelta(dt):
        now = datetime.utcnow()
        delta = now - dt
        hours, remainder = divmod(int(delta.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        years, days = divmod(days, 365)

        if days:
            if hours:
                return '%s und %s' % (Plural(Tag=days), Plural(Stunde=hours))
            return Plural(day=days)

        if hours:
            if minutes:
                return '%s und %s' % (Plural(Stunde=hours), Plural(Minute=minutes))
            return Plural(hour=hours)

        if minutes:
            if seconds:
                return '%s und %s' % (Plural(Minute=minutes), Plural(Sekunde=seconds))
            return Plural(Minute=minutes)
        return Plural(Sekunde=seconds)

class Plural:
    def __init__(self, **attr):
        iterator = attr.items()
        self.name, self.value = next(iter(iterator))

    def __str__(self):
        v = self.value
        if v > 1:
            return '%s %sn' % (v, self.name)
        return '%s %s' % (v, self.name)



class timerCog(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    @commands.command(aliases=['reminder'])
    @commands.cooldown(1, 30, commands.cooldowns.BucketType.user)
    async def timer(self, ctx, time : TimeParser, *, message=''):




            # HELP IN UTILITIES






        reminder = None
        completed = None
        message = message.replace('@everyone', '@\u200beveryone').replace('@here', '@\u200bhere')

        if not message:
            reminder = ':timer: Ok {0.mention}, set timer on {1}.'
            completed = ':alarm_clock: Ding Ding Ding {0.mention}! Your timer expired.'
        else:
            reminder = ':timer: Ok {0.mention}, set a timer for `{2}` on {1}.'
            completed = ':alarm_clock: Ding Ding Ding {0.mention}! Timer for `{1}` expired.'

        human_time = datetime.utcnow() - timedelta(seconds=time.seconds)
        human_time = TimeParser.human_timedelta(human_time)
        await ctx.send(reminder.format(ctx.author, human_time, message))
        await asyncio.sleep(time.seconds)
        await ctx.send(completed.format(ctx.author, message, human_time))

    @timer.error
    async def timer_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(str(error))
        elif isinstance(error, commands.errors.CommandOnCooldown):
            seconds = str(error)[34:]
            await ctx.send(f':alarm_clock: Cooldown! Try it in {seconds} again')





def setup(bot):
    bot.add_cog(timerCog(bot))