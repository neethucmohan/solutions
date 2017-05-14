# Problem 4

import os
def findfiles():
 c=0
 for path,dirn,filen in os.walk(os.getcwd()):
  fnames=filen
 for f in fnames:
  if '.py' in f:
   c=c+1
 print c

findfiles() 


