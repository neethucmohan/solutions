#Problem 7

def max(list):
 larg=list[0]
 for i in list:
  if larg<i:
   larg=i
 return larg

def min(list):
 small=list[0]
 for i in list:
  if small>i:
   small=i
 return small

print max([3,2,9,5,1,8,7])
print min([6,5,8,4,1,9,6])
  
 
