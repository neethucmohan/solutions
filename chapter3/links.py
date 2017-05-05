# Problem 8
 
def links(url):
 response=urllib.urlopen(url)
 content=response.read()
 links = re.findall('"((http|ftp)s?://.*?)"',content)
 for i in links:
  print i[0]

import sys
import urllib
import re
links(sys.argv[1])
