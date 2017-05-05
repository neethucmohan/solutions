# Problem 9

def val(no):
 exp=r"\d{10}|\d{4}[-\s]\d{7}|[(]\d{2}[)]\d{10}"
 if re.match(exp,no):
  print "valid phn no"
 else:
  print "Not a valid no"

import sys
import re
val(sys.argv[1])



