import math
import lib601.util as util
import lib601.soarWorld as soarWorld
from soar.io import io
from mazeAnswers import *

import tk
import soarWorld
tk.setInited()

worldname = 'dl9World'
# worldname = 'bigEmptyWorld'

PATH_TO_WORLD = '%s.py' % worldname
world = [i.strip() for i in open('%s.txt' % worldname).readlines()]

bounds = {'dl9World': (0.0,0.0,10.8,10.8),
          'bigEmptyWorld': (0.0,0.0,4.05,4.05)}

def getPath(worldname, maze):
    if worldname == 'dl9World':
        goal_test = lambda (r,c): (r,c) == maze.goal
        return search(maze_successors(maze),maze.start,goal_test)
    else:
        return [util.Point(0.911250, 0.911250), util.Point(1.721250, 0.506250), util.Point(2.531250, 1.316250), util.Point(1.721250, 1.721250), util.Point(0.911250, 2.126250), util.Point(1.721250, 2.936250), util.Point(2.531250, 2.531250)]
        

class RobotMaze(Maze):
    def __init__(self, mapText, x0, y0, x1, y1):
        Maze.__init__(self, mapText) #run Maze's __init__ on this instance
        self.x0 = float(x0)
        self.y0 = float(y0)
        self.x1 = float(x1)
        self.y1 = float(y1)
    
    def pointToIndices(self, point):
        ix = int(math.floor((point.x-self.x0)*self.width/(self.x1-self.x0)))
        iix = min(max(0,ix),self.width-1)
        iy = int(math.floor((point.y-self.y0)*self.height/(self.y1-self.y0)))
        iiy = min(max(0,iy),self.height-1)
        return ((self.height-1-iiy,iix))

    def indicesToPoint(self, (r,c)):
        x = self.x0 + (c+0.5)*(self.x1-self.x0)/self.width
        y = self.y0 + (self.height-r-0.5)*(self.y1-self.y0)/self.height
        return util.Point(x,y)

# this function is called when the brain is loaded
def setup():
    robot.maze = RobotMaze(world, *(bounds[worldname]))
    robot.path = getPath(worldname, robot.maze)
    (robot.window, robot.initialLocation) = \
                   soarWorld.plotSoarWorldDW(PATH_TO_WORLD)
    if robot.path:
        robot.window.drawPath([i.x - \
                               robot.initialLocation.x \
                               for i in robot.path],
                              [i.y - \
                               robot.initialLocation.y \
                               for i in robot.path], color = 'purple')
    else:
        print 'no plan from', robot.maze.start, 'to', robot.maze.goal
    robot.slimeX = []
    robot.slimeY = []

# this function is called when the start button is pushed
def brainStart():
    pass

# this function is called 10 times per second
i = 0
def step():
    global i
    x, y, theta = io.getPosition()
    robot.slimeX.append(x)
    robot.slimeY.append(y)
    
    currentPoint = util.Point(x,y).add(robot.initialLocation)
    currentAngle = theta
    destinationPoint = robot.path[i]
    thetad = currentPoint.angleTo(destinationPoint)
    
    if util.nearAngle(currentAngle,thetad,math.pi/180.0):
        io.setForward(0.1)
        io.setRotational(0)
        if currentPoint.distance(destinationPoint) < 0.02:
            i += 1
            print i
    else:
        theta_constant = util.fixAnglePlusMinusPi(thetad - currentAngle)
        io.setRotational(theta_constant)
        io.setForward(0)



# called when the stop button is pushed
def brainStop():
    for i in range(len(robot.slimeX)):
        robot.window.drawPoint(robot.slimeX[i], robot.slimeY[i], 'red')

# called when brain or world is reloaded (before setup)
def shutdown():
    pass
