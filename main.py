# import sentry_sdk
from tqdm import tqdm
import requests
from urllib.request import urlopen, urljoin
from bs4 import BeautifulSoup
import os
from os import system, name
import urllib.parse as urlparse
import sys

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system("clear")


class Downloader:

    def download(self, link, filename, format):
        response = requests.get(link, stream=True)
        total_length = response.headers.get('content-length')
        file_size = int(response.headers['content-length'])
        downloaded = 0
        downloaded_file_name = filename + "." + format

        if os.path.isfile(downloaded_file_name):
            file_size_local = os.stat(downloaded_file_name).st_size
            if file_size_local == file_size:
                print("" + downloaded_file_name + " => File already exists")
        else:
            print("Downloading "+downloaded_file_name)
            with open(downloaded_file_name, 'wb') as f:
                for data in tqdm(iterable=response.iter_content(chunk_size=1024), total=file_size / 1024, unit='KB'):
                    if data:
                        f.write(data)
            print(downloaded_file_name+" downloaded")

    def scrape(self, url):
        src = urlopen(url)
        codebase = BeautifulSoup(src, 'html.parser')
        y = codebase.findAll("a")
        req = []
        names = []
        print("Format of videos ? (FLV, MP4 or 3GP): ")
        x = input()
        x = x.lower()
        for i in y:
            temp = i.get("href")
            if x in temp:
                a = urljoin(url, temp)
                parsed = urlparse.urlparse(a)
                name = urlparse.parse_qs(parsed.query)['subjectName']
                for g in name:
                    if '/' in g:
                        g = g.replace("/", "")
                    names.append(g)
                req.append(a)

        for i in range(len(req)):
            self.download(req[i], names[i], x)

clear()
x = input("Enter URL address of download page: ")
# Course to be downloaded https://nptel.ac.in/courses/nptel_download.php?subjectid=106102064
download = Downloader()
download.scrape(x)
