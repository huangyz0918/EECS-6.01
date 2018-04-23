def floatRange(lo, hi, stepSize):
	if type(lo) == type(hi) == type(stepSize) == int:
		return range(lo,hi,stepSize)
	else:
		value = lo
		rangeList = [value]
		while value + stepSize < hi:
			value += stepSize
			rangeList.append(value)
		return rangeList

print floatRange(1.5,5.5,.5)