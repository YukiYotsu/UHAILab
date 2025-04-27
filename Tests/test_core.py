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
from GRASP import core

# this test Python file has not completed
libc = ctypes.CDLL("libunrestricted.dylib")
libc.unrestricted_damerau_levenshtein.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
libc.unrestricted_damerau_levenshtein.restype = ctypes.c_int

class TestDamerauLevenshtein(unittest.TestCase):
    """ Implement test Damerau-Levenshtein distance.

    Keyword arguments:
        unittest.TestCase: All classes extending unittest.TestCase are recognized as test case.

    """
    @classmethod
    def setUpClass(cls):
        source_lib = os.path.join(os.path.dirname(__file__), "..", "libunrestricted.dylib")
        target_lib = os.path.join(os.path.dirname(__file__), "..", "GRASP", "libunrestricted.dylib")

    def test_same_strings(self):
        self.assertEqual(libc.unrestricted_damerau_levenshtein(b"hello", b"hello"), 0)

    def test_single_insertion(self):
        self.assertEqual(libc.unrestricted_damerau_levenshtein(b"helo", b"hello"), 1)

    def test_single_deletion(self):
        self.assertEqual(libc.unrestricted_damerau_levenshtein(b"hello", b"helo"), 1)

    def test_single_substitution(self):
        self.assertEqual(libc.unrestricted_damerau_levenshtein(b"hello", b"jello"), 1)

    def test_single_transposition(self):
        self.assertEqual(libc.unrestricted_damerau_levenshtein(b"hlelo", b"hello"), 1)

    def test_multiple_operations(self):
        self.assertEqual(libc.unrestricted_damerau_levenshtein(b"kitten", b"sitting"), 3)

    def test_long_strings(self):
        self.assertEqual(libc.unrestricted_damerau_levenshtein(b"abcdefghij", b"acbdefjhig"), 3)

    def test_empty_strings(self):
        self.assertEqual(libc.unrestricted_damerau_levenshtein(b"", b""), 0)

    def test_one_empty_string(self):
        self.assertEqual(libc.unrestricted_damerau_levenshtein(b"hello", b""), 5)

    def test_case_sensitivity(self):
        self.assertEqual(libc.unrestricted_damerau_levenshtein(b"Hello", b"hello"), 1)

    def test_special_characters(self):
        self.assertEqual(libc.unrestricted_damerau_levenshtein(b"h@llo!", b"hello"), 2)

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
        self.assertEqual(core.lemmatize("dictionaries"),"dictionary")
        self.assertEqual(core.lemmatize("wolves"),"wolf")
        self.assertEqual(core.lemmatize("heroes"),"hero")

    def test_remove_ly_suffix(self):
        self.assertEqual(core.remove_ly_suffix("table"),"table")
        self.assertEqual(core.remove_ly_suffix("quickly"), "quick")
        self.assertEqual(core.remove_ly_suffix("happily"), "happi")

    # *NOT BEING USED in the latest version*
    # def test_get_keyboard_distance(self):
    #     self.assertEqual(core.get_keyboard_distance('a', 'a'), 0)
    #     self.assertEqual(core.get_keyboard_distance('a', 's'), 0.2)
    #     self.assertEqual(core.get_keyboard_distance('a', 'g'), 0.45)

    def test_trie_operations(self):
        trie = core.Trie()
        trie.insert("hello")
        self.assertTrue(trie.search("hello"))
        self.assertFalse(trie.search("hell"))
        self.assertFalse(trie.search("helloo"))
        trie.insert("hell")
        self.assertTrue(trie.search("hell"))
        self.assertFalse(trie.search("he"))

    def test_get_closest_word(self):
        vocabulary = ["hello", "world", "help", "held"]
        dummy_dictionary={}
        self.assertEqual(core.get_closest_word("hellp", dummy_dictionary), None)
        self.assertEqual(core.get_closest_word("hellp", vocabulary), "hello")
        self.assertEqual(core.get_closest_word("xyz", vocabulary), "❓UNIQUE")

    def test_merge_dictionaries(self):
        base_dict = ["hello", "world"]
        user_dict = ["custom", "define"]
        merged = core.merge_dictionaries(base_dict, user_dict)
        self.assertIn("hello", merged)
        self.assertIn("custom", merged)

    def test_split_code(self):
        code = "they/he/she are penguins(emperor)"
        tokens = core.split_code(code)
        expected_tokens = ["they","he","she","are","penguins","emperor"]
        self.assertEqual(tokens, expected_tokens)

    def test_spell_check_code(self):
        text = "It was a beautifull day in the nieghborhood."
        dictionary = ["it", "was", "a", "beautiful", "day", "in", "the", "neighborhood"]
        expected_suggestions = {"beautifull": "beautiful", "nieghborhood": "neighborhood"}
        self.assertEqual(core.spell_check_code(text, dictionary), expected_suggestions)

    def test_spell_check_code_empty_string(self):
        dictionary = ["hello", "world"]
        expected_suggestions = {}
        self.assertEqual(core.spell_check_code("", dictionary), expected_suggestions)

    def test_load_user_defined_corrections(self):
        corrections = core.load_user_defined_corrections(self.test_file)
        expected_corrections = ["misspell", "the"]
        self.assertEqual(corrections, expected_corrections)

    def test_merge_dictionaries_with_empty_user_dict(self):
        base_dict = ["hello", "world"]
        user_dict = []
        merged = core.merge_dictionaries(base_dict, user_dict)
        self.assertEqual(merged, base_dict)

    def test_get_closest_word_with_print(self):
        vocabulary = ["hello", "world", "help", "held"]
        with patch('builtins.print') as mocked_print:
            self.assertEqual(core.get_closest_word("hellp", vocabulary), "hello")
            mocked_print.assert_any_call("Checking word: hellp")
            mocked_print.assert_any_call("Final closest word: hello")

    def test_load_user_defined_corrections_file_not_found(self):
        non_existent_file = "non_existent.csv"
        with patch("builtins.print") as mocked_print:
            corrections = core.load_user_defined_corrections(non_existent_file)
            self.assertEqual(corrections, [])
            mocked_print.assert_called_with(f"‼️ User-defined corrections file not found: {non_existent_file}")

    def test_save_user_defined_correction(self):
            core.save_user_defined_correction("wrng", "wrong")
            corrections = core.load_user_defined_corrections(USER_DEFINED_CORRECTIONS_FILE_Path)
            self.assertIn("wrong", corrections)

    # def test_get_keyboard_distance_edge_cases(self):
    #     self.assertEqual(core.get_keyboard_distance('', 'a'), 0.45)  # case: empty character
    #     self.assertEqual(core.get_keyboard_distance('a', ''), 0.45)  # reverse
    #     self.assertEqual(core.get_keyboard_distance('#', '@'), 0.45)  # symbols
        
if __name__ == "__main__":
    unittest.main()
