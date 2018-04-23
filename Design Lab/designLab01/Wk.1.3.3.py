#
#  MIT 6.01 (Week 1)
#  Design Lab 1. Problem 1.3.3

class Car:
	weight = 1000

	def __init__(self, weight, driver):
		self.weight = weight
		self.driver = driver

class Person:
	weight = 100

	def __init__(self, weight):
		self.weight = weight

# 1.
# Person
# <__main__.Person instance at 0x0000000001C53748>

# 2.
p = Person(150)
print "p is %r" % p

#3. 
c = Car(2000, p)
print "Car.weight is %r" % Car.weight

#4
print "c.weight is %r" % c.weight 

#5
print "c.driver.weight is %r" % c.driver.weight