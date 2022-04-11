import os
import zipfile
from tqdm import tqdm

import requests


class GetManifest:


    def get_manifest(self):
        manifest_url = 'http://www.bungie.net/Platform/Destiny2/Manifest/'
        HEADERS = {"x-api-key": "941d92034e1b4563a6eefd80dc6786f8"}
        # get the manifest location from the json
        r = requests.get(manifest_url, headers=HEADERS, stream=True)

        manifest = r.json()
        mani_url = 'http://www.bungie.net' + manifest['Response']['mobileWorldContentPaths']['en']
        r = requests.get(mani_url)

        # Download the file, write it to 'MANZIP'
        with open("MANZIP", "wb") as zip:
            manifest_Size = int(r.headers.get('content-length', 0))
            print(manifest_Size)
            block_Size = 1024
            progress_bar = tqdm(total=manifest_Size, unit='iB', unit_scale=True)
            for data in r.iter_content(block_Size):
                progress_bar.update(len(data))
                zip.write(data)
            progress_bar.close()
        if manifest_Size != 0 and progress_bar.n != manifest_Size:
            print("ERROR, something went wrong")
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


