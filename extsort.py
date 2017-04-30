# Problem 16

def extsort(list):
 i=0
 while i<len(list):
  list[i].split('.')
  i=i+1
 list.sort(key=lambda x:len(x))
 i=0
 while i<len(list):
  '.'.join(list[i])
  i=i+1
 return list

print extsort(['a.c','a.py','b.py','bar.txt','foo.txt','x.c'])



