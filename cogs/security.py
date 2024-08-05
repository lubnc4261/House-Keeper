import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions, BadArgument, MissingRequiredArgument, CommandInvokeError
import asyncio

class securityCog(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    @commands.command()
    async def security(self, ctx):
        embed = discord.Embed(
            title="prefix before every command",
            color = discord.Color.red()
        )
        embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
        embed.add_field(name=":red_square: `block <@mention>`", value="Blocks a user from the chanenl", inline=True)
        embed.add_field(name=":green_square: `unblock <@mention>`", value="Unblock the user from the channel", inline=True)
        embed.set_footer(text="Server Security from the House Keeper Bot")

        await ctx.send(embed=embed)


    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def block(self, ctx, member: discord.Member):
        # check if he is blocked
        permission = ctx.channel.permissions_for(member)
        if permission.send_messages:
            pass
        else:
            embed = discord.Embed(
                    title=f"{member} is already blocked",
                    color=discord.Color.red()
                )
            embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
            embed.set_image(url="https://media.discordapp.net/attachments/1268538785340063755/1268892955037532250/cat_lookingcats.gif?ex=66ae1427&is=66acc2a7&hm=a8caa93f74c3fb5a3f0afe1594bf9f0979912c8ad4889a8520bbe054222fa741&=")
            embed.set_footer(text=f"block requested by {ctx.message.author}")
            await ctx.reply(embed=embed,mention_author=False)
            return

        try:
            await ctx.channel.set_permissions(member, read_messages=True,
                                                    send_messages=False)

            embed = discord.Embed(
                title="Successfully",
                color = discord.Color.green()
            )
            embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
            embed.add_field(name=":white_check_mark:", value=f"{member.mention} is not able to send messages into **{ctx.channel}** anymore")
            embed.add_field(name="**Note**", value=f"If {member.mention} has the manage_roles permission he can unmute himself")
            embed.set_footer(text=f"Member block requested by {ctx.author}")
            embed.set_image(url="https://cdn.discordapp.com/attachments/1268177354614640661/1269322982065705081/bingus-silencio.gif?ex=66afa4a5&is=66ae5325&hm=ab9f4e45ce4aa31f2386c7fcd75119bc7edd1e5ccbbe4e3d1041e33907b66c6b&")
            await ctx.reply(embed=embed,mention_author=False)

        # wont ever gets executed thats why i added the Note section above
        except discord.Forbidden:
            embed = discord.Embed(
                    title=f"I could not block {member}",
                    color=discord.Color.red()
                )
            embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
            embed.add_field(name="Reason", value=f"{member} has more rights than i have")
            embed.set_image(url="https://cdn.discordapp.com/attachments/1268538785340063755/1268870776615075841/cat-mod.gif?ex=66adff7f&is=66acadff&hm=3d6e39b6b8a1dc2524851f3201e479dd38734ed97c2d3fe4012a302e74b9916d&")
            await ctx.reply(embed=embed,mention_author=False)



    @block.error
    async def block_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            cross = '❌'
            await ctx.message.add_reaction(cross)


    @commands.command()
    @commands.has_permissions(manage_roles=True, manage_channels=True, administrator=True)
    async def unblock(self, ctx, member: discord.Member):
        # check if user is aleady unblocked
        permission = ctx.channel.permissions_for(member)
        if permission.send_messages:
            embed = discord.Embed(
                    title=f"{member} is not blocked",
                    color=discord.Color.red()
                )
            embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
            embed.set_image(url="https://media.discordapp.net/attachments/1268538785340063755/1268892955037532250/cat_lookingcats.gif?ex=66ae1427&is=66acc2a7&hm=a8caa93f74c3fb5a3f0afe1594bf9f0979912c8ad4889a8520bbe054222fa741&=")
            embed.set_footer(text=f"unblock requested by {ctx.message.author}")
            await ctx.reply(embed=embed,mention_author=False)
            return

        try:
            await ctx.channel.set_permissions(member, read_messages=True,
                                                    send_messages=True)

            embed = discord.Embed(
                title="Successfully",
                color = discord.Color.green()
            )
            embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
            embed.add_field(name=":white_check_mark:", value=f"{member.mention} is able to send messages into **{ctx.channel}** again")
            embed.set_footer(text=f"Member unblock requested by {ctx.author}")
            embed.set_image(url="https://cdn.discordapp.com/attachments/1268177354614640661/1269339730206658650/finally-unmute.gif?ex=66afb43e&is=66ae62be&hm=d763922ae81ccfb339cc573b4d64a54475bea7b5f55b59af64e0916cf0009fb0&")
            await ctx.reply(embed=embed,mention_author=False)
    
        # also wont ever get executed
        except Exception:
            embed = discord.Embed(
            title="Block Error",
            color = discord.Color.red()
            )
            embed.add_field(name=":question:", value=f"Something went wrong with unblocking user {member.name}")

            await ctx.send(embed=embed)


    @unblock.error
    async def unblock_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            cross = '❌'
            await ctx.message.add_reaction(cross)



async def setup(bot):
    await bot.add_cog(securityCog(bot))