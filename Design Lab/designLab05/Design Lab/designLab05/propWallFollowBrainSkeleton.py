import math
import lib601.sm as sm
from soar.io import io
import lib601.gfx as gfx
import lib601.util as util
import lib601.sonarDist as sonarDist

reload(gfx)

######################################################################
#
#            Brain SM
#
######################################################################

desiredRight = 0.5
forwardVelocity = 0.1


# No additional delay
class Sensor(sm.SM):
    def getNextValues(self, state, inp):
        return (state, sonarDist.getDistanceRight(inp.sonars))


# inp is the distance to the right
class WallFollower(sm.SM):
    def getNextValues(self, state, inp):
        ################
        # Your code here
        ################
        pass


mySM = sm.Cascade(Sensor(), WallFollower())


######################################################################
#
#            Running the robot
#
######################################################################

def plotDist():
    func = lambda: sonarDist.getDistanceRight(io.SensorInput().sonars)
    robot.gfx.addStaticPlotFunction(y=('d_o', func))


def setup():
    robot.gfx = gfx.RobotGraphics(drawSlimeTrail=False)
    plotDist()
    robot.behavior = mySM
    robot.behavior.start(traceTasks=robot.gfx.tasks())


def step():
    robot.behavior.step(io.SensorInput()).execute()


def brainStart():
    # Do this to be sure that the plots are cleared whenever you restart
    robot.gfx.clearPlotData()


def brainStop():
    pass


def shutdown():
    pass
