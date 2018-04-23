import lib601.sf as sf
import lib601.optimize as optimize
import operator


def delayPlusPropModel(k1, k2):
	T = 0.1
	V = 0.1

	# Controller:  your code here
	controller = sf.FeedbackSubtract(sf.Gain(k1), sf.Cascade(sf.Gain(k2), sf.R()))
	# The plant is like the one for the proportional controller.  Use
	# your definition from last week.]
	plant1 = sf.Cascade(sf.Cascade(sf.Gain(T), sf.R()), sf.FeedbackAdd(sf.Gain(1), sf.R()))
	plant2 = sf.Cascade(sf.Cascade(sf.Gain(T * V), sf.R()), sf.FeedbackAdd(sf.Gain(1), sf.R()))
	# Combine the three parts
	sys = sf.FeedbackSubtract(sf.Cascade(sf.Cascade(controller, plant1), plant2))
	return sys


# You might want to define, and then use this function to find a good
# value for k2.

# Given k1, return the value of k2 for which the system converges most
# quickly, within the range k2Min, k2Max.  Should call optimize.optOverLine.

def loopk2(k1, k2Min, k2Max, numSteps):
	func = lambda k2: abs(delayPlusPropModel(k1, k2).dominantPole())
	bestValue, bestK2 = optimize.optOverLine(func, k2Min, k2Max, numSteps)
	return (bestValue, bestK2)
	pass


def anglePlusPropModel(k3, k4):
	T = 0.1
	V = 0.1

	# plant 1 is as before
	plant1 = sf.Cascade(sf.Cascade(sf.Gain(T), sf.R()), sf.FeedbackAdd(sf.Gain(1), sf.R()))
	# plant2 is as before
	plant2 = sf.Cascade(sf.Cascade(sf.Gain(T * V), sf.R()), sf.FeedbackAdd(sf.Gain(1), sf.R()))
	# The complete system
	sys = sf.FeedbackSubtract(sf.Cascade(sf.Cascade(sf.Gain(k3), sf.FeedbackSubtract(plant1, sf.Gain(k4))), plant2))

	return sys


# Given k3, return the value of k4 for which the system converges most
# quickly, within the range k4Min, k4Max.  Should call optimize.optOverLine.

def loopk4(k3, k4Min, k4Max, numSteps):
	func = lambda k4: max(anglePlusPropModel(k3, k4).poleMagnitudes())
	bestValue, bestK4 = optimize.optOverLine(func, k4Min, k4Max, numSteps)
	return (bestValue, bestK4)
	pass


if __name__ == '__main__':
    bestValues_1 = []
    bestValues_2 = []
    k2Values = []
    k4Values = []
	k1s = [10, 30, 100, 300]
	k3s = [1, 3, 10, 30]
	for k1 in k1s:
		bestValue, k2 = loopk2(k1, -1000, 1000, 20000)
		bestValues_1.append(bestValue)
		k2Values.append(k2)
#    print(bestValues_1)
#    print(k2Values)
	for k3 in k3s:
		bestValue, k4 = loopk4(k3, -100, 100, 2000)
		bestValues_2.append(bestValue)
		k4Values.append(k4)
#    print(bestValues_2)
#    print(k4Values)

