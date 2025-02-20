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
  # 1
  def test_convert_to_lowercase(self):
    self.assertEqual(self.sample_tp.convert_to_lowercase(), "hello! this is a sample text 1. contact me at user@example.com. python is awesome. the python programming language is widely used. #python #nlp check out https://example.com.")
    self.assertEqual(self.empty_tp.convert_to_lowercase(), "")
    self.assertEqual(TP(r"\N").convert_to_lowercase(), r"\n") # TODO dont know if this if right
    self.assertEqual(TP("123456789"), "123456789")

  # 2
  def test_extract_emails(self):
    self.assertListEqual(self.sample_tp.extract_emails(), ["user@example.com"])
    self.assertListEqual(self.empty_tp.extract_emails(), [])
    self.assertListEqual(TP(
      "This@is@not@an@email address. but this@might.be; this+also@might-be.com.But not the dot; email @ validity.ishard; finally this@is.n ot",
    ).extract_emails(), [
      ["this@might.be", "this+also@might-be.com"]
    ])
    self.assertListEqual(TP(
      "Really@really@reaaally.hard. And impossible_to@test. ",
    ).extract_emails(), [
      ["really@reaaally.hard"]
    ])

  # 3
  def test_count_hashtags(self):
    self.assertEqual(self.sample_tp.count_hashtags(), 2)
    self.assertEqual(self.empty_tp.count_hashtags(), 0)
    self.assertEqual(TP("#Python #Python #NotPython #Python #python").count_hashtags(), 2) # 2 or 3?
    self.assertEqual(TP("#").count_hashtags(), 0)
    self.assertEqual(TP("# notahashtag").count_hashtags(), 0)
    self.assertEqual(TP("#. Also not a hashtag").count_hashtags(), 0)
    self.assertEqual(TP("#; Also not a hashtag").count_hashtags(), 0)
    self.assertEqual(TP("#hash; is an hashtag").count_hashtags(), 1)
    self.assertEqual(TP("This #1 is an hashtag").count_hashtags(), 1)
  
  # 4
  def test_extract_links(self):
    # https://mathiasbynens.be/demo/url-regex
    self.assertListEqual(self.sample_tp.extract_links(), ["https://example.com"])
    self.assertListEqual(self.empty_tp.extract_links(), [])
    self.assertListEqual(TP("This is a link: https://example.com. This is another https://example.com; shouldThis.count ? ftp://foo.bar/baz? and what about 192.1.28.2:25? and http://1.1.1.1 ? but what about http://0.0.0.0 ? // alone? and foo.com? and what about htt\np://google.com and http://thisisnots.com:25 ? url matching is hard").extract_links(), ["https://example.com", "https://example.com", "ftp://foo.bar/baz?", "http://1.1.1.1", "http://thisisnots.com:25"])
  
  # 5
  def test_avg_word_length(self):
    # skipping sample cause it's too long
    self.assertAlmostEqual(self.empty_tp.avg_word_length(), 0)
    self.assertAlmostEqual(TP(" ").avg_word_length(), 0)
    self.assertAlmostEqual(TP("This is a test").avg_word_length(), (4 + 2 + 1 + 4) / 4)
    self.assertAlmostEqual(TP("This is a test.").avg_word_length(), (4 + 2 + 1 + 4) / 4)
    self.assertAlmostEqual(TP("This is a test;different word").avg_word_length(), (4 + 2 + 1 + 4 + 9 + 4) / 6)
    self.assertAlmostEqual(TP(" This is a test.").avg_word_length(), (4 + 2 + 1 + 4) / 4)
    self.assertAlmostEqual(TP("This is a test. 123456").avg_word_length(), (4 + 2 + 1 + 4 + 6) / 5)
    self.assertAlmostEqual(TP("This-is-the-same-word").avg_word_length(), 21)
    self.assertAlmostEqual(TP("föregår ett r").avg_word_length(), (7 + 3 + 1) / 3)
    self.assertAlmostEqual(TP("S.P.E.C.T.R.E").avg_word_length(), 7)
    self.assertAlmostEqual(TP("Mom's spaghetti").avg_word_length(), (4+9)/2)
    self.assertAlmostEqual(TP('"cogito, ergo sum" - René Descartes').avg_word_length(), (6 + 4 + 3 + 4 + 9) / 5)

  # 6 TODO
  def test_top_words(self):
    pass
  
  # 7
  def test_longest_word(self):
    self.assertEqual(self.sample_tp.longest_word(), "https://example.com")
    self.assertEqual(self.empty_tp.longest_word(), None)
    self.assertEqual(TP(" "), None)
    
  # 8
  def test_identify_sentences(self):
    self.assertEqual(self.sample_tp.identify_sentences(), ["Python is awesome.", "The Python programming language is widely used.", "#Python #NLP Check out https://example.com."])

  # 9 TODO
  def test_remove_special(self):
    pass
  
  # 10
  def test_num_to_words(self):
    self.assertEqual(self.sample_tp.num_to_words(), "Hello! This is a sample text one. Contact me at user@example.com. Python is awesome. The Python programming language is widely used. #Python #NLP Check out https://example.com.")
    self.assertEqual(TP("This is sample text 1, 2, 3"), "This is sample text one, two, three")
    self.assertEqual(TP("1 2 3 4 5 6 7 8 9 10.").num_to_words(), "one two three four five six seven eight nine ten.")
    self.assertEqual(TP("10120"), "tenonetwo0")


if __name__ == "__main__":
  unittest.main(verbosity=2)
  """
  To generate an HTML report
  coverage run -a --branch Task1_Unittest_rover.py 
  coverage run -a --branch Task2_unittest.py 
  coverage report -m
  coverage html
  """
