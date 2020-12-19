from ..io.frame import frame as f
from ..error import error as e
class single_qubit:
    def __init__(self):
        df = f.get_frame()
    def gate(df=f.get_frame(),
             gate='h',
             target='0'):
        gate_data = {
            'target': target,
            'gate': gate,
        }
        gate_frame = f.get_frame(data=gate_data)
