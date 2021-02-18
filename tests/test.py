from qbitkit.io import frame as __f__
from unittest import TestCase as __tc__


class QKTestCase(__tc__):

    def ranger(span=8):
        range_span = range(span)
        range_list = []
        for x in range_span:
            range_list.append(x)
        return range_list

    def repeater(value='x', repeats=8):
        range_span = range(repeats)
        range_list = []
        for x in range_span:
            range_list.append(value)
        return range_list

    def example_frame(measurements=True,
                      scale_qubit=8):
        xgate = {'gate' : QKTestCase.ranger(scale_qubit),
                 'targetA' : QKTestCase.repeater('x',
                                                 scale_qubit)}
        meas = {'gate' : QKTestCase.repeater('x',
                                             scale_qubit),
                'targetA' : QKTestCase.ranger(scale_qubit),
                'targetB' : QKTestCase.ranger(scale_qubit)}
        xgates_frame = __f__.Frame.get_frame(data=xgate)
        measurements_frame = __f__.Frame.get_frame(data=meas)
        if measurements == False:
            frame = xgates_frame
        elif measurements == True:
            frame = xgates_frame.append(measurements_frame)

        return frame
