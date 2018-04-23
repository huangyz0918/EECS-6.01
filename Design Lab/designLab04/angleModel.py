import lib601.poly as poly
import lib601.sf as sf
from lib601.optimize import bisection

def angleModel(Kp, Ka):
    T = 0.1
    V = 0.1
    plant1 = sf.SystemFunctional(poly.Polynomial([Ka*T,0]),poly.Polynomial([-1,1]))
    plant2 = sf.SystemFunctional(poly.Polynomial([V*T,0]),poly.Polynomial([-1,1]))
    inner_system = sf.FeedbackSubtract(plant1,sf.Gain(1))
    system = sf.Cascade(sf.Cascade(sf.Gain(Kp/Ka),inner_system), plant2)
    al = sf.FeedbackSubtract(system,sf.Gain(1))
    return al

def f(Ka):
    return abs(angleModel(300,Ka).dominantPole())

# Given Kp, return the value of Ka for which the system converges most
# quickly, within the range KaMin, KaMax.

def bestKa(Kp, KaMin, KaMax):
    return bisection(f, KaMin, KaMax, 1e-4)


kp = bestKa(1,0,10)
kp = bestKa(3,0,10)
kp = bestKa(10,0,25)
kp = bestKa(30,0,25)
kp = bestKa(100,0,25)
kp = bestKa(300,0,25)

print kp, kp[1], angleModel(300,kp[0]).dominantPole()
    



