import asyncio
import os.path
import tkinter as tk
from tkinter import *
from tkinter.ttk import Progressbar

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
from GenerateDB import GenerateDB


class Main:

    def __init__(self):
        UI().createInitialWindow()


class UI(tk.Tk):
    def createInitialWindow(self):
        waitLabel = Label(text="Please wait while the database is loading . . .")
        waitLabel.anchor(anchor=CENTER)

        mainFrame = Frame()


        pbar = Progressbar(self, orient=HORIZONTAL, mode='determinate')
        pbar.anchor(anchor=CENTER)
        pbar.pack()
        waitLabel.pack()
        mainFrame.pack(expand=1)

        GenerateDB().initializationRun()

        self.eval('tk::PlaceWindow . center')

        self.mainloop()


if __name__ == '__main__':
    Main()
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
