from tests.qktest import QKTestCase as __tc__
from qbitkit.io import list as __lst__
from numpy.random import randint as __rng__
from unittest import main as __ut_main__


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
    def test_count_range(self):
        niterations = __rng__(0,256)
        test_list = __lst__.count_range(end=niterations)
        expected_list = __tc__.ranger(niterations)
        self.assertEqual(test_list,
                         expected_list)


if __name__ == '__main__':
    __ut_main__()
