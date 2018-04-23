import lib601.sm as sm

class CommentsSM(sm.SM):	# This works just like the turnstyle in 2.1.2
    startState = 'off'  
    def getNextValues(self, state, inp):
		if state == 'off':
			if inp == '#':
				return('on',inp)	# its on so start reading
			else:
				return('off',None)	# its off so stop reading
		if state == "on":
			if inp == '\n':
				return('off',None)
			else:
				return('on',inp)

 

def runTestsComm():
    m = CommentsSM()
    # Return only the outputs that are not None
    print 'Test1:',  [c for c in CommentsSM().transduce(x1) if not c==None]
    print 'Test2:',  [c for c in CommentsSM().transduce(x2) if not c==None]
    # Test that self.state is not being changed.
    m = CommentsSM()
    m.start()
    [m.getNextValues(m.state, i) for i in ' #foo #bar']
    print 'Test3:', [c for c in [m.step(i) for i in x2] if not c==None]

# execute runTestsComm() to carry out the testing, you should get:
runTestsComm()
#Test1: ['#', ' ', 'f', 'u', 'n', 'c', '#', ' ', 't', 'e', 's', 't', '#', ' ', 'c', 'o', 'm', 'm', 'e', 'n', 't']
#Test2: ['#', 'i', 'n', 'i', 't', 'i', 'a', 'l', ' ', 'c', 'o', 'm', 'm', 'e', 'n', 't', '#', ' ', 'f', 'u', 'n', 'c', '#', ' ', 't', 'e', 's', 't', '#', ' ', 'c', 'o', 'm', 'm', 'e', 'n', 't']
#Test3: ['#', 'i', 'n', 'i', 't', 'i', 'a', 'l', ' ', 'c', 'o', 'm', 'm', 'e', 'n', 't', '#', ' ', 'f', 'u', 'n', 'c', '#', ' ', 't', 'e', 's', 't', '#', ' ', 'c', 'o', 'm', 'm', 'e', 'n', 't']

##################################