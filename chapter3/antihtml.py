# Problem 6

def antihtml(url):
 response=urllib.urlopen(url)
 content=response.read()
 p=re.compile(r'<.*?>')
 return p.sub('',content) 

import sys
import urllib
import re
print antihtml(sys.argv[1])
