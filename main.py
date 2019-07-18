import requests
from urllib.request import urlopen, urljoin
from bs4 import BeautifulSoup
import os
from os import system, name
import urllib.parse as urlparse

def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system("clear")

class Downloader:

	def download(self, link, filename):
		r = requests.get(link, stream = True)
		with open(filename, 'wb') as f:
			for chunk in r.iter_content(chunk_size = 1024*1024):
				if chunk:
					f.write(chunk)
		print(filename)

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
					names.append(g)
				req.append(a)

		for i in range(len(req)):
			print("File Name => " + names[i])
			print("Link => " + req[i])
			self.download(req[i], names[i])

clear()
x = input("Enter URL address of download page: ")
download = Downloader()
download.scrape(x)
