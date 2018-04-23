import operator
# Part 1: Argmin

def f(x):
	return (x-3)**2

def argmin(f, input):
	bestValSoFar = f(input[0])
	bestArgSoFar = input[0]
	for x in input:
		if f(x) < bestValSoFar:
			bestValSoFar = f(x)
			bestArgSoFar = x
	return (bestValSoFar,bestArgSoFar)

# Part 2: Argopt

def argopt(f,input,comp):
	bestValSoFar = f(input[0])
	bestArgSoFar = input[0]
	for x in input:
		if comp(f(x),bestValSoFar):
			bestValSoFar = f(x)
			bestArgSoFar = x
	return (bestValSoFar,bestArgSoFar)

# print argopt(lambda x: (x-3)**2, [1,2,3,4], operator.lt)
# print argopt(lambda x: x[0], [(1,2),(3,4)], operator.lt)