# Problem 30

def parse_csv(fname):
 c=open(fname).read().split()
 i=0
 while i<len(c):
  c[i]=c[i].split(',')
  i=i+1
 return c

import sys
print parse_csv(sys.argv[1])
