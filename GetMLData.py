import os
import time
from GetUrls import GetUrls
from DownloadImags import downloadImages
from cleanData import scan_and_clean_directory

import threading
classes = ["Boat", "car", "bike", "motorccycle", "scoter"]

for c in classes:
    GetUrls(c, f"Classes/{c}.log")

for c in classes:
    if not os.path.exists(f"raw_data/{c}"):
        os.makedirs(f"raw_data/{c}")
    threading.Thread(target=downloadImages, args=(
        f"Classes/{c}.log", f"raw_data/{c}")).start()


while (threading.active_count() > 1):
    time.sleep(5)
scan_and_clean_directory(os.join(os.getcwd(), "raw_data"))

print("[Finished]")
