# TEST OF CHARACTER FREQUENCY COUNTER EXCERCISE

import unittest
from excercise_2_character_frequency_counter import get_frequency

# AUTOMATED TEST, DO NOT MODIFY
class TestStringMethods(unittest.TestCase):
    def test_basic_test_cases(self):
        self.assertEqual(get_frequency("Géza kék az ég"), {'G': 1, 'é': 3, 'z': 2, 'a': 2, 'k': 2, 'g': 1}) #{'G': 1, 'é': 3, 'z': 2, 'a': 2, 'k': 2, 'g': 1}
        self.assertEqual(get_frequency("De a bikini felsőt már lazán dobja hátra A vitorláson amin elmegy Afrikába"), {'D': 1, 'e': 4, 'a': 6, 'b': 3, 'i': 6, 'k': 2, 'n': 4, 'f': 2, 'l': 4, 's': 2, 'ő': 1, 't': 3, 'm': 3, 'á': 5, 'r': 4, 'z': 1, 'd': 1, 'o': 3, 'j': 1, 'h': 1, 'A': 2, 'v': 1, 'g': 1, 'y': 1})

    def test_basic_test_cases_with_none(self):
        self.assertEqual(get_frequency([]), None)
        self.assertEqual(get_frequency(None), None)


if __name__ == '__main__':
    unittest.main()