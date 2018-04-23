import lib601.poly as poly
import sfSkeleton as sf
reload(sf)


import math
import lib601.poly as poly
import lib601.util as util

# Part 1: Stable?

s1 = sf.SystemFunction(poly.Polynomial([-1]),poly.Polynomial([1,5./6.,-1]))
print "dominant pole magnitude :", s1.dominantPole()
print "unstable, non oscillatory"

s2 = sf.SystemFunction(poly.Polynomial([1]),poly.Polynomial([3./8.,5./4.,1]))
print "dominant pole magnitude :", abs(s2.dominantPole())
print "stable, oscillatory"

s3 = sf.SystemFunction(poly.Polynomial([1]),poly.Polynomial([9./8.,3./2.,1]))
print "dominant pole magnitude :", abs(s3.dominantPole())
print "unstable, oscillatory"

s4 = sf.SystemFunction(poly.Polynomial([1]),poly.Polynomial([1./2.,1,1]))
print "dominant pole magnitude :", abs(s4.dominantPole())
print "stable, oscillatory"

# Part 2: DiffEq Behavior
sA = sf.SystemFunction(poly.Polynomial([1]),poly.Polynomial([42./64.,-13./8.,1]))
print sA.dominantPole()

sB = sf.SystemFunction(poly.Polynomial([1]),poly.Polynomial([42./64.,13./8.,1]))
print sB.dominantPole()

sC = sf.SystemFunction(poly.Polynomial([1]),poly.Polynomial([63./64.,2.,1.]))
print sC.dominantPole()

sD = sf.SystemFunction(poly.Polynomial([1]),poly.Polynomial([-63./64.,-2./8,1]))
print sD.dominantPole()

# A,4
# B,2
# C,1
# D,3