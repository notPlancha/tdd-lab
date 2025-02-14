'''
    Student shall write their names here
        1. Student 1
        2. Student 2
'''

import unittest
from Task2 import TextProcessor

class TestTextProcessor(unittest.TestCase):
    tp = None
    def setUp(self):
        """
        You can start with the sample text below but please feel free to add more text to cover all scenarios. 
        """
        self.sample_text = "Hello! This is a sample text 1. Contact me at user@example.com. Python is awesome. The Python programming language is widely used. #Python #NLP Check out https://example.com."
        global tp 
        tp = TextProcessor(self.sample_text)



    """
        One example case test case is provided below but the implmentation of the function is missing to get you
        going with the TDD. Please note the test case will fail without implementation of the function in task2.py. 
        You will see an assertion error AssertionError: None != 'hello! this is a sample text 1. contact [130 chars]com.'. 
        The error will go away once you implement the function.
    """
    #TC for User story no 1 - This will fail!
    def test_convert_to_lowercase(self):
        self.assertEqual(tp.convert_to_lowercase(), self.sample_text.lower())


if __name__ == '__main__':
    unittest.main(verbosity=2)
    
    """
    To generate an HTML report
    coverage run -a --branch Task1_Unittest_rover.py 
    coverage run -a --branch Task2_unittest.py 
    coverage report -m
    coverage html
    """
