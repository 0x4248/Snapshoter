# Snapshoter
# Lets you take a snapshot of a file on HTTPS for datamining
# Github: https://www.github.com/0x4248/snapshoter
# Licence: GNU General Public License v3.0
# By: 0x4248

import os
import requests
import json
from datetime import datetime

def main():
    urls = []
    with open("config.json") as f:
        urls = json.load(f)["urls"]

    if not os.path.exists("snapshots"):
        os.makedirs("snapshots")

    if not os.path.exists("snapshots/current"): 
        os.makedirs("snapshots/current")

    now = datetime.now()


    for url in urls:
        r = requests.get(url)
        r.raise_for_status()

        url_converted = url.replace("https://", "").replace("http://", "").replace("/", "_")
        file_name = url.split("/")[-1]

        file_path = f"snapshots/current/{url_converted}"

        if not os.path.exists(file_path) or open(file_path).read() != r.text:
            with open(file_path, "w") as f:
                f.write(r.text)

            date_path = f"snapshots/{url_converted}/{now.year}/{now.month}/{now.day}"
            if not os.path.exists(date_path):
                os.makedirs(date_path)

            with open(f"{date_path}/{file_name}", "w") as f:
                f.write(r.text)
            
            os.system(f"python3 -m FP {date_path}/{file_name} -o {date_path}/{file_name}.fingerprint.json")
            with open(f"{date_path}/{file_name}.headers.json", "w") as f:
                json.dump(dict(r.headers), f, indent=4)

            print(f"Saved {url_converted} to {date_path}")
        else:
            print(f"File {url_converted} is the same")

if __name__ == "__main__":
    main()