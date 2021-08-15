from qbitkit.io import frame as __f__
from unittest import TestCase as __tc__
from os import linesep as __sep__
from numpy import pi as __pi__


class QKTestCase(__tc__):

    def ranger(span=8):
        return [number for number in range(span)]

    def repeater(value='x', repeats=8):
        return [value for iteration in range(repeats)]

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

        return frame
    def example_frame_with_rotations(measurements=True,
                                     scale_qubit=8,
                                     theta=float(__pi__/2)):
        rygate = {'gate' : QKTestCase.repeater('ry', scale_qubit),
                  'targetA': QKTestCase.ranger(scale_qubit),
                  'theta': theta}
        meas = {'gate': QKTestCase.repeater('m', scale_qubit),
                'targetA': QKTestCase.ranger(scale_qubit)}
        ry_frame = __f__.get_frame(data=rygate)
        m_frame = __f__.get_frame(data=meas)
        if measurements == False:
            compiled_frame = ry_frame
        elif measurements == True:
            compiled_frame = ry_frame.append(m_frame)
        else:
            compiled_frame = rygate
        return compiled_frame
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
