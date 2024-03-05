import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """string a
        """
        expect = str(Program([VarDecl(Id("a"), StringType())]))
        self.assertTrue(TestAST.test(input, expect, 300))
        
    def test_simple_program_2(self):
        input = """string a <- "Hello"
        
        """
        expect = str(Program([VarDecl(Id("a"), StringType(), None, StringLiteral("Hello"))]))
        self.assertTrue(TestAST.test(input, expect, 301))
        
    def test_simple_program_3(self):
        input = """string a <- f(1,2,3)
        """
        expect = str(Program([VarDecl(Id("a"), StringType(), None, CallExpr(Id("f"), [NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)]))]))
        self.assertTrue(TestAST.test(input, expect, 302))
        
    def test_simple_program_4(self):
        input = """string a <- f(1+2,"k",3) + 1
        """
        expect = str(Program([VarDecl(Id("a"), StringType(), None, BinaryOp("+", CallExpr(Id("f"), [BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0)), StringLiteral("k"), NumberLiteral(3.0)]), NumberLiteral(1.0)))]))
        self.assertTrue(TestAST.test(input, expect, 303))
        
    def test_simple_program_5(self):
        input = """number a[3] <- [1,2,3]
        """
        expect = str(Program([VarDecl(Id("a"), ArrayType([3.0], NumberType()), None, ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)]))]))
        self.assertTrue(TestAST.test(input, expect, 304))
        
    def test_simple_program_6(self):
        input = """number a[3] <- [1,2,3]
        number b <- a
        """
        expect = str(Program([VarDecl(Id("a"), ArrayType([3.0], NumberType()), None, ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)])), VarDecl(Id("b"), NumberType(), None, Id("a"))]))
        self.assertTrue(TestAST.test(input, expect, 305))
        
    def test_simple_program_7(self):
        input = """bool a[3,2] <- [true,false,true and false,[true or true, not true]]
        number b
        """
        expect = str(Program([VarDecl(Id("a"), ArrayType([3.0, 2.0], BoolType()), None, ArrayLiteral([BooleanLiteral(True), BooleanLiteral(False), BinaryOp("and", BooleanLiteral(True), BooleanLiteral(False)), ArrayLiteral([BinaryOp("or", BooleanLiteral(True), BooleanLiteral(True)), UnaryOp("not", BooleanLiteral(True))])])), VarDecl(Id("b"), NumberType())]))
        self.assertTrue(TestAST.test(input, expect, 306))
        
    def test_simple_program_8(self):
        input = """number a[3] <- [1,2,3]
        number b <- f[1]
        """
        expect = str(Program([VarDecl(Id("a"), ArrayType([3.0], NumberType()), None, ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)])), VarDecl(Id("b"), NumberType(), None, ArrayCell(Id("f"), [NumberLiteral(1.0)]))]))
        self.assertTrue(TestAST.test(input, expect, 307))
        
    def test_simple_program_9(self):
        input = """number a[3] <- [1,2,3]
        number b <- f("h")[1]
        """
        expect = str(Program([VarDecl(Id("a"), ArrayType([3.0], NumberType()), None, ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)])), VarDecl(Id("b"), NumberType(), None, ArrayCell(CallExpr(Id("f"), [StringLiteral("h")]), [NumberLiteral(1.0)]))]))
        self.assertTrue(TestAST.test(input, expect, 308))
        
    def test_simple_program_10(self):
        input = """func print(number a)
        begin
            print(a)
        end
        """
        expect = str(Program([FuncDecl(Id("print"), [VarDecl(Id("a"), NumberType())], Block([CallStmt(Id("print"), [Id("a")])]))]))
        self.assertTrue(TestAST.test(input, expect, 309))
        
    def test_simple_program_11(self):
        input = """func print(number a)
        """
        expect = str(Program([FuncDecl(Id("print"), [VarDecl(Id("a"), NumberType())], None)]))
        self.assertTrue(TestAST.test(input, expect, 310))
        
    def test_simple_program_12(self):
        input = """func print()
        """
        expect = str(Program([FuncDecl(Id("print"), [], None)]))
        self.assertTrue(TestAST.test(input, expect, 311))
        
    def test_simple_program_13(self):
        input = """func print()
        begin
        end
        """
        expect = str(Program([FuncDecl(Id("print"), [], Block([]))]))
        self.assertTrue(TestAST.test(input, expect, 312))
        
    def test_simple_program_14(self):
        input = """
number a
number b[5,4]
dynamic k
var s <- "Hello"
##this is a comment
string str <- "\\' Hi My name is 'Huy', I say: '\"Hello'\"" ## this is a comment
func print (number a)
func main() begin
    var i <- 0
    for i until i < 8 by 1 begin
        if (i % 2 = 0) 
            print(i)
        elif (i % 3 = 0) print(i)
        elif (i % 4 = 0) break
        else
            continue
    end
end
func print (number a) begin
    a <- 1
end
func ah(string b[9,10], bool c) begin
    a <- 1
    for a until a < 8 + 9 by 1 begin
        if (i % 2 = 0) begin
            a <- 10.4e3
            ah(a,b)
        end
        elif (i % 3 = 0) return 1
        elif (i % 4 = 0) break
        else
            continue
    end
end

        """
        expect = str(Program([
            VarDecl(Id("a"), NumberType()),
            VarDecl(Id("b"), ArrayType([5.0, 4.0], NumberType())),
            VarDecl(Id("k"), None, "dynamic"),
            VarDecl(Id("s"), None, "var", StringLiteral("Hello")),
            VarDecl(Id("str"), StringType(), None, StringLiteral("\\' Hi My name is 'Huy', I say: '\"Hello'\"")),
            FuncDecl(Id("print"), [VarDecl(Id("a"), NumberType())], None),
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("i"), None, "var", NumberLiteral(0.0)),
                For(Id("i"), BinaryOp("<", Id("i"), NumberLiteral(8.0)), NumberLiteral(1.0), Block([
                    If(BinaryOp("=", BinaryOp("%", Id("i"), NumberLiteral(2.0)), NumberLiteral(0.0)), 
                       CallStmt(Id("print"), [Id("i")]),
                       [(BinaryOp("=", BinaryOp("%", Id("i"), NumberLiteral(3.0)), NumberLiteral(0.0)), CallStmt(Id("print"), [Id("i")])),
                        (BinaryOp("=", BinaryOp("%", Id("i"), NumberLiteral(4.0)), NumberLiteral(0.0)), Break()),
                       ],
                       Continue()
                    ),
                ])),
            ])),
            FuncDecl(Id("print"), [VarDecl(Id("a"), NumberType())], Block([Assign(Id("a"), NumberLiteral(1.0))])),  
            FuncDecl(Id("ah"), [VarDecl(Id("b"), ArrayType([9.0, 10.0], StringType())), VarDecl(Id("c"), BoolType())], Block([
                Assign(Id("a"), NumberLiteral(1.0)),
                For(Id("a"), BinaryOp("<", Id("a"), BinaryOp("+", NumberLiteral(8.0), NumberLiteral(9.0))), NumberLiteral(1.0), Block([
                    If(BinaryOp("=", BinaryOp("%", Id("i"), NumberLiteral(2.0)), NumberLiteral(0.0)), 
                       Block([Assign(Id("a"), NumberLiteral(10400.0)), CallStmt(Id("ah"), [Id("a"), Id("b")])]),
                       [(BinaryOp("=", BinaryOp("%", Id("i"), NumberLiteral(3.0)), NumberLiteral(0.0)), Return(NumberLiteral(1.0))),
                        (BinaryOp("=", BinaryOp("%", Id("i"), NumberLiteral(4.0)), NumberLiteral(0.0)), Break()),
                       ],
                       Continue()
                    ),
                ])),
            ]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 313))
        
    def test_simple_program_15(self):
        input = """func main() return 1
        """
        expect = str(Program([FuncDecl(Id("main"), [], Return(NumberLiteral(1.0)))]))
        self.assertTrue(TestAST.test(input, expect, 314))
