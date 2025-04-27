import unittest
import time
from katas.time_me import measure_execution_time


def sleep_function():
    time.sleep(0.1)

class TestTimeMe(unittest.TestCase):
    def test_measure_execution_time(self):

        duration = measure_execution_time(sleep_function)

        self.assertGreaterEqual(duration, 0.09)
        self.assertLess(duration, 0.2)



