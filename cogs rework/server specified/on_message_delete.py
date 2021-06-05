import discord
from discord import Embed

@commands.Cog.listener()
async def on_message_delete(self, message):

    channel = "xxxxxxxxxxxxxxxxxxxxx"

    deleted = Embed(
        description=f"Message deleted in {message.channel.mention}", color=0x4040EC
    ).set_author(name=message.author, url=Embed.Empty, icon_url=message.author.avatar_url)

    deleted.add_field(name="Message", value=message.content)
    deleted.timestamp = message.created_at
    await channel.send(embed=deleted)