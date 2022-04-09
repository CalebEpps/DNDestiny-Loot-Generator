import os
import zipfile

import requests


class GetManifest:


    def get_manifest(self):
        manifest_url = 'http://www.bungie.net/Platform/Destiny2/Manifest/'
        HEADERS = {"x-api-key": "941d92034e1b4563a6eefd80dc6786f8"}
        # get the manifest location from the json
        r = requests.get(manifest_url, headers=HEADERS)
        manifest = r.json()
        mani_url = 'http://www.bungie.net' + manifest['Response']['mobileWorldContentPaths']['en']

        # Download the file, write it to 'MANZIP'
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

        if os.path.exists("MANZIP"):
            os.remove("MANZIP")

        if os.path.exists("world_sql_content_13b84b23c9f2eb57c71ac6633ffd8c3f.content"):
            os.remove("world_sql_content_13b84b23c9f2eb57c71ac6633ffd8c3f.content")


