import lib601.sf as sf


# the proportional gain, k, applied to the error.
# returns the system function of a system
# whose input is the distance error' and
# whose output is the commanded velocity.'
def controllerSF(k):
    pass


# the time step duration T.
# returns a system function for a system
# whose input is the commanded' velocity and
# whose output is the actual distance to the wall.'
def plantSF(T):
    pass


# returns a system function for a system
# whose input is the actual sensor value and
# whose output is a one-step delayed sensor reading.
def sensorSF():
    pass


# the time step duration T.
# the proportional gain, k, applied to the error.
# returns a system function for a system
# whose input is the desired distance' and
# whose output is the actual distance to the wall.'
def wallFinderSystemSF(T, k):
    pass
