import asyncio
import os.path
import tkinter as tk
from tkinter import *

import async_timeout
import pydest
from os.path import exists
import sqlite3
from PIL import ImageTk, Image
import requests
import json


# Populate destinyDB.json on first run. Decodes hashes from manifest and sorts them into the
# appropriate tables

# to get information, use SQLite database worldContent to get hashes
# Use pydest Async Loading in order to decode hashes.
# Only decode on first startup. You may also delete manifest once the user has
# generated the database of relevant items.

# UI:
# Engram Type
# Possible Items
# Season Checklist
# Lock by Class

# Handle UI / Initialization
class Main:
    destiny = pydest.Pydest("941d92034e1b4563a6eefd80dc6786f8")

    async def main(self):
        if os.path.exists("destinyDB.json"):
            print("Database already exists")
        else:
            print("Database does not exist.")
            destiny = pydest.Pydest('na')
            json = await destiny.decode_hash(80726883, 'DestinyActivityDefinition')
            await destiny.close()
            print(json)


# runGenerateDB

# Build custom DB at startup based on current manifest version. "DestinyDB"



# async def main():
#     if(os.path.exists('destinyDB.txt')):
#         print("\n\nDatabase Exists, continuing...\n\n")
#     else:
#         destiny = pydest.Pydest("941d92034e1b4563a6eefd80dc6786f8")
#         jsonTest = await destiny.api.get_destiny_manifest()
#         mani_url = 'http://www.bungie.net' + jsonTest['Response']['jsonWorldContentPaths']['en']['']
#         jsonDB = json.loads(requests.get(mani_url).text)
#         print(jsonDB)
#         print(mani_url)
#         with open('Test_FIles/destinyDB.txt', 'w') as f:
#             json.dump(jsonDB, f)


loop = asyncio.get_event_loop()
main = Main()
loop.run_until_complete(main.main())
loop.close()

# How to make window and display image
# class MainWindow(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Image Loading")
#         self.geometry('500x300')
#         self.img = tk.PhotoImage(file=("Test_FIles/Falling Guillotine (rigged by BUNGIE).png"))
#
#         tk.Label(self, image=self.img).pack()
#
#
# if __name__ == "__main__":
#     mainWindow = MainWindow()
#     mainWindow.mainloop()
