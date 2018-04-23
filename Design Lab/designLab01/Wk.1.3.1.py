#
#  MIT 6.01 (Week 1)
#  Design Lab 1. Problem 1.3.1

def fib(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)


# Test the Fibonacci procedure
firstTest = 6  # fib(6) -> 8
secondTest = 7 # fib(7) -> 13
thirdTest = 8  # fib(8) -> 21
firstResult = fib(firstTest)
secondResult = fib(secondTest)
thirdResult = fib(thirdTest)

print "fib1(%r) = %r" % (firstTest, firstResult)
print "fib2(%r) = %r" % (secondTest, secondResult)
print "fib3(%r) = %r" % (thirdTest, thirdResult)