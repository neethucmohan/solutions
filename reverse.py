def reverse(list):
 l=len(list)
 s=l
 newlist=[None]*l
 for i in list:
  s=s-1
  newlist[s]=i
 return newlist

