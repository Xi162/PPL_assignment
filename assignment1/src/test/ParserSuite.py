import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_program1(self):
        """Simple program: int main() {} """
        input = """func main () return 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
        
    def test_program2(self):
        """Simple program: int main() {} """
        input = """int main () {
            putIntLn(4);
        }
        """
        expect = "Error on line 1 col 0: int"
        self.assertTrue(TestParser.test(input,expect,202))
    
    def test_program3(self):
        """Simple program: int main() {} """
        input = """func a(number b[5]) return 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))
    
    def test_program4(self):
        """Simple program: int main() {} """
        input = """
        number a <- 1
        
        
        number b <- 2
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))
    
    def test_program5(self):
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
        self.assertTrue(TestParser.test(input,expect,205))
        
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
func print (number a) begin
    putIntLn(a)
end

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))
            
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
func print (number a) a <- 1

        """
        expect = "Error on line 15 col 22: a"
        self.assertTrue(TestParser.test(input,expect,207))
        
    def test_program8(self):
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
        self.assertTrue(TestParser.test(input,expect,208))
        
    def test_program9(self):
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
        self.assertTrue(TestParser.test(input,expect,209))
        
    def test_program10(self):
        """ """
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
        
    def test_program11(self):
        """ """
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
            if (i % 5 = 0) print(i)
            elif (true) print(i)
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
        self.assertTrue(TestParser.test(input,expect,211))
        
    def test_program12(self):
        """ """
        input = """
string _AM
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))
    
    def test_program13(self):
        """ """
        input = """
## Hi
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,213))
    
    def test_program14(self):
        """ """
        input = """
dynamic _a3
var hell0 <- "Hello"
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))
    
    def test_program15(self):
        """ """
        input = """
if (a = 4) number a <- 1
        """
        expect = "Error on line 2 col 0: if"
        self.assertTrue(TestParser.test(input,expect,215))
        
    def test_program16(self):
        """ """
        input = """
func print (number a) begin
    putIntLn(a)
end
func main () 

begin
    if (a = 4) number a <- 1
    else 
    begin
        number i <- 0
        for i until i < 8 by 1 begin
            if (i % 2 = 0) 
                if (i % 5 = 0) print(i)
                elif (true) print(i)
            elif (i % 3 = 0) print(i)
            elif (i % 4 = 0) break
            else
                continue
                
                
        end
        
        
    end 
    
    
end


        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,216))
    
    def test_program17(self):
        """ """
        input = """
func print (number a) begin
    putIntLn(a)
end
func main () 

begin
    if (a = 4) number a <- 1
    else 
    begin
        number i <- 0
        for i until i < 8 by 1 begin
            if (i % 2 = 0) 
                if (i % 5 = 0) print(i)
                elif (true) print(i)
                else a[1] <- a()[2]\n\r
            elif (i % 3 = 0) print(i)
            elif (i % 4 = 0) break
            else
                continue
                
                
        end
        
        
    end 
    
    
end


        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,217))
    
    def test_program18(self):
        """ """
        input = """
var a <- 1 < false >= 2
func print (number a) begin
    putIntLn(a)
end
func main () 

begin
    if (a = 4) number a <- 1
    else 
    begin
        number i <- 0
        for i until i < 8 by 1 begin
            if (i % 2 = 0) 
                if (i % 5 = 0) print(i)
                elif (true) print(i)
                else a[1] <- a()[2]\n\r
            elif (i % 3 = 0) print(i)
            elif (i % 4 = 0) break
            else
                continue
                
                
        end
        
        
    end 
    
    
