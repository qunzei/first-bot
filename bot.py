import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "-")

chat_filter = ["PINEAPPLE", "APPLE", "CHROME"]

bypass_list = []

@client.event
async def on_ready():
    print("Bot is online, and connected to Discord!")

@client.event    
async def on_message(message):
    if message.content.upper().startswith('!PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))
    if message.content.upper().startswith('!SAY'):
        if message.author.id == "331292975776792576":
            args = message.content.split(" ")
            await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
        else:
            await client.send_message(message.channel, "You do not have permission.")
    if message.content.upper().startswith('!AMIADMIN'):
        if "507407339930779649" is [role.id for role in message.author.roles]:
            await client.send_message(message.channel, "You are an admin.")
        else:
            await client.send_message(message.channel, "You are not an admin.")
    contents = message.content.split(" ") #contents is a list type
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await client.delete_message(message)
                    await client.send_message(message.channel, "**Hey!** You're not allowed to use that word here.")
                except discord.errors.NotFound:
                    return
    if message.content.upper().startswith('!SAVVY'):
        await client.send_message(message.channel, "Cinema is a queer.")
                            




client.run("NTA3MzY5OTQ4NTExNzMxNzEy.DrvtKA.UfiHy-UTB-6WnorwGfxrQV-TiiM")
