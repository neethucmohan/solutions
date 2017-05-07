# Problem 14

def extract(wpage):
 response=urllib.urlopen(wpage)
 soup=BeautifulSoup.BeautifulSoup(response)
 attr={'href':re.compile("^http://")}
 for line in soup.findAll('a',attr):
  print line.get('href')

import sys
import urllib
import BeautifulSoup
import re
extract(sys.argv[1])

