"""
Student shall write their names here
  1. André Plancha
  2. Yana Zlatanova
"""

import unittest
from Task2 import TextProcessor


class TestTextProcessor(unittest.TestCase):
  def setUp(self):
    # TODO consider other sample texts
    self.sample_text = "Hello! This is a sample text 1. Contact me at user@example.com. Python is awesome. The Python programming language is widely used. #Python #NLP Check out https://example.com."
    self.tp = TextProcessor(self.sample_text)

  """
  One example case test case is provided below but the implmentation of the function is missing to get you
  going with the TDD. Please note the test case will fail without implementation of the function in task2.py. 
  You will see an assertion error AssertionError: None != 'hello! this is a sample text 1. contact [130 chars]com.'. 
  The error will go away once you implement the function.
  """

  # TC for User story no 1 - This will fail!
  def test_convert_to_lowercase(self):
    self.assertEqual(self.tp.convert_to_lowercase(), self.sample_text.lower())

  def test_extract_emails(self):
    pass

  def test_count_hashtags(self):
    pass

  def test_extract_links(self):
    pass

  def test_avg_word_length(self):
    pass

  def test_top_words(self):
    pass

  def test_longest_word(self):
    pass

  def test_identify_sentences(self):
    pass

  def test_remove_special(self):
    pass

  def test_num_to_words(self):
    pass


if __name__ == "__main__":
  unittest.main(verbosity=2)
  """
  To generate an HTML report
  coverage run -a --branch Task1_Unittest_rover.py 
  coverage run -a --branch Task2_unittest.py 
  coverage report -m
  coverage html
  """
