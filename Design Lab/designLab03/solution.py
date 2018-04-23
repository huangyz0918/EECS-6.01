import math
import lib601.poly as poly
import lib601.sf as sf

def wallFollowerModel(K, T=0.1, V=0.1):
    numerator = poly.polynomial([K*T*T*V,0,0])
    denominator = poly.polynomial([K*T*T*V + 1, -2,1])
    result = sf.SystemFunctional(numerator,denominator)
    return result

def periodOfPole(pole):
    real = pole.real
    imag = pole.imag
    if math.atan2(imag,real) == 0:
        return real
    else:
        return abs(2*math.pi/math.atan2(imag,real))

def Pole(K):
    return (2+math.sqrt(abs(4-4*(1+K*0.1*0.1*0.1))))/2

for k in [0.2, 1, 10, 50, 100]:
    numerator = poly.Polynomial([k*0.1*0.1*0.1,0,0])
    denominator = poly.Polynomial([k*0.1*0.1*0.1 + 1, -2,1])
    result = sf.SystemFunctional(numerator,denominator)
    print result.dominantPole(), periodOfPole(result.dominantPole()) 
