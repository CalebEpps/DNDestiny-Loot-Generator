import asyncio
import json
import os
import re
import sqlite3

import pydest


class GenerateDB:
    global path
    path = "world_sql_content_13b84b23c9f2eb57c71ac6633ffd8c3f.content"

    weapon_Types = {"Hand Cannon", "Scout Rifle", "Sniper Rifle", "Submachine Gun",
                    "Auto Rifle", "Sidearm", "Rocket Launcher", "Machine Gun",
                    "Fusion Rile", "Linear Fusion Rifle", "Shotgun", "Grenade Launcher"}
    rarities = {"Uncommon", "Rare", "Legendary", "Exotic"}

    armor_Types = {"Leg Armor", "Hunter Cloak", "Warlock Bond", "Titan Something",
                   "Gauntlets", "Helmet"}

    season_List = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}

    # {Weapon Name: {Type, Rarity, Description, Lore}}
    weaponDict = {}

    # {Item Name: {Type, Rarity, Description, Lore}}
    hunterDict = {}
    warlockDict = {}
    titanDict = {}
    extrasDict = {}

    def dbExistsCheck(self):
        if (os.path.exists(path)):
            print("Destiny manifest downloaded")
        else:
            print("Destiny manifest needs to be downloaded")

    def splitUpDB(self):
        destiny = pydest.Pydest("No Key Needed, DB Already Downloaded")
        # Move the items
        conDefault = sqlite3.connect(path)
        conModified = sqlite3.connect("modifiedDB.db")
        cursorDefault = conDefault.cursor()
        #WHERE json_extract(j.value, '$.name') LIKE 'NAME_IN%');
        for row in cursorDefault.execute("select * from DestinyInventoryItemDefinition limit 5"):
            print(row[1])
            jsonT = json.loads(row[1])
            print(jsonT['displayProperties']['name'])
            print(jsonT['itemTypeAndTierDisplayName'])
            print("\n")
            # VERY LARGE insert into statement where you insert the defaultDB values into the modifiedDB values using Regex.
            # Will take a large statement but will save a lot of time later. :) MAKE IT MODULAR


GenerateDB().splitUpDB()
