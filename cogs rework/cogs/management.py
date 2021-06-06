import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions, BadArgument, MissingRequiredArgument, CommandInvokeError, has_permissions
import json
import os
import sys


class managementCog(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    @commands.command(aliases=['mod'])
    async def management(self, ctx):
        embed = discord.Embed(
            title="prefix before every command",
            color = discord.Color.magenta()
        )
        embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
        embed.add_field(name=":wastebasket: `clear <amount>`", value="Clears the chat", inline=True)
        embed.add_field(name=":foot: `kick <@mention> <reason>`", value="Kicks a user", inline=True)
        embed.add_field(name=":judge: `ban <@mention> <reason>`", value="Banns a user", inline=True)
        embed.add_field(name=":open_hands: `unban <name>#<diskriminator>`", value="Unbanns a user", inline=True)
        embed.add_field(name=":newspaper: `getbans`", value="Get active bans from the guild", inline=True)
        embed.add_field(name=":newspaper2: `bans`", value="See current bans with reason", inline=True)
        embed.add_field(name=":cowboy: `nick <@mention> <new_name>`", value="Change a user's nick", inline=True)
        embed.add_field(name=":clap: `give <@mention> <@role | id | name>`", value="Gives a user the role", inline=True)
        embed.add_field(name=":thumbsdown: `rmrank <name#diskriminator> <rolename>`", value="Removes a role from the user", inline=True)
        embed.add_field(name=":eyes: `moverole <@role> <int>`", value="Moves a role to the <int> place", inline=True)
        embed.add_field(name=":mechanic: `name <name>`", value="Changes the Server name", inline=True)
        embed.add_field(name=":technologist: `poll <text-for-poll> <vote1> <vote2>`", value="Make a poll", inline=True)
        embed.add_field(name=":paperclip: `log <limit>`", value="Saves the chat and send the File to chat", inline=True)
        embed.add_field(name=":man_mage: `delcat <category>`", value="Delete a category", inline=True)
        embed.set_footer(text="Help Box for the House Keeper Bot")

        await ctx.send(embed = embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True, administrator=True, manage_channels=True)
    async def clear(self, ctx, amount=13):
        await ctx.channel.purge(limit=amount + 1)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, MissingPermissions):

            embed = discord.Embed(
                title="Command Error",
                color=discord.Color.red()
            )

            embed.add_field(name=":thinking:", value="You are not allowed to clear the chat")

            await ctx.send(embed=embed)

    
    @commands.command()
    @commands.has_permissions(kick_members=True, administrator=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        embed = discord.Embed(
            title="User got kicked",
            color = discord.Color.green()
        )

        embed.add_field(name=":green_square:", value=f"User {member} got kicked")

        await ctx.send(embed=embed)


    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            embed = discord.Embed(
                title="Command Error",
                color=discord.Color.red()
            )

            embed.add_field(name=":thinking:", value="You don't have Permissions to kick people")

            await ctx.send(embed=embed)

    
        else:
            await ctx.send("An error occured :red_square:")

    

    
    #@commands.command()
    #@commands.has_permissions(ban_members=True, kick_members=True, administrator=True)
    #async def ban(self, ctx, member : discord.Member, *, reason=None):
    #    await member.ban(reason=reason)
    #    embed = discord.Embed(
    #        title="User got banned",
    #        color=discord.Color.green()
    #    )
    #    embed.add_field(name=":green_square:", value=f'User {member} got banned.')

    #    await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        try:
            if reason == None:

                await member.ban(reason=reason)
                await ctx.message.delete()

                embed = discord.Embed(
                    title="User got banned",
                    color = discord.Color.green()
                )
                embed.add_field(name=":green_square:", value=f"User {member} got banned")
                embed.add_field(name="Reason", value="No reason set")
                
                await ctx.send(embed=embed)

            else:
                await member.ban(reason=reason)
                await ctx.message.delete()

                embed = discord.Embed(
                    title="User got banned",
                    color = discord.Color.green()
                )
                embed.add_field(name=":green_square:", value=f"User {member} got banned")
                embed.add_field(name="Reason", value=reason)

                await ctx.send(embed=embed)

        except discord.Forbidden:
            await ctx.channel.send(f"Bot doesn't have enough permission to ban someone. Upgrade the Permissions")


    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            embed = discord.Embed(
                title="Command Error",
                color=discord.Color.red()
            )

            embed.add_field(name=":thinking:", value="You miss the ban member Permission")

            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True, administrator=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if(user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed = discord.Embed(
                    title="User got unbanned",
                    color=discord.Color.green()
                )

                embed.add_field(name=":green_square:", value=f'Unbanned {user.name}#{user.discriminator}')
                return

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            embed = discord.Embed(
                title="Command Error",
                color=discord.Color.red()
            )

            embed.add_field(name=":thinking:", value="You miss unban permissions")

            await ctx.send(embed=embed)

        else:
            await ctx.send("An error occured :red_square:")

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_nicknames=True, administrator=True)
    async def nick(self, ctx, member: discord.Member, nick):
        await member.edit(nick=nick)
        embed =discord.Embed(
            title="User got nicked",
            color=discord.Color.green()
        )

        embed.add_field(name=":green_square:", value=f'Nickname got changed to {member.mention}')
        await ctx.send(embed=embed)

    @nick.error
    async def nick_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            embed = discord.Embed(
                title="Command Error",
                color=discord.Color.red()
            )

            embed.add_field(name=":thinking:", value="You miss the Permission to nick people")

            await ctx.send(embed=embed)

    
        else:
            await ctx.send("An error occured :red_square:")

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_roles = True, administrator=True)
    async def give(self, ctx, user: discord.Member, role: discord.Role):
        try:

            await user.add_roles(role)
            await ctx.send(f"Hey {ctx.author.name}, {user.name} has been giving a role called: {role.name}")
        
        except Exception:
            await ctx.send("Error")

    @give.error
    async def give_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            embed = discord.Embed(
                title="Command Error",
                color=discord.Color.red()
            )

            embed.add_field(name=":thinking:", value="You miss the manage role permission")

            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_roles=True, administrator=True)
    async def moverole(self, ctx, role: discord.Role, pos: int):
        try:
            await role.edit(position=pos)
            await ctx.send("Role moved.")
        except discord.Forbidden:
            await ctx.send("You do not have permission to do that")
        except discord.HTTPException:
            await ctx.send("Failed to move role")
        except discord.InvalidArgument:
            await ctx.send("Invalid argument")

    @moverole.error
    async def moverole_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            embed = discord.Embed(
                title="Command Error",
                color=discord.Color.red()
        )

            embed.add_field(name=":thinking:", value="You miss the Permission to move roles")

            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_guild=True, administrator=True)
    async def name(self, ctx, name, member: discord.Member = None):
        await ctx.guild.edit(name=f"{name}")
        embed = discord.Embed(
            title="Guild rename",
            color = discord.Color.green()
        )
        embed.add_field(name=":green_square:", value=f"Successfully renamed to {name}")


    @name.error
    async def name_error(self, ctx, error):
        if isinstance(error, MissingPermissions):

            embed = discord.Embed(
                title="Command Error",
                color=discord.Color.red()
            )

            embed.add_field(name=":thinking:", value="You miss the manage guild permission")

            await ctx.send(embed=embed)


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def getbans(self, ctx):
 
        x = await ctx.message.guild.bans()
        x = '\n'.join([str(y.user) for y in x])
        embed = discord.Embed(title="List of Banned Members", description=x, colour=0xFFFFF)
        return await ctx.send(embed=embed)
    
    @getbans.error
    async def getbans_error(self, ctx, error):
        if isinstance(error, MissingPermissions):

            embed = discord.Embed(
                title="Command Error",
                color=discord.Color.red()
            )

            embed.add_field(name=":thinking:", value="You miss the ban members permission")

            await ctx.send(embed=embed)

    @commands.command()
    @has_permissions(ban_members=True)
    async def bans(self, ctx):
        users = await ctx.guild.bans()
        if len(users) > 0:
            msg = f'`{"ID":21}{"Name":25} Reason\n'
            for entry in users:
                userID = entry.user.id
                userName = str(entry.user)
                if entry.user.bot:
                    username = '🤖' + userName #:robot: emoji
                reason = str(entry.reason) #Could be None
                msg += f'{userID:<21}{userName:25} {reason}\n'
            embed = discord.Embed(color=0xe74c3c) #Red
            embed.set_thumbnail(url=ctx.guild.icon_url)
            embed.set_footer(text=f'Server: {ctx.guild.name}')
            embed.add_field(name='Ranks', value=msg + '`', inline=True)
            await ctx.send(embed=embed)
        else:
            await ctx.send('**:negative_squared_cross_mark:** There are no banned users!')

    @bans.error
    async def bans_error(self, ctx, error):
        if isinstance(error, MissingPermissions):

            embed = discord.Embed(
                title="Command Error",
                color=discord.Color.red()
            )

            embed.add_field(name=":thinking:", value="You miss the ban members permission")

            await ctx.send(embed=embed)


    @commands.command(pass_context=True, alies=['rmrole', 'removerole', 'removerank'])
    @commands.has_permissions(manage_roles = True)
    async def rmrank(self, ctx, member: discord.Member=None, *rankName: str):

        rank = discord.utils.get(ctx.guild.roles, name=' '.join(rankName))
        if member is not None:
            await member.remove_roles(rank)
            await ctx.send(f':white_check_mark: Role **{rank.name}** removed from **{member.name}** ')
        else:
            await ctx.send(':red_square: You have to specify a user!')
            
            
    @rmrank.error
    async def rmrank_error(self, ctx, error):
        if isinstance(error, MissingPermissions):

            embed = discord.Embed(
                title="Command Error",
                color=discord.Color.red()
            )

            embed.add_field(name=":thinking:", value="You miss the manage roles permission")

            await ctx.send(embed=embed)

    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def prefix(self, ctx, *, pre):
        with open ("prefixes.json", "r") as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = pre
        await ctx.send(f"New prefix is `{pre}`")

        with open ("prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)
            
            
    @prefix.error
    async def prefix_error(self, ctx, error):
        if isinstance(error, MissingPermissions):

            embed = discord.Embed(
                title="Command Error",
                color=discord.Color.red()
            )

            embed.add_field(name=":thinking:", value="You miss the administrator permission")

            await ctx.send(embed=embed)
            
    @commands.command()
    @has_permissions(manage_channels = True)
    async def delcat(self, ctx, category: discord.CategoryChannel, *, reason=None):
        await category.delete(reason=reason)
        await ctx.send(f"I deleted category {category.name} for you")

    @delcat.error
    async def delcat_error(self, ctx, error):
        if isinstance(error, MissingPermissions):

            embed = discord.Embed(
                title="Command Error",
                color=discord.Color.red()
            )

            embed.add_field(name=":thinking:", value="You miss the manage channels permission")

            await ctx.send(embed=embed)




    

def setup(bot):
    bot.add_cog(managementCog(bot))
