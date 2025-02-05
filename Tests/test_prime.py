import unittest
import subprocess # implement outer programs or commands.
import os
import sys
from pathlib import Path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from GRASP import core # retrieve the path of the target for the test

class TestDamerauLevenshtein(unittest.TestCase):
    """ Implement basic test.

    Keyword arguments:
        unittest.TestCase: All classes extending unittest.TestCase are recognized as test case.

    """
    def test_same_strings(self):
        """ Implement test.
        
        Keyword Arguments:
        """
        self.assertEqual(core.unrestricted_damerau_levenshtein_distance("hello", "hello"),0)

    def test_single_insertion(self):
        """ Implement test.
        
        Keyword Arguments:
        """
        self.assertEqual(core.unrestricted_damerau_levenshtein_distance("helo", "hello"), 1)

    def test_single_deletion(self):
        """ Implement test.
        
        Keyword Arguments:
        """
        self.assertEqual(core.unrestricted_damerau_levenshtein_distance("hello", "helo"), 1)

    def test_single_substitution(self):
        """ Implement test.
        
        Keyword Arguments:
        """
        self.assertEqual(core.unrestricted_damerau_levenshtein_distance("hello", "jello"), 1)

    def test_single_transposition(self):
        """ Implement test.
        
        Keyword Arguments:
        """
        self.assertEqual(core.unrestricted_damerau_levenshtein_distance("hlelo", "hello"), 1)

    def test_multiple_operations(self):
        """ Implement test.
        
        Keyword Arguments:
        """
        self.assertEqual(core.unrestricted_damerau_levenshtein_distance("kitten", "sitting"), 3)

    def test_long_strings(self):
        """ Implement test.
        
        Keyword Arguments:
        """
        self.assertEqual(core.unrestricted_damerau_levenshtein_distance("abcdefghij", "acbdefjhig"), 3)

if __name__ == "__main__":
    unittest.main()