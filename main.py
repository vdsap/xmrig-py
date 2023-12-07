import json
import os
import sys
import requests

try: latest_release = requests.get('https://api.github.com/repos/xmrig/xmrig/releases/latest')
except Exception as e:
    print(e)
    sys.exit(-1)
json_release = json.loads(latest_release.text)
for i in json_release['assets']:
    if i["name"].find("linux-static-x64.tar.gz") != -1:
        download_url = i['browser_download_url']

os.system(f'wget {download_url} -O xmrig.tar.gz')
try: os.system(f"tar -xvf xmrig.tar.gz")
except Exception as e:
    print(e)
    sys.exit(-1)
files = os.listdir()
for i in files:
    if i.find("xmrig-") != -1:
        folder = i
os.system("mkdir xmrig")
os.system(f"cp {folder}/* xmrig")
