import operator
import lib601.util as util

#-----------------------------------------------------------------------------

class DDist:
    """
    Discrete distribution represented as a dictionary.  Can be
    sparse, in the sense that elements that are not explicitly
    contained in the dictionary are assumed to have zero probability.
    """
    def __init__(self, dictionary):
        self.d = dictionary
        """ Dictionary whose keys are elements of the domain and values
        are their probabilities. """

    def dictCopy(self):
        """
        @returns: A copy of the dictionary for this distribution.
        """
        return self.d.copy()

    def prob(self, elt):
        """
        @param elt: an element of the domain of this distribution
        (does not need to be explicitly represented in the dictionary;
        in fact, for any element not in the dictionary, we return
        probability 0 without error.)
        @returns: the probability associated with C{elt}
        """
        if self.d.has_key(elt):
            return self.d[elt]
        else:
            return 0

    def support(self):
        """
        @returns: A list (in arbitrary order) of the elements of this
        distribution with non-zero probabability.
        """
        return [k for k in self.d.keys() if self.prob(k) > 0]

    def __repr__(self):
        if len(self.d.items()) == 0:
            return "Empty DDist"
        else:
            dictRepr = reduce(operator.add,
                              [util.prettyString(k)+": "+\
                               util.prettyString(p)+", " \
                               for (k, p) in self.d.items()])
            return "DDist(" + dictRepr[:-2] + ")"
    __str__ = __repr__

#-----------------------------------------------------------------------------

def incrDictEntry(d, k, v):
    """
    If dictionary C{d} has key C{k}, then increment C{d[k]} by C{v}.
    Else set C{d[k] = v}.
    
    @param d: dictionary
    @param k: legal dictionary key (doesn't have to be in C{d})
    @param v: numeric value
    """
    if d.has_key(k):
        d[k] += v
    else:
        d[k] = v


#-----------------------------------------------------------------------------

class MixtureDist:
	def __init__(self, d1, d2, p):
		distDict = {}
		domain = []
		for value in d1.support() + d2.support():
			domain.append(value)
		domain = list(set(domain))	# removes repeated values
		for value in domain:
			distDict[value] = p*d1.prob(value) + (1.-p)*d2.prob(value)
		self.dist = DDist(distDict)
	def prob(self, elt):
		return self.dist.prob(elt)
	def support(self):
		return self.dist.support()
	def __str__(self):
		result = 'MixtureDist({'
		elts = self.support()
		for x in elts[:-1]:
			result += str(x) + ' : ' + str(self.prob(x)) + ', '
		result += str(elts[-1]) + ' : ' + str(self.prob(elts[-1])) + '})'
		return result
	__repr__ = __str__

def squareDist(lo, hi, loLimit = None, hiLimit = None):
	distDict = {}
	prob = 1./(hi-lo)
	if loLimit == hiLimit == None:
		for value in range(lo,hi):
			distDict[value] = prob
	else:
		if lo < loLimit:
			distDict[loLimit] = 0.
		if hi > hiLimit:
			distDict[hiLimit] = 0.
		for value in range(lo,hi):
			if hiLimit >= value >= loLimit:
				if value not in distDict.keys():
					distDict[value] = prob
				else:
					distDict[value] += prob
			elif value < loLimit:
				distDict[loLimit] += prob
			elif value > hiLimit:
				distDict[hiLimit] += prob
	return DDist(distDict)

def triangleDist(peak, halfWidth, loLimit = None, hiLimit = None):
	distDict = {}
	if loLimit == None:	loLimit = peak - 10*halfWidth
	if hiLimit == None: 	hiLimit = peak + 10*halfWidth
	nStates = float(halfWidth**2)
	if peak - halfWidth + 1 >= loLimit and peak + halfWidth - 1 <= hiLimit:
		for value in range(halfWidth):
			distDict[peak+value] = abs(value-halfWidth)/nStates
			distDict[peak-value] = abs(value-halfWidth)/nStates
	else:
		if peak - halfWidth + 1 < loLimit:
			distDict[loLimit] = 0.
		if peak + halfWidth - 1 > hiLimit:
			distDict[hiLimit] = 0.
		for value in range(halfWidth):
			if peak+value <= hiLimit:
				distDict[peak+value] = abs(value-halfWidth)/nStates
			else:
				distDict[hiLimit] += abs(value-halfWidth)/nStates
			if peak-value >= loLimit:
				distDict[peak-value] = abs(value-halfWidth)/nStates
			else:
				distDict[loLimit] += abs(value-halfWidth)/nStates
		if peak < loLimit:
			distDict[loLimit] += distDict[peak]
			del distDict[peak]
		if peak > hiLimit:
			distDict[hiLimit] += distDict[peak]
			del DistDict[peak]
	return DDist(distDict)
	
print MixtureDist(squareDist(2,4),squareDist(10,12),0.5)
print MixtureDist(squareDist(2,4),squareDist(10,12),0.9)
print MixtureDist(squareDist(2,6),squareDist(4,8),0.5)
#-----------------------------------------------------------------------------
# If you want to plot your distributions for debugging, put this file
# in a directory that contains lib601, and where that lib601 contains
# sig.pyc.  Uncomment all of the following.  Then you can plot a
# distribution with something like:
# plotIntDist(MixtureDist(squareDist(2, 6), squareDist(4, 8), 0.5), 10)

# import lib601.sig as sig

# class IntDistSignal(sig.Signal):
#     def __init__(self, d):
#         self.dist = d
#     def sample(self, n):
#         return self.dist.prob(n)
# def plotIntDist(d, n):
#     IntDistSignal(d).plot(end = n, yOrigin = 0)

