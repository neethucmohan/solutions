# Problem 37

def valuesort(dic):
 s=[]
 a=0
 r=[]
 s=sorted(dic.items(),key=lambda x:x[0])
 while a<len(s):
  r.append(s[a][1])
  a=a+1
 return r
 
print valuesort({'x':1,'y':2,'a':3})
