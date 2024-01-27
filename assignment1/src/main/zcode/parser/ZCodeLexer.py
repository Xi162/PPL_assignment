# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65")
        buf.write("\u01a4\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\n8\39\39\3:\3:\3:\7:\u0177\n:\f:\16:\u017a\13:\3:\3:")
        buf.write("\5:\u017e\n:\3:\3:\3;\6;\u0183\n;\r;\16;\u0184\3;\3;\3")
        buf.write("<\3<\3<\3=\3=\7=\u018e\n=\f=\16=\u0191\13=\3=\3=\3=\3")
        buf.write("=\3=\3>\3>\3>\7>\u019b\n>\f>\16>\u019e\13>\3>\5>\u01a1")
        buf.write("\n>\3>\3>\3\u018f\2?\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write("= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\2_\2a\2c\2e\2g\2i")
        buf.write("\2k\2m\2o\2q\60s\61u\62w\63y\64{\65\3\2\f\4\2GGgg\4\2")
        buf.write("--//\5\2\f\f$$^^\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\3\2")
        buf.write("\f\f\5\2\n\13\16\17\"\"\t\2))^^ddhhppttvv\3\3\f\f\2\u01b0")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2q\3\2")
        buf.write("\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3")
        buf.write("\2\2\2\3~\3\2\2\2\5\u0098\3\2\2\2\7\u009a\3\2\2\2\t\u00a5")
        buf.write("\3\2\2\2\13\u00aa\3\2\2\2\r\u00b0\3\2\2\2\17\u00b7\3\2")
        buf.write("\2\2\21\u00bc\3\2\2\2\23\u00c3\3\2\2\2\25\u00ca\3\2\2")
        buf.write("\2\27\u00ce\3\2\2\2\31\u00d6\3\2\2\2\33\u00db\3\2\2\2")
        buf.write("\35\u00df\3\2\2\2\37\u00e5\3\2\2\2!\u00e8\3\2\2\2#\u00ee")
        buf.write("\3\2\2\2%\u00f7\3\2\2\2\'\u00fa\3\2\2\2)\u00ff\3\2\2\2")
        buf.write("+\u0104\3\2\2\2-\u010a\3\2\2\2/\u010e\3\2\2\2\61\u0112")
        buf.write("\3\2\2\2\63\u0116\3\2\2\2\65\u0119\3\2\2\2\67\u011b\3")
        buf.write("\2\2\29\u011d\3\2\2\2;\u011f\3\2\2\2=\u0121\3\2\2\2?\u0123")
        buf.write("\3\2\2\2A\u0126\3\2\2\2C\u0128\3\2\2\2E\u012b\3\2\2\2")
        buf.write("G\u012d\3\2\2\2I\u012f\3\2\2\2K\u0132\3\2\2\2M\u0135\3")
        buf.write("\2\2\2O\u0139\3\2\2\2Q\u013c\3\2\2\2S\u013e\3\2\2\2U\u0140")
        buf.write("\3\2\2\2W\u0142\3\2\2\2Y\u0144\3\2\2\2[\u0146\3\2\2\2")
        buf.write("]\u014d\3\2\2\2_\u014f\3\2\2\2a\u0152\3\2\2\2c\u0155\3")
        buf.write("\2\2\2e\u0158\3\2\2\2g\u015b\3\2\2\2i\u015e\3\2\2\2k\u0161")
        buf.write("\3\2\2\2m\u0164\3\2\2\2o\u016f\3\2\2\2q\u0171\3\2\2\2")
        buf.write("s\u0173\3\2\2\2u\u0182\3\2\2\2w\u0188\3\2\2\2y\u018b\3")
        buf.write("\2\2\2{\u0197\3\2\2\2}\177\5]/\2~}\3\2\2\2\177\u0080\3")
        buf.write("\2\2\2\u0080~\3\2\2\2\u0080\u0081\3\2\2\2\u0081\u0089")
        buf.write("\3\2\2\2\u0082\u0086\7\60\2\2\u0083\u0085\5]/\2\u0084")
        buf.write("\u0083\3\2\2\2\u0085\u0088\3\2\2\2\u0086\u0084\3\2\2\2")
        buf.write("\u0086\u0087\3\2\2\2\u0087\u008a\3\2\2\2\u0088\u0086\3")
        buf.write("\2\2\2\u0089\u0082\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u0094")
        buf.write("\3\2\2\2\u008b\u008d\t\2\2\2\u008c\u008e\t\3\2\2\u008d")
        buf.write("\u008c\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u0090\3\2\2\2")
        buf.write("\u008f\u0091\5]/\2\u0090\u008f\3\2\2\2\u0091\u0092\3\2")
        buf.write("\2\2\u0092\u0090\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0095")
        buf.write("\3\2\2\2\u0094\u008b\3\2\2\2\u0094\u0095\3\2\2\2\u0095")
        buf.write("\4\3\2\2\2\u0096\u0099\5\t\5\2\u0097\u0099\5\13\6\2\u0098")
        buf.write("\u0096\3\2\2\2\u0098\u0097\3\2\2\2\u0099\6\3\2\2\2\u009a")
        buf.write("\u009f\7$\2\2\u009b\u009e\5o8\2\u009c\u009e\n\4\2\2\u009d")
        buf.write("\u009b\3\2\2\2\u009d\u009c\3\2\2\2\u009e\u00a1\3\2\2\2")
        buf.write("\u009f\u009d\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a2\3")
        buf.write("\2\2\2\u00a1\u009f\3\2\2\2\u00a2\u00a3\7$\2\2\u00a3\u00a4")
        buf.write("\b\4\2\2\u00a4\b\3\2\2\2\u00a5\u00a6\7v\2\2\u00a6\u00a7")
        buf.write("\7t\2\2\u00a7\u00a8\7w\2\2\u00a8\u00a9\7g\2\2\u00a9\n")
        buf.write("\3\2\2\2\u00aa\u00ab\7h\2\2\u00ab\u00ac\7c\2\2\u00ac\u00ad")
        buf.write("\7n\2\2\u00ad\u00ae\7u\2\2\u00ae\u00af\7g\2\2\u00af\f")
        buf.write("\3\2\2\2\u00b0\u00b1\7p\2\2\u00b1\u00b2\7w\2\2\u00b2\u00b3")
        buf.write("\7o\2\2\u00b3\u00b4\7d\2\2\u00b4\u00b5\7g\2\2\u00b5\u00b6")
        buf.write("\7t\2\2\u00b6\16\3\2\2\2\u00b7\u00b8\7d\2\2\u00b8\u00b9")
        buf.write("\7q\2\2\u00b9\u00ba\7q\2\2\u00ba\u00bb\7n\2\2\u00bb\20")
        buf.write("\3\2\2\2\u00bc\u00bd\7u\2\2\u00bd\u00be\7v\2\2\u00be\u00bf")
        buf.write("\7t\2\2\u00bf\u00c0\7k\2\2\u00c0\u00c1\7p\2\2\u00c1\u00c2")
        buf.write("\7i\2\2\u00c2\22\3\2\2\2\u00c3\u00c4\7t\2\2\u00c4\u00c5")
        buf.write("\7g\2\2\u00c5\u00c6\7v\2\2\u00c6\u00c7\7w\2\2\u00c7\u00c8")
        buf.write("\7t\2\2\u00c8\u00c9\7p\2\2\u00c9\24\3\2\2\2\u00ca\u00cb")
        buf.write("\7x\2\2\u00cb\u00cc\7c\2\2\u00cc\u00cd\7t\2\2\u00cd\26")
        buf.write("\3\2\2\2\u00ce\u00cf\7f\2\2\u00cf\u00d0\7{\2\2\u00d0\u00d1")
        buf.write("\7p\2\2\u00d1\u00d2\7c\2\2\u00d2\u00d3\7o\2\2\u00d3\u00d4")
        buf.write("\7k\2\2\u00d4\u00d5\7e\2\2\u00d5\30\3\2\2\2\u00d6\u00d7")
        buf.write("\7h\2\2\u00d7\u00d8\7w\2\2\u00d8\u00d9\7p\2\2\u00d9\u00da")
        buf.write("\7e\2\2\u00da\32\3\2\2\2\u00db\u00dc\7h\2\2\u00dc\u00dd")
        buf.write("\7q\2\2\u00dd\u00de\7t\2\2\u00de\34\3\2\2\2\u00df\u00e0")
        buf.write("\7w\2\2\u00e0\u00e1\7p\2\2\u00e1\u00e2\7v\2\2\u00e2\u00e3")
        buf.write("\7k\2\2\u00e3\u00e4\7n\2\2\u00e4\36\3\2\2\2\u00e5\u00e6")
        buf.write("\7d\2\2\u00e6\u00e7\7{\2\2\u00e7 \3\2\2\2\u00e8\u00e9")
        buf.write("\7d\2\2\u00e9\u00ea\7t\2\2\u00ea\u00eb\7g\2\2\u00eb\u00ec")
        buf.write("\7c\2\2\u00ec\u00ed\7m\2\2\u00ed\"\3\2\2\2\u00ee\u00ef")
        buf.write("\7e\2\2\u00ef\u00f0\7q\2\2\u00f0\u00f1\7p\2\2\u00f1\u00f2")
        buf.write("\7v\2\2\u00f2\u00f3\7k\2\2\u00f3\u00f4\7p\2\2\u00f4\u00f5")
        buf.write("\7w\2\2\u00f5\u00f6\7g\2\2\u00f6$\3\2\2\2\u00f7\u00f8")
        buf.write("\7k\2\2\u00f8\u00f9\7h\2\2\u00f9&\3\2\2\2\u00fa\u00fb")
        buf.write("\7g\2\2\u00fb\u00fc\7n\2\2\u00fc\u00fd\7u\2\2\u00fd\u00fe")
        buf.write("\7g\2\2\u00fe(\3\2\2\2\u00ff\u0100\7g\2\2\u0100\u0101")
        buf.write("\7n\2\2\u0101\u0102\7k\2\2\u0102\u0103\7h\2\2\u0103*\3")
        buf.write("\2\2\2\u0104\u0105\7d\2\2\u0105\u0106\7g\2\2\u0106\u0107")
        buf.write("\7i\2\2\u0107\u0108\7k\2\2\u0108\u0109\7p\2\2\u0109,\3")
        buf.write("\2\2\2\u010a\u010b\7g\2\2\u010b\u010c\7p\2\2\u010c\u010d")
        buf.write("\7f\2\2\u010d.\3\2\2\2\u010e\u010f\7p\2\2\u010f\u0110")
        buf.write("\7q\2\2\u0110\u0111\7v\2\2\u0111\60\3\2\2\2\u0112\u0113")
        buf.write("\7c\2\2\u0113\u0114\7p\2\2\u0114\u0115\7f\2\2\u0115\62")
        buf.write("\3\2\2\2\u0116\u0117\7q\2\2\u0117\u0118\7t\2\2\u0118\64")
        buf.write("\3\2\2\2\u0119\u011a\7-\2\2\u011a\66\3\2\2\2\u011b\u011c")
        buf.write("\7/\2\2\u011c8\3\2\2\2\u011d\u011e\7,\2\2\u011e:\3\2\2")
        buf.write("\2\u011f\u0120\7\61\2\2\u0120<\3\2\2\2\u0121\u0122\7\'")
        buf.write("\2\2\u0122>\3\2\2\2\u0123\u0124\7>\2\2\u0124\u0125\7/")
        buf.write("\2\2\u0125@\3\2\2\2\u0126\u0127\7?\2\2\u0127B\3\2\2\2")
        buf.write("\u0128\u0129\7#\2\2\u0129\u012a\7?\2\2\u012aD\3\2\2\2")
        buf.write("\u012b\u012c\7>\2\2\u012cF\3\2\2\2\u012d\u012e\7@\2\2")
        buf.write("\u012eH\3\2\2\2\u012f\u0130\7>\2\2\u0130\u0131\7?\2\2")
        buf.write("\u0131J\3\2\2\2\u0132\u0133\7@\2\2\u0133\u0134\7?\2\2")
        buf.write("\u0134L\3\2\2\2\u0135\u0136\7\60\2\2\u0136\u0137\7\60")
        buf.write("\2\2\u0137\u0138\7\60\2\2\u0138N\3\2\2\2\u0139\u013a\7")
        buf.write("?\2\2\u013a\u013b\7?\2\2\u013bP\3\2\2\2\u013c\u013d\7")
        buf.write(".\2\2\u013dR\3\2\2\2\u013e\u013f\7*\2\2\u013fT\3\2\2\2")
        buf.write("\u0140\u0141\7+\2\2\u0141V\3\2\2\2\u0142\u0143\7]\2\2")
        buf.write("\u0143X\3\2\2\2\u0144\u0145\7_\2\2\u0145Z\3\2\2\2\u0146")
        buf.write("\u014a\t\5\2\2\u0147\u0149\t\6\2\2\u0148\u0147\3\2\2\2")
        buf.write("\u0149\u014c\3\2\2\2\u014a\u0148\3\2\2\2\u014a\u014b\3")
        buf.write("\2\2\2\u014b\\\3\2\2\2\u014c\u014a\3\2\2\2\u014d\u014e")
        buf.write("\t\7\2\2\u014e^\3\2\2\2\u014f\u0150\7^\2\2\u0150\u0151")
        buf.write("\7d\2\2\u0151`\3\2\2\2\u0152\u0153\7^\2\2\u0153\u0154")
        buf.write("\7h\2\2\u0154b\3\2\2\2\u0155\u0156\7^\2\2\u0156\u0157")
        buf.write("\7t\2\2\u0157d\3\2\2\2\u0158\u0159\7^\2\2\u0159\u015a")
        buf.write("\7p\2\2\u015af\3\2\2\2\u015b\u015c\7^\2\2\u015c\u015d")
        buf.write("\7v\2\2\u015dh\3\2\2\2\u015e\u015f\7^\2\2\u015f\u0160")
        buf.write("\7)\2\2\u0160j\3\2\2\2\u0161\u0162\7^\2\2\u0162\u0163")
        buf.write("\7^\2\2\u0163l\3\2\2\2\u0164\u0165\7)\2\2\u0165\u0166")
        buf.write("\7$\2\2\u0166n\3\2\2\2\u0167\u0170\5_\60\2\u0168\u0170")
        buf.write("\5a\61\2\u0169\u0170\5c\62\2\u016a\u0170\5e\63\2\u016b")
        buf.write("\u0170\5g\64\2\u016c\u0170\5i\65\2\u016d\u0170\5k\66\2")
        buf.write("\u016e\u0170\5m\67\2\u016f\u0167\3\2\2\2\u016f\u0168\3")
        buf.write("\2\2\2\u016f\u0169\3\2\2\2\u016f\u016a\3\2\2\2\u016f\u016b")
        buf.write("\3\2\2\2\u016f\u016c\3\2\2\2\u016f\u016d\3\2\2\2\u016f")
        buf.write("\u016e\3\2\2\2\u0170p\3\2\2\2\u0171\u0172\7\f\2\2\u0172")
        buf.write("r\3\2\2\2\u0173\u0174\7%\2\2\u0174\u0178\7%\2\2\u0175")
        buf.write("\u0177\n\b\2\2\u0176\u0175\3\2\2\2\u0177\u017a\3\2\2\2")
        buf.write("\u0178\u0176\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u017d\3")
        buf.write("\2\2\2\u017a\u0178\3\2\2\2\u017b\u017e\7\2\2\3\u017c\u017e")
        buf.write("\3\2\2\2\u017d\u017b\3\2\2\2\u017d\u017c\3\2\2\2\u017e")
        buf.write("\u017f\3\2\2\2\u017f\u0180\b:\3\2\u0180t\3\2\2\2\u0181")
        buf.write("\u0183\t\t\2\2\u0182\u0181\3\2\2\2\u0183\u0184\3\2\2\2")
        buf.write("\u0184\u0182\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0186\3")
        buf.write("\2\2\2\u0186\u0187\b;\3\2\u0187v\3\2\2\2\u0188\u0189\13")
        buf.write("\2\2\2\u0189\u018a\b<\4\2\u018ax\3\2\2\2\u018b\u018f\7")
        buf.write("$\2\2\u018c\u018e\13\2\2\2\u018d\u018c\3\2\2\2\u018e\u0191")
        buf.write("\3\2\2\2\u018f\u0190\3\2\2\2\u018f\u018d\3\2\2\2\u0190")
        buf.write("\u0192\3\2\2\2\u0191\u018f\3\2\2\2\u0192\u0193\7^\2\2")
        buf.write("\u0193\u0194\n\n\2\2\u0194\u0195\3\2\2\2\u0195\u0196\b")
        buf.write("=\5\2\u0196z\3\2\2\2\u0197\u019c\7$\2\2\u0198\u019b\5")
        buf.write("o8\2\u0199\u019b\n\4\2\2\u019a\u0198\3\2\2\2\u019a\u0199")
        buf.write("\3\2\2\2\u019b\u019e\3\2\2\2\u019c\u019a\3\2\2\2\u019c")
        buf.write("\u019d\3\2\2\2\u019d\u01a0\3\2\2\2\u019e\u019c\3\2\2\2")
        buf.write("\u019f\u01a1\t\13\2\2\u01a0\u019f\3\2\2\2\u01a1\u01a2")
        buf.write("\3\2\2\2\u01a2\u01a3\b>\6\2\u01a3|\3\2\2\2\25\2\u0080")
        buf.write("\u0086\u0089\u008d\u0092\u0094\u0098\u009d\u009f\u014a")
        buf.write("\u016f\u0178\u017d\u0184\u018f\u019a\u019c\u01a0\7\3\4")
        buf.write("\2\b\2\2\3<\3\3=\4\3>\5")
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
            "'...'", "'=='", "','", "'('", "')'", "'['", "']'", "'\n'" ]

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
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise IllegalEscape(self.text[1:len(self.text)])
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise UncloseString(self.text[1:len(self.text)-1]) if(self.text[len(self.text)-1] == '\n') else UncloseString(self.text[1:len(self.text)])
     


