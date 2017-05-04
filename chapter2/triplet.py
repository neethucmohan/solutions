# Problem 27

def triplets(no):
 return [(a,b,c) for a in range(no) for b in range(no) for c in range(no) if a+b==c and a!=0 and b!=0 and c!=0]

import sys
print triplets(int(sys.argv[1]))

