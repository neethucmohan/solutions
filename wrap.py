# Problem 21

def wrap(fname,width):
 lines=open(fname).readlines()
 nline=[None]
 sline=[None]
 for i in lines:
  l=len(i)
  if width<l:
   nline=i[0:width+1]
   sline=i[width+1:]
   print nline
   print sline
  else:
   print i

import sys
wrap(sys.argv[1],int(sys.argv[2]))
