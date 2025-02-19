"""
Student shall write their names here
  1. André Plancha
  2. Yana Zlatanova
"""

import unittest
from Task2 import TextProcessor as TP


class TestTextProcessor(unittest.TestCase):
  def setUp(self):
    self.sample_tp = TP("Hello! This is a sample text 1. Contact me at user@example.com. Python is awesome. The Python programming language is widely used. #Python #NLP Check out https://example.com.")
    self.empty_tp = TP("")
    
  """
  One example case test case is provided below but the implmentation of the function is missing to get you
  going with the TDD. Please note the test case will fail without implementation of the function in task2.py. 
  You will see an assertion error AssertionError: None != 'hello! this is a sample text 1. contact [130 chars]com.'. 
  The error will go away once you implement the function.
  """

  def test_convert_to_lowercase(self):
    self.assertEqual(self.sample_tp.convert_to_lowercase(), "hello! this is a sample text 1. contact me at user@example.com. python is awesome. the python programming language is widely used. #python #nlp check out https://example.com.")
    self.assertEqual(self.empty_tp.convert_to_lowercase(), "")
    self.assertEqual(TP("123456789"), "123456789")

  def test_extract_emails(self):
    self.assertListEqual(self.sample_tp.extract_emails(), ["user@example.com"])
    self.assertListEqual(self.empty_tp.extract_emails(), [])
    self.assertListEqual(TP(
      "This@is@not@an@email address. but this@might.be; this+also@might-be.com.But not the dot; email @ validity.ishard",
    ).extract_emails(), [
      ["this@might.be", "this+also@might-be.com"]
    ])

  def test_count_hashtags(self):
    self.assertEqual(self.sample_tp.count_hashtags(), 2)
    self.assertEqual(self.empty_tp.count_hashtags(), 0)
    self.assertEqual(TP("#Python #Python #NotPython #Python #python").count_hashtags(), 2) # 2 or 3?
    self.assertEqual(TP("#"), 0)
    self.assertEqual(TP("# notahashtag"), 0)
    self.assertEqual(TP("#. Also not a hashtag"), 0)
    self.assertEqual(TP("#; Also not a hashtag"), 0)
    self.assertEqual(TP("#hash; is an hashtag"), 1)

    

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