end


        """
        expect = "Error on line 2 col 19: >="
        self.assertTrue(TestParser.test(input,expect,218))
        
    def test_program19(self):
        input = '''
func zvz ()
	return "'"'"'""
var E2
func Ow (number nj[65,484.398,0], number t2T[5,4.602], string DlM)
	begin
		## Ok/MVZydJT1QZnKsLj^
		## )`+b?/tNH$
		## gydY46Y"P
	end
func R1v6 (var A4a[5.355,0.199])
	return 9.105
func Ztn ()
	return

'''
        expect = '''Error on line 4 col 6: 
'''
        self.assertTrue(TestParser.test(input, expect, 219))
        
    def test_program20(self):
        input = '''
func main()
begin
    if (a = 4) number a <- 1
end
'''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))
        
    def test_program21(self):
        input = '''
func main()
begin
    if (a = 4) number a <- 1
    else return 2
end
'''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))
        
    def test_program22(self):
        input = '''
func main()
begin
    if (a = 4) number a <- 1
    else return 2
    else return 3
end
'''
        expect = "Error on line 6 col 4: else"
        self.assertTrue(TestParser.test(input, expect, 222))
        
    def test_program23(self):
        input = '''
func main()
begin
    if (a = 4) number a <- 1
    elif(a = 5) number a <- 2
    else return 2
end
'''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))
        
    def test_program24(self):
        input = '''
func main()
begin
    if (a = 4) number a <- 1
    elif(a = 5) number a <- 2
    elif(a = 6) 
        number a <- 3
    else return 2
end
'''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))
        
    def test_program25(self):
        input = '''
func main()
begin
    if (a = 4) number a <- 1
    elif(a = 5) begin
        number a <- 2
        return 1
    end
    elif(a = 6) 
        number a <- 3
    else return 2
end
'''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))
        
    def test_program26(self):
        input = '''
func main()
begin
    if (a = 4) number a <- 1
    elif(a = 5) 
        begin
            number a <- 2
            return 1
        end
    elif(a = 6) 
        number a <- 3
    else return 2
    return 3
end
'''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))
        
    def test_program27(self):
        input = '''
        
func main()
begin
    if (a = 4) number a <- 1
    elif(a = 5) 
        begin
            number a <- 2 ... (2 ... 2)
            return 1
        end
    elif(a = 6) 
        number a <- 3
    else return 2
    return 3
end
'''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))
        
    def test_program28(self):
        input = '''
        
func main()
begin
    for i until i < 8 by 1 begin
        i <- i + 1
        i <- i + 1
    end
end
'''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))
        
    def test_program29(self):
        input = '''
        bool a[5,4]
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))
    
    def test_program30(self):
        input = '''
        string a[5,4] <- ["hello", "world"]
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))
        
    def test_program31(self):
        input = '''
        number a[5,4] <- [1,2,3,4, [1,3,4,6%8]]
        func main()
            return 0
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))
        
    def test_program32(self):
        input = '''
        bool flag <- true
        func main()
            if (flag) return 1
        '''
        expect = "Error on line 4 col 12: if"
        self.assertTrue(TestParser.test(input, expect, 232))
        
    def test_program33(self):
        input = '''
        func print(string a[5,4], bool b) 
            begin
                putString(a[1])
            end
        func main()
            begin
            end
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))
    
    def test_program34(self):
        input = '''
        if (a = 4) number a <- 1
        '''
        expect = "Error on line 2 col 8: if"
        self.assertTrue(TestParser.test(input, expect, 234))
        
    def test_program35(self):
        input = '''
        ## Hello this is a  comment
        '''
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 235))
        
    def test_program36(self):
        input = '''
        ## declare a variable
        number A <- 1
        func main()
            begin
                print(A)
                return 0*3
            end
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))
        
    def test_program37(self):
        input = '''
        bool flag <- true ## comment inline
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))
        
    def test_program38(self):
        input = '''
        var a
        '''
        expect = "Error on line 2 col 13: \n"
        self.assertTrue(TestParser.test(input, expect, 238))
        
    def test_program39(self):
        input = '''
        number i <- 0
        func _A() for i until i < 8 by 1 begin
            print(i)
        end
        '''
        expect = "Error on line 3 col 18: for"
        self.assertTrue(TestParser.test(input, expect, 239))
        
    def test_program40(self):
        input = '''
        number i <- 0
        for i until i < 8 by 1 begin
            continue
        end
        '''
        expect = "Error on line 3 col 8: for"
        self.assertTrue(TestParser.test(input, expect, 240))
        
    def test_program41(self):
        input = '''
        bool flag <- true
        func main()
            begin
                continue flag
            end
        '''
        expect = "Error on line 5 col 25: flag"
        self.assertTrue(TestParser.test(input, expect, 241))
        
    def test_program42(self):
        input = '''
        func main() continue
        '''
        expect = "Error on line 2 col 20: continue"
        self.assertTrue(TestParser.test(input, expect, 242))
        
    def test_program43(self):
        input = '''
        func print(string a)
        func main() return print("Hello")
        func print(string a)
            begin
                putString(a)
            end
        
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))
        
    def test_program44(self):
        input = '''
        func print(string a)
        func print(string a)
        func print1(string a)
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))
        
    def test_program45(self):
        input = '''
        ## Hello this is a comment
        string a <- "Hello"
        func print() return a
        func main()
        func main() return print(print())
        ## the end
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))
        
    def test_program46(self):
        input = '''
        func a() begin
            b <- [1,2,3]
        end
        '''
        expect = "Error on line 3 col 17: ["
        self.assertTrue(TestParser.test(input, expect, 246))
        
    def test_program47(self):
        input = '''
        var a <- [1,2,3]
        '''
        expect = "Error on line 2 col 17: ["
        self.assertTrue(TestParser.test(input, expect, 247))
        
    def test_program48(self):
        input = '''
        dynamic a[5] <- 2
        '''
        expect = "Error on line 2 col 17: ["
        self.assertTrue(TestParser.test(input, expect, 248))
        
    def test_program49(self):
        input = '''
        func a=() return 1
        '''
        expect = "Error on line 2 col 14: ="
        self.assertTrue(TestParser.test(input, expect, 249))
        
    def test_program50(self):
        input = '''
        a[1] <- 2
        '''
        expect = "Error on line 2 col 8: a"
        self.assertTrue(TestParser.test(input, expect, 250))
        
    def test_program51(self):
        input = '''
        number a()[5] <- [1,2,4]
        '''
        expect = "Error on line 2 col 16: ("
        self.assertTrue(TestParser.test(input, expect, 251))
        
    def test_program52(self):
        input = '''
        
        
        func () return 1
        '''
        expect = "Error on line 4 col 13: ("
        self.assertTrue(TestParser.test(input, expect, 252))
        
    def test_program53(self):
        input = '''
        func _(number a) return 1
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))
        
    def test_program54(self):
        input = '''
        var _ <- 1
        func _a_() return _
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))
        
    def test_program55(self):
        input = '''
        continue
        '''
        expect = "Error on line 2 col 8: continue"
        self.assertTrue(TestParser.test(input, expect, 255))
        
    def test_program56(self):
        input = '''
        return break
        '''
        expect = "Error on line 2 col 8: return"
        self.assertTrue(TestParser.test(input, expect, 256))
        
    def test_program57(self):
        input = '''
        func main() return break
        '''
        expect = "Error on line 2 col 27: break"
        self.assertTrue(TestParser.test(input, expect, 257))
        
    def test_program58(self):
        input = '''
        func main() 
            begin
                break
            end
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))
        
    def test_program59(self):
        input = '''
        dynamic a <- (print()) ... (print())
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))
        
    def test_program60(self):
        input = '''
        var a <- (a= b - c) or (1 + 2 % 6 * 2) and (a = 4)
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))
    
    def test_program61(self):
        input = '''
        var a <- a <= var 
        '''
        expect = "Error on line 2 col 22: var"
        self.assertTrue(TestParser.test(input, expect, 261))
        
    def test_program62(self):
        input = '''
        var a <- a + dynamic + or
        '''
        expect = "Error on line 2 col 21: dynamic"
        self.assertTrue(TestParser.test(input, expect, 262))
        
    def test_program63(self):
        input = '''
        var a <-  and + or
        '''
        expect = "Error on line 2 col 18: and"
        self.assertTrue(TestParser.test(input, expect, 263))
        
    def test_program64(self):
        input = '''
        func main(number a()) return 1
        '''
        expect = "Error on line 2 col 26: ("
        self.assertTrue(TestParser.test(input, expect, 264))

    def test_program65(self):
        input = '''
        func (main)(number a) return 1
        '''
        expect = "Error on line 2 col 13: ("
        self.assertTrue(TestParser.test(input, expect, 265))

    def test_program66(self):
        input = '''
        func a[2](number a) return 1
        '''
        expect = "Error on line 2 col 14: ["
        self.assertTrue(TestParser.test(input, expect, 266))

    def test_program67(self):
        input = '''
        func a(number a)
            begin
                a <- 1.0e-3 ... 1
            end
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test_program68(self):
        input = '''
        func a(number a)
            begin
                a <- 1.0e-3 ... 1.2prtint((a(), b)
            end
        '''
        expect = "Error on line 4 col 35: prtint"
        self.assertTrue(TestParser.test(input, expect, 268))

    def test_program69(self):
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
        self.assertTrue(TestParser.test(input, expect, 269))

    def test_program70(self):
        input = """
