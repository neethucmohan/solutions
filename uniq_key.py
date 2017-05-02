# Problem 14

def unique(list):
 nlist=[]
 for i in list:
  if i not in nlist:
   nlist.append(i)
 return nlist

def key_uniq(nlist,key=lambda x:x):
 return unique(map(key,nlist))

print key_uniq(['python','java','Python','Java'],key=lambda s:s.lower())
