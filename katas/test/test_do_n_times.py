import unittest
from katas.do_n_times import do_n_times


class Counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1


class TestDonTimes(unittest.TestCase):
    def test_do_n_times(self):
        counter = Counter()
        do_n_times(counter.increment,4)
        self.assertEqual(counter.count ,4)

    def test_do_n_times_zero(self):
        counter = Counter()
        do_n_times(counter.increment,0)
        self.assertEqual(counter.count ,0)





