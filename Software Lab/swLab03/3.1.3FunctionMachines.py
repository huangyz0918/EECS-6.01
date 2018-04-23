import lib601.sm as sm

class PureFunction(sm.SM):
	def __init__(self, f):
		self.f = f
	def getNextValues(self,state,inp):
		return (state,self.f(inp))