"""
Student shall write their names here
    1. Yana Zlatanova
    2. André Plancha Fernandes
"""

import unittest
from Task1_Rover import rovar


class test_string(unittest.TestCase):
  """
  _LOWER_CONSTANTS = "bcdfhjklmnpqrstvwxz"
  _UPPER_CONSTANTS = "BCFGHJKLMNPQRSTVWXZ"
  Swedish vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'å', 'ä', 'ö']

  Write your TCs based on the lab instructions. One TC has been written below as an example

  """

  @classmethod
  def setUpClass(cls):
    """
    Set up shared resources = Class instance to access rover class methods
    """
    cls.rv = rovar()


  # Example test case to check lower case rover
  def test_enrove_small(self):
    self.assertEqual(self.rv.enrove("b"), "bob")

  # You can continue writing your test cases here based on the assignment description
 
  def test_null_cases_enrove(self):
    """Null Input Test """
    self.assertIsNone(self.rv.enrove(None))

  def test_null_cases_derove(self):
    """Null Input Test """
    self.assertIsNone(self.rv.derove(None))
  
  def test_empty_cases_enrove(self):
    """Empty Input Test """
    self.assertEqual(self.rv.enrove(""), "")

  def test_empty_cases_derove(self):
    """Empty Input Test """
    self.assertEqual(self.rv.derove(""), "")

# Test encoding
  def test_consonants_encode_decode(self):
    """Test encoding and decoding of consonants """
    test_cases = {
               # Lowercase
            "b": "bob",
            "c": "coc",
            "d": "dod",
            "f": "fof",
            "g": "gog",
            "h": "hoh",
            "j": "joj",
            "k": "kok",
            "l": "lol",
            "m": "mom",
            "n": "non",
            "p": "pop",
            "q": "qoq",
            "r": "ror",
            "s": "sos",
            "t": "tot",
            "v": "vov",
            "w": "wow",
            "x": "xox",
            "z": "zoz",
            # Uppercase
            "B": "BOB",
            "C": "COC",
            "D": "DOD",
            "F": "FOF",
            "G": "GOG",
            "H": "HOH",
            "J": "JOJ",
            "K": "KOK",
            "L": "LOL",
            "M": "MOM",
            "N": "NON",
            "P": "POP",
            "Q": "QOQ",
            "R": "ROR",
            "S": "SOS",
            "T": "TOT",
            "V": "VOV",
            "W": "WOW",
            "X": "XOX",
            "Z": "ZOZ",
            # Multiple consonants
            "br": "bobror",
            "str": "sostotror",
            # Mixed case consonants
            "B": "BOB",
            "Kr": "KOKror"
        }
        
    for input_str, expected in test_cases.items():
        encoded = self.rv.enrove(input_str)
        with self.subTest(input_str=input_str):
            self.assertEqual(encoded, expected, 
                f"Encoding failed for '{input_str}': got '{encoded}', expected '{expected}'")
                # Test decoded
            self.assertEqual(self.rv.derove(encoded), input_str,
                f"Decoding failed for '{input_str}': got '{encoded}', expected '{expected}'")

  def test_vowels_unchanged_encode_decode(self):
    """Test encoding and decoding of vowels """
    test_cases = {
            "a": "a",
            "e": "e",
            "i": "i",
            "o": "o",
            "u": "u",
            "y": "y",
            "A": "A",
            "E": "E",
            "I": "I",
            "O": "O",
            "U": "U",
            "Y": "Y",
        }
        
    for input_str, expected in test_cases.items():
            encoded = self.rv.enrove(input_str)
            self.assertEqual(encoded, expected, 
                f"Encoding failed for '{input_str}': got '{encoded}', expected '{expected}'")
            # Test decoded
            self.assertEqual(self.rv.derove(encoded), input_str,
                f"Decoding failed for '{input_str}': got '{encoded}', expected '{expected}'")

  def test_numbers_and_symbols_unchanged_encode_decode(self):
        """Test encoding and decoding of numbers and symbols """

        test_cases = {
            "123": "123",
            ".!” #€%&/(),.": ".!” #€%&/(),.",
            "...": "...",
            ".,:": ".,:"
        }
        
        for input_str, expected in test_cases.items():
            encoded = self.rv.enrove(input_str)
            self.assertEqual(encoded, expected, 
                f"Encoding failed for '{input_str}': got '{encoded}', expected '{expected}'")
            # Test decoded
            self.assertEqual(self.rv.derove(encoded), input_str,
                f"Decoding failed for '{input_str}': got '{encoded}', expected '{expected}'")

  def test_mixed_strings(self):
        test_cases = {
            # consonants and vowels
            "rovar": "rorovovaror",
            # Mixed case
            "Hello": "HOHelollolo",
            # With numbers
            "test123": "totesostot123",
            # With symbols
            "hi!": "hohi!",
            # Multiple words
            "my cat": "momy cocatot",
            # Complex mixed string
            "Hello, World 123!": "HOHelollolo, WOWororloldod 123!"
        }
        
        for input_str, expected in test_cases.items():
            encoded = self.rv.enrove(input_str)
            self.assertEqual(encoded, expected,
                f"Encoding failed for '{input_str}': got '{encoded}', expected '{expected}'")
            # Test decoded
            self.assertEqual(self.rv.derove(encoded), input_str,
                f"Decoding failed for '{input_str}': got '{encoded}', expected '{expected}'")



if __name__ == "__main__":
  print("***********START OF All TEST CASES RESULTS SHOWN BELOW**************")
  unittest.main(verbosity=2)
