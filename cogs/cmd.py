import discord
from discord.ext import commands

class helpCog(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    @commands.command()
    async def help(self, ctx):

        async with ctx.typing():

            embed=discord.Embed(title="prefix before every command", color=0xf0d419)
            embed.set_author(name="House Keeper", icon_url="https://cdn.discordapp.com/avatars/735221653998534688/0f3d1717085e0a4c83bd914470581e80.webp?size=1024")
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/443208943213477889/601699371221909504/imagesfidosfhdis.jpg?width=598&height=585")
            embed.add_field(name=":lock: **mod**\n``management``", value="Commands for the server management", inline=True)
            embed.add_field(name=":detective: **security**\n``security``", value="Easier server security", inline=True)
            embed.add_field(name=":paperclip: **utilities**\n``utilities``", value="Commands for usefull utilities", inline=True)
            embed.add_field(name=":smile: **fun**\n``fun``", value="Bot commands for funny stuff", inline=True)
            embed.add_field(name=":joystick: **games**\n``game``", value="Play games with the bot", inline=True)
            embed.add_field(name=":magic_wand: **slash**\n``slash``", value="Lists all slash interactions", inline=True)
            embed.add_field(name=":desktop: **bot**\n``bot``", value="Commands for the Bot itself", inline=True)
            embed.set_footer(text="Help Box for the House Keeper Bot")

        await ctx.send(embed=embed)





async def setup(bot):
    await bot.add_cog(helpCog(bot))
