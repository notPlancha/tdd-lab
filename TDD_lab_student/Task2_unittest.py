"""
Student shall write their names here
  1. André Plancha
  2. Yana Zlatanova
"""

import unittest
from Task2 import TextProcessor as TP

# TODO change to [subtests](https://docs.python.org/3/library/unittest.html#subtests)

class TestTextProcessor(unittest.TestCase):
  def setUp(self):
    self.sample_tp = TP("Hello! This is a sample text 1. Contact me at user@example.com. Python is awesome. The Python programming language is widely used. #Python #NLP Check out https://example.com.")
    self.empty_tp = TP("")
    self.repeting_words = TP("This is a test. Testing for my test. I am doing this test for testing my tests. This this this this is a test.")
    self.repeting_words_mixed_casing = TP("Cat, dog, CAT, one, two, three, Dog, dog, doG, DoG, cat, cat, five, one, one, two")
    self.repeting_words_mixed_casing_numbers_symbols = TP("Cat, !!, 12, dog, CAT, one, two, three, 136, Dog, dog, doG, DoG, cat, cat, five, one, one, two, !!, !!, !!, ....................................., 11 11 11 11 11")
    self.lot_of_links = TP("This is a link: https://example.com. This is another https://example.com; shouldThis.count ? ftp://foo.bar/baz? but http://google.com/?q=hello and what about 192.1.28.2:25? and http://1.1.1.1 ? // alone? and foo.com? and what about htt p://google.com and http://thisisnots.com:25 ? url matching is hard.")

  # 1
  def test_convert_to_lowercase(self):
    self.assertEqual(self.sample_tp.convert_to_lowercase(), "hello! this is a sample text 1. contact me at user@example.com. python is awesome. the python programming language is widely used. #python #nlp check out https://example.com.")
    self.assertEqual(self.empty_tp.convert_to_lowercase(), "")
    self.assertEqual(TP(r"\N").convert_to_lowercase(), r"\n") # TODO dont know if this if right
    self.assertEqual(TP("123456789").convert_to_lowercase(), "123456789")

  # 2
  def test_extract_emails(self):
    self.assertListEqual(self.sample_tp.extract_emails(), ["user@example.com"])
    self.assertListEqual(self.empty_tp.extract_emails(), [])
    self.assertListEqual(TP(
      "This@is@not@an@email address. but this@might.be; also_this@is.email this+also@might-be.com.But not the dot; email @ validity.ishard; finally this@is.n ot",
    ).extract_emails(), [
      "this@might.be", "also_this@is.email", "this+also@might-be.com"
    ])
    self.assertListEqual(TP(
      "Really@really@reaaally.hard. And impossible_to@test. ",
    ).extract_emails(), [
      "really@reaaally.hard"
    ])

  # 3
  def test_count_hashtags(self):
    # https://en.wikipedia.org/wiki/Hashtag#Format
    self.assertEqual(self.sample_tp.count_hashtags(), 2)
    self.assertEqual(self.empty_tp.count_hashtags(), 0)
    self.assertEqual(TP("#Python #Python #NotPython #Python #python").count_hashtags(), 2)
    self.assertEqual(TP("#").count_hashtags(), 0)
    self.assertEqual(TP("# notahashtag").count_hashtags(), 0)
    self.assertEqual(TP("#. Also not a hashtag").count_hashtags(), 0)
    self.assertEqual(TP("#; Also not a hashtag").count_hashtags(), 0)
    self.assertEqual(TP("#hash; is an hashtag").count_hashtags(), 1)
    self.assertEqual(TP("This #1 is an hashtag").count_hashtags(), 1)
    self.assertEqual(TP("#_thisAlsoCounts #And_This #__Andthis").count_hashtags(), 3)
  
  # 4
  def test_extract_links(self):
    # https://mathiasbynens.be/demo/url-regex
    temp = ["https://example.com", "https://example.com", "ftp://foo.bar/baz", "http://google.com/?q=hello", "http://1.1.1.1", "http://thisisnots.com:25"] 
  
    self.assertListEqual(self.sample_tp.extract_links(), ['https://example.com'])
    self.assertListEqual(self.empty_tp.extract_links(), [])
    self.assertListEqual(
      list1 = self.lot_of_links.extract_links(), list2 = temp
    )
  
  # 5
  def test_avg_word_length(self):
    # skipping sample cause it's too long
    # https://en.wikipedia.org/wiki/Word
    # _ isn't expected
    self.assertAlmostEqual(self.empty_tp.avg_word_length(), 0)
    self.assertAlmostEqual(TP(" ").avg_word_length(), 0)
    self.assertAlmostEqual(TP("This is a test").avg_word_length(), (4 + 2 + 1 + 4) / 4)
    self.assertAlmostEqual(TP("This is a test.").avg_word_length(), (4 + 2 + 1 + 5) / 4)
    self.assertAlmostEqual(TP("This is a test;different word").avg_word_length(), (4 + 2 + 1 + 14 + 4) / 5)
    self.assertAlmostEqual(TP(" This is a test.").avg_word_length(), (4 + 2 + 1 + 5) / 4)
    self.assertAlmostEqual(TP("This is a test. 123456").avg_word_length(), (4 + 2 + 1 + 5 + 6) / 5)
    self.assertAlmostEqual(TP("This-is-the-same-word").avg_word_length(), 21)
    self.assertAlmostEqual(TP("föregår ett r").avg_word_length(), (7 + 3 + 1) / 3)
    self.assertAlmostEqual(TP("Mom's spaghetti").avg_word_length(), (5+9)/2)

  # 6
  def test_top_words_null(self):
    self.assertEqual(TP(" ").top_words(), None) # null

  def test_top_words_empty(self):
    self.assertEqual(self.empty_tp.top_words(), None) # empty

  def test_top_words_basic(self):
    # Basic string with words
    self.assertEqual(self.repeting_words.top_words(), "this: 6, test: 4, a: 2")

  def test_top_words_mixed_casing(self):
    # String with words mixed casing
    self.assertEqual(self.repeting_words_mixed_casing.top_words(), "dog: 5, cat: 4, one: 3")

  def test_top_words_mixed_casing_numbers_symbols(self):
    # String with mixed casing, numbers and symbols
    self.assertEqual(self.repeting_words_mixed_casing_numbers_symbols.top_words(), "dog: 5, cat: 4, one: 3")

  
  # 7
  def test_longest_word(self):
    self.assertEqual(self.sample_tp.longest_word(), "https://example.com.")
    self.assertEqual(self.empty_tp.longest_word(), "")
    self.assertEqual(TP(" ").longest_word(), "")
    
  # 8
  def test_identify_sentences(self):
    # Hello! This is a sample text 1. Contact me at user@example.com. Python is awesome. The Python programming language is widely used. #Python #NLP Check out https://example.com.
    self.assertEqual(self.sample_tp.identify_sentences(), ["Python is awesome", "The Python programming language is widely used"])

  # 9
  def test_remove_special_null(self):
    self.assertEqual(TP(" ").remove_special(), None) # null

  def test_remove_special_empty(self):
    self.assertEqual(self.empty_tp.remove_special(), None) # empty

  def test_remove_special_basic(self): # basic
    self.assertEqual(self.sample_tp.remove_special(), "Hello This is a sample text 1 Contact me at userexamplecom Python is awesome The Python programming language is widely used Python NLP Check out httpsexamplecom")

  
  # 10
  def test_num_to_words(self):
    self.assertEqual(self.sample_tp.num_to_words(), "Hello! This is a sample text one. Contact me at user@example.com. Python is awesome. The Python programming language is widely used. #Python #NLP Check out https://example.com.")
    self.assertEqual(TP("This is sample text 1, 2, 3").num_to_words(), "This is sample text one, two, three")
    self.assertEqual(TP("1 2 3 4 5 6 7 8 9 10.").num_to_words(), "one two three four five six seven eight nine ten.")
    self.assertEqual(TP("10120").num_to_words(), "tenonetwo0")


if __name__ == "__main__":
  unittest.main(verbosity=2)
  """
  To generate an HTML report
  coverage run -a --branch Task1_Unittest_rover.py 
  coverage run -a --branch Task2_unittest.py 
  coverage report -m
  coverage html
  """
