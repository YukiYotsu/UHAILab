import unittest
import subprocess
import os
import sys
from pathlib import Path
from unittest.mock import patch

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from GRASP import core, ui

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
    def test_get_keyboard_distance(self):
        self.assertEqual(core.get_keyboard_distance('a', 'a'), 0)
        self.assertEqual(core.get_keyboard_distance('a', 's'), 0.2)
        self.assertEqual(core.get_keyboard_distance('a', 'z'), 1)

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
        self.assertEqual(core.get_closest_word("hellp", vocabulary), "help")
        self.assertEqual(core.get_closest_word("xyz", vocabulary), "❓UNIQUE")

    def test_spell_check_code(self):
        code = "int main() { retrun 0; }"
        dictionary = ["int", "main", "return"]
        expected_suggestions = {"retrun": "return"}
        self.assertEqual(core.spell_check_code(code, dictionary), expected_suggestions)

    def test_get_keyboard_distance_edge_cases(self):
        self.assertEqual(core.get_keyboard_distance('', 'a'), 1)  # 空文字列の場合
        self.assertEqual(core.get_keyboard_distance('a', ''), 1)  # 逆のケース
        self.assertEqual(core.get_keyboard_distance('#', '@'), 1.5)  # 記号

    def test_extract_identifiers_edge_cases(self):
        code = "int _main_var1() { return a_2 + var3; }"
        expected_identifiers = {"int", "_main_var1", "return", "a_2", "var3"}
        self.assertEqual(core.extract_identifiers(code), expected_identifiers)

    def test_spell_check_code_complex(self):
        code = "int mian() { rturn 0; }"
        dictionary = ["int", "main", "return"]
        expected_suggestions = {"mian": "main", "rturn": "return"}
        self.assertEqual(core.spell_check_code(code, dictionary), expected_suggestions)

if __name__ == "__main__":
    unittest.main()
