# Problem 5

def wget(url):
 n=url.split('/')
 name=n[-1]
 if name=='':
  name="index.html"  
 urllib.urlretrieve(url,name)

import sys
import urllib
wget(sys.argv[1])
