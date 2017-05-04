#Problem 18

def reverse(fname):
 l=open(fname).readlines()
 r=map(lambda line:line.strip()[::-1],l)
 print '\n'.join(r)
 
import sys
reverse(sys.argv[1])
