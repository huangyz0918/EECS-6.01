import lib601.sm as sm

##################################
# Double Delay SM
##################################


class Delay2Machine(sm.SM):
    def __init__(self, val0, val1):
        self.startState = (val0, val1)		# the start state is a tup of two states
    def getNextValues(self, state, inp):
		(previousState, state) = state		# previous state = state[0], state = state[1]
		return ((state, inp), previousState)# returning (state, inp) as the next 2 and
											# previousState as the current state

# list1 = [0,1,2,3,4,5,6,7,8,9]
# list2 = [0,2,0,4,0,6,0,8,0,10]
# a = Delay2Machine(0,1)
# a.transduce([3,1,2,5,9], verbose = True)
# a.transduce(list1,verbose = True)
# a.transduce(list2,verbose = True)

def runTestsDelay():
    print 'Test1:', Delay2Machine(100, 10).transduce([1,0,2,0,0,3,0,0,0,4])
    print 'Test2:', Delay2Machine(10, 100).transduce([0,0,0,0,0,0,1])
    print 'Test3:', Delay2Machine(-1, 0).transduce([1,2,-3,1,2,-3])
    # Test that self.state is not being changed.
    m = Delay2Machine(100, 10)
    m.start()
    [m.getNextValues(m.state, i) for i in [-1,-2,-3,-4,-5,-6]]
    print 'Test4:', [m.step(i) for i in [1,0,2,0,0,3,0,0,0,4]]

runTestsDelay()
# execute runTestsDelay() to carry out the testing, you should get:
#Test1: [100, 10, 1, 0, 2, 0, 0, 3, 0, 0]
#Test2: [10, 100, 0, 0, 0, 0, 0]
#Test3: [-1, 0, 1, 2, -3, 1]
#Test4: [100, 10, 1, 0, 2, 0, 0, 3, 0, 0]

##################################