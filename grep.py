# Problem 20

def grep(fname,string):
 lines=open(fname).readlines()
 k=0
 for i in lines:
  if string in i:
   print i

import sys
grep(sys.argv[1],sys.argv[2])
