import discord
from discord.ext import commands

class idCog(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    
    @commands.command()
    async def DBCheck(self, ctx):
        if str(ctx.author.id) in open ("idstuff/owner.py").read():
        

            embed = discord.Embed(
                color = discord.Color.green(),
                title="Check the Files ",
                description="Parameter <ask `content`> is optional, with this you can interact to the Files Remotely"
            )
            embed.add_field(name="`DBbypass_read /_add`", value="force users", inline=False)
            embed.add_field(name="`DBnukers_read /_add`", value="nuke users", inline=False)
            embed.add_field(name="`DBsens_read /_add`", value="sens users", inline=False)
            embed.add_field(name="`DBblacklistcomms_read /_add`", value="anti force server", inline=False)
            embed.add_field(name="`DBblacklistedserver_read /_add`", value="nonuke server", inline=False)
            embed.add_field(name="`DBdenylinks_read`", value="list deny links channel id's", inline=False)
            embed.add_field(name="`owner_read /_add`", value="user that = owner", inline=False)

            await ctx.send(embed=embed)

        else:
            pass

    @commands.command()
    async def ask(self, ctx, ask):


        if ask == "DBbypass":
            await ctx.send("Users that can use the force commands and dev_commands", delete_after = 4.0)

        if ask == "DBnukers":
            await ctx.send("Users that are allowed to use the Nuker function", delete_after = 4.0)

        if ask == "DBsens":
            await ctx.send("Users that can use sensitive commands", delete_after = 4.0)

        if ask == "DBblacklistcomms":
            await ctx.send("Server that cannot be forced on", delete_after = 4.0)

        if ask == "DBblacklistserver":
            await ctx.send("Servers that cannot be nuked", delete_after = 4.0)

        if ask == "owner":
            await ctx.send("Commands that only the owners can use (inc. this command)", delete_after = 4.0)

        else:
            await ctx.send("Invalid argument")

    @commands.command()
    async def DBbypass_read(self, ctx):   

        if str(ctx.author.id) in open ("idstuff/owner.py").read():
            f = open("idstuff/allowedbypass.py", "r")
            content = f.read()
            await ctx.send(content)
            f.close()

        else:
            pass

    @commands.command()
    async def DBbypass_add(self, ctx, id):

        if str(ctx.author.id) in open ("idstuff/owner.py").read():
            if id is not None:
                f = open("idstuff/allowedbypass.py", "a")
                f.write("\n"+id)
                await ctx.send("Added " +id+ "to the List")
                f.close

            if id is None:
                await ctx.send("Parameter ID is missing")

        else:
            pass

        #################

    @commands.command()
    async def DBnukers_read(self, ctx):

        if str(ctx.author.id) in open ("idstuff/owner.py").read():
            f = open("idstuff/allowednukers.py", "r")
            content = f.read()
            await ctx.send(content)
            f.close()

        else:
            pass

    @commands.command()
    async def DBnukers_add(self, ctx, id):

        if str(ctx.author.id) in open ("idstuff/owner.py").read():
            if id is not None:
                f = open("idstuff/allowednukers.py", "a")
                f.write("\n"+id)
                await ctx.send("Added " +id+ "to the List")
                f.close

            if id is None:
                await ctx.send("Parameter ID is missing")

        else:
            pass

        ##################

    @commands.command()
    async def DBsens_read(self, ctx):

        if str(ctx.author.id) in open ("idstuff/owner.py").read():
            f = open("idstuff/allowedsens.py", "r")
            content = f.read()
            await ctx.send(content)
            f.close()

        else:
            pass

    @commands.command()
    async def DBsens_add(self, ctx, id):

        if str(ctx.author.id) in open ("idstuff/owner.py").read():
            if id is not None:
                f = open("idstuff/allowedsens.py", "a")
                f.write("\n"+id)
                await ctx.send("Added " +id+ "to the List")
                f.close

            if id is None:
                await ctx.send("Parameter ID is missing")

        else:
            pass

        ########################

    @commands.command()
    async def DBblacklistcomms_read(self, ctx):

        if str(ctx.author.id) in open ("idstuff/owner.py").read():
            f = open("idstuff/blacklistedguildcommands", "r")
            content = f.read()
            await ctx.send(content)
            f.close()

        else:
            pass

    @commands.command()
    async def DBblacklistcomms_add(self, ctx, id):

        if str(ctx.author.id) in open ("idstuff/owner.py").read():
            if id is not None:
                f = open("idstuff/blacklistedguildcommands.py", "a")
                f.write("\n"+id)
                await ctx.send("Added " +id+ "to the List")
                f.close

            if id is None:
                await ctx.send("Parameter ID is missing")

        else:
            pass

    @commands.command()
    async def DBblacklistedserver_read(self, ctx):

        if str(ctx.author.id) in open ("idstuff/owner.py").read():
            f = open("idstuff/blacklistedserver.py", "r")
            content = f.read()
            await ctx.send(content)
            f.close()

        else:
            pass

    @commands.command()
    async def DBblacklistedserver_add(self, ctx, id):

        if str(ctx.author.id) in open ("idstuff/owner.py").read():
            if id is not None:
                f = open("idstuff/blacklistedserver.py", "a")
                f.write("\n"+id)
                await ctx.send("Added " +id+ "to the List")
                f.close

            if id is None:
                await ctx.send("Parameter ID is missing")

        else:
            pass

        ###############

    @commands.command()
    async def DBowner_read(self, ctx):

        if str(ctx.author.id) in open ("idstuff/owner.py").read():
            f = open("idstuff/owner.py", "r")
            content = f.read()
            await ctx.send(content)
            f.close()

        else:
            pass


    @commands.command()
    async def DBowner_add(self, ctx, id):

        if str(ctx.author.id) in open ("idstuff/owner.py").read():
            if id is not None:
                f = open("idstuff/owner.py", "a")
                f.write("\n"+id)
                await ctx.send("Added " +id+ "to the List")
                f.close

            if id is None:
                await ctx.send("Parameter ID is missing")

        else:
            pass

    @commands.command()
    async def DBdenylinks_read(self, ctx):

        try:


            if str(ctx.author.id) in open ("idstuff/owner.py").read():
                f = open("idstuff/links/deny.py", "r")
                content = f.read()
                await ctx.send(content)
                f.close()

            else:
                pass

        except Exception as e:
            await ctx.send(e)



def setup(bot):
    bot.add_cog(idCog(bot))