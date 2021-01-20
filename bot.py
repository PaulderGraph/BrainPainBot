import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Bot is ready')



@client.event
async def on_message(message):
    msg = message.content.lower()
    msg = msg.replace(" ", "")
    if any(s in msg for s in ("zensur", "brinder", "zensuhr", "zensieren", "brin", "zens", "znesur")):
        await message.channel.purge(limit=1)
        print('Message deleted')




client.run('NzkxMjg1MDc5NDQyOTgwODY2.X-M7qA.b3UtL6Yanh6djd0eNapG-ae6jAM')
