# Problem 10

def unique(list):
 nlist=[]
 for i in list:
  if i not in nlist:
   nlist.append(i)
 return nlist

print unique([1,2,1,3,2,5])

