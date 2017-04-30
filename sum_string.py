# Problem 3
def sum(list):
 l=len(list)
 i=1
 while i<l:
  list[i]=list[i-1]+list[i]
  i=i+1
 return list[i-1]
print sum(["hello","world"])
print sum(["aa","bb","cc"])
