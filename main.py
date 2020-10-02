from os.path import basename
from tqdm import tqdm
import requests
from urllib.request import urlopen, urljoin
from bs4 import BeautifulSoup
import argparse
import os

class Downloader:
    @classmethod
    def download(self, link, filename, folder):
        response = requests.get(link, stream=True)
        file_size = int(response.headers['content-length'])
        downloaded_file_name = filename

        downloaded_file_path = folder + "/" + downloaded_file_name
        if os.path.isfile(downloaded_file_path):
            file_size_local = os.stat(downloaded_file_path).st_size
            if file_size_local == file_size:
                print("" + downloaded_file_name + " => File already exists")
        else:
            print("Downloading "+downloaded_file_name)
            with open(downloaded_file_path, 'wb') as f:
                for data in tqdm(iterable=response.iter_content(chunk_size=1024), total=file_size / 1024, unit='KB'):
                    if data:
                        f.write(data)
            print(downloaded_file_name+" downloaded")

    def scrape(self, url, folder):

        if not os.path.exists(folder):
            os.makedirs(folder)

        src = urlopen(url)
        codebase = BeautifulSoup(src, 'html.parser')
        y = codebase.findAll("a")
        req = []
        names = []
        for i in y:
            temp = i.get("href")
            if ".mp4" in temp:
                a = urljoin(url, temp)
                name = basename(a)
                names.append(name)
                req.append(a)

        if folder:
            for i in range(len(req)):
                self.download(req[i], names[i], folder)
        else:
            for i in range(len(req)):
                self.download(req[i], names[i])

def start():
    parser = argparse.ArgumentParser(description='NPTEL Downloader. Download the videos of your favorite course on NPTEL. Just paste the web address of the course page, and start downloading those videos. ')
    parser.add_argument("-u", "--url", help="Enter the course page url")
    parser.add_argument("-f", "--folder", help="Enter the folder name where the videos have to be downloaded")
    args = parser.parse_args()
    if not args.url:
        x = input("Enter URL address of download page: ")
    download = Downloader()
    if args.url and args.folder:
        download.scrape(args.url, args.folder)
    elif args.folder and x:
        download.scrape(x, args.folder)
    elif args.url:
        download.scrape(args.url, "Videos")
    else:
        download.scrape(x, "Videos")

if __name__ == "__main__":
    start()
