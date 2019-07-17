from html.parser import HTMLParser
import sys
import urllib3
links = []

class Parser(HTMLParser):

	def handle_starttag(self, tag, attrs):
		if tag != 'a':
			return
		attr = dict(attrs)
		links.append(attr)

def start():
	if len(sys.argv) != 2:
		print('Usage: {} URL'.format(sys.argv[0]))
		return
	url = sys.argv[1]
	try:
		f = urllib.request.urlopen(url)
		html = f.read()
		f.close()
	except:
		print('while fetching', url)
		return
	parser = MyHTMLParser()
	parser.links = []
	parser.feed(html)
	for l in links:
		print(l)

start()