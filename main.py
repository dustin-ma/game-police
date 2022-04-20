import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# @client.event
# async def on_message(message):
#     print('[' + message.channel.name + '] ' + message.author.name + ': ' + message.content)
#     if message.author == client.user:
#         return

#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello!')

@client.command()
async def ping(ctx):
    await ctx.send('No!')

client.run(os.getenv('BOT_TOKEN'))