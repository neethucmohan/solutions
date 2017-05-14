# Problem 1

class reverse_iter:
	def __init__(self,list):
	 self.list=list
         self.i=len(self.list)-1
	def __iter__(self):
	 return self
	def next(self):
	 if self.i>=0:
	  i=self.i
	  self.i-=1
	  return self.list[i]
	 else:
	  raise StopIteration()

c=reverse_iter([7,5,9,1,6])
while True:
 print c.next()



