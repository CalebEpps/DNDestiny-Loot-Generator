import asyncio
import os.path
import tkinter as tk
from tkinter import *

import pydest
from os.path import exists
import sqlite3
from PIL import ImageTk, Image
import requests
import json


# Request Example
async def main():
    if(os.path.exists('destinyDB.txt')):
        print("\n\nDatabase Exists, continuing...\n\n")
    else:
        destiny = pydest.Pydest("941d92034e1b4563a6eefd80dc6786f8")
        jsonTest = await destiny.api.get_destiny_manifest()
        mani_url = 'http://www.bungie.net' + jsonTest['Response']['jsonWorldContentPaths']['en']['']
        jsonDB = json.loads(requests.get(mani_url).text)
        print(jsonDB)
        print(mani_url)
        with open('Test_FIles/destinyDB.txt', 'w') as f:
            json.dump(jsonDB, f)





loop = asyncio.get_event_loop()
loop.run_until_complete(main())
#loop.close()


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
