# Problem 13

def c2e(cname,ename):
 data=tablib.Dataset()
 d=open(cname).readlines()
 k=0
 for i in d:
  data.append([k,i])
  k=k+1
 with open(ename,'wb') as f:
  f.write(data.xls)

import sys
import tablib
c2e(sys.argv[1],sys.argv[2])





