import pydest
import requests, zipfile, os
import json, sqlite3
import pickle  # Optional

# Reading the Destiny API Manifest in Python. [How I Did It, Anyway]

weapon_types = ['Rocket Launcher', 'Scout Rifle', 'Fusion Rifle', 'Sniper Rifle',
                'Shotgun', 'Machine Gun', 'Pulse Rifle', 'Auto Rifle', 'Hand Cannon', 'Sidearm']

# dictionary that tells where to get the hashes for each table
# FULL DICTIONARY
hash_dict = {
             'DestinyClassDefinition': 'classHash',
             'DestinyInventoryItemDefinition': 'itemHash',
             'DestinyProgressionDefinition': 'progressionHash',
             'DestinyStatDefinition': 'statHash',
             'DestinyDestinationDefinition': 'destinationHash',
             'DestinyPlaceDefinition': 'placeHash',
             'DestinyStatGroupDefinition': 'statGroupHash',
             'DestinyVendorCategoryDefinition': 'categoryHash',
             'DestinyEnemyRaceDefinition': 'raceHash'}

hashes_trunc = {
    'DestinyInventoryItemDefinition': 'itemHash',
    'DestinyTalentGridDefinition': 'gridHash',
    'DestinyHistoricalStatsDefinition': 'statId',
    'DestinyStatDefinition': 'statHash',
    'DestinySandboxPerkDefinition': 'perkHash',
    'DestinyStatGroupDefinition': 'statGroupHash'
}

HEADERS = {'x-api-key': "941d92034e1b4563a6eefd80dc6786f8"}


def get_manifest():
    manifest_url = 'http://www.bungie.net/Platform/Destiny2/Manifest/'
    # get the manifest location from the json
    r = requests.get(manifest_url, headers=HEADERS)
    manifest = r.json()
    #print(manifest)
    mani_url = 'http://www.bungie.net' + manifest['Response']['mobileWorldContentPaths']['en']
    print(mani_url)
    # Download the file, write it to MANZIP
    r = requests.get(mani_url)
    with open("MANZIP", "wb") as zip:
        zip.write(r.content)
    print("Download Complete!")

    # Extract the file contents, and rename the extracted file
    # to 'Manifest.content'
    with zipfile.ZipFile('MANZIP') as zip:
        name = zip.namelist()
        zip.extractall()
    os.rename(name[0], 'Manifest.content')
    print('Unzipped!')


def build_dict(hash_dict):
    # connect to the manifest
    con = sqlite3.connect('Manifest.content')
    print('Connected')
    # create a cursor object
    cur = con.cursor()

    all_data = {}
    # for every table name in the dictionary
    for table_name in hash_dict.keys():
        # get a list of all the jsons from the table
        cur.execute('SELECT json from ' + table_name)
        print('Generating ' + table_name + ' dictionary....')

        # this returns a list of tuples: the first item in each tuple is our json
        items = cur.fetchall()

        # create a list of jsons
        item_jsons = [json.loads(item[0]) for item in items]

        # create a dictionary with the hashes as keys
        # and the jsons as values
        item_dict = {}
        hash = hash_dict[table_name]
        print(hash)
        for item in item_jsons:
            item_dict[item[hash]] = item

        # add that dictionary to our all_data using the name of the table
        # as a key.
        all_data[table_name] = item_dict
    print('Dictionary Generated!')
    return all_data


# check if pickle exists, if not create one.
if os.path.isfile('manifest.pickle') == False:
    get_manifest()
    all_data = build_dict(hash_dict)
    with open('manifest.pickle', 'wb') as data:
        pickle.dump(all_data, data)
    print("'manifest.pickle' created!\nDONE!")
else:
    print('Pickle Exists')

with open('manifest.pickle', 'rb') as data:
    all_data = pickle.load(data)

destinyDB = open("Test_FIles/destinyDB.txt", "a")
destiny = pydest.Pydest("941d92034e1b4563a6eefd80dc6786f8")

for (i) in all_data["DestinyInventoryItemDefinition"]:
    current_item = all_data["DestinyInventoryItemDefinition"][i]
    if ('itemName' in current_item and 'itemTypeName' in current_item):
        print(i)
        print('Name: ' + current_item['itemName'])
        print('Type: ' + current_item['itemTypeName'])
        print("Icon Link: " + current_item["icon"])
        print("\n")
        if (current_item["itemTypeName"] in weapon_types):
            destinyDB.write("\nHash Code: " + str(i) + "\nName: " + current_item["itemName"] + "\n"
                            + "Type: " + current_item["itemTypeName"] + "\n")

destinyDB.close()

hash = 1274330687
ghorn = all_data['DestinyInventoryItemDefinition'][hash]

print('Name: ' + ghorn['itemName'])
print('Type: ' + ghorn['itemTypeName'])
print('Tier: ' + ghorn['tierTypeName'])
print(ghorn['itemDescription'])
