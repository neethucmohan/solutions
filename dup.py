# Problem 11

def dups(list):
 l=len(list)
 nlist=[]
 i=0
 while i<l:
  k=0
  while k<l:
   if i!=k:
    if list[i]==list[k]:
      nlist.append(list[i])
      a=list[i]
      for x in list:
       if a==x:
        list[i]=None
   k=k+1
  i=i+1
 return nlist
   

print dups([1,2,1,3,2,5])
