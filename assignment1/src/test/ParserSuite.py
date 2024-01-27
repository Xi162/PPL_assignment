import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """func main () return 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
        
    def test_simple_program1(self):
        """Simple program: int main() {} """
        input = """int main () {
            putIntLn(4);
        }
        """
        expect = "Error on line 1 col 0: int"
        self.assertTrue(TestParser.test(input,expect,202))
    
    def test_simple_program2(self):
        """Simple program: int main() {} """
        input = """int main( {}
        """
        expect = "Error on line 1 col 0: int"
        self.assertTrue(TestParser.test(input,expect,203))
    
    def test_program3(self):
        """Simple program: int main() {} """
        input = """func a(number b[5]) return 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))
    
    def test_program4(self):
        """Simple program: int main() {} """
        input = """
        number a <- 1
        
        
        number b <- 2
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))
    
    def test_program4(self):
        """Simple program: int main() {} """
        input = """
number a <- 1
number b[5,4] <- [1,2,3,[a,3], a + 1]
func print (number a)
func main() begin
    var i <- 0
    for i until i < 8 by 1 print(i)
end
func print (number a) begin
    putIntLn(a)
end

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))
        
        
    def test_program5(self):
        """ """
        input = """
number a <- 1
number b[5,4] <- [1,2,3,[a,3], a + 1]
func print (number a)
func main() begin
    var i <- 0
    for i until i < 8 by 1 begin
        if (i % 2 = 0) print(i)
        elif (i % 3 = 0) print(i)
        elif (i % 4 = 0) break
        else
            continue
    end
end
func print (number a) begin
    putIntLn(a)
end

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))
        
        
    def test_program6(self):
        """ """
        input = """
number a <- 1
number b[5,4] <- [1,2,3,[a,3], a + 1]
func print (number a)
func main() begin
    var i <- 0
    for i until i < 8 by 1 begin
        if (i % 2 = 0) print(i)
        elif (i % 3 = 0) print(i)
        elif (i % 4 = 0) break
        else
            continue
    end
end
func print (number a) a <- 1

        """
        expect = "Error on line 15 col 22: a"
        self.assertTrue(TestParser.test(input,expect,208))
        
    def test_program7(self):
        """ """
        input = """
number a <- 1
number b[5,4] <- [1,2,3,[a,3], a + 1]
func print (number a)
func main() begin
    var i <- 0
    for i until i < 8 by 1 begin
        if (i % 2 = 0) print(i)
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))
        
    def test_program8(self):
        """ """
        input = """
number a <- 1
number b[5,4] <- [1,2,3,[a,3], a + 1]
##this is a comment
string str <- "\\' Hi My name is 'Huy', I say: '\"Hello'\"" ## this is a comment
func print (number a)
func main() begin
    var i <- 0
    for i until i < 8 by 1 begin
        if (i % 2 = 0) print(i)
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,210))
        