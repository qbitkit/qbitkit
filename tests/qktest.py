from qbitkit.io import frame as __f__
from unittest import TestCase as __tc__
from os import linesep as __sep__
from numpy import pi as __pi__


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
        xgate = {'gate' : QKTestCase.repeater('x', scale_qubit),
                 'targetA' : QKTestCase.ranger(scale_qubit)}
        meas = {'gate' : QKTestCase.repeater('m',
                                             scale_qubit),
                'targetA' : QKTestCase.ranger(scale_qubit),
                'targetB' : QKTestCase.ranger(scale_qubit)}
        xgates_frame = __f__.Frame.get_frame(data=xgate)
        measurements_frame = __f__.Frame.get_frame(data=meas)
        if measurements == False:
            frame = xgates_frame
        elif measurements == True:
            frame = xgates_frame.append(measurements_frame)

    def example_frame_with_rotations(measurements=True,
                                         scale_qubit=8):
        theta_value = __pi__ / 2
        rygate = {'gate': QKTestCase.repeater('ry', scale_qubit),
                  'targetA': QKTestCase.ranger(scale_qubit),
                  'theta': QKTestCase.repeater(str(float(theta_value)),
                                               scale_qubit)}
        meas = {'gate': QKTestCase.repeater('m',
                                            scale_qubit),
                'targetA': QKTestCase.ranger(scale_qubit),
                'targetB': QKTestCase.ranger(scale_qubit)}
        rygates_frame = __f__.Frame.get_frame(data=rygate)
        measurements_frame = __f__.Frame.get_frame(data=meas)
        if measurements == False:
            frame = rygates_frame
        elif measurements == True:
            frame = rygates_frame.append(measurements_frame)
        return frame


    def compare(actual_value=None,
                expected_value=None):
        expected_equals_actual = False
        if actual_value == expected_value:
            print(f"--> Success! {__sep__}",
                  f"---> Expected value: '{expected_value}'",
                  f"= Actual Value: {actual_value}")
            expected_equals_actual = True
        else:
            print("--> Actual Output Did not Match Expected Output.",
                  f"{__sep__}---> Expected Output: '{expected_value}'",
                  f"{__sep__}---> Actual Value: '{actual_value}'")
            expected_equals_actual = False
        return expected_equals_actual
