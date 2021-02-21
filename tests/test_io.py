from tests.qktest import QKTestCase as __tc__
from qbitkit.io import list as __lst__
from numpy.random import randint as __rng__


class TestListTools(__tc__):
    def test_fill_range(self):
        fill_val = 'x'
        niterations = __rng__(0,256)
        test_list = __lst__.fill_range(fill=fill_val,
                                       iterations=niterations,
                                       append=None)
        expected_list = __tc__.repeater(value=fill_val,
                                        repeats=niterations)
        self.assertEquals(test_list,
                          expected_list)
