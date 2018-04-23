class SM:
    startState = None

    def getStartState(self):
        return self.startState

    def getNextValues(self, state, inp):
        newState = state
        output = inp
        return (newState, output)

    def start(self):
        self.state = self.getStartState()

    def step(self, inp):
        (s, o) = self.getNextValues(self.state, inp)
        self.state = s
        return o

    def transduce(self, inps):
        result = []
        self.start()
        for i in inps:
            result.append(self.step(i))
        return result

######################################################################
#    block diagram components
######################################################################
class R(SM):
    def __init__(self, startState):
        self.startState = startState

    def getNextValues(self, state, inp):
        nextState = inp
        output = state
        return (nextState, output)

class Gain(SM):
    def __init__(self, K):
        self.K = K
        self.startState = self.K

    def getNextValues(self, state, inp):
        nextState = self.K * inp
        output = self.K * inp
        return (nextState, output)

######################################################################
#    Compositions
######################################################################
class Cascade(SM):
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
        self.startState = (m1.startState, m2.startState)

    def getNextValues(self, state, inp):
        m1 = self.m1
        m2 = self.m2
        m1_next_state = m1.getNextValues(state[0],inp)[0]
        m2_next_state = m2.getNextValues(state[1], m1.getNextValues(state[0],inp)[1])
        nextState = (m1_next_state, m2_next_state[0])
        output = m2_next_state[1]
        return (nextState, output)


def testCascadeRG():
    r = R(3.0)
    g = Gain(3)
    s = Cascade(r,g)
    s.start()
    print s.step(2.0)
    print s.step(5.0)
    print s.step(3.0)

def testCascadeRR():
    ans = Cascade(R(-4.0), R(4.0)).transduce([-8.0,5.0,-5.0,-2.0,3.0])
    print ans
# [4.0, -4.0, -8.0, 5.0, -5.0]


class FeedbackAdd(SM):
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def getStartState(self):
        # Start state is tuple of start states of the two machines
        return (self.m1.getStartState(), self.m2.getStartState())

    def getNextValues(self, state, inp):
        (s1, s2) = state
        # Find the output of m2 by propagating an arbitrary input through
        # the cascade of m1 and m2
        (ignore, o1) = self.m1.getNextValues(s1, 99999999)
        (ignore, o2) = self.m2.getNextValues(s2, o1)
        # Now get a real new state and output
        (newS1, output) = self.m1.getNextValues(s1, inp+o2)
        (newS2, o2) = self.m2.getNextValues(s2, output)
        return ((newS1, newS2), output)


mystery = FeedbackAdd(FeedbackAdd(R(0),Gain(1)), R(0))
# sm = SM()
# print sm.start()
testCascadeRR()
