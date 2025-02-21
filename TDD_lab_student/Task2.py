import string
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
    return re.findall(r"[\w_.+-]+@[\w-]+\.\w{2,}", self.text)

  # 3
  def count_hashtags(self) -> int:
    """Find and count all unique hashtags (words or phrases starting with #) used in the document."""
    l = re.findall(r"\#[\w]+", self.text.lower())
    return len(set(l))

  # 4
  def extract_links(self) -> list[str]:
    """Identify and list all URLs mentioned in the text."""
    # https://mathiasbynens.be/demo/url-regex
    # https://urlregex.com/
    # https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml
    # https://github.com/mccutchen/twitter-url-regexen/blob/master/twitter_regex.py
    w = r"[a-zA-Z0-9]"
    return re.findall(fr"[{w}\+\.\-]{{2,}}://(www\.)?[\S]+[\w&=#/]", self.text)

  # helper
  def get_words(self, lower = False) -> list[str]:
    """Get all words in the document."""
    return re.findall(r"\p{L}+(?:[\-']?\p{L}+)+", self.text if not lower else self.text.lower())

  # 5
  def avg_word_length(self) -> float:
    """Calculate the average word length in the document."""
    words = self.get_words()
    # remove ' and - from the words
    words = [re.sub(r"[\-']+", "", word) for word in words]
    return sum(len(word) for word in words) / len(words)

  # 6 TODO
  def top_words(self, n: int = 3) -> list[str]:
    """Find and list the top n most frequent words in the document."""

    if not self.text or self.text.isspace():
        return None
    
    # Convert to lowercase and skip numbers/special chars
    cleaned_text = ""
    for char in self.text:        
        if char.isalpha():
            cleaned_text += char.lower()
        elif char.isspace():
            cleaned_text += char
    
    # Split into words and count frequencies
    words = cleaned_text.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            
    # Sort words by frequency (highest to lowest)
    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    
    # Format the top n words with their counts
    top_n = sorted_words[:n]
    if not top_n:
        return None
        
    result = ", ".join(f"{word}: {count}" for word, count in top_n)
    return result


  # 7
  def longest_word(self) -> str:
    """Find and return the longest word in the document."""
    words = self.get_words()
    return max(words, key=len)

  # 8
  def identify_sentences(self, word="Python") -> list[str]:
    """Find and list all sentences containing the specified word."""
    # Assuming the text is a valid sentence
    splitted = self.text.split(". ")
    ret = []
    for sentence in splitted:
      words = self.get_words(lower=True)
      if word.lower() in [w.lower() for w in words]:
        ret.append(sentence + ("." if sentence[-1] != "." else ""))
    return ret

  # 9 TODO
  def remove_special(self) -> str:
    """Remove all punctuation and special characters from the document."""
  
    if not self.text or self.text.isspace():
        return None
    
    cleaned_text = ""
    for char in self.text:
        if char not in string.punctuation:
            cleaned_text += char

    return cleaned_text

  # 10
  def num_to_words(self) -> str:
    """Convert numerical figures between 1-10 (inclusive) within the text into their respective written-out forms (for example, "This is sample text 1, 2, 3" shall become "This is sample text one, two, three")."""
    subs =  {
      "10": "ten",
      "9": "nine",
      "8": "eight",
      "7": "seven",
      "6": "six",
      "5": "five",
      "4": "four",
      "3": "three",
      "2": "two",
      "1": "one"
    }
    text = self.text
    for k, v in subs.items():
      text = text.replace(k, v)
    return text