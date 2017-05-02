# Problem 22

def wrap(fname,width):
 wl=len(open(fname).read().split())
 words=open(fname).read().split()
 nline=['']*wl
 i=0
 k=0
 while i<wl:
  if len(words[i])<=width-len(nline[k]):
   nline[k]=nline[k]+' '+words[i]
   i=i+1
  else:
   nline[k]=nline[k]+'\n'
   k=k+1
 i=1
 while i<len(nline):
  nline[0]=nline[0]+nline[i]
  i=i+1
 return nline[0]

import sys
print wrap(sys.argv[1],int(sys.argv[2]))
