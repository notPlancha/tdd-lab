"""
Student shall write their names here
    1. Student 1
    2. Student 2
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


if __name__ == "__main__":
  print("***********START OF All TEST CASES RESULTS SHOWN BELOW**************")
  unittest.main(verbosity=2)