var a <- 1 < false >= 2
func print (number a) begin
    putIntLn(a)
end
func main () 

begin
    if (a = 4) number a <- 1
    else 
    begin
        number i <- 0
        for i until i < 8 by 1 begin
            if (i % 2 = 0) 
                if (i % 5 = 0) print(i)
                elif (true) print(i)
                else a[1] <- a()[2]\n\r
            elif (i % 3 = 0) print(i)
            elif (i % 4 = 0) break
            else
                continue
                
                
        end
        
        
    end 
    
    
end


        """
        expect = "Error on line 2 col 19: >="
        self.assertTrue(TestParser.test(input, expect, 270))

    def test_program71(self):
        input = '''
        bool flag <- true
        func main()
            begin
                continue flag
            end
        '''
        expect = "Error on line 5 col 25: flag"
        self.assertTrue(TestParser.test(input, expect, 271))

    def test_program72(self):
        input = '''
        func main() begin
            ## some 
            ## comments
            ## at the
            ##
            ##
        end
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))

    def test_program73(self):
        input = '''
        func main() begin end
        '''
        expect = "Error on line 2 col 26: end"
        self.assertTrue(TestParser.test(input, expect, 273))

    def test_program74(self):
        input = '''
        func main() begin
        '''
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 274))

    def test_program75(self):
        input = """
