import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions, BadArgument, MissingRequiredArgument, CommandInvokeError, has_permissions

class ownerCog(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    @commands.command()
    async def owner(self, ctx):
        if str(ctx.author.id) in open ("idstuff/owner.py").read():
            embed = discord.Embed(
                title="Owner Commands",
                color = discord.Color.magenta()
            )
            embed.add_field(name=":electric_plug: `shutdown`", value="Shut down the Bot", inline=False)
            embed.add_field(name=":satellite: `rename <name>`", value="Rename the Bot", inline=False)

            await ctx.send(embed=embed)

        else:
            pass

    @commands.command()
    async def rename(self, ctx, name):
        if str(ctx.author.id) in open ("idstuff/owner.py").read():
            user = ctx.author

            try:


                await commands.user.edit(username=name)

                embed = discord.Embed(
                    title="Name Changed",
                    color = discord.Color.green()
                )

                embed.add_field(name=":green_square:", value=F"name changed to {name}")

                await ctx.send(embed = embed)

            except Exception as e:
                await ctx.send(e)

                embed = discord.Embed(
                    title="Name change failed",
                    color = discord.Color.red()
                )

                embed.add_field(name=":red_square:", value=f"Couldn't change name to: {name}")

                await ctx.send(embed = embed)



def setup(bot):
    bot.add_cog(ownerCog(bot))
