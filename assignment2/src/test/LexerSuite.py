import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_simple_string(self):
        """test simple string"""
        self.assertTrue(TestLexer.test("'Yanxi Palace - 2018'","Error Token '",101))

    def test_complex_string(self):
        """test complex string"""
        self.assertTrue(TestLexer.test("'isn''t'","Error Token '",102))
    