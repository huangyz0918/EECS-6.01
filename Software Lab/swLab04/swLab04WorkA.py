import lib601.poly as poly
import lib601.sig
from lib601.sig import *

## You can evaluate expressions that use any of the classes or
## functions from the sig module (Signals class, etc.).  You do not
## need to prefix them with "sig."


# s = CosineSignal()
# a = CosineSignal(omega = .25, phase = 0.5)
# s.plot(-5,5)
# a.plot(-5,5)

# Problem Wk.4.1.1: Constructing Signals
# Use any: ConstantSignal, UnitSampleSignal, CosineSignal, StepSignal,
# SummedSignal, ScaledSignal, R, Rn and polyR (all defined in handout).
# They are all defined for you already

# = 3.0 for t>= 3 and 0 otherwise
step1 = Rn(ScaledSignal(StepSignal(),3),3)
#step1.plot(-5,5)
step2 = SummedSignal(Rn(step1,5),ConstantSignal(-3))
#step2.plot(-10,10)
stepUpDown = SummedSignal(step1,SummedSignal(Rn(step1,4),ConstantSignal(-3)))
# stepUpDown.plot(-10,10)
p = poly.Polynomial([5,0,3,0,1,0])
stepUpDownPoly = polyR(UnitSampleSignal(),p)
stepUpDownPoly.plot(0,10)