# Problem 6

def reverse(list):
 l=len(list)
 s=l
 newlist=[None]*l
 for i in list:
  s=s-1
  newlist[s]=i
 return newlist

print reverse([1,2,3,4])
print reverse(reverse([1,2,3,4]))
