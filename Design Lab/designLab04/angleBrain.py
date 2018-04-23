from soar.io import io
import lib601.sonarDist as sonarDist
import lib601.plotWindow as plotWindow
import lib601.util as util
import time

desiredRight = 0.4
forwardVelocity = 0.1


def setup():
    robot.distances = []
    robot.rvels = []
    robot.rvels2 = []
    robot.pTh = None
    robot.pTi = None

def brainStart():
    io.setForward(forwardVelocity)


def step():
    sonars = io.getSonars()
    (distanceRight, theta) = sonarDist.getDistanceRightAndAngle(sonars)
    print 'd_o =',distanceRight,' theta =',theta
    robot.distances.append(distanceRight)
    Kp = 1
    Ka = 0.632
    rotationalVelocity = Ka*((Kp/Ka)*(0.4 - distanceRight) - theta)

    io.setRotational(rotationalVelocity)
    
    computePlotValues(rotationalVelocity) 

def brainStop():
    plotWindow.PlotWindow(title="distanceRight vs time").plot(robot.distances)
    plotWindow.PlotWindow(title="rotationalVelocity vs time").plot(zip(robot.rvels,robot.rvels2))


def computePlotValues(rotationalVelocity):
    robot.rvels.append(rotationalVelocity)
    current = time.time()
    if robot.pTi is not None:
        dT = current-robot.pTi
    else:
        dT = 0.1
    robot.pTi = current
    t = io.getPosition()[2]
    if robot.pTh is not None:
        robot.rvels2.append(util.fixAnglePlusMinusPi(t-robot.pTh)/dT)
    robot.pTh = t


def shutdown():
    pass
