# Problem 38

def invertdict(dic):
 it=dic.items()
 temp={}
 i=0
 while i<len(it):
  temp[it[i][1]]=it[i][0]
  i=i+1 
 return temp  

print invertdict({'x':1,'y':2,'z':3})
