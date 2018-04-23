import lib601.sig as sig
import lib601.ts as ts
import lib601.poly as poly
import lib601.sf as sf
import math


def controller(k):
    return sf.SystemFunction(poly.Polynomial([k]), poly.Polynomial([1]))


def plant1(T):
    return sf.SystemFunction(poly.Polynomial([T, 0]), poly.Polynomial([-1, 1]))


def plant2(T, V):
    return sf.SystemFunction(poly.Polynomial([T * V, 0]), poly.Polynomial([-1, 1]))


def wallFollowerModel(k, T, V):
    one = sf.Cascade(sf.Cascade(controller(k), plant1(T)), plant2(T, V))
    return sf.FeedbackSubtract(one, sf.Gain(1))


if __name__ == '__main__':
    for k in range(1, 10):
        model = wallFollowerModel(k, 0.1, 0.1)
        T = 2 * math.pi / (model.dominantPole() - 1)
        print 'k:%d,T:%r' % (k, T)
