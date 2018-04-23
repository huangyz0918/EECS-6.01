# Part 1: Add
# 
# Supply the base case for the recursive adding method

def add(a, b):
	if b == 0:
		return a
	else:
		return add(a, b-1) + 1
		
# print add(2,3)

# Part 2: Execution
# 
# 1. What conditions must be true of a and b for the procedure to terminate?
# 
# a can be any number and b must be a non-negative integer
# 
# 2. In order to compute add(5,2), what recursive calls are made to add?
# 
# add(5,2)
# add(5,1)
# add(5,0)

# Part 3: Sub

def sub(a,b):
	if b==0:
		return a
	else:
		return sub(a,b-1) - 1
		
# print sub(25,15)