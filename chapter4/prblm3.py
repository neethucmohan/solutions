# Problem 3

try:
    print "a"
    raise Exception("doom")
except:
    print "b"
else:
    print "c"
finally:
    print "d"


"""
   output
    a
    b
    d

"""
