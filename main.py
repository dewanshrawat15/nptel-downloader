from os.path import basename
from tqdm import tqdm
import requests
from urllib.request import urlopen, urljoin
from bs4 import BeautifulSoup
import argparse

class Downloader:
    @classmethod
    def download(self, link, filename):
        response = requests.get(link, stream=True)
        file_size = int(response.headers['content-length'])
        downloaded_file_name = filename

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
        for i in y:
            temp = i.get("href")
            if ".mp4" in temp:
                a = urljoin(url, temp)
                name = basename(a)
                names.append(name)
                req.append(a)
            else:
                print("Links not found")
                return 1

        for i in range(len(req)):
            self.download(req[i], names[i])

def start():
    parser = argparse.ArgumentParser(description='NPTEL Downloader. Download the videos of your favorite course on NPTEL. Just paste the web address of the course page, and start downloading those videos. ')
    parser.add_argument("-u", "--url", help="Enter the course page url")
    args = parser.parse_args()
    if not args.url:
        x = input("Enter URL address of download page: ")
    download = Downloader()
    if args.url:
        download.scrape(args.url)
    else:
        download.scrape(x)

if __name__ == "__main__":
    start()
