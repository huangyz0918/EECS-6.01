#
#  MIT 6.01 (Week 1)
#  Design Lab 1. Problem 1.3.2

class Car:
 color = 'gray'
 def describeCar(self):
	return 'A cool ' + Car.color + ' car'
 def describeSelf(self):
	return 'A cool ' + self.color + ' car'

nona = Car()
print "1. nona.describeCar() yields: %s" % nona.describeCar()
print "2. nona.describeSelf() yields: %s" %  nona.describeSelf()
print "3. nona.color yields: %s" % nona.color

lola = Car()
lola.color = 'plaid'
 

print "4. lola.describeCar() yields: %s" % lola.describeCar()
print "5. lola.describeSelf() yields: %s" %  lola.describeSelf()
print "6. lola.color yields: %s" % lola.color 
print "7. nona.describeSelf() yields: %s" %  nona.describeSelf() 

nona.size = 'small'

# print "8. lola.size yields: %s" % lola.size
print "8. lola.size yields: %s" % "AttributeError: Car instance has no attribute 'size'"

Car.size = 'big'

print "9. lola.size yields: %s" % lola.size 
print "10. nona.size yields: %s" % nona.size 