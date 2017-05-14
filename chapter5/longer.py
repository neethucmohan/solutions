# Problem 2 

def readfiles(filenames):
  for line in open(f):
   yield line

def grep(lines):
 return (line for line in lines if len(line)>40)

def printlines(lines):
 try:
  for line in lines:
   print line
 except IOError:
  print "no files"


def main(filenames):+
 lines=readfiles(filenames)
 lines=grep(lines)
 printlines(lines)

import sys
l=len(sys.argv)
filenames=[sys.argv[x] for x in range(1,l)]
main(filenames)

