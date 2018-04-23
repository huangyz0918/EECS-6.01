# Consider the following program:

class NN:
	def __init__(self):
		self.n = 0
	def get(self):
		self.n += 1
		return str(self.n)
	def reset(self):
		self.n = 0

class NS(NN):
	def get(self,s):
		return s + NN.get(self)
		
# 1. What does this print?

foo = NS()
print foo.get('a')	# a1
print foo.get('b') 	# b2
foo.reset()
print foo.get('c') 	# c1