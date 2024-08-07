import discord
from discord.ext import commands
from discord import app_commands
import datetime


class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tree = bot.tree  # Use the existing CommandTree

        self.bot.loop.create_task(self.sync_commands())

    async def sync_commands(self):
        await self.bot.wait_until_ready()
        await self.tree.sync()

        # Interactions
    @commands.command()
    @commands.guild_only()
    async def slash(self, ctx):

        async with ctx.typing():


            embed=discord.Embed(title="/ before every command", color=0xf0d419)
            embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/443208943213477889/601699371221909504/imagesfidosfhdis.jpg?width=598&height=585")
            embed.add_field(name=":closed_lock_with_key: `ban <@mention> <reason>`", value="Ban a user", inline=True)
            embed.add_field(name=":ticket: `userinfo <@mention>`",value="Shows user related information", inline=True)
            embed.add_field(name=":face_with_monocle: `permissions <@mention>`" ,value="Check a users permission's", inline=True)
            embed.add_field(name=":no_mouth: `avatar <@mention>`", value="Profile Picture of the User in PNG", inline=True)
            embed.add_field(name=":computer: `youtube <search>`", value="Search something on youtube", inline=True)
            embed.add_field(name=":lock: `lock <channel> <reason>`", value="Lockdown a channel", inline=True)
            embed.add_field(name=":unlock: `unlock <channel> <reason>`", value="Unlock a channel" ,inline=True)
            embed.set_footer(text="Help Box for the House Keeper Bot")
            embed.set_footer(text="Help Box for the House Keeper Bot")

            await ctx.reply(embed=embed, mention_author = False)


    @app_commands.guild_only()
    @app_commands.default_permissions(ban_members=True)
    @app_commands.command(name="ban", description="Ban a user")
    async def ban(self, interaction: discord.Interaction, member: discord.Member,reason: str=None):
        execution_time = datetime.datetime.now()

        if interaction.user == member:
            embed=discord.Embed(
                title="Dont ban yourself :(",
                color=discord.Color.yellow()
            )
            embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
            embed.set_image(url="https://cdn.discordapp.com/attachments/1268538785340063755/1268866182077743115/blender-annoying-orange.gif?ex=66adfb38&is=66aca9b8&hm=b6f26472dc030d5f35fc904f870202168b8b0e22ae545b31b3ae19af7d22a949&")
            await interaction.response.send_message(embed=embed)
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
            await interaction.response.send_message(embed=embed)

        # Using the Audit-Log to verify if the user really got bannned
        async for entry in interaction.guild.audit_logs(action=discord.AuditLogAction.ban, user=interaction.guild.me, after=execution_time):
            if entry.target == member:
                
                embed = discord.Embed(
                title=f"{member} got banned",
                color = discord.Color.green()
            )
                embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
                embed.set_footer(text=f"Banned by {interaction.user}")
                embed.set_image(url="https://cdn.discordapp.com/attachments/1268538785340063755/1268880199064358993/bane-no-ezgif.com-video-to-gif-converter.gif?ex=66ae0846&is=66acb6c6&hm=256758cd112e1450616371d32282b32836facf1088358284579e196abcd3ba48&")
                await interaction.response.send_message(embed=embed)
                # sending a DM to the banned user 
                dmembed = discord.Embed(
                    title=f"You got banned from `{interaction.guild}`",
                    color=discord.Color.orange()
                )
                dmembed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
                dmembed.add_field(name="Reason", value=f"{entry.reason}")
                await member.send(embed=dmembed)


    @app_commands.guild_only()
    @app_commands.command(name="userinfo", description="Get user informations")
    @app_commands.guild_only()
    async def userinfo(self, interaction: discord.Interaction, member: discord.Member=None):
        try:

            embed = discord.Embed(
                color= member.color
            )

            embed.set_author(name=f"User Info for {member.display_name}", icon_url=member.display_avatar.url)
            embed.set_thumbnail(url=member.display_avatar.url)
            embed.set_footer(text=f"Requested from {interaction.user.mention} | {interaction.user.id}")

            embed.add_field(name="User", value=f"{member.mention}")
            embed.add_field(name="ID", value=member.id)
            embed.add_field(name="Permissions", value=f"Use `/permissions`")
            if member.bot == False:
                embed.add_field(name="Bot ?", value="No")
            else:
                embed.add_field(name="Bot ?", value="Yes")

            embed.add_field(name="Account Created at", value=member.created_at.strftime('%Y-%m-%d %H:%M:%S'))
            embed.add_field(name="Server joined at", value=member.joined_at.strftime('%Y-%m-%d %H:%M:%S'))
            if member.premium_since == None:
                embed.add_field(name="Booster since", value="Never")
            else:

                embed.add_field(name="Booster since", value=member.premium_since.strftime('%Y-%m-%d %H:%M:%S'))


            await interaction.response.send_message(embed=embed)

        except discord.errors.HTTPException:
            pass

    @app_commands.command(name="permissions", description="Get a user's permissions")
    @app_commands.guild_only()
    async def permissions(self, interaction: discord.Interaction, member: discord.Member=None):
        try:

            embed = discord.Embed(
                color= member.color
            )
            perms = member.guild_permissions
            perm_list = [perm for perm, value in perms if value]  # Listet alle Berechtigungen auf, die auf True gesetzt sind
            perm_string = ", ".join(perm_list)
            try:

                embed.set_author(name=f"Permission info for {member.display_name}", icon_url=member.display_avatar.url)
            except AttributeError:
                pass
            
            embed.set_thumbnail(url=member.display_avatar.url)
            embed.set_footer(text=f"Requested from {interaction.user} | {interaction.user.id}")

            embed.add_field(name="Permissions", value=perm_string)

            await interaction.response.send_message(embed=embed)
        except discord.errors.HTTPException:
            pass

    @app_commands.command(name="avatar", description="Get a user's avatar")
    @app_commands.guild_only()
    async def avatar(self, interaction: discord.Interaction, member: discord.Member=None):
        if member == interaction.user:
            embed = discord.Embed(
            title=f"Here is your avatar, {interaction.user}",
            color=member.color
        )
            embed.set_footer(text=f"Requested by {interaction.user}")
            embed.set_image(url=f"{interaction.user.avatar.url}")
            try:
                embed.set_author(name=f"{member.guild}", icon_url=f"{member.guild.icon.url}")
            except AttributeError:
                pass

        if member == interaction.client.user:
            embed = discord.Embed(
            title=f"Here is my avatar, {interaction.user}",
            color=member.color
            )
            embed.set_footer(text=f"Requested by {interaction.user}")
            embed.set_image(url=f"{member.avatar.url}")
            try:
                embed.set_author(name=f"{member.guild}", icon_url=f"{member.guild.icon.url}")
            except AttributeError:
                pass

        else:
            embed = discord.Embed(
            title=f"Here is the avatar of, {member}",
            color=member.color
            )
            embed.set_footer(text=f"Requested by {interaction.user}")
            embed.set_image(url=f"{member.avatar.url}")
            try:
                embed.set_author(name=f"{member.guild}", icon_url=f"{member.guild.icon.url}")
            except AttributeError:
                pass

        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="youtube", description="Search for a video on youtube")
    @app_commands.guild_only()
    async def youtube(self, interaction: discord.Interaction, *, search: str):
        from urllib import parse, request
        import re
        try:


            query_string = parse.urlencode({'search_query': search})
            html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
            search_results = re.findall( r"watch\?v=(\S{11})", html_content.read().decode())
            await interaction.response.send_message('https://www.youtube.com/watch?v=' + search_results[0])

        except Exception as e:
            await interaction.response.send_message(e)


    @app_commands.command(name="lock", description="Lockdown a channel")
    @app_commands.guild_only()
    @app_commands.default_permissions(manage_channels=True)
    async def lock(self, interaction: discord.Interaction, channel: discord.TextChannel, reason: str):
        await channel.set_permissions(
                    interaction.guild.default_role,
                    send_messages=False
                    )
        
        embed = discord.Embed(
            title=":lock: Channel has been locked!",
            color=discord.Color.green()
            )
        embed.add_field(name=f"{interaction.user} has locked {channel.mention}!",value=f"Reason: {reason}")
        embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
        embed.set_image(url="https://cdn.discordapp.com/attachments/1185379683072741436/1270692180205375498/devil-or-your-angel-cat.gif?ex=66b49fd0&is=66b34e50&hm=54e866f18974f3087d9c6e3f6e2d86074f6eab9f6c9858a4cc8be38016b865ba&")
        
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="unlock", description="allow messages in the channel again")
    @app_commands.guild_only()
    @app_commands.default_permissions(manage_channels=True)
    async def unlock(self, interaction: discord.Interaction, channel: discord.TextChannel, reason: str):
        await channel.set_permissions(
                    interaction.guild.default_role,
                    send_messages=True
                    )
        
        embed = discord.Embed(
            title=":unlock: Channel has been unlocked!",
            color=discord.Color.green()
            )
        embed.add_field(name=f"{interaction.user} has unlocked {channel.mention}!",value=f"Reason: {reason}")
        embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
        embed.set_image(url="https://media.discordapp.net/attachments/1036690507604168774/1152543409639268432/SPOILER_7DFBB949-DB82-4D5A-A400-BE6AEDAC1F7A.gif?ex=66b49632&is=66b344b2&hm=35fe80a4029b93d02b0c68ef44f64a7e426b8377da27025ee2fbe872d8e8c8a9&")
        
        await interaction.response.send_message(embed=embed)



async def setup(bot):
    await bot.add_cog(Slash(bot))
