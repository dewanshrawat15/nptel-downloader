from os.path import basename
from urllib.request import urlopen, urljoin
from bs4 import BeautifulSoup
import urllib.parse as urlparse
class Downloader:

    def scrape(self, url):
        src = urlopen(url)
        codebase = BeautifulSoup(src, 'html.parser')
        y = codebase.findAll("a")
        req = []
        names = []
        print(y)
        flag = -1
        for i in y:
            temp = i.get("href")
            if ".mp4" in temp:
                flag = 1
                break
            else:
                flag = 0
        if flag == 1:
            print("Successful found download links")
            return 1
        else:
            print("Links not found")
            return 0

def start():
    download = Downloader()
    downloadURL = "https://nptel.ac.in/courses/106/106/106106213/"
    download.scrape(downloadURL)

if __name__ == "__main__":
    start()
