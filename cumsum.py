# Problem 8

def cumulative_sum(list):
 i=1
 while i<len(list):
  list[i]=list[i-1]+list[i]
  i=i+1
 return list

print cumulative_sum([1,2,3,4]) 
print cumulative_sum([4,3,2,1])
print cumulative_sum(['a','ab','abc','abcd'])
