# Write a recursive Python procedure slowMod that takes two arguments
# a and b, both of which are z>0, and returns the mod of a and b using
# only addition, subtraction, and simple tests

def slowMod(a,b):	# Think of this like long division
	if a < b:
		return a	# Here is the remainder
	else:
		return slowMod(a - b,b)		# Here we chop away at a in increments of b
	

print slowMod(5,2)
print slowMod(6,2)
print slowMod(8,3)
print slowMod(4,6)