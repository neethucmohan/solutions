# Problem 9

def cumulative_product(list):
 i=1
 while i<len(list):
  list[i]=list[i-1]*list[i]
  i=i+1
 return list

print cumulative_product([1,2,3,4])
print cumulative_product([4,3,2,1])

