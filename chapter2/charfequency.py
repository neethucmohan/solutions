# Problem 35

def charfrequency(fname):
 c=('#include','<stdio.h>','printf','scanf')
 p=('import','def','print','items()')
 frequency={}
 lines=open(fname).read().split()
 for word in lines:
  for ch in word:
   frequency[ch]=frequency.get(ch,0)+1
 for char,count in frequency.items():
  print char,count
 j=0
 k=0
 for word in lines:
  i=0
  while i<4:
   if word==c[i]:
    j=j+1
    i=i+1
    break
   elif word==p[i]:
    k=k+1
    i=i+1
    break
   else:
    i=i+1
 if j>=2:
  print "Its a c file"
 elif k>=2:
  print "Its a python file"
 else:
  print " Its a text file"
     
 
import sys
charfrequency(sys.argv[1])
