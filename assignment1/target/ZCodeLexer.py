# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *
id = "2152578"



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65")
        buf.write("\u01a8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\3\2\6\2\177\n\2\r\2\16\2\u0080")
        buf.write("\3\2\3\2\7\2\u0085\n\2\f\2\16\2\u0088\13\2\5\2\u008a\n")
        buf.write("\2\3\2\3\2\5\2\u008e\n\2\3\2\6\2\u0091\n\2\r\2\16\2\u0092")
        buf.write("\5\2\u0095\n\2\3\3\3\3\5\3\u0099\n\3\3\4\3\4\3\4\7\4\u009e")
        buf.write("\n\4\f\4\16\4\u00a1\13\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3$\3")
        buf.write("$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3\'\3(\3(\3(\3)\3)\3*")
        buf.write("\3*\3+\3+\3,\3,\3-\3-\3.\3.\7.\u0149\n.\f.\16.\u014c\13")
        buf.write(".\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3")
        buf.write("\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\66\3\66")
        buf.write("\3\66\3\67\3\67\3\67\38\38\38\38\38\38\38\38\58\u0170")
        buf.write("\n8\39\39\39\39\59\u0176\n9\3:\3:\3:\7:\u017b\n:\f:\16")
        buf.write(":\u017e\13:\3:\3:\5:\u0182\n:\3:\3:\3;\6;\u0187\n;\r;")
        buf.write("\16;\u0188\3;\3;\3<\3<\3<\3=\3=\7=\u0192\n=\f=\16=\u0195")
        buf.write("\13=\3=\3=\3=\3=\3=\3>\3>\3>\7>\u019f\n>\f>\16>\u01a2")
        buf.write("\13>\3>\5>\u01a5\n>\3>\3>\3\u0193\2?\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34")
        buf.write("\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\2_\2")
        buf.write("a\2c\2e\2g\2i\2k\2m\2o\2q\60s\61u\62w\63y\64{\65\3\2\f")
        buf.write("\4\2GGgg\4\2--//\6\2\f\f\17\17$$^^\5\2C\\aac|\6\2\62;")
        buf.write("C\\aac|\3\2\62;\4\2\f\f\17\17\5\2\n\13\16\16\"\"\t\2)")
        buf.write(")^^ddhhppttvv\4\3\f\f\17\17\2\u01b5\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3")
        buf.write("\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2")
        buf.write("\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2")
        buf.write("\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3")
        buf.write("\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W")
        buf.write("\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2")
        buf.write("u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\3~\3\2\2\2")
        buf.write("\5\u0098\3\2\2\2\7\u009a\3\2\2\2\t\u00a5\3\2\2\2\13\u00aa")
        buf.write("\3\2\2\2\r\u00b0\3\2\2\2\17\u00b7\3\2\2\2\21\u00bc\3\2")
        buf.write("\2\2\23\u00c3\3\2\2\2\25\u00ca\3\2\2\2\27\u00ce\3\2\2")
        buf.write("\2\31\u00d6\3\2\2\2\33\u00db\3\2\2\2\35\u00df\3\2\2\2")
        buf.write("\37\u00e5\3\2\2\2!\u00e8\3\2\2\2#\u00ee\3\2\2\2%\u00f7")
        buf.write("\3\2\2\2\'\u00fa\3\2\2\2)\u00ff\3\2\2\2+\u0104\3\2\2\2")
        buf.write("-\u010a\3\2\2\2/\u010e\3\2\2\2\61\u0112\3\2\2\2\63\u0116")
        buf.write("\3\2\2\2\65\u0119\3\2\2\2\67\u011b\3\2\2\29\u011d\3\2")
        buf.write("\2\2;\u011f\3\2\2\2=\u0121\3\2\2\2?\u0123\3\2\2\2A\u0126")
        buf.write("\3\2\2\2C\u0128\3\2\2\2E\u012b\3\2\2\2G\u012d\3\2\2\2")
        buf.write("I\u012f\3\2\2\2K\u0132\3\2\2\2M\u0135\3\2\2\2O\u0139\3")
        buf.write("\2\2\2Q\u013c\3\2\2\2S\u013e\3\2\2\2U\u0140\3\2\2\2W\u0142")
        buf.write("\3\2\2\2Y\u0144\3\2\2\2[\u0146\3\2\2\2]\u014d\3\2\2\2")
        buf.write("_\u014f\3\2\2\2a\u0152\3\2\2\2c\u0155\3\2\2\2e\u0158\3")
        buf.write("\2\2\2g\u015b\3\2\2\2i\u015e\3\2\2\2k\u0161\3\2\2\2m\u0164")
        buf.write("\3\2\2\2o\u016f\3\2\2\2q\u0175\3\2\2\2s\u0177\3\2\2\2")
        buf.write("u\u0186\3\2\2\2w\u018c\3\2\2\2y\u018f\3\2\2\2{\u019b\3")
        buf.write("\2\2\2}\177\5]/\2~}\3\2\2\2\177\u0080\3\2\2\2\u0080~\3")
        buf.write("\2\2\2\u0080\u0081\3\2\2\2\u0081\u0089\3\2\2\2\u0082\u0086")
        buf.write("\7\60\2\2\u0083\u0085\5]/\2\u0084\u0083\3\2\2\2\u0085")
        buf.write("\u0088\3\2\2\2\u0086\u0084\3\2\2\2\u0086\u0087\3\2\2\2")
        buf.write("\u0087\u008a\3\2\2\2\u0088\u0086\3\2\2\2\u0089\u0082\3")
        buf.write("\2\2\2\u0089\u008a\3\2\2\2\u008a\u0094\3\2\2\2\u008b\u008d")
        buf.write("\t\2\2\2\u008c\u008e\t\3\2\2\u008d\u008c\3\2\2\2\u008d")
        buf.write("\u008e\3\2\2\2\u008e\u0090\3\2\2\2\u008f\u0091\5]/\2\u0090")
        buf.write("\u008f\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0090\3\2\2\2")
        buf.write("\u0092\u0093\3\2\2\2\u0093\u0095\3\2\2\2\u0094\u008b\3")
        buf.write("\2\2\2\u0094\u0095\3\2\2\2\u0095\4\3\2\2\2\u0096\u0099")
        buf.write("\5\t\5\2\u0097\u0099\5\13\6\2\u0098\u0096\3\2\2\2\u0098")
        buf.write("\u0097\3\2\2\2\u0099\6\3\2\2\2\u009a\u009f\7$\2\2\u009b")
        buf.write("\u009e\5o8\2\u009c\u009e\n\4\2\2\u009d\u009b\3\2\2\2\u009d")
        buf.write("\u009c\3\2\2\2\u009e\u00a1\3\2\2\2\u009f\u009d\3\2\2\2")
        buf.write("\u009f\u00a0\3\2\2\2\u00a0\u00a2\3\2\2\2\u00a1\u009f\3")
        buf.write("\2\2\2\u00a2\u00a3\7$\2\2\u00a3\u00a4\b\4\2\2\u00a4\b")
        buf.write("\3\2\2\2\u00a5\u00a6\7v\2\2\u00a6\u00a7\7t\2\2\u00a7\u00a8")
        buf.write("\7w\2\2\u00a8\u00a9\7g\2\2\u00a9\n\3\2\2\2\u00aa\u00ab")
        buf.write("\7h\2\2\u00ab\u00ac\7c\2\2\u00ac\u00ad\7n\2\2\u00ad\u00ae")
        buf.write("\7u\2\2\u00ae\u00af\7g\2\2\u00af\f\3\2\2\2\u00b0\u00b1")
        buf.write("\7p\2\2\u00b1\u00b2\7w\2\2\u00b2\u00b3\7o\2\2\u00b3\u00b4")
        buf.write("\7d\2\2\u00b4\u00b5\7g\2\2\u00b5\u00b6\7t\2\2\u00b6\16")
        buf.write("\3\2\2\2\u00b7\u00b8\7d\2\2\u00b8\u00b9\7q\2\2\u00b9\u00ba")
        buf.write("\7q\2\2\u00ba\u00bb\7n\2\2\u00bb\20\3\2\2\2\u00bc\u00bd")
        buf.write("\7u\2\2\u00bd\u00be\7v\2\2\u00be\u00bf\7t\2\2\u00bf\u00c0")
        buf.write("\7k\2\2\u00c0\u00c1\7p\2\2\u00c1\u00c2\7i\2\2\u00c2\22")
        buf.write("\3\2\2\2\u00c3\u00c4\7t\2\2\u00c4\u00c5\7g\2\2\u00c5\u00c6")
        buf.write("\7v\2\2\u00c6\u00c7\7w\2\2\u00c7\u00c8\7t\2\2\u00c8\u00c9")
        buf.write("\7p\2\2\u00c9\24\3\2\2\2\u00ca\u00cb\7x\2\2\u00cb\u00cc")
        buf.write("\7c\2\2\u00cc\u00cd\7t\2\2\u00cd\26\3\2\2\2\u00ce\u00cf")
        buf.write("\7f\2\2\u00cf\u00d0\7{\2\2\u00d0\u00d1\7p\2\2\u00d1\u00d2")
        buf.write("\7c\2\2\u00d2\u00d3\7o\2\2\u00d3\u00d4\7k\2\2\u00d4\u00d5")
        buf.write("\7e\2\2\u00d5\30\3\2\2\2\u00d6\u00d7\7h\2\2\u00d7\u00d8")
        buf.write("\7w\2\2\u00d8\u00d9\7p\2\2\u00d9\u00da\7e\2\2\u00da\32")
        buf.write("\3\2\2\2\u00db\u00dc\7h\2\2\u00dc\u00dd\7q\2\2\u00dd\u00de")
        buf.write("\7t\2\2\u00de\34\3\2\2\2\u00df\u00e0\7w\2\2\u00e0\u00e1")
        buf.write("\7p\2\2\u00e1\u00e2\7v\2\2\u00e2\u00e3\7k\2\2\u00e3\u00e4")
        buf.write("\7n\2\2\u00e4\36\3\2\2\2\u00e5\u00e6\7d\2\2\u00e6\u00e7")
        buf.write("\7{\2\2\u00e7 \3\2\2\2\u00e8\u00e9\7d\2\2\u00e9\u00ea")
        buf.write("\7t\2\2\u00ea\u00eb\7g\2\2\u00eb\u00ec\7c\2\2\u00ec\u00ed")
        buf.write("\7m\2\2\u00ed\"\3\2\2\2\u00ee\u00ef\7e\2\2\u00ef\u00f0")
        buf.write("\7q\2\2\u00f0\u00f1\7p\2\2\u00f1\u00f2\7v\2\2\u00f2\u00f3")
        buf.write("\7k\2\2\u00f3\u00f4\7p\2\2\u00f4\u00f5\7w\2\2\u00f5\u00f6")
        buf.write("\7g\2\2\u00f6$\3\2\2\2\u00f7\u00f8\7k\2\2\u00f8\u00f9")
        buf.write("\7h\2\2\u00f9&\3\2\2\2\u00fa\u00fb\7g\2\2\u00fb\u00fc")
        buf.write("\7n\2\2\u00fc\u00fd\7u\2\2\u00fd\u00fe\7g\2\2\u00fe(\3")
        buf.write("\2\2\2\u00ff\u0100\7g\2\2\u0100\u0101\7n\2\2\u0101\u0102")
        buf.write("\7k\2\2\u0102\u0103\7h\2\2\u0103*\3\2\2\2\u0104\u0105")
        buf.write("\7d\2\2\u0105\u0106\7g\2\2\u0106\u0107\7i\2\2\u0107\u0108")
        buf.write("\7k\2\2\u0108\u0109\7p\2\2\u0109,\3\2\2\2\u010a\u010b")
        buf.write("\7g\2\2\u010b\u010c\7p\2\2\u010c\u010d\7f\2\2\u010d.\3")
        buf.write("\2\2\2\u010e\u010f\7p\2\2\u010f\u0110\7q\2\2\u0110\u0111")
        buf.write("\7v\2\2\u0111\60\3\2\2\2\u0112\u0113\7c\2\2\u0113\u0114")
        buf.write("\7p\2\2\u0114\u0115\7f\2\2\u0115\62\3\2\2\2\u0116\u0117")
        buf.write("\7q\2\2\u0117\u0118\7t\2\2\u0118\64\3\2\2\2\u0119\u011a")
        buf.write("\7-\2\2\u011a\66\3\2\2\2\u011b\u011c\7/\2\2\u011c8\3\2")
        buf.write("\2\2\u011d\u011e\7,\2\2\u011e:\3\2\2\2\u011f\u0120\7\61")
        buf.write("\2\2\u0120<\3\2\2\2\u0121\u0122\7\'\2\2\u0122>\3\2\2\2")
        buf.write("\u0123\u0124\7>\2\2\u0124\u0125\7/\2\2\u0125@\3\2\2\2")
        buf.write("\u0126\u0127\7?\2\2\u0127B\3\2\2\2\u0128\u0129\7#\2\2")
        buf.write("\u0129\u012a\7?\2\2\u012aD\3\2\2\2\u012b\u012c\7>\2\2")
        buf.write("\u012cF\3\2\2\2\u012d\u012e\7@\2\2\u012eH\3\2\2\2\u012f")
        buf.write("\u0130\7>\2\2\u0130\u0131\7?\2\2\u0131J\3\2\2\2\u0132")
        buf.write("\u0133\7@\2\2\u0133\u0134\7?\2\2\u0134L\3\2\2\2\u0135")
        buf.write("\u0136\7\60\2\2\u0136\u0137\7\60\2\2\u0137\u0138\7\60")
        buf.write("\2\2\u0138N\3\2\2\2\u0139\u013a\7?\2\2\u013a\u013b\7?")
        buf.write("\2\2\u013bP\3\2\2\2\u013c\u013d\7.\2\2\u013dR\3\2\2\2")
        buf.write("\u013e\u013f\7*\2\2\u013fT\3\2\2\2\u0140\u0141\7+\2\2")
        buf.write("\u0141V\3\2\2\2\u0142\u0143\7]\2\2\u0143X\3\2\2\2\u0144")
        buf.write("\u0145\7_\2\2\u0145Z\3\2\2\2\u0146\u014a\t\5\2\2\u0147")
        buf.write("\u0149\t\6\2\2\u0148\u0147\3\2\2\2\u0149\u014c\3\2\2\2")
        buf.write("\u014a\u0148\3\2\2\2\u014a\u014b\3\2\2\2\u014b\\\3\2\2")
        buf.write("\2\u014c\u014a\3\2\2\2\u014d\u014e\t\7\2\2\u014e^\3\2")
        buf.write("\2\2\u014f\u0150\7^\2\2\u0150\u0151\7d\2\2\u0151`\3\2")
        buf.write("\2\2\u0152\u0153\7^\2\2\u0153\u0154\7h\2\2\u0154b\3\2")
        buf.write("\2\2\u0155\u0156\7^\2\2\u0156\u0157\7t\2\2\u0157d\3\2")
        buf.write("\2\2\u0158\u0159\7^\2\2\u0159\u015a\7p\2\2\u015af\3\2")
        buf.write("\2\2\u015b\u015c\7^\2\2\u015c\u015d\7v\2\2\u015dh\3\2")
        buf.write("\2\2\u015e\u015f\7^\2\2\u015f\u0160\7)\2\2\u0160j\3\2")
        buf.write("\2\2\u0161\u0162\7^\2\2\u0162\u0163\7^\2\2\u0163l\3\2")
        buf.write("\2\2\u0164\u0165\7)\2\2\u0165\u0166\7$\2\2\u0166n\3\2")
        buf.write("\2\2\u0167\u0170\5_\60\2\u0168\u0170\5a\61\2\u0169\u0170")
        buf.write("\5c\62\2\u016a\u0170\5e\63\2\u016b\u0170\5g\64\2\u016c")
        buf.write("\u0170\5i\65\2\u016d\u0170\5k\66\2\u016e\u0170\5m\67\2")
        buf.write("\u016f\u0167\3\2\2\2\u016f\u0168\3\2\2\2\u016f\u0169\3")
        buf.write("\2\2\2\u016f\u016a\3\2\2\2\u016f\u016b\3\2\2\2\u016f\u016c")
        buf.write("\3\2\2\2\u016f\u016d\3\2\2\2\u016f\u016e\3\2\2\2\u0170")
        buf.write("p\3\2\2\2\u0171\u0176\t\b\2\2\u0172\u0173\7\17\2\2\u0173")
        buf.write("\u0174\7\f\2\2\u0174\u0176\b9\3\2\u0175\u0171\3\2\2\2")
        buf.write("\u0175\u0172\3\2\2\2\u0176r\3\2\2\2\u0177\u0178\7%\2\2")
        buf.write("\u0178\u017c\7%\2\2\u0179\u017b\n\b\2\2\u017a\u0179\3")
        buf.write("\2\2\2\u017b\u017e\3\2\2\2\u017c\u017a\3\2\2\2\u017c\u017d")
        buf.write("\3\2\2\2\u017d\u0181\3\2\2\2\u017e\u017c\3\2\2\2\u017f")
        buf.write("\u0182\7\2\2\3\u0180\u0182\3\2\2\2\u0181\u017f\3\2\2\2")
        buf.write("\u0181\u0180\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0184\b")
        buf.write(":\4\2\u0184t\3\2\2\2\u0185\u0187\t\t\2\2\u0186\u0185\3")
        buf.write("\2\2\2\u0187\u0188\3\2\2\2\u0188\u0186\3\2\2\2\u0188\u0189")
        buf.write("\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u018b\b;\4\2\u018b")
        buf.write("v\3\2\2\2\u018c\u018d\13\2\2\2\u018d\u018e\b<\5\2\u018e")
        buf.write("x\3\2\2\2\u018f\u0193\7$\2\2\u0190\u0192\13\2\2\2\u0191")
        buf.write("\u0190\3\2\2\2\u0192\u0195\3\2\2\2\u0193\u0194\3\2\2\2")
        buf.write("\u0193\u0191\3\2\2\2\u0194\u0196\3\2\2\2\u0195\u0193\3")
        buf.write("\2\2\2\u0196\u0197\7^\2\2\u0197\u0198\n\n\2\2\u0198\u0199")
        buf.write("\3\2\2\2\u0199\u019a\b=\6\2\u019az\3\2\2\2\u019b\u01a0")
        buf.write("\7$\2\2\u019c\u019f\5o8\2\u019d\u019f\n\4\2\2\u019e\u019c")
        buf.write("\3\2\2\2\u019e\u019d\3\2\2\2\u019f\u01a2\3\2\2\2\u01a0")
        buf.write("\u019e\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u01a4\3\2\2\2")
        buf.write("\u01a2\u01a0\3\2\2\2\u01a3\u01a5\t\13\2\2\u01a4\u01a3")
        buf.write("\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\u01a7\b>\7\2\u01a7")
        buf.write("|\3\2\2\2\26\2\u0080\u0086\u0089\u008d\u0092\u0094\u0098")
        buf.write("\u009d\u009f\u014a\u016f\u0175\u017c\u0181\u0188\u0193")
        buf.write("\u019e\u01a0\u01a4\b\3\4\2\39\3\b\2\2\3<\4\3=\5\3>\6")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NUMLIT = 1
    BOOLLIT = 2
    STRINGLIT = 3
    TRUE = 4
    FALSE = 5
    NUMBER = 6
    BOOL = 7
    STRING = 8
    RETURN = 9
    VAR = 10
    DYNAMIC = 11
    FUNC = 12
    FOR = 13
    UNTIL = 14
    BY = 15
    BREAK = 16
    CONTINUE = 17
    IF = 18
    ELSE = 19
    ELIF = 20
    BEGIN = 21
    END = 22
    NOT = 23
    AND = 24
    OR = 25
    ADDOP = 26
    SUBOP = 27
    MULOP = 28
    DIVOP = 29
    MODOP = 30
    ASSIGNOP = 31
    EQUALOP = 32
    DIFFOP = 33
    SMALLEROP = 34
    GREATEROP = 35
    SEQOP = 36
    GEQOP = 37
    ELLIPOP = 38
    DOUBLEEQOP = 39
    COMMA = 40
    LRB = 41
    RRB = 42
    LSQB = 43
    RSQB = 44
    IDENTIFIER = 45
    LINEBREAK = 46
    COMMENT = 47
    WS = 48
    ERROR_CHAR = 49
    ILLEGAL_ESCAPE = 50
    UNCLOSE_STRING = 51

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'number'", "'bool'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'not'", "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'<-'", "'='", "'!='", "'<'", "'>'", "'<='", "'>='", 
            "'...'", "'=='", "','", "'('", "')'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>",
            "NUMLIT", "BOOLLIT", "STRINGLIT", "TRUE", "FALSE", "NUMBER", 
            "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", 
            "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
            "END", "NOT", "AND", "OR", "ADDOP", "SUBOP", "MULOP", "DIVOP", 
            "MODOP", "ASSIGNOP", "EQUALOP", "DIFFOP", "SMALLEROP", "GREATEROP", 
            "SEQOP", "GEQOP", "ELLIPOP", "DOUBLEEQOP", "COMMA", "LRB", "RRB", 
            "LSQB", "RSQB", "IDENTIFIER", "LINEBREAK", "COMMENT", "WS", 
            "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    ruleNames = [ "NUMLIT", "BOOLLIT", "STRINGLIT", "TRUE", "FALSE", "NUMBER", 
                  "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", "FUNC", 
                  "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", 
                  "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "ADDOP", "SUBOP", 
                  "MULOP", "DIVOP", "MODOP", "ASSIGNOP", "EQUALOP", "DIFFOP", 
                  "SMALLEROP", "GREATEROP", "SEQOP", "GEQOP", "ELLIPOP", 
                  "DOUBLEEQOP", "COMMA", "LRB", "RRB", "LSQB", "RSQB", "IDENTIFIER", 
                  "DIGIT", "BACKSPACEESC", "FORMFEEDESC", "CARRETURNESC", 
                  "NEWLINEESC", "TABESC", "SQUOTEESC", "BACKLASHESC", "DQUOTEESC", 
                  "ESC", "LINEBREAK", "COMMENT", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[2] = self.STRINGLIT_action 
            actions[55] = self.LINEBREAK_action 
            actions[58] = self.ERROR_CHAR_action 
            actions[59] = self.ILLEGAL_ESCAPE_action 
            actions[60] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def LINEBREAK_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = '\n'
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise ErrorToken(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise IllegalEscape(self.text[1:len(self.text)])
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise UncloseString(self.text[1:len(self.text)-1]) if(self.text[len(self.text)-1] == '\n' or self.text[len(self.text)-1] == '\r' ) else UncloseString(self.text[1:len(self.text)])
     


