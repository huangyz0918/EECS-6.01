
# Structured Assignments
# a,b = (2,3)
# a + b = 5
# a,b = [2,3]
# a + b = 5
# [a, b] = [2, 3]
# a + b = 5
# (a,b) = (2,3,4)
# a + b = error.
# (a,b) = (2)
# a + b = error.
# (a, (b, c)) = (2, (3,4))
# a + b + c = 9
# (a, (b, c)) = (2, 3, 4)
# a + b + c = error.

# Nested and Shared Structure
# Nesting
# c = [[[4]],[1],[2,[-5]],-2]
# Sharing 1
# a = [1,2,3]
# b = [a[0],a[0]]
# Sharing 2
# a = [3,[1,2]]
# b = a

# List Comprehensions
# Even Squares
def evenSquares(list):
	# takes a list of number as input and returns a list of the
	# squares of the input values that are even
	newList = []
	for number in list:
		if number % 2 == 0: # even
			newList.append(number**2)
		else: # not even
			newList.append(number)
	return newList

# Sum of abs product
def sumAbsProd(list1,list2):
	# returns the sum of the absolute values of the products of
	# all the pairs of number where one is drawn from each of the
	# two input lists
	# use the sum and abs built-in functions (seems unnecessary)
	productsOfPairs	= []
	for i in list1:
		for j in list2:
			productsOfPairs.append(abs(i*j))
	return sum(productsOfPairs)

# OOPs 1.4.4
# Part1: Thing 1
class Thing:
	def set(self,v):
		self.x = v
	def get(self):
		return self.x
	def mangle(self):
		self.set(self.get() + 1)
		self.hasBeenMangled = True
	def clone(self):
		newThing = Thing()
		newThing.set(self.get())
		return newThing
	def __str__(self):
		return "This is a Thing with value "+str(self.get())		
a = Thing()
a.x = 6
# a.get(): Type int, value 6

b = Thing()
a.set(b)
# a.x: Type instance, Thing b

b.set(7)
# a.x.x: Type int, 7

# a.get(): Type instance, Thing b

# a.x.get(): Type int, 7

# 3 + a.get().get(): Type int, 10

c = a.get()
# c.x: Type int, 7

a.set(1-a.get().get())
# a.x: Type int, -6

c.set(3)
# a.get().get(): Type noneType, error

a = Thing()
b = Thing()
a.set(b)
b.set(a)
# a.x == b: Type boolean, True

# a.x.x == a: Type boolean, True

# a.x.x.x == b # Type boolean, True

# Part 2: Thing 2
def thingMangle(arg):
	arg.set(arg.get() + 1)
	arg.hasBeenMangled = True

a = Thing()
a.set(5)
thingMangle(a)
a.get() # int 6
a.hasBeenMangled # boolean True
b = Thing()
b.set(Thing())
b.get().set(3)
thingMangle(b.get())
b.get() # instance Thing (the Thing in b.set(Thing()))
b.get().get() # int 4
c = Thing()
# thingMangle(c) # noneType error nothing to mangle

# Part 3: Thing Mangle
# add a method called mangle to Thing which has the same effect as thingMangle
# added to the thing class

a = Thing()
a.set(3)
a.mangle()
# print a.get(), a.hasBeenMangled
a = Thing()
a.set(3)
thingMangle(a)
# print a.get(), a.hasBeenMangled

# Part 4: More mangling
# Define a procedure mangled that takes one argument, a number z, and which does:
# Creates a new Thing, sets its x value to be z, mangles it, and returns it
# use set, get, and mangle methods of Thing, do not access x directly
def mangled(z):
	a = Thing()
	a.set(z)
	a.mangle()
	return a
	
# print mangled(2).get()

# OOPs 1.4.5.
# Part 1: Assign
# Write a procedure, called assignThing, that takes two Things, thing1 and thing2
# as arguments and sets the stored value (x) of thing1 to the stored value of thing2.
# Use the set and get methods of Thing, do not access x directly
def assignThing(thing1,thing2):
	thing1.set(thing2.get())

# a = Thing()
# b = Thing()
# a.set(3)
# b.set(10)
# assignThing(a,b)
# print a.get() # Should be 10

# Part 2: Swap
# Write a procedure called swapThing, that takes two Things as arguments and 
# swaps the stored values (x) of the input Things
def swapThing(thing1,thing2):
	tempVal = thing1.get()
	assignThing(thing1,thing2)
	thing2.set(tempVal)

# a = Thing()
# b = Thing()
# a.set(3)
# b.set(10)
# swapThing(a,b)
# print a.get(),b.get() # Should be 10, 3

# Part 3: Sum
# Write a procedure, called sumOfThings that takes two Things as args and
# returns a new Thing whose stored value (x) is the sum of the stored values
# of the inputs
def sumOfThings(thing1,thing2):
	newThing = Thing()
	newThing.set(thing1.get() + thing2.get())
	return newThing
	
# a = Thing()
# b = Thing()
# a.set(3)
# b.set(10)
# print sumOfThings(a,b).get() # Should be 13

# Part 4: Sum of all
# Write a new procedure called sumOfAllThings, that takes a list of Things
# as its argument and returns a new Thing whose stored value, (x), is the
# sum of the stored values of all the input Things. The sum of an empty list
# is 0
def sumOfAllThings(thingsList):
	newThing = Thing()
	values = []
	for thing in thingsList:
		values.append(thing.get())
	newThing.set(sum(values))
	return newThing

# a = Thing()
# b = Thing()
# a.set(3)
# b.set(10)
# list = [a,b]
# print sumOfAllThings(list).get() # Should be 13
# c.set(100)
# list.append(c)
# print sumOfAllThings(list).get() # Should be 113
# print sumOfAllThings([]).get() # Should be 0

# OOPs 1.4.6
# Part 1: Thing clone
# Add a method clone to the Thing class which returns a completely new Thing
# with the same stored value
a = Thing()
a.set(3)
b = a.clone()
# print b.get() # should be 3

# Part 2: Thing str
# Add a __str__ method to the Thing class so that printing a Thing instance
# generates an informative string
# This is a Thing with a value of x
print a

# This assignment was pretty easy, but the practice was nice since I haven't
# done much OOP previously