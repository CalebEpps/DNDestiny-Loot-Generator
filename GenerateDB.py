import json
import os
import pickle
import sqlite3

import pandas as pandas


# noinspection PyGlobalUndefined,PyRedeclaration
from GetManifest import GetManifest


class GenerateDB:
    global path
    global weaponDict
    global weapon_Types
    global titanDict
    global hunterDict
    global warlockDict
    global picklesChecklist

    path = "Manifest.content"

    weapon_Types = {"Hand Cannon", "Scout Rifle", "Sniper Rifle", "Submachine Gun",
                    "Auto Rifle", "Sidearm", "Rocket Launcher", "Machine Gun",
                    "Fusion Rile", "Linear Fusion Rifle", "Shotgun", "Grenade Launcher"}

    # Replace nums with the endings of endpoints for icon watermarks. Then check to assign item seasons.
    season_List = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}

    ChancesDict = {'Rare': 75, 'Legendary': 20, 'Exotic': 5}

    picklesChecklist = {"weaponDict.pickle", "hunterDict.pickle", "warlockDict.pickle", "titanDict.pickle"}

    # USE ICON WATERMARK TO DETERMINE SEASON!!!!!!
    # {Weapon Name: {Type, Rarity, Description, Lore}}
    weaponDict = {}

    # {Item Name: {Type, Rarity, Description, Lore}}
    # Parse "class type" in returned json in order to sort into respective class dictionaries
    # Titan - 0
    # Hunter - 1
    # Warlock - 2
    hunterDict = {}
    warlockDict = {}
    titanDict = {}

    def __init__(self):
        print("Generating DB. . . ")
        #initializationRun()
        pass

    def fileCheck(self):
        allExist = True
        for i in picklesChecklist:
            if (os.path.exists(i)):
                continue
            else:
                allExist = False
        return allExist

    def initializationRun(self):
        if os.path.exists(path) and self.fileCheck():
            print("Start Program")
            weaponDict = pandas.read_pickle(r'weaponDict.pickle')
            titanDict = pandas.read_pickle(r'titanDict.pickle')
            warlockDict = pandas.read_pickle(r'warlockDict.pickle')
            hunterDict = pandas.read_pickle(r'hunterDict.pickle')
            # for i in weaponDict:
            #     print(weaponDict[i]["Rarity"])
        else:
            print("Files Missing. Reacquiring....")
            if(os.path.exists(path)):
                self.generateDictionaries()
            else:
                Manifest = GetManifest()
                Manifest.get_manifest()
                self.generateDictionaries()



    def generateDictionaries(self):  # Move the items
        conDefault = sqlite3.connect("Manifest.content")
        cursorDefault = conDefault.cursor()
        # You were overthinking this way too hard. Now just build dictionaries and learn to make a pickle.
        for row in cursorDefault.execute("select * from DestinyInventoryItemDefinition"):
            jsonT = json.loads(row[1])
            if jsonT['displayProperties']['name'] == "Classified":
                print("Classified")
            else:
                # May need to separate this whole thing into it's own method
                if jsonT['itemTypeDisplayName'] in weapon_Types:
                    weaponDict[jsonT['displayProperties']['name']] = {"type": jsonT['itemTypeDisplayName'],
                                                                      "Rarity": jsonT['inventory']['tierTypeName'],
                                                                      "HashCode": row[0]}
                elif jsonT['classType'] == 0:
                    titanDict[jsonT['displayProperties']['name']] = {"type": jsonT['itemTypeDisplayName'],
                                                                     "Rarity": jsonT['inventory']['tierTypeName'],
                                                                     "Hashcode": row[0]}
                elif jsonT['classType'] == 1:
                    hunterDict[jsonT['displayProperties']['name']] = {"type": jsonT['itemTypeDisplayName'],
                                                                      "Rarity": jsonT['inventory']['tierTypeName'],
                                                                      "Hashcode": row[0]}
                elif jsonT['classType'] == 2:
                    warlockDict[jsonT['displayProperties']['name']] = {"type": jsonT['itemTypeDisplayName'],
                                                                       "Rarity": jsonT['inventory']['tierTypeName'],
                                                                       "Hashcode": row[0]}

        conDefault.close()

        with open('weaponDict.pickle', 'wb') as handle:
            pickle.dump(weaponDict, handle)
            handle.close()
        with open('titanDict.pickle', 'wb') as handle:
            pickle.dump(titanDict, handle)
            handle.close()
        with open('hunterDict.pickle', 'wb') as handle:
            pickle.dump(hunterDict, handle)
            handle.close()
        with open('warlockDict.pickle', 'wb') as handle:
            pickle.dump(warlockDict, handle)
            handle.close()

        for key in weaponDict:
            print("The weapon is called " + key + ", it is a  " + weaponDict[key]['type'] + " and it is of rarity " +
                  weaponDict[key]['Rarity'] + " with a hashcode of " + str(weaponDict[key]['HashCode']) + ".")


GenerateDB().initializationRun()
