# Problem 26

def filter(f,list):
 return [a for a in list if f(a)==True]
def even(list):
 return list%2==0

print filter(even,range(10))
