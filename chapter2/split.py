# Problem 12

def group(list,size):
 nlist=[]
 while len(list)>size:
  s=list[:size]
  nlist.append(s)
  list=list[size:]
 nlist.append(list)
 return nlist

print group([1,2,3,4,5,6,7,8,9],3)
print group([1,2,3,4,5,6,7,8,9],4)

