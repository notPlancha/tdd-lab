import re
from collections import Counter


class TextProcessor:
  def __init__(self, text):
    self.text = text

  """
  The TC for User story 1 will fail as there is no implementation added. Add the implementation of your user stories below.
  """

  def convert_to_lowercase(self) -> str:
    """Convert all words to lowercase."""
    pass

  def extract_emails(self) -> list:
    """Find and extract all email addresses from the document."""
    pass

  def count_hashtags(self) -> int:
    """Find and count all unique hashtags (words or phrases starting with #) used in the document."""
    pass

  def extract_links(self) -> list:
    """Identify and list all URLs mentoned in the text."""
    pass

  def avg_word_length(self) -> float:
    """Calculate the average word length in the document."""
    pass

  def top_words(self, n: int = 3) -> list[str]:
    """Find and list the top n most frequent words in the document."""
    pass

  def longest_word(self) -> str:
    """Find and return the longest word in the document."""
    pass

  def identify_sentences(self, word="Python") -> list[str]:
    """Find and list all sentences containing the specified word."""
    pass

  def remove_special(self) -> str:
    """Remove all punctuation and special characters from the document."""
    pass

  def num_to_words(self) -> str:
    """Convert all numerical figures (1-10) within the text into their respective written-out forms (for example, "This is sample text 1, 2, 3" shall become "This is sample text one, two, three")."""
    pass
