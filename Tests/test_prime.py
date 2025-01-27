import unittest
import subprocess # implement outer programs or commands.
import os
import sys
from pathlib import Path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from GRASP import __main__ as target_main # retrieve the path of the target for the test

class TestFunc(unittest.TestCase):
    """ Implement basic test.

    Keyword arguments:
        unittest.TestCase: All classes extending unittest.TestCase are recognized as test case.

    """
    def test_func(self):
        """ Implement test.
        
        Keyword Arguments:
        """
        current_directory = Path(__file__).resolve().parent
        
        value1 = 1
        value2 = 2
        expected = 3
        actual = target_main.connectiontest(value1, value2) # this is used only to test relations between some files
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()