# Problem 11

def zipfil(fname,f):
 z=ZipFile(fname,"w")
 for i in f:
  z.write(i)
 print "zip file created"

import sys
from zipfile import *
zipfil(sys.argv[1],sys.argv[2:])
