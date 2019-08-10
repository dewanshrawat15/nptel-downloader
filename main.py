from tqdm import tqdm
import requests
from urllib.request import urlopen, urljoin
from bs4 import BeautifulSoup
import os
from os import system, name
import urllib.parse as urlparse
import sys
import argparse

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

    def scrape(self, url, vid_format):
        src = urlopen(url)
        codebase = BeautifulSoup(src, 'html.parser')
        y = codebase.findAll("a")
        req = []
        names = []
        if vid_format is None:
            print("Format of videos ? (FLV, MP4 or 3GP): ")
            x = input()
            x = x.lower()
        else:
            x = vid_format
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

    def fetch_page(self, course_url, vid_format):
        src = urlopen(course_url)
        codebase = BeautifulSoup(src, 'html.parser')
        links = codebase.findAll("a")
        for i in links:
            urlText = i.getText()
            if "Download Videos & Transcripts" in urlText:
                downloadPageURL = urljoin(course_url, i.get("href"))
                print(downloadPageURL)
                break
            else:
                print("Links not found")
                return 1
        self.scrape(downloadPageURL, vid_format)

def start():
    clear()
    parser = argparse.ArgumentParser(description='NPTEL Downloader. Download the videos of your favorite course on NPTEL. Just paste the web address of the course page, and start downloading those videos. ')
    parser.add_argument("-u", "--url", help="Enter the course page url")
    parser.add_argument("-f", "--format", help="Enter the format in which the videos have to be downloaded. Broadly supported formats are FLV, 3GP and MP4.")
    # parser.add_argument("-p", "--path", help="Enter the path where the videos have to be downloaded")g
    args = parser.parse_args()
    if not args.url:
        x = input("Enter URL address of download page: ")
        # Course to be downloaded https://nptel.ac.in/courses/nptel_download.php?subjectid=106102064
    download = Downloader()
    supported_formats = ['mp4', 'flv', '3gp']
    if args.format and args.format.lower() in supported_formats:
        download.fetch_page(args.url, args.format.lower())
    else:
        download.fetch_page(x, None)

if __name__ == "__main__":
    start()
