import io
import os

import aiohttp
import discord
from dotenv import load_dotenv
from DiscordLootGenerator import DiscordLootGenerator

client = discord.Client()
lootGenerator = DiscordLootGenerator()
load_dotenv()


@client.event
async def on_message(message):
    # Listener for !loot command
    if message.content.startswith("!loot"):
        # Passes needed info from lootGenerator
        lootEmbed = discord.Embed(description=lootGenerator.printRandomLoot(message.content), title=lootGenerator.currentName,
                                  color=0x71368a)
        # Set image based on screenshot url if available
        if lootGenerator.screenshot_Url != "No Screenshot Available":
            lootEmbed.set_image(url=lootGenerator.screenshot_Url)
        # Send Message
        await message.channel.send(embed=lootEmbed)


client.run(os.getenv('TOKEN'))
