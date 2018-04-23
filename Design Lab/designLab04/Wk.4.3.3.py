import lib601.sm as sm


# Use sm.R, sm.Gain, sm.Cascade, sm.FeedbackAdd and sm.FeedbackSubtract
# to construct the state machines
# y(n)=y(n-1)+x(n)
def accumulator(init):
    none_there = sm.Gain(1)
    y_delay = sm.R(init)
    y = sm.FeedbackAdd(none_there, y_delay)
    return y


def accumulatorDelay(init):
    x_delay = sm.R(0)
    return sm.Cascade(x_delay, accumulator(init))


def accumulatorDelayScaled(s, init):
    x_scale = sm.Gain(s)
    return sm.Cascade(x_scale, accumulatorDelay(init))


if __name__ == '__main__':
    def test_accumulator():
        y = accumulator(0)
        print y.transduce(list(range(10)))


    def test_accumulatorDelay():
        y = accumulatorDelay(0)
        print y.transduce(list(range(10)))


    def test_accumulatorDelayScaled():
        y = accumulatorDelayScaled(2, 0)
        print y.transduce(list(range(10)))


    test_accumulator()
    test_accumulatorDelay()
    test_accumulatorDelayScaled()
