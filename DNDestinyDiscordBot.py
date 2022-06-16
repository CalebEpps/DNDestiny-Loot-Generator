import os

import discord
from dotenv import load_dotenv

import MainWindow

client = discord.Client()
lootGenerator = MainWindow.Ui_MainWindow()
load_dotenv()



@client.event
async def on_message(message):
    if message.content.startswith("!loot"):
        channel = client.get_channel(986359602536923236)
        await message.channel.send("```" + lootGenerator.printRandomLoot() + "```")


client.run(os.getenv('TOKEN'))
