from qbitkit import circuit as __circuit__
from tests.qktest import QKTestCase as __qkt__
import pandas as __pd__


class TestCircuitFrame(__qkt__):
    def test_empty_creation(self):
        self.assertEqual(__circuit__.CircuitFrame().df.to_json(),
                         __pd__.DataFrame().to_json())
