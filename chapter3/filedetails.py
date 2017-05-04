# Problem 3

def filedetails(dir):
 files=os.listdir(dir)
 for i in files:
  size=os.stat(i).st_size
  date=time.ctime(os.stat(i).st_mtime)
  print i,'\t',size,'\t',date

import sys
import os
import time
filedetails(sys.argv[1])
