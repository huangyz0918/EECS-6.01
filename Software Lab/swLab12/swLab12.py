import lib601.dist as dist
import lib601.hmm as hmm
from simulator import Simulator
from random import randrange

def obsGivenLoc(loc):
    if loc == 0 or loc == 3:
        return dist.DDist({1: .8, 8 : .2})
    else:
        return dist.DDist({1: .2, 8 : .8})

ideal = [1,8,8,1,1,8,1,8,8]
numStates = len(ideal)

PA = dist.DDist({0:0, 1:0.0625, 2:0.25, 3:0.6874999999999999})
PBgA = obsGivenLoc
b = 1

# print dist.bayesRule(PA, PBgA, b)


## OBSERVATION MODELS

def perfectObsModel(state):
    return dist.deltaDist(ideal[state])

ideal = [1,8,8,1,1]

def obsModelA(state):
    return dist.mixture(dist.deltaDist(ideal[state]),dist.deltaDist(0),0.7)

def obsModelB(state):
    return dist.mixture(dist.deltaDist(ideal[state]),dist.uniformDist(range(10)),0.7)

def obsModelC(state):
    return dist.DDist({9-ideal[state]:1.0})

def obsModelD(state):
    return dist.DDist({9-ideal[state]:0.5, ideal[state]:0.5})

## TRANSITION MODELS

def moveRightModel(state):
    return dist.deltaDist(min(state+1, numStates-1))

def teleportModel(state):
    nominal = moveRightModel(state)
    return dist.mixture(dist.uniformDist(range(numStates)), nominal,0.3)

def resetModel(state):
    nominal = moveRightModel(state)
    return dist.mixture(dist.deltaDist(0), nominal, 0.3)

def teleportModel2(state):
    nominal = dist.deltaDist(state)
    return dist.mixture(dist.uniformDist(range(numStates)), nominal,0.3)

def resetModel2(state):
    nominal = dist.deltaDist(state)
    return dist.mixture(dist.deltaDist(0), nominal, 0.3)

## STARTING DISTRIBUTIONS

alwaysLeftPrior = dist.DDist({0:1.0})
uniformPrior = dist.uniformDist(range(len(ideal)))

hallwayPerfect = hmm.HMM(uniformPrior, moveRightModel, perfectObsModel)

## SIMULATION CODE

def simulate(m):
    Simulator(m, ideal).simulate()    

simulate(hallwayPerfect)
