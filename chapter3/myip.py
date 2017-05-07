# Problem 10

def ip(url):
 response=urllib.urlopen(url).read()
 content=json.loads(response)
 print content["origin"]
 
 
import urllib
import json
ip('http://httpbin.org/get')