var a <- 1 < false >= 2
func print (number a) begin
    putIntLn(a)
end
func main () 

begin
    if (a = 4) number a <- 1
    else 
    begin
        number i <- 0
        for i until i < 8 by 1 begin
            if (i % 2 = 0) 
                if (i % 5 = 0) print(i)
                elif (true) print(i)
                else a[1] <- a()[2]\n\r
            elif (i % 3 = 0) print(i)
            elif (i % 4 = 0) break
            else
                continue
                
                
        end
        
        
    end 
    
    
end


        """
        expect = "Error on line 2 col 19: >="
        self.assertTrue(TestParser.test(input, expect, 275))

    def test_program76(self):
        input = '''
        func main() begin
            begin
                continue
            end
        '''
        expect = "Error on line 6 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 276))

    def test_program77(self):
        input = '''
        func main() begin
        end'''
        expect = "Error on line 3 col 11: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 277))

    def test_program78(self):
        input = '''var a <- 1 < false + 2'''
        expect = "Error on line 1 col 22: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 278))

    def test_program79(self):
        input = '''
        bool flag <- true
        func main()
            begin
                continue flag
            end
        '''
        expect = "Error on line 5 col 25: flag"
        self.assertTrue(TestParser.test(input, expect, 279))

    def test_program80(self):
        input = '''
        number a[foo()] <- [1,2,3]
        '''
        expect = "Error on line 2 col 17: foo"
        self.assertTrue(TestParser.test(input, expect, 280))

    def test_program81(self):
        input = '''
        string a[1+2] <- ["hello", "world"]
        '''
        expect = "Error on line 2 col 18: +"
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_program82(self):
        input = '''
        ## some
        bool flag <- true ## thing
        func main()
            begin
                continue flag ## is hidden
            end
        '''
        expect = "Error on line 6 col 25: flag"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_program83(self):
        input = '''
        func main() begin
            number a[1] <- [1,2,3]
            a[0] <-1
        end
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_program84(self):
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
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_program85(self):
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
            if (i % 5 = 0) print(i)
            elif (true) print(i)
        elif (i % 3 = 0) print(i)
        elif (i % 4 = 0) for i until i < 8 by 1 begin
            continue
        end
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
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_program86(self):
        input = '''
        func ifs() begin if (a = 4) number a <- 1 end
        '''
        expect = "Error on line 2 col 25: if"
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_program87(self):
        input = """
