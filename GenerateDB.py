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
    global weaponDict
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
        cursorDefault = conDefault.cursor()
        # You were overthinking this way too hard. Now just build dictionaries and learn to make a pickle.
        counter = 0
        for row in cursorDefault.execute("select * from DestinyInventoryItemDefinition"):
            jsonT = json.loads(row[1])
            if jsonT['displayProperties']['name'] == "Classified":
                print("Classified")
            else:
                if jsonT['itemTypeDisplayName'] == "Hand Cannon":
                    weaponDict[jsonT['displayProperties']['name']] = {"type": jsonT['itemTypeDisplayName'], "Rarity": jsonT['inventory']['tierTypeName']}
                    counter += 1
        for key in weaponDict:
            print("The hand cannon's name is " + key +  "and it's a/an " + weaponDict[key]["Rarity"] + ".")



GenerateDB().splitUpDB()
