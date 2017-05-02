# Problem 34

def word_freq(words):
 frequency={}
 for w in words:
  frequency[w]=frequency.get(w,0)+1
 return frequency
 
def read_words(fname):
 return open(fname).read().split()

def main(fname):
 frequency=word_freq(read_words(fname))
 v=frequency.items()
 v.sort(key=lambda x:x[1])
 for i in v:
  print i[0],i[1] 

import sys
main(sys.argv[1])

