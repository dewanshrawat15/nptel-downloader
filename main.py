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

	def progress_bar(self, downloaded, file_size):
		percent = (int(downloaded)/int(file_size)) * 100
		percent = int((round(percent, 2)))
		output = "\r %s%% downloaded" % percent
		sys.stdout.write(output)
		sys.stdout.flush()

	def download(self, link, filename, format):
		response = requests.get(link, stream = True)
		total_length = response.headers.get('content-length')
		file_size = int(response.headers['content-length'])
		downloaded = 0
		downloaded_file_name = filename + "." + format
		if os.path.isfile(downloaded_file_name):
			file_size_local = os.stat(downloaded_file_name).st_size
			if file_size_local == file_size:
				print(""+ downloaded_file_name +" => File already exists")
		else:
			print("Downloading")
			with open(downloaded_file_name, 'wb') as f:
				for chunk in response.iter_content(chunk_size = 1024*1024):
					downloaded = downloaded + len(chunk)
					self.progress_bar(downloaded, total_length)
					if chunk:
						f.write(chunk)

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
			self.download(req[i], names[i], x)

clear()
x = input("Enter URL address of download page: ")
download = Downloader()
download.scrape(x)
