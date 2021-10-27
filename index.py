from asyncio.tasks import wait_for
import discord
from discord.ext import commands
import asyncio
import os
import random

client = commands.Bot(command_prefix = 'py') #Your prefix goes here!

@client.event
async def on_message(message):
    channel = client.get_channel() #The Channel ID of channel where you want to get notified about messages sent to bot.
    if message.channel == message.author.dm_channel:
        await channel.send("@here Someone DMed me!")
        embed = discord.Embed(
            title = 'New Bot DM',
            description = f'`{message.content}`',
            color = 0x75FF53
            )
        embed.set_footer(text=f'Applied by:{message.author.display_name} | ID: {message.author.id}')
        await channel.send(embed=embed)
        print("Support requested by {} | ID-{}!" .format(message.author, message.author.id))
        print("Content: '{}'." .format(message.content))
    await client.process_commands(message)

client.run('') #Your Bot token goes here!
