"""
Class and some supporting functions for representing and manipulating system functions. 
"""

import math
import lib601.poly as poly
import lib601.util as util


class SystemFunction():
    """
    Represent a system function as a ratio of polynomials in R
    """
    def __init__(self,numeratorPoly,denominatorPoly):
    	self.numerator = numeratorPoly
    	self.denominator = denominatorPoly	
    def poles(self):	# returns a list of the poles
    # the poles are the solutions to the poly in the denom
    # where z = 1/R
    	coeffsInZ = self.denominator.coeffs[:]
    	coeffsInZ = list(reversed(coeffsInZ))
    	polyInZ = poly.Polynomial(coeffsInZ)
    	return polyInZ.roots()
    def poleMagnitudes(self):
    	poleMags = []
    	poles = self.poles()
    	for pole in poles:
    		poleMags.append(abs(pole))
    	return poleMags
    def dominantPole(self):
    	poles = self.poles()
    	dominantPole = util.argmax(poles,abs)
    	return dominantPole
    	

    def __str__(self):
        return 'SF(' + self.numerator.__str__('R') + \
               '/' + self.denominator.__str__('R') + ')'

    __repr__ = __str__


def Cascade(sf1, sf2):
	cascadedNumerator = sf1.numerator*sf2.numerator
	cascadedDenominator = sf1.denominator*sf2.denominator
	return SystemFunction(cascadedNumerator,cascadedDenominator)

def FeedbackSubtract(sf1, sf2=None):
	fsNumerator = sf1.numerator*sf2.denominator
	fsDenominator = sf1.numerator*sf2.numerator + sf1.denominator*sf2.denominator
	return SystemFunction(fsNumerator,fsDenominator)



