import os
import requests
from duckduckgo_search import DDGS
from fastcore.all import *
from PIL import Image

max_img = 50


def search_images(term, max_images=max_img):
    print(f"Searching for '{term}'")
    with DDGS() as ddgs:
        search_results = ddgs.images(
            keywords=term, max_results=1000)
        image_data = list(search_results)
        image_urls = [
            item.get("image")+"\n" for item in image_data[:max_images]]
        return L(image_urls)


def GetUrls(phrase, file):
    urls = []
    if (os.path.exists(file)):
        with open(file, "r") as f:
            for i in f.readlines():
                urls.append(i)

    for line in search_images(phrase):
        urls.append(line)

    urls = list(dict.fromkeys(urls))

    with open(file, "w") as f:
        try:
            f.writelines(urls)
        except:
            pass
