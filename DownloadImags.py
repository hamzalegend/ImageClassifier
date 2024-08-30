import os

import requests


def download(urls: list, directory: str):

    for i, f in enumerate(urls):

        # print(f'Downloading {i}/{len(urls)}')
        filename = f.split('/')[-1]
        print(filename)
        filepath = os.path.join(directory, filename)

        if not os.path.exists(filename):
            pass

        try:
            with open(filepath, 'wb') as g:
                g.write(requests.get(f).content)
                pass
                # time.sleep(5)
        except Exception as err:
            print(err)
            # time.sleep(30)
            pass
    print(f"images downloaded at '{directory}'")


def downloadImages(file, dir):
    raw_folder = os.path.join(os.getcwd(), "raw_data")

    urls = []
    with open(file, "r") as f:
        urls = f.readlines()
        urls = [i.strip() for i in urls]
    # print(urls)

    download(urls, dir)


# downloadImages("log.txt", "raw_data/dogs")
