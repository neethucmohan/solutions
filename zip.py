# Problem 24

def zip(a,b):
 lb=len(b)
 i=0
 nlist=[None]*lb
 list=[(x,y) for x in a for y in b]
 while i<lb:
  nlist[i]=list[i]
  i=i+1
 return nlist

print zip([1,2,3],["a","b","c"])
