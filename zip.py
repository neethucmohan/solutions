# Problem 24

def zip(a,b):
 lb=len(b)
 i=0
 nlist=[None]*lb
 list=[(x,y) for x in a for y in b]
 k=0
 while i<lb:
  nlist[i]=list[k]
  i=i+1
  k=k+lb+1
 return nlist

print zip([1,2,3],["a","b","c"])
