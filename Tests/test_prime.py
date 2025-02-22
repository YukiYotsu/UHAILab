# this test Python file has not completed
import unittest
import os
import sys
import csv
from pathlib import Path
import ctypes
from unittest.mock import patch

sys.path.append(str(Path(__file__).resolve().parent.parent))
sys.path.append(str(Path(__file__).resolve().parent.parent / "GRASP"))

from config import USER_DEFINED_CORRECTIONS_FILE_Path
from GRASP import core, ui

# this test Python file has not completed
lib = ctypes.CDLL("libunrestricted.dylib")
lib.unrestricted_damerau_levenshtein_distance.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
lib.unrestricted_damerau_levenshtein_distance.restype = ctypes.c_int

class TestDamerauLevenshtein(unittest.TestCase):
    """ Implement test Damerau-Levenshtein distance.

    Keyword arguments:
        unittest.TestCase: All classes extending unittest.TestCase are recognized as test case.

    """
    def test_same_strings(self):
        self.assertEqual(core.unrestricted_damerau_levenshtein_distance("hello", "hello"), 0)

    def test_single_insertion(self):
        self.assertEqual(core.unrestricted_damerau_levenshtein_distance("helo", "hello"), 1)

    def test_single_deletion(self):
        self.assertEqual(core.unrestricted_damerau_levenshtein_distance("hello", "helo"), 1)

    def test_single_substitution(self):
        self.assertEqual(core.unrestricted_damerau_levenshtein_distance("hello", "jello"), 1)

    def test_single_transposition(self):
        self.assertEqual(core.unrestricted_damerau_levenshtein_distance("hlelo", "hello"), 1)

    def test_multiple_operations(self):
        self.assertEqual(core.unrestricted_damerau_levenshtein_distance("kitten", "sitting"), 3)

    def test_long_strings(self):
        self.assertEqual(core.unrestricted_damerau_levenshtein_distance("abcdefghij", "acbdefjhig"), 3)

    def test_empty_strings(self):
        self.assertEqual(core.unrestricted_damerau_levenshtein_distance("", ""), 0)

    def test_one_empty_string(self):
        self.assertEqual(core.unrestricted_damerau_levenshtein_distance("hello", ""), 5)

    def test_case_sensitivity(self):
        self.assertEqual(core.unrestricted_damerau_levenshtein_distance("Hello", "hello"), 1)

    def test_special_characters(self):
        self.assertEqual(core.unrestricted_damerau_levenshtein_distance("h@llo!", "hello"), 2)

    def test_japanese_characters(self):
        self.assertEqual(core.unrestricted_damerau_levenshtein_distance("こんにちは", "こんいちは"), 1)

class TestUI(unittest.TestCase):
    """ Implement the test on UI.

    These functions are made to test UI.
    Keyword Arguments:
        unittest.TestCase: All classes extending unittest.TestCase are recognized as test case.
    """
    def test_user_input(self):
        with patch('builtins.input', return_value='hello'):
            self.assertEqual(ui.get_user_input(), 'hello')

    def test_display_output(self):
        with patch('builtins.print') as mocked_print:
            ui.display_output("Test Output")
            mocked_print.assert_called_with("Test Output")

class TestCoreFunctions(unittest.TestCase):
    """ Implement test on core functions beside Damarau-Levenshtein distance.

    Keyword Arguments:
        unittest.TestCase: All classes extending unittest.TestCase are recognized as test case.
    """
    sys.path.append(str(Path(__file__).resolve().parent.parent))
    sys.path.append(str(Path(__file__).resolve().parent.parent / "Tests"))
    test_file = "test_user_corrections.csv"
    sample_vocabulary = ["hello", "world", "help", "held", "spell"]
    original_user_defined_file = USER_DEFINED_CORRECTIONS_FILE_Path

    def testcsv_Setup(self):
        with open(self.test_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["mispell", "misspell"])
            writer.writerow(["teh", "the"])

    def testcsv_Clean(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        
        temp_lines = []
        with open(self.original_user_defined_file, "r", encoding="utf-8") as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                if row != ["wrng", "wrong"]:
                    temp_lines.append(row)

        with open(self.original_user_defined_file, "w", newline="", encoding="utf-8") as f:
            csv_writer = csv.writer(f)
            csv_writer.writerows(temp_lines)

    def test_lemmatize(self):
        self.assertEqual(core.lemmatize("children"), "child")
        self.assertEqual(core.lemmatize("eating"), "eat")
        self.assertEqual(core.lemmatize("running"), "run")
        self.assertEqual(core.lemmatize("better"), "good")
        self.assertEqual(core.lemmatize("plays"), "play")

    def test_get_keyboard_distance(self):
        self.assertEqual(core.get_keyboard_distance('a', 'a'), 0)
        self.assertEqual(core.get_keyboard_distance('a', 's'), 0.2)
        self.assertEqual(core.get_keyboard_distance('a', 'g'), 1)

    def test_trie_operations(self):
        trie = core.Trie()

        trie.insert("hello")
        self.assertTrue(trie.search("hello"))
        self.assertFalse(trie.search("hell"))
        self.assertFalse(trie.search("helloo"))

        trie.insert("hell")
        self.assertTrue(trie.search("hell"))
        self.assertFalse(trie.search("he"))

    def test_extract_identifiers(self):
        code = "int main() { return 0; }"
        expected_identifiers = {"int", "main", "return"}
        self.assertEqual(core.extract_identifiers(code), expected_identifiers)

    def test_get_closest_word(self):
        vocabulary = ["hello", "world", "help", "held"]
        self.assertEqual(core.get_closest_word("hellp", vocabulary), "hello")
        self.assertEqual(core.get_closest_word("xyz", vocabulary), "❓UNIQUE")

    def test_spell_check_code(self):
        code = "int main() { retrun 0; }"
        dictionary = ["int", "main", "return"]
        expected_suggestions = {"retrun": "return"}
        self.assertEqual(core.spell_check_code(code, dictionary), expected_suggestions)

    def test_load_user_defined_corrections(self):
            corrections = core.load_user_defined_corrections(self.test_file)
            expected_corrections = ["misspell", "the"]
            self.assertEqual(corrections, expected_corrections)

    def test_save_user_defined_correction(self):
            core.save_user_defined_correction("wrng", "wrong")
            corrections = core.load_user_defined_corrections(USER_DEFINED_CORRECTIONS_FILE_Path)
            self.assertIn("wrong", corrections)

    def test_get_keyboard_distance_edge_cases(self):
        self.assertEqual(core.get_keyboard_distance('', 'a'), 1)  # case: empty character
        self.assertEqual(core.get_keyboard_distance('a', ''), 1)  # reverse
        self.assertEqual(core.get_keyboard_distance('#', '@'), 1)  # symbols

    def test_extract_identifiers_edge_cases(self):
        code = "int _main_var1() { return a_2 + var3; }"
        expected_identifiers = {"int", "_main_var1", "return", "a_2", "var3"}
        self.assertEqual(core.extract_identifiers(code), expected_identifiers)
        
if __name__ == "__main__":
    unittest.main()
