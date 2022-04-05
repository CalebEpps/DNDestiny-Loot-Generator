import asyncio
import tkinter as tk
from tkinter import *

import pydest
from PIL import ImageTk, Image
import requests
import json


# Request Example
async def main():
    destiny = pydest.Pydest("941d92034e1b4563a6eefd80dc6786f8")
    jsonTest = await destiny.api.search_destiny_entities("DestinyInventoryItemDefinition", "Guil")
    newjson = await destiny.decode_hash(3844826443, "DestinyInventoryItemDefinition")
    dP = newjson['displayProperties']
    print(dP['name'])
    await destiny.close()


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
