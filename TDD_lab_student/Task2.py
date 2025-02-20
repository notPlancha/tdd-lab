import re
from collections import Counter


class TextProcessor:
  def __init__(self, text: str):
    # text isn't expecting any other type
    self.text = text

  # 1
  def convert_to_lowercase(self) -> str:
    """Convert all words to lowercase."""
    return self.text.lower()

  # 2
  def extract_emails(self) -> list[str]:
    """Find and extract all email addresses from the document."""
    # https://emailregex.com/
    return re.findall(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", self.text)

  # 3
  def count_hashtags(self) -> int:
    """Find and count all unique hashtags (words or phrases starting with #) used in the document."""
    pass

  # 4
  def extract_links(self) -> list[str]:
    """Identify and list all URLs mentioned in the text."""
    pass

  # 5
  def avg_word_length(self) -> float:
    """Calculate the average word length in the document."""
    pass

  # 6 TODO
  def top_words(self, n: int = 3) -> list[str]:
    """Find and list the top n most frequent words in the document."""
    pass

  # 7
  def longest_word(self) -> str:
    """Find and return the longest word in the document."""
    pass

  # 8
  def identify_sentences(self, word="Python") -> list[str]:
    """Find and list all sentences containing the specified word."""
    pass

  # 9 TODO
  def remove_special(self) -> str:
    """Remove all punctuation and special characters from the document."""
    pass

  # 10
  def num_to_words(self) -> str:
    """Convert numerical figures between 1-10 (inclusive) within the text into their respective written-out forms (for example, "This is sample text 1, 2, 3" shall become "This is sample text one, two, three")."""
    pass