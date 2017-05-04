# Problem 2

def extcount(dir):
 filelist=os.listdir(dir)
 dic={}
 i=0
 while i<len(filelist):
  filelist[i]=filelist[i].split('.')
  dic[filelist[i][1]]=dic.get(filelist[i][1],0)+1
  i=i+1 
 for ext,count in dic.items():
  print ext,count

import sys
import os
extcount(sys.argv[1])

