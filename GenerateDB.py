import json
import os
import sqlite3

import pydest


class GenerateDB:
    global path
    path = "world_sql_content_13b84b23c9f2eb57c71ac6633ffd8c3f.content"
    global defaultDB
    defaultDB = {}


    def dbExistsCheck(self):
        if(os.path.exists(path)):
            print("Destiny manifest downloaded")
        else:
            print("Destiny manifest needs to be downloaded")


    def createmodifiedDB(self):



    def splitUpDB(self):
        destiny = pydest.Pydest("No Key Needed, DB Already Downloaded")
 # Move the items
        conDefault = sqlite3.connect(path)
        conModified = sqlite3.connect("modifiedDB.db")
        cursorDefault = conDefault.cursor()
        cursorModified = conModified.cursor()
        stop_at = 25
        for row in cursorDefault.execute("select * from DestinyInventoryItemDefinition limit 5"):
            defaultDB[row[0]] = row
            print(defaultDB[row[0]])
            # VERY LARGE insert into statement where you insert the defaultDB values into the modifiedDB values using Regex.
            # Will take a large statement but will save a lot of time later. :) MAKE IT MODULAR






GenerateDB().splitUpDB()
