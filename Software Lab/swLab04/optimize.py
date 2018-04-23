import lib601.sf as sf
import lib601.poly as poly
from lib601.plotWindow import PlotWindow
import rl

def makeSF(K):
    return sf.SystemFunctional(poly.Polynomial([K,0]),poly.Polynomial([K,-1,1]))

def viewRootLocus():
    # make an instance of RootLocus and start the viewer with K = 0.01
    rl.RootLocus(makeSF).view(0.01)

def stemplot(response):
    PlotWindow().stem(range(len(response)), response)

def bisection(f, xmin, xmax, threshold=1e-4):
    midpoint = 0.5*(xmin + xmax)
    slope = (f(midpoint + threshold) - f(midpoint - threshold))/ (2*threshold)
    while slope > threshold + 0 or slope < 0 - threshold:
        if slope > threshold:
            xmax = midpoint
            midpoint = 0.5*(xmax + xmin)
            slope = (f(midpoint + threshold) - f(midpoint - threshold))/ (2*threshold)
        else:
            xmin = midpoint
            midpoint = 0.5*(xmax + xmin)
            slope = (f(midpoint + threshold) - f(midpoint - threshold))/ (2*threshold)
    return (midpoint, f(midpoint))
