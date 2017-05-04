#Problem 23

def cntr(fname):
 lines=open(fname).readlines()
 for i in lines:
  print(i.center(40))

import sys
cntr(sys.argv[1])
