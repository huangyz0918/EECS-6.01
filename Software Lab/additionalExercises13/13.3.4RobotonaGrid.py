import lib601.search as search
import lib601.sm as sm

class RobotMoves(sm.SM):
	legalInputs = ['left','right','down','up']
	startState = None
	def __init__(self,s):
		self.s = s
		self.goal = (3,4)
	def getNextValues(self, state, inp):
		if state == None:
			state = self.s
		nextState = list(state)
		if inp not in self.legalInputs:
			return (state,state)
		else:
			if inp == 'left':
				nextState[0] -= 1
			elif inp == 'right':
				nextState[0] += 1
			elif inp == 'up':
				nextState[1] += 1
			elif inp == 'down':
				nextState[1] -= 1
		nextState = tuple(nextState)
		return (nextState, nextState) 
	def done(self, state):
		return state == self.goal
		
sm = RobotMoves((0,0))
sm.transduce(['up','right','right','up','up','right','up','right','up'],verbose = True)