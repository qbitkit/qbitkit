from qbitkit.io.frame import frame as f
from qbitkit.error import error as e
class single_qubit:
    def gate(append=False,
             append_df=f.get_frame(),
             gate='h',
             target0='0'):

        gate_data = {
            'target0': target0,
            'gate': gate,
        }
        gate_frame = f.get_frame(data=gate_data)
        if append == True:
            appended_df = append_df.append(gate_frame)
            return appended_df
        elif append == False:
            return gate_frame
        else:
            return gate_frame

class double_qubit:
    def gate(append=False,
             append_df=f.get_frame(),
             gate='cnot',
             target0='0',
             target1='1'):

        gate_data = {
            'target0': target0,
            'target1': target1,
            'gate': gate,
        }
        gate_frame = f.get_frame(data=gate_data)
        if append == True:
            appended_df = append_df.append(gate_frame)
            return appended_df
        elif append == False:
            return gate_frame
        else:
            return gate_frame
class triple_qubit:
    def __init__(self):
        df = f.get_frame()

    def gate(append=False,
             append_df=f.get_frame(),
             gate='ccnot',
             target0='0',target1='1',target2=2):

        gate_data = {
            'target0': target0,
            'target1': target1,
            'target2': target2,
            'gate': gate,
        }
        gate_frame = f.get_frame(data=gate_data)
        if append == True:
            appended_df = append_df.append(gate_frame)
            return appended_df
        elif append == False:
            return gate_frame
        else:
            return gate_frame