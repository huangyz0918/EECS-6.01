# coding=utf-8
import math
import lib601.util as util
import lib601.sm as sm
import lib601.gfx as gfx
from soar.io import io

import os

labPath = os.getcwd()
from sys import path

if not labPath in path:
	path.append(labPath)
	print 'setting labPath to', labPath

from boundaryFollower import boundaryFollowerClass


class boundaryFollowerClass2(boundaryFollowerClass):
	def __init__(self):
		pass

	def getNextValues(self, state, inp):
		V4 = inp.analogInputs[2]
		V6 = inp.analogInputs[1]
		# print 'inputs ==>',inp.analogInputs
		print 'V4 ===>', V4
		print 'V6 ===>', V6
		# neckVoltage = inp.analogInputs[1]
		# outputVoltage = io.Action(fvel=0, rvel=0,voltage = V0)
		V0 = ((5 * (V6 - V4) / 2.08)* 0.5 + 5)
		print 'V0 ===>', V0
		if V0 < 0:
			V0 = 0
		if V0 > 10:
			V0 = 10

		V_light = 6.2
		# return state, io.Action(fvel=0.0, rvel=0, voltage=V0)
		if V6 > V_light:
			print 'find light'
			return state, io.Action(fvel = 0.1, rvel = 0.3 * (V0 - 5), voltage=V0)
		else:
			print 'boundaryFollower'
			return boundaryFollowerClass.getNextValues(self, state, inp)


# inp.analoginputs : List of 4 analog input values.
# analoginputs[0] ==> PIN 1
# analoginputs[1] ==> PIN 3: AIN2
# analoginputs[2] ==> PIN 5: AIN3
# analoginputs[3] ==> PIN 7: AOUT

# PIN4: left voltage
# PIN6: right voltage
# PIN4 - PIN6 : PIN5 ==> AOUT

mySM = boundaryFollowerClass2()
mySM.name = 'brainSM'


# 使用沿墙走的功能，则取消注释这句话
# mySM = boundaryFollowerClass()

######################################################################
###
###          Brain methods
###
######################################################################

def setup():
	robot.gfx = gfx.RobotGraphics(drawSlimeTrail=False)


def brainStart():
	robot.behavior = mySM
	robot.behavior.start(robot.gfx.tasks())
	robot.data = []


def step():
	inp = io.SensorInput()
	robot.behavior.step(inp).execute()


# print


def brainStop():
	pass


def shutdown():
	pass
