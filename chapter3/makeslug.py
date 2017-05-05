# Problem 7

def make_slug(name):
 print name
 exp=r'[\W\s]'
 sname=re.sub(exp,'-',name)
 s=''
 c=0
 for i in sname:
  if i in string.ascii_letters:
   s=s+i
   c=1
  else:
   if i=='-' and c==0:
    continue
   else:
    s=s+i
    c=0
 if s[-1]=='-':
  s=s[:-1]
 print s

import sys
import re
import string
make_slug(sys.argv[1])
