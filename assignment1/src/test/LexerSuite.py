import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_simple_string(self):
        """test simple string"""
        self.assertTrue(TestLexer.test("\"I have a cow - what ?\"","I have a cow - what ?,<EOF>",101))

    def test_complex_string(self):
        """test complex string"""
        self.assertTrue(TestLexer.test("\"isn\\'t\"","isn\\'t,<EOF>",102))
        
    def test_identifier(self):
        """ test identifier """
        self.assertTrue(TestLexer.test("abc","abc,<EOF>",103))
        
    def test_boollit(self):
        """ test boollit """
        self.assertTrue(TestLexer.test("true","true,<EOF>",104))
        
    def test_numlit1(self):
        """ test numlit 1 """
        self.assertTrue(TestLexer.test("12.","12.,<EOF>",105))
    
    def test_numlit2(self):
        """ test numlit 2 """
        self.assertTrue(TestLexer.test("12.33333","12.33333,<EOF>",106))
    
    def test_numlit3(self):
        """ test numlit 3 """
        self.assertTrue(TestLexer.test("12.33333e-3","12.33333e-3,<EOF>",107))
    
    def test_numlit4(self):
        """ test numlit 4 """
        self.assertTrue(TestLexer.test("12.33333E3","12.33333E3,<EOF>",108))
    
    def test_numlit5(self):
        """ test numlit 5 """
        self.assertTrue(TestLexer.test("12.33333E+3","12.33333E+3,<EOF>",109))
    
    def test_numlit6(self):
        """ test numlit 6 """
        self.assertTrue(TestLexer.test("12.33333Ee+3","12.33333,Ee,+,3,<EOF>",110))
    
    def test_comment(self):
        """ test comment """
        self.assertTrue(TestLexer.test("## cnja scjsjdncnaks jkcsakjdnc\n 123","\n,123,<EOF>",111))
    
    def test_all1(self):
        """ test all 1 """
        self.assertTrue(TestLexer.test("## cnja scjsjdncnaks jkcsakjdnc\n 123 == I_am_penguin\n\ttrue <= false","\n,123,==,I_am_penguin,\n,true,<=,false,<EOF>",112))
        
    def test_error(self):
        """ test error """
        self.assertTrue(TestLexer.test("abcvvv;","abcvvv,Error Token ;",113))
    
    def test_error1(self):
        """ test error """
        self.assertTrue(TestLexer.test("\"njhf s \n","Unclosed String: njhf s \n",114))
    
    def test_error2(self):
        """ test error """
        self.assertTrue(TestLexer.test("\"; \n\"","Unclosed String: ; \n",115))
    
    def test_error3(self):
        """ test error """
        self.assertTrue(TestLexer.test("\"hhh","Unclosed String: hhh",116))
    
    def test_error4(self):
        """ test error """
        self.assertTrue(TestLexer.test("\"\'k\"","\'k,<EOF>",117))
    
    def test_error5(self):
        """ test error """
        self.assertTrue(TestLexer.test("\"hbh\\khuh\"","Illegal Escape In String: hbh\\k",118))
    
    def test_error6(self):
        """ test error """
        self.assertTrue(TestLexer.test("\"\'\"","Unclosed String: \'\"",119))
    
    def test_error7(self):
        """ test error """
        self.assertTrue(TestLexer.test("\"\'\"\"","\'\",<EOF>",120))
    
    def test_string(self):
        """ test string """
        self.assertTrue(TestLexer.test("\"\' \"","\' ,<EOF>",121))
    
    def test_string2(self):
        """ test string """
        self.assertTrue(TestLexer.test("\"Hi my name is\\\'Huy\' \"","Hi my name is\\\'Huy\' ,<EOF>",122))
    
    def test_string3(self):
        """ test string """
        self.assertTrue(TestLexer.test("\"\' '\"","Unclosed String: \' \'\"",123))
        
    def test_comment2(self):
        """ test comment """
        self.assertTrue(TestLexer.test("## cnja scjsjdncnaks jkcsakjdnc","<EOF>",124))