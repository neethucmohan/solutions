# Problem 28

def enumerate(list):
 ind=range(len(list))
 nlist=zip(ind,list)
 return nlist

print enumerate(["a","b","c"])
for index,value in enumerate(["a","b","c"]):
 print index,value
