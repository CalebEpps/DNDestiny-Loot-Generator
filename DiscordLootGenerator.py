import json
import random

from GenerateDB import GenerateDB
from dbOps import dbOps


class DiscordLootGenerator:
    dpOps = dbOps()
    destinyDB = dpOps.db.destinyDict
    generateDB = GenerateDB()

    list_Of_Engram_Weights = [5, 25, 70]
    current_Engram_Chance_Total = 100
    list_Of_Engram_Types = ['Exotic', 'Legendary', 'Rare']
    jsonPerks = None

    screenshot_Url = "No Screenshot Available"
    currentName = "None"

    def __init__(self):
        file = open("bin/Weapon Perks.json")
        self.jsonPerks = json.load(file)

    @staticmethod
    def getClassTypeByName(classType):
        if classType == "Titan":
            return 0
        elif classType == "Hunter":
            return 1
        elif classType == "Warlock":
            return 2
        else:
            return "Weapon"

    @staticmethod
    def getClassTypeFromNumber(classType):
        if classType == 0:
            return "Titan"
        elif classType == 1:
            return "Hunter"
        elif classType == 2:
            return "Warlock"
        else:
            return "Weapon"

    @staticmethod
    def getClassFromString(strToBreak):
        if 'warlock' in strToBreak.lower():
            print("Warlock")
            return 2
        elif 'hunter' in strToBreak.lower():
            return 1
        elif 'titan' in strToBreak.lower():
            return 0
        else:
            return 3

    @staticmethod
    def getSeasonFromString(strToBreak):
        toReturn = ""
        for character in strToBreak:
            if character.isdigit():
                toReturn += character
        print("Season: ", toReturn)

        if toReturn == "" or int(toReturn) > 17:
            return 17
        else:
            return int(toReturn)

    @staticmethod
    def armorOnlyCheck(strToBreak):
        if 'armor' in strToBreak.lower():
            return True
        else:
            return False

    def returnRandomLoot(self, strToBreak):
        allowedList = self.createSubDictionaries(self.destinyDB,
                                                 self.getClassFromString(strToBreak),
                                                 self.getSeasonFromString(strToBreak), self.armorOnlyCheck(strToBreak))

        try:
            itemToReturn = random.choice(allowedList)
            print(itemToReturn)
            return itemToReturn
        except IndexError:
            print("Index Problem in Return Random Loot")

    def printRandomLoot(self, strToBreak):
        randomItem = self.returnRandomLoot(strToBreak)
        if randomItem is None:
            return
        randomItemDict = self.destinyDB.get(randomItem)
        self.currentName = randomItem
        # Prevents the program from crashing if the item doesn't have a season. Only affects some items, I'm not too
        # sure how to fix it right now.
        # if randomItemDict['season'] is None or randomItemDict['season'] == "No season Identified":
        #     randomItemDict['season'] = 1
        # TODO: If Screenshot is not available, then display 'no image available' image.
        self.screenshot_Url = "No Screenshot Available"
        perks = None

        if 'screenshot' in randomItemDict:
            # Make Screenshot Link
            self.screenshot_Url = self.generateScreenshotUrl(randomItemDict['screenshot'])
            print("Screenshot: ", self.screenshot_Url)
        else:
            print(self.screenshot_Url)

        if randomItemDict['classType'] != 3:
            armorType = randomItemDict['armor tier']
        else:
            armorType = "None"
            perks = self.getRandomPerks(randomItemDict['type'])

        if armorType is None:
            return (self.lootToString(randomItem, randomItemDict['type'], randomItemDict['season'],
                                      randomItemDict['Rarity'],
                                      randomItemDict['classType'], perks))
        else:
            return (self.lootToString(randomItem, randomItemDict['type'], randomItemDict['season'],
                                      randomItemDict['Rarity'],
                                      randomItemDict['classType'], perks, armorType=armorType))

    def lootToString(self, name, type, season, rarity, classType, perks, armorType="None"):
        # Uncomment this AND change the next line to '+=' for general use
        # returnStr = "Name: " + name
        returnStr = "Type: " + type
        returnStr += "\nSeason: " + str(season)
        returnStr += "\nRarity: " + rarity

        if armorType != "None":
            returnStr += "\nClass: " + self.getClassTypeFromNumber(classType)
            returnStr += "\nArmor Type: " + armorType

        if classType == 3:
            returnStr += "\nPerk 1: " + perks[0]
            returnStr += "\nPerk 2: " + perks[1]
            returnStr += "\nPerk 3: " + perks[2]

        return returnStr

    def getRandomPerks(self, randomItem):
        print(randomItem in self.jsonPerks)

        perksSetOne = self.jsonPerks[randomItem]['Slot 1 Perks']
        perkOne = random.choice(perksSetOne)
        print("Perk 1: ", perkOne)

        perksSetTwo = self.jsonPerks[randomItem]['Slot 2 Perks']
        perkTwo = random.choice(perksSetTwo)
        print("Perk 2: ", perkTwo)

        perksSetThree = self.jsonPerks[randomItem]['Slot 3 Perks']
        perkThree = random.choice(perksSetThree)
        print("Perk 3: ", perkThree)

        return [perkOne, perkTwo, perkThree]

    @staticmethod
    def generateScreenshotUrl(urlEnd):
        return "https://bungie.net/" + urlEnd

    # Creates A sub dictionary of allowed items based on class, season, and engram type restrictions
    def createSubDictionaries(self, itemDictionary, classType, season, armorOnly):
        list_Of_Allowed_items = []
        for i in itemDictionary:
            if (itemDictionary[i]['classType'] == classType or itemDictionary[i][
                'classType'] == 3) and armorOnly is False and self.getEngramType() == itemDictionary[i]['Rarity']:
                try:
                    if season == itemDictionary[i]['season']:
                        list_Of_Allowed_items.append(i)
                        print("Item: ", i)
                        print("Season: ", str(season), " Type: ", classType)
                except IndexError:
                    print("Index Error in createSubDictionaries()")
            elif itemDictionary[i]['classType'] == classType and armorOnly is True and self.getEngramType() == \
                    itemDictionary[i]['Rarity']:
                try:
                    if season == itemDictionary[i]['season']:
                        list_Of_Allowed_items.append(i)
                        print("Item: ", i)
                        print("Season: ", str(season), " Type: ", classType)
                except IndexError:
                    print("Index Error in createSubDictionaries()")

        return list_Of_Allowed_items

    def getEngramType(self):
        try:
            return random.choices(self.list_Of_Engram_Types, weights=self.list_Of_Engram_Weights)[0]
        except ValueError:
            print("VALUE Error in getEngramType()")
