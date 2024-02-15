import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_simple_string(self):
        """test simple string"""
        self.assertTrue(TestLexer.test("\"My ID is 2152578\"","My ID is 2152578,<EOF>",101))

    def test_simple_string2(self):
        """test simple string"""
        self.assertTrue(TestLexer.test("\"isn\\'t\"","isn\\'t,<EOF>",102))
        
    def test_sinmple_string3(self):
        """test simple string"""
        self.assertTrue(TestLexer.test("\"\\\\n\"","\\\\n,<EOF>",103))
        
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
        self.assertTrue(TestLexer.test("12e+30","12e+30,<EOF>",110))
    
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
        self.assertTrue(TestLexer.test("\"njhf s \n","Unclosed String: njhf s ",114))
    
    def test_error2(self):
        """ test error """
        self.assertTrue(TestLexer.test("\"; \n\"","Unclosed String: ; ",115))
    
    def test_error3(self):
        """ test error """
        self.assertTrue(TestLexer.test("\"hhh","Unclosed String: hhh",116))
    
    def test_single_quote(self):
        """ test single quote in string"""
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
    
    def test_newline(self):
        """ test newline """
        self.assertTrue(TestLexer.test("abc\r","abc,\n,<EOF>",125))
        
    def test_newline2(self):
        """ test newline """
        self.assertTrue(TestLexer.test("abc\r","abc,\n,<EOF>",126))
        
    def test_newline3(self):
        self.assertTrue(TestLexer.test('''abc"'\r'""''', '''abc,Unclosed String: \'''', 127))
        
    def test_identifier(self):
        """ test identifier """
        self.assertTrue(TestLexer.test("abc","abc,<EOF>",128))
    
    def test_identifier2(self):
        """ test identifier """
        self.assertTrue(TestLexer.test("_aBc","_aBc,<EOF>",129))
        
    def test_identifier3(self):
        """ test identifier """
        self.assertTrue(TestLexer.test("aBc_11","aBc_11,<EOF>",130))
        
    def test_identifier4(self):
        """ test identifier """
        self.assertTrue(TestLexer.test("aBc_.11","aBc_,Error Token .",131))
    
    def test_identifier5(self):
        """ test identifier """
        self.assertTrue(TestLexer.test("aB19c_11","aB19c_11,<EOF>",132))
    
    def test_identifier6(self):
        """ test identifier """
        self.assertTrue(TestLexer.test("aB19c_11##comment","aB19c_11,<EOF>",133))
    
    def test134(self):
        """ test """
        self.assertTrue(TestLexer.test("aB19c_11##commentrue\n -1\n","aB19c_11,\n,-,1,\n,<EOF>",134))
    
    def test135(self):
        """ test """
        self.assertTrue(TestLexer.test("aB19c_11##commen\rtrue\n -1\n","aB19c_11,\n,true,\n,-,1,\n,<EOF>",135))
        
    def test136(self):
        """ test """
        self.assertTrue(TestLexer.test("aB19c_11~##commen\rtrue\n -1\n","aB19c_11,Error Token ~",136))
        
    def test137(self):
        """ test """
        self.assertTrue(TestLexer.test("aB19c_11##commen\ttrue\n -1\n","aB19c_11,\n,-,1,\n,<EOF>",137))
    
    def test138(self):
        """ test """
        self.assertTrue(TestLexer.test("aB19c_11\b","aB19c_11,<EOF>",138))
        
    def test139(self):
        """ test """
        self.assertTrue(TestLexer.test("aB19c_11\b\f","aB19c_11,<EOF>",139))
    
    def test140(self):
        """ test """
        self.assertTrue(TestLexer.test("\"aB19c_11\b\f\"","aB19c_11\b\f,<EOF>",140))
        
    def test141(self):
        """ test """
        self.assertTrue(TestLexer.test("12e3falseaB19c_11\b\f","12e3,falseaB19c_11,<EOF>",141))
    
    def test142(self):
        """ test """
        self.assertTrue(TestLexer.test("12e3false dynamic func aB19c_11\b\f","12e3,false,dynamic,func,aB19c_11,<EOF>",142))
        
    def test143(self):
        """ test """
        self.assertTrue(TestLexer.test("or=","or,=,<EOF>",143))
        
    def test144(self):
        """ test """
        self.assertTrue(TestLexer.test("or==","or,==,<EOF>",144))
        
    def test145(self):
        """ test """
        self.assertTrue(TestLexer.test("<==>","<=,=,>,<EOF>",145))
        
    def test146(self):
        """ test """
        self.assertTrue(TestLexer.test("<-->","<-,-,>,<EOF>",146))
    
    def test147(self):
        """ test """
        self.assertTrue(TestLexer.test("<=>=","<=,>=,<EOF>",147))
        
    def test148(self):
        """ test """
        self.assertTrue(TestLexer.test("===>","==,=,>,<EOF>",148))
        
    def test149(self):
        """ test """
        self.assertTrue(TestLexer.test("*=>===-=+==<=>","*,=,>=,==,-,=,+,==,<=,>,<EOF>",149))
        
    def test150(self):
        """ test """
        self.assertTrue(TestLexer.test("<<-->>","<,<-,-,>,>,<EOF>",150))
        
    def test151(self):
        """ test """
        self.assertTrue(TestLexer.test("=!==!==>=","=,!=,=,!=,=,>=,<EOF>",151))
        
    def test152(self):
        """ test """
        self.assertTrue(TestLexer.test("ifelif","ifelif,<EOF>",152))
        
    def test153(self):
        """ test """
        self.assertTrue(TestLexer.test("if elifelse","if,elifelse,<EOF>",153))
        
    def test154(self):
        """ test """
        self.assertTrue(TestLexer.test("if<-elif else","if,<-,elif,else,<EOF>",154))
        
    def test155(self):
        """ test """
        self.assertTrue(TestLexer.test("if(<-)+elif[...]ifelse","if,(,<-,),+,elif,[,...,],ifelse,<EOF>",155))
        
    def test156(self):
        """ test """
        self.assertTrue(TestLexer.test("(,]","(,,,],<EOF>",156))
        
    def test157(self):
        """ test """
        self.assertTrue(TestLexer.test("(..)","(,Error Token .",157))
        
    def test158(self):
        """ test """
        self.assertTrue(TestLexer.test("\"if(<-)+elif[..]ifelse\"","if(<-)+elif[..]ifelse,<EOF>",158))
        
    def test159(self):
        """ test """
        self.assertTrue(TestLexer.test("\"????\"","????,<EOF>",159))
        
    def test160(self):
        """ test """
        self.assertTrue(TestLexer.test("????","Error Token ?",160))
    
    def test161(self):
        """ test """
        self.assertTrue(TestLexer.test("","<EOF>",161))
        
    def test162(self):
        """ test """
        self.assertTrue(TestLexer.test("????\"\"","Error Token ?",162))
    
    def test163(self):
        """ test """
        self.assertTrue(TestLexer.test("\"????\"\"","????,Unclosed String: ",163))
        
    def test164(self):
        """ test """
        self.assertTrue(TestLexer.test("\"\"",",<EOF>",164))
        
    def test165(self):
        """ test """
        self.assertTrue(TestLexer.test("\"\"\"",",Unclosed String: ",165))
        
    def test166(self):
        """ test """
        self.assertTrue(TestLexer.test("\"\"\"\"",",,<EOF>",166))
        
    def test167(self):
        """ test """
        self.assertTrue(TestLexer.test("\"\"\"\'\"",",Unclosed String: \'\"",167))
        
    def test168(self):
        """ test """
        self.assertTrue(TestLexer.test("\"\"\"\'\"\"",",'\",<EOF>",168))
        
    def test169(self):
        """ test """
        self.assertTrue(TestLexer.test("\"\\ \"","Illegal Escape In String: \\ ",169))
        
    def test170(self):
        """ test """
        self.assertTrue(TestLexer.test("\"\\t\"","\\t,<EOF>",170))
        
    def test171(self):
        """ test """
        self.assertTrue(TestLexer.test("\"\\n\"","\\n,<EOF>",171))
        
    def test172(self):
        """ test """
        self.assertTrue(TestLexer.test("\"\\r\"","\\r,<EOF>",172))
        
    def test173(self):
        """ test """
        self.assertTrue(TestLexer.test("\"\\b\"","\\b,<EOF>",173))
        
    def test174(self):
        """ test """
        self.assertTrue(TestLexer.test("\"\\f\"","\\f,<EOF>",174))
    
    def test175(self):
        """ test """
        self.assertTrue(TestLexer.test("\"\\\'\"","\\\',<EOF>",175))
        
    def test176(self):
        """ test """
        self.assertTrue(TestLexer.test("\"\\\"\"","Illegal Escape In String: \\\"",176))
        
    def test177(self):
        """ test """
        self.assertTrue(TestLexer.test("var a <- 1.0e+1","var,a,<-,1.0e+1,<EOF>",177))
        
    def test178(self):
        """ test """
        self.assertTrue(TestLexer.test("[1+2,4*5.+4,foo()]","[,1,+,2,,,4,*,5.,+,4,,,foo,(,),],<EOF>",178))
        
    def test179(self):
        """ test """
        self.assertTrue(TestLexer.test("for i=0 until 1\n","for,i,=,0,until,1,\n,<EOF>",179))
        
    def test180(self):
        """ test """
        self.assertTrue(TestLexer.test("for \"for\"","for,for,<EOF>",180))
    
    def test181(self):
        """ test """
        self.assertTrue(TestLexer.test("by a by until","by,a,by,until,<EOF>",181))
        
    def test182(self):
        """ test """
        self.assertTrue(TestLexer.test("""\"Dear teacher, I see that in Window, '\"\\n'\" is automatically convert to '\"\\r\\n'\" . Which result in 2 newline after reading the solution file. Regarding the '\"\\r'\" is now not a whitespace, but also not a newline. We found inconsistent between many friends regarding the '\"\\r\\n'\" , '\"\\r'\" is skip or count as the second '\"\\n'\". This result in error in different column.\"""","""Dear teacher, I see that in Window, '\"\\n'\" is automatically convert to '\"\\r\\n'\" . Which result in 2 newline after reading the solution file. Regarding the '\"\\r'\" is now not a whitespace, but also not a newline. We found inconsistent between many friends regarding the '\"\\r\\n'\" , '\"\\r'\" is skip or count as the second '\"\\n'\". This result in error in different column.,<EOF>""",182))
        
    def test183(self):
        """ test """
        self.assertTrue(TestLexer.test("1 + 2 and or true","1,+,2,and,or,true,<EOF>",183))
        
    def test184(self):
        """ test """
        self.assertTrue(TestLexer.test("1 ...##2","1,...,<EOF>",184))
        
    def test185(self):
        """ test """
        self.assertTrue(TestLexer.test("something_intresting","something_intresting,<EOF>",185))
        
    def test186(self):
        """ test """
        self.assertTrue(TestLexer.test("class A:","class,A,Error Token :",186))
        
    def test187(self):
        """ test """
        self.assertTrue(TestLexer.test("func function","func,function,<EOF>",187))
        
    def test188(self):
        """ test """
        self.assertTrue(TestLexer.test("aBN <- true \"\"","aBN,<-,true,,<EOF>",188))
        
    def test189(self):
        """ test """
        self.assertTrue(TestLexer.test("1 + 2 ... and 3 /% 4","1,+,2,...,and,3,/,%,4,<EOF>",189))
        
    def test190(self):
        """ test """
        self.assertTrue(TestLexer.test("EOF\t\"EOF\"","EOF,EOF,<EOF>",190))
        
    def test191(self):
        """ test """
        self.assertTrue(TestLexer.test("\\t","Error Token \\",191))
        
    def test192(self):
        """ test """
        self.assertTrue(TestLexer.test("t\tt","t,t,<EOF>",192))
        
    def test193(self):
        """ test """
        self.assertTrue(TestLexer.test("try(catch)","try,(,catch,),<EOF>",193))
        
    def test194(self):
        """ test """
        self.assertTrue(TestLexer.test("try...2","try,...,2,<EOF>",194))
        
    def test195(self):
        """ test """
        self.assertTrue(TestLexer.test("\"nj\"...\"kk\"","nj,...,kk,<EOF>",195))
        
    def test196(self):
        """ test """
        self.assertTrue(TestLexer.test("\"'","Unclosed String: '",196))
        
    def test197(self):
        """ test """
        self.assertTrue(TestLexer.test("....","...,Error Token .",197))
        
    def test198(self):
        """ test """
        self.assertTrue(TestLexer.test("......","...,...,<EOF>",198))
        
    def test199(self):
        """ test """
        self.assertTrue(TestLexer.test(".....","...,Error Token .",199))
        
    def test100(self):
        """ test """
        self.assertTrue(TestLexer.test("0.!==...","0.,!=,=,...,<EOF>",100))