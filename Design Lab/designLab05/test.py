from lib601 import sf
from lib601.poly import Polynomial
from lib601.sf import SystemFunction

fun = SystemFunction(Polynomial([1, 2]), Polynomial([3, 4, 5]))
print fun
print fun.poles()
print fun.dominantPole()
print fun.poleMagnitudes()
print fun.differenceEquation()
print fun.differenceEquation().systemFunction()
machine = fun.differenceEquation().stateMachine()
print fun.differenceEquation().stateMachine()
