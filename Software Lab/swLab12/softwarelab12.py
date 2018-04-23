from dist.py import *

def obsGivenLoc(loc):
    if loc == 0 or loc == 3:
        return DDist({1: .8, 8 : .2})
    else:
        return DDist({1: .2, 8 : .8})


