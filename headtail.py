# Problem 19

def headtail(f):
 line=open(f).readlines()
 f=line[:10]
 print "First 10 lines\n", ''.join(f).strip()
 l=line[-10:]
 print "last 10 lines\n", ''.join(l).strip()
    
import sys
headtail(sys.argv[1])
