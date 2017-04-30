# Problem 25

def map(func,list):
  return [func(a) for a in list]
def square(list):
 return list*list

print map(square,range(5)) 
