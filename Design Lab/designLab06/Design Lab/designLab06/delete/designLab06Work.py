# coding=utf-8
import lib601.sf as sf
import lib601.optimize as optimize
import operator


# the proportional gain k1 applied to the error at time n, and
# the delay gain k2 applied to the error at time n-1
# and which returns a system function for a system whose input is the desired distance
# and whose output is the actual distance.
def delayPlusPropModel(k1, k2):
    T = 0.1
    V = 0.1
    print k2

    # Controller:  your code here
    # omega[n] = k1 * e[n] + k2 * e[n-1].
    controller = sf.FeedforwardAdd(sf.Gain(k1), sf.Cascade(sf.R(), sf.Gain(k2)))
    # print controller
    # The plant is like the one for the proportional controller.  Use
    # your definition from last week.
    # θ[n]=T∙ω[n-1]+θ[n-1]
    plant1 = sf.Cascade(sf.Cascade(sf.R(), sf.Gain(T)), sf.FeedbackAdd(sf.Gain(1), sf.R()))
    # d_0 [n]=VT∙sinθ[n-1]+d_0 [n-1]≈VT∙θ[n-1]+d_0 [n-1]
    plant2 = sf.Cascade(sf.Cascade(sf.R(), sf.Gain(T * V)), sf.FeedbackAdd(sf.Gain(1), sf.R()))
    # Combine the three parts
    sys = sf.FeedbackSubtract(sf.Cascade(sf.Cascade(controller, plant1), plant2), sf.Gain(1))
    # print sys
    return sys


# if __name__ == '__main__':
#     delayPlusPropModel(10, 20)
#     delayPlusPropModel(10, 30)


# You might want to define, and then use this function to find a good
# value for k2.

# Given k1, return the value of k2 for which the system converges most
# quickly, within the range k2Min, k2Max.  Should call optimize.optOverLine.


def bestk2(k1, k2Min, k2Max, numSteps):
    return optimize.optOverLine(objective=lambda k2: delayPlusPropModel(k1, k2)
                                , xmin=k2Min, xmax=k2Max, numXsteps=numSteps)


if __name__ == '__main__':
    print bestk2(10, 0, 20, 200)
    print bestk2(10, 0, 20, 100)
    # print bestk2(30, 0, 20, 200)
    # print bestk2(100, 0, 20, 200)
    # print bestk2(300, 0, 20, 200)


def anglePlusPropModel(k3, k4):
    T = 0.1
    V = 0.1

    # plant 1 is as before
    plant1 = None
    # plant2 is as before
    plant2 = None
    # The complete system
    sys = None

    return sys


# Given k3, return the value of k4 for which the system converges most
# quickly, within the range k4Min, k4Max.  Should call optimize.optOverLine.

def bestk4(k3, k4Min, k4Max, numSteps):
    pass
