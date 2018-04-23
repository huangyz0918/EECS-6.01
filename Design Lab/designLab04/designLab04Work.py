import lib601.sig as sig  # Signal
import lib601.ts as ts  # TransducedSignal
import lib601.sm as sm  # SM


######################################################################
##  Make a state machine model using primitives and combinators
######################################################################

# the proportional gain, k, applied to the error


def controller(k):
    return sm.Gain(k)


# the time step duration T.
# the initial actual distance to the wall, initD.
def plant(T, initD):
    gain = sm.Gain(T)
    delay_x = sm.R(0)

    delay_y = sm.FeedbackAdd(sm.Gain(1), sm.R(initD))

    return sm.Cascade(sm.Cascade(gain, delay_x), delay_y)


# the initial (actual) distance to the wall, initD.
def sensor(initD):
    return sm.R(initD)


# the time step duration T.
# the initial actual distance to the wall, initD
# the proportional gain, k, applied to the error.
def wallFinderSystem(T, initD, k):
    controller_v = controller(k)
    plant_v = plant(T, initD)
    sensor_v = sensor(initD)
    return sm.Cascade(sm.Gain(-1), sm.FeedbackAdd(sm.Cascade(controller_v, plant_v), sensor_v))


# Plots the sequence of distances when the robot starts at distance
# initD from the wall, and desires to be at distance 0.7 m.  Time step
# is 0.1 s.  Parameter k is the gain;  end specifies how many steps to
# plot. 

initD = 1.5


def plotD(k, end=50):
    d = ts.TransducedSignal(sig.ConstantSignal(0.7),
                            wallFinderSystem(0.1, initD, k))
    d.plot(0, end, newWindow='Gain ' + str(k))


if __name__ == '__main__':
    plotD(1)
