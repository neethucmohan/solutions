# Problem 4

def f():
    try:
	print "a"
	return
    except:
	print "b"
    else:
	print "c"
    finally:
	print "d"
f()


"""
       output
         a
         d

"""
