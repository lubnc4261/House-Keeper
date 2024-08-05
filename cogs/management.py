import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions, BadArgument, MissingRequiredArgument, CommandInvokeError, has_permissions
import json
import datetime
import re

# prettify the result from the getbans command


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
        embed.add_field(name=":open_hands: `unban <name>`", value="Unbanns a user", inline=True)
        embed.add_field(name=":cowboy: `nick <@mention> <new_name>`", value="Change a user's nick", inline=True)
        embed.add_field(name=":clap: `give <@mention> <@role>`", value="Gives a user the role", inline=True)
        embed.add_field(name=":thumbsdown: `rmrank <name> <rolename>`", value="Removes a role from the user", inline=True)
        embed.add_field(name=":eyes: `moverole <@role> <int>`", value="Moves a role to the <int> place", inline=True)
        embed.add_field(name=":mechanic: `name <name>`", value="Changes the Server name", inline=True)
        embed.add_field(name=":paperclip: `log <limit>`", value="Saves the chat and send the File to chat", inline=True)
        embed.add_field(name=":paperclip: `savemembers`", value="Saves all members and send the File in channel", inline=True)
        embed.add_field(name=":man_mage: `delcat <category>`", value="Delete a category", inline=True)
        embed.set_footer(text="Help Box for the House Keeper Bot")

        await ctx.reply(embed=embed,mention_author=False)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=10):
        await ctx.channel.purge(limit=amount + 1)


    
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        # Dont get a spam of possible kick events from the past
        execution_time = datetime.datetime.now()

        if ctx.message.author == member:
            embed=discord.Embed(
                title="Dont kick yourself :(",
                color=discord.Color.yellow()
            )
            embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
            embed.set_image(url="https://cdn.discordapp.com/attachments/1268538785340063755/1268866182077743115/blender-annoying-orange.gif?ex=66adfb38&is=66aca9b8&hm=b6f26472dc030d5f35fc904f870202168b8b0e22ae545b31b3ae19af7d22a949&")
            await ctx.reply(embed=embed,mention_author=False)
            # blocking the discord.Forbidden Error message
            return
        try:

            await member.kick(reason=reason)
        except discord.Forbidden:
            embed = discord.Embed(
                    title=f"I could not kick {member}",
                    color=discord.Color.red()
                )
            embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
            embed.add_field(name="Reason", value=f"{member} has more rights than i have")
            embed.set_image(url="https://cdn.discordapp.com/attachments/1268538785340063755/1268870776615075841/cat-mod.gif?ex=66adff7f&is=66acadff&hm=3d6e39b6b8a1dc2524851f3201e479dd38734ed97c2d3fe4012a302e74b9916d&")
            await ctx.reply(embed=embed,mention_author=False)

        # Using the Audit-Log to verify if the user really got kicked
        async for entry in ctx.guild.audit_logs(action=discord.AuditLogAction.kick, user=ctx.guild.me, after=execution_time):
            if entry.target == member:
                
                embed = discord.Embed(
                title=f"{member} got kicked",
                color = discord.Color.green()
            )
                embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
                embed.set_footer(text=f"Kicked by {ctx.message.author}")
                embed.set_image(url="https://blogs-images.forbes.com/kevinmurnane/files/2018/10/Spartan-Kick_Ubisoft.png")
                await ctx.reply(embed=embed,mention_author=False)
                # sending a DM to the kicked user 
                dmembed = discord.Embed(
                    title=f"You got kicked from `{ctx.guild}`",
                    color=discord.Color.orange()
                )
                dmembed.add_field(name="Reason", value=f"{entry.reason}")
                await member.send(embed=dmembed)



    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        execution_time = datetime.datetime.now()

        if ctx.message.author == member:
            embed=discord.Embed(
                title="Dont ban yourself :(",
                color=discord.Color.yellow()
            )
            embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
            embed.set_image(url="https://cdn.discordapp.com/attachments/1268538785340063755/1268866182077743115/blender-annoying-orange.gif?ex=66adfb38&is=66aca9b8&hm=b6f26472dc030d5f35fc904f870202168b8b0e22ae545b31b3ae19af7d22a949&")
            await ctx.reply(embed=embed,mention_author=False)
            # blocking the discord.Forbidden Error message
            return
        try:

            await member.ban(reason=reason)
        except discord.Forbidden:
            embed = discord.Embed(
                    title=f"I could not ban {member}",
                    color=discord.Color.red()
                )
            embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
            embed.add_field(name="Reason", value=f"{member} has more rights than i have")
            embed.set_image(url="https://cdn.discordapp.com/attachments/1268538785340063755/1268870776615075841/cat-mod.gif?ex=66adff7f&is=66acadff&hm=3d6e39b6b8a1dc2524851f3201e479dd38734ed97c2d3fe4012a302e74b9916d&")
            await ctx.reply(embed=embed,mention_author=False)

        # Using the Audit-Log to verify if the user really got bannned
        async for entry in ctx.guild.audit_logs(action=discord.AuditLogAction.ban, user=ctx.guild.me, after=execution_time):
            if entry.target == member:
                
                embed = discord.Embed(
                title=f"{member} got banned",
                color = discord.Color.green()
            )
                embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
                embed.set_footer(text=f"Banned by {ctx.message.author}")
                embed.set_image(url="https://cdn.discordapp.com/attachments/1268538785340063755/1268880199064358993/bane-no-ezgif.com-video-to-gif-converter.gif?ex=66ae0846&is=66acb6c6&hm=256758cd112e1450616371d32282b32836facf1088358284579e196abcd3ba48&")
                await ctx.reply(embed=embed)
                # sending a DM to the banned user 
                dmembed = discord.Embed(
                    title=f"You got banned from `{ctx.guild}`",
                    color=discord.Color.orange()
                )
                dmembed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
                dmembed.add_field(name="Reason", value=f"{entry.reason}")
                await member.send(embed=dmembed)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, user: discord.User, *, reason=None):
        execution_time = datetime.datetime.now()
        # discord.Member would be wrong because it isnt a member (yet), just a user
        try:

            await ctx.guild.unban(user, reason=reason)
        except discord.NotFound:
            embed = discord.Embed(
                    title=f"{user} is not banned",
                    color=discord.Color.red()
                )
            embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
            embed.set_image(url="https://media.discordapp.net/attachments/1268538785340063755/1268892955037532250/cat_lookingcats.gif?ex=66ae1427&is=66acc2a7&hm=a8caa93f74c3fb5a3f0afe1594bf9f0979912c8ad4889a8520bbe054222fa741&=")
            embed.set_footer(text="user not banned")
            await ctx.reply(embed=embed,mention_author=False)

        async for entry in ctx.guild.audit_logs(action=discord.AuditLogAction.unban, user=ctx.guild.me, after=execution_time):
            if entry.target == user:
                embed = discord.Embed(
                    title=f"{user} got unbanned",
                    color=discord.Color.green()
                )
                embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
                embed.set_image(url="https://cdn.discordapp.com/attachments/1268538785340063755/1268891693634027571/cat-cat-jumping.gif?ex=66ae12fa&is=66acc17a&hm=89d34af4d3f170a8ae2ff2e5a3c60cd994188e01e4f4e2eac10df64061b039a6&")
                embed.set_footer(text=f"Unbanned by {ctx.message.author}")
                await ctx.reply(embed=embed,mention_author=False)
                break


    @commands.command(pass_context=True)
    @commands.guild_only()
    @commands.has_permissions(manage_nicknames=True)
    async def nick(self, ctx, member: discord.Member, nick):
        execution_time = datetime.datetime.now()
        before = member

        try:

            await member.edit(nick=nick)
        except discord.Forbidden:
            embed = discord.Embed(
                    title=f"I could not nick {member}",
                    color=discord.Color.red()
                )
            embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
            embed.add_field(name="Reason", value=f"{member} has more rights than i have")
            embed.set_image(url="https://cdn.discordapp.com/attachments/1268538785340063755/1268870776615075841/cat-mod.gif?ex=66adff7f&is=66acadff&hm=3d6e39b6b8a1dc2524851f3201e479dd38734ed97c2d3fe4012a302e74b9916d&")
            await ctx.reply(embed=embed,mention_author=False)

        async for entry in ctx.guild.audit_logs(action=discord.AuditLogAction.member_update, user=ctx.guild.me, after=execution_time):
            if entry.target == member:
                embed =discord.Embed(
                title=f'Nickname got changed from {before}',
                color=discord.Color.green()
            )
                embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
                embed.set_image(url="https://media.discordapp.net/attachments/1268538785340063755/1268909367110013010/angry-cat.gif?ex=66ae2370&is=66acd1f0&hm=8082c52c9e6fbbdf91a4c1cce01538741ad2db92b1e5e427a96835ca6c5447eb&=")
                embed.add_field(name="To: ", value=f"{member.mention}")
                embed.set_footer(text=f"Nicked by {ctx.message.author}")
                await ctx.reply(embed=embed,mention_author=False)


    @commands.command(pass_context=True)
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True, administrator=True)
    async def give(self, ctx, user: discord.Member, role: discord.Role):
        execution_time = datetime.datetime.now()
        try:

            await user.add_roles(role)
        except discord.Forbidden:
            embed = discord.Embed(
                    title=f"I could not give {user} : {role}",
                    color=discord.Color.red()
                )
            embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
            embed.add_field(name="Reason", value=f"`{role}` is higher than my own role")
            embed.set_image(url="https://cdn.discordapp.com/attachments/1268538785340063755/1268926384810491915/idk.gif?ex=66ae3349&is=66ace1c9&hm=4aaebc591aba2e68a205d5875cd5123f412b0e86fc6711bf4eeb6bcb971d4816&")
            await ctx.reply(embed=embed,mention_author=False)


        async for entry in ctx.guild.audit_logs(action=discord.AuditLogAction.member_role_update, user=ctx.guild.me, after=execution_time):
            if entry.target == user:
                embed = discord.Embed(
                    title=f"{user} successfully got: {role}",
                    color=discord.Color.green()
                )
                embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
                embed.set_image(url="https://cdn.discordapp.com/attachments/1268538785340063755/1268925636043477102/queen-royalty.gif?ex=66ae3297&is=66ace117&hm=ea9c8cffadbb1aee7f5ceadfb010ef132e153b690b0a01fbb6785d69f89e124d&")
                embed.set_footer(text=f"Role granted by {ctx.message.author}")

                await ctx.send(embed=embed,mention_author=False)


    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    async def moverole(self, ctx, role: discord.Role, pos: int):
            if type(pos) == int:
                try:
                    await role.edit(position=pos)

                except discord.Forbidden:
                    embed = discord.Embed(
                    title=f"I could not move {role}",
                    color=discord.Color.red()
                    )
                    embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
                    embed.add_field(name="Reason", value=f"{pos} is higher than my own role")
                    embed.set_footer(text=f"Move requested by {ctx.message.author}")
                    embed.set_image(url="https://cdn.discordapp.com/attachments/1268538785340063755/1268926384810491915/idk.gif?ex=66ae3349&is=66ace1c9&hm=4aaebc591aba2e68a205d5875cd5123f412b0e86fc6711bf4eeb6bcb971d4816&")
                    await ctx.reply(embed=embed,mention_author=False)
                    #return stops the success embed from sending if pos = role.position by default
                    return

                if role.position == pos:
                    embed = discord.Embed(
                        title=f"Moved the role {role} to place {pos}",
                        color=discord.Color.green()
                    )
                    embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
                    embed.set_footer(text=f"Move requested by {ctx.message.author}")
                    embed.set_image(url="https://media.discordapp.net/attachments/1268538785340063755/1268931552939737219/viralhog-cats.gif?ex=66ae3819&is=66ace699&hm=f703b0441f8ef57b5fe99b6b893e9c03942e6a4dafc3faeedc527439b7bee1a1&=")
                    await ctx.reply(embed=embed,mention_author=False)
 

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_guild=True)
    async def name(self, ctx, name):
        if name == ctx.guild.name:
            embed = discord.Embed(
                title=f"Guild is already called {name}",
                color=discord.Color.orange()
            )
            embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
            embed.set_footer(text=f"Guild rename requested by {ctx.author.name}")
            embed.set_image(url="https://media.discordapp.net/attachments/1268538785340063755/1268892955037532250/cat_lookingcats.gif?ex=66ae1427&is=66acc2a7&hm=a8caa93f74c3fb5a3f0afe1594bf9f0979912c8ad4889a8520bbe054222fa741&=")
            await ctx.reply(embed=embed,mention_author=False)
            return
        else:

            await ctx.guild.edit(name=f"{name}")

            embed = discord.Embed(
                title=f"Guild renamed to {name}",
                color = discord.Color.green()
            )
            embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
            embed.set_image(url="https://media.discordapp.net/attachments/1268538785340063755/1268936740006002799/no-maam-what-it-do-baby.gif?ex=66ae3cee&is=66aceb6e&hm=6b62c94ad451144385a6197eb67b05f86f5721720de05628de6819c95e7c6723&=")
            embed.set_footer(text=f"Guild rename requested by {ctx.message.author}")

            await ctx.reply(embed=embed,mention_author=False)


    @commands.command(pass_context=True, alies=['rmrole', 'removerole', 'removerank'])
    @commands.has_permissions(manage_roles = True)
    @commands.guild_only()
    async def rmrank(self, ctx, member: discord.Member, rank: discord.Role):
        execution_time = datetime.datetime.now()
        try:
            await member.remove_roles(rank)
        except discord.HTTPException:
            await ctx.reply("Role doesnt exist")

        async for entry in ctx.guild.audit_logs(action=discord.AuditLogAction.member_role_update, user=ctx.guild.me, after=execution_time):
            if entry.target == member and rank in entry.before.roles and rank not in entry.after.roles:
                await ctx.reply("Successfully removed")

        

    
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def prefix(self, ctx, *, pre):
        with open ("prefixes.json", "r") as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = pre
        await ctx.reply(f"New prefix is `{pre}`",mention_author=False)

        with open ("prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)
            

    @commands.command(pass_context=True)
    @commands.guild_only()
    @has_permissions(manage_channels = True)
    async def delcat(self, ctx, category: discord.CategoryChannel, *, reason=None):
        execution_time = datetime.datetime.now()
        try:

            for channel in category.channels:

                await channel.delete(reason=reason)
                

            await  category.delete(reason=reason)

        except discord.Forbidden:
            await ctx.send("Forbidden")

        async for entry in ctx.guild.audit_logs(action=discord.AuditLogAction.channel_delete, user=ctx.guild.me, after=execution_time):
            if entry.target == category:
                embed=discord.Embed(
                title=f"Removed category: {category.name}",
                color=discord.Color.green()
            )
                embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
                embed.set_footer(f"Category removed by {ctx.message.author}")
                embed.set_image(url="https://cdn.discordapp.com/attachments/1268538785340063755/1268947421199597608/chick-fil-a-no-chick-fil-a-sauce.gif?ex=66ae46e1&is=66acf561&hm=a71e15868a68bb0b1ac68816dd2d3737e8e327c244ae70b032090226df5714de&")
                await ctx.reply(embed=embed,mention_author=False)
            
    @commands.command()
    @commands.guild_only()
    @has_permissions(ban_members=True)
    async def softban(self, ctx, member: discord.Member, *, reason=""):
        execution_time = datetime.datetime.now()

        if ctx.message.author == member:
            embed=discord.Embed(
                title="Dont ban yourself :(",
                color=discord.Color.yellow()
            )
            embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
            embed.set_image(url="https://cdn.discordapp.com/attachments/1268538785340063755/1268866182077743115/blender-annoying-orange.gif?ex=66adfb38&is=66aca9b8&hm=b6f26472dc030d5f35fc904f870202168b8b0e22ae545b31b3ae19af7d22a949&")
            await ctx.reply(embed=embed,mention_author=False)
            # blocking the discord.Forbidden Error message
            return
        try:

            await member.ban(reason=reason)
            await ctx.guild.unban(member)

        except discord.Forbidden:
            embed = discord.Embed(
                    title=f"I could not softban {member}",
                    color=discord.Color.red()
                )
            embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
            embed.add_field(name="Reason", value=f"{member} has more rights than i have")
            embed.set_image(url="https://cdn.discordapp.com/attachments/1268538785340063755/1268870776615075841/cat-mod.gif?ex=66adff7f&is=66acadff&hm=3d6e39b6b8a1dc2524851f3201e479dd38734ed97c2d3fe4012a302e74b9916d&")
            await ctx.reply(embed=embed,mention_author=False)


        async for entry in ctx.guild.audit_logs(action=discord.AuditLogAction.ban, user=ctx.guild.me, after=execution_time):
            if entry.target == member:
                
                embed = discord.Embed(
                title=f"{member} got softbanned",
                color = discord.Color.green()
            )
                embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
                embed.set_footer(text=f"Banned by {ctx.message.author}")
                embed.set_image(url="https://cdn.discordapp.com/attachments/1268538785340063755/1268880199064358993/bane-no-ezgif.com-video-to-gif-converter.gif?ex=66ae0846&is=66acb6c6&hm=256758cd112e1450616371d32282b32836facf1088358284579e196abcd3ba48&")
                await ctx.send(embed=embed)
                # sending a DM to the banned user 
                dmembed = discord.Embed(
                    title=f"You got softbanned from `{ctx.guild}` you can directly rejoin",
                    color=discord.Color.orange()
                )
                dmembed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
                dmembed.add_field(name="Reason", value=f"{entry.reason}")
                await member.send(embed=dmembed)

    @commands.command()
    @commands.guild_only()
    @has_permissions(administrator=True)
    async def setuplog(self, ctx):

        guild = ctx.guild

            
        overwrites = {
                guild.default_role: discord.PermissionOverwrite(send_messages=False),
                guild.me: discord.PermissionOverwrite(send_messages=True)
        }


        await ctx.guild.create_text_channel("hk-logging", overwrites=overwrites, reason="logs")

        await ctx.send("Created the logging channel")






    
async def setup(bot):
    await bot.add_cog(managementCog(bot))
