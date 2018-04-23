import math
import lib601.sm as sm
from soar.io import io
import lib601.gfx as gfx
import lib601.util as util

######################################################################
#
#            Do your work in this file
#
######################################################################

dDesired = 0.7


# Input is output of Sensor machine (below); output is an action.
# Note that this machine must also compute E, the error, and output
# the velocity, based on that.
class Controller(sm.SM):
    k = -2.8

    def getNextValues(self, state, inp):
        ################
        # Your code here
        ################
        error = dDesired - inp
        output = self.k * error

        velocity = output

        return state, io.Action(fvel=velocity, rvel=0)


# Input is SensorInput instance; output is a delayed front sonar reading
class Sensor(sm.SM):
    def __init__(self, initDist, numDelays):
        self.startState = [initDist] * numDelays

    def getNextValues(self, state, inp):
        print inp.sonars[3]
        output = state[-1]
        state = [inp.sonars[3]] + state[:-1]
        return state, output


mySM = sm.Cascade(Sensor(1.5, 1), Controller())
mySM.name = 'brainSM'


######################################################################
###
###          Brain methods
###
######################################################################

def plotSonar(sonarNum):
    robot.gfx.addStaticPlotFunction(y=('sonar' + str(sonarNum),
                                       lambda: io.SensorInput().sonars[sonarNum]))


def setup():
    robot.gfx = gfx.RobotGraphics(drawSlimeTrail=False)
    plotSonar(3)
    robot.behavior = mySM
    robot.behavior.start(traceTasks=robot.gfx.tasks())


def brainStart():
    pass


def step():
    robot.behavior.step(io.SensorInput()).execute()


def brainStop():
    pass


def shutdown():
    pass