var a <- 1 < false >= 2
func print (number a) begin
    putIntLn(a)
end
func main () 

begin
    if (a = 4) number a <- 1
    else 
    begin
        number i <- 0
        for i until i < 8 by 1 begin
            if (i % 2 = 0) 
                if (i % 5 = 0) print(i)
                elif (true) print(i)
                else a[1] <- a()[2]\n\r
            elif (i % 3 = 0) print(i)
            elif (i % 4 = 0) break
            else
                continue
                
                
        end
        
        
    end 
    
    
end


        """
        expect = "Error on line 2 col 19: >="
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_program88(self):
        input = '''
        number fish er <- 1
        '''
        expect = "Error on line 2 col 20: er"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_program89(self):
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
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_program90(self):
        input = '''
        var a <- 1 < false ... 2
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_program91(self):
        input = '''
        func Number() return aNumber + Number()
        func main() return Number()
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_program92(self):
        input = '''
        number 100a <- 1
        '''
        expect = "Error on line 2 col 15: 100"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_program93(self):
        input = """
var a <- 1 < false >= 2
func print (number a) begin
    putIntLn(a)
end
func main () 

begin
    if (a = 4) number a <- 1
    else 
    begin
        number i <- 0
        for i until i < 8 by 1 begin
            if (i % 2 = 0) 
                if (i % 5 = 0) print(i)
                elif (true) print(i)
                else a[1] <- a()[2]\n\r
            elif (i % 3 = 0) print(i)
            elif (i % 4 = 0) break
            else
                continue
                
                
        end
        
        
    end 
    
    
end


        """
        expect = "Error on line 2 col 19: >="
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_program94(self):
        input = '''
        var a100 <- 1 or "Hello"
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_program95(self):
        input = '''
        bool flag <- true
        func main()
            begin
                continue flag
            end
        '''
        expect = "Error on line 5 col 25: flag"
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_program96(self):
        input = """
dynamic _a3
var hell0 <- "Hello"
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_program97(self):
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
        self.assertTrue(TestParser.test(input, expect, 297))

    def test_program98(self):
        input = '''
        number a[a,b,c] <- [[1,2,3],[4,5,6],[7,8,9]]
        '''
        expect = "Error on line 2 col 17: a"
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_program99(self):
        input = '''
        number Employee[5,4] <- [1,2,3,4, [1,3,4,68]]
        func main() begin
            number a[1,2] <- [Employee(p())[1,2]]
            Employee[a,b] <- Employee[1,2] + 1
        end
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))
        
    def test_program(self):
        input = '''
        '''
        expect = "Error on line 2 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 200))
