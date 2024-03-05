# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("\u0209\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\3\2\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4\u0090\n\4\3\5\3")
        buf.write("\5\3\5\3\5\5\5\u0096\n\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\5\b\u00a5\n\b\3\t\3\t\3\t\3\t\3")
        buf.write("\t\5\t\u00ac\n\t\3\n\3\n\3\n\3\n\5\n\u00b2\n\n\3\13\3")
        buf.write("\13\3\13\3\13\5\13\u00b8\n\13\3\f\3\f\5\f\u00bc\n\f\3")
        buf.write("\r\3\r\5\r\u00c0\n\r\3\r\3\r\3\r\5\r\u00c5\n\r\3\r\3\r")
        buf.write("\3\r\3\r\5\r\u00cb\n\r\3\16\3\16\3\17\3\17\3\17\3\20\3")
        buf.write("\20\3\20\3\20\3\20\5\20\u00d7\n\20\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\5\23\u00e4\n\23\3")
        buf.write("\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\5\27\u00f5\n\27\3\30\3\30\3\31\3")
        buf.write("\31\3\31\3\31\5\31\u00fd\n\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\5\32\u0108\n\32\3\33\3\33\3\33\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\35\3\35\5\35\u0114\n\35\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\3")
        buf.write("!\3!\3\"\3\"\3\"\3\"\5\"\u012a\n\"\3#\3#\3#\3#\5#\u0130")
        buf.write("\n#\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\5%\u013c\n%\3&\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\5)\u0150")
        buf.write("\n)\3)\3)\3*\3*\3*\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\5,\u0161")
        buf.write("\n,\3-\3-\3-\3-\5-\u0167\n-\3.\3.\3.\3.\3.\5.\u016e\n")
        buf.write(".\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3")
        buf.write("/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\5/\u018d\n/\3\60\3")
        buf.write("\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\7\60\u0198\n\60")
        buf.write("\f\60\16\60\u019b\13\60\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\61\7\61\u01a6\n\61\f\61\16\61\u01a9\13\61")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\7\62\u01b7\n\62\f\62\16\62\u01ba\13\62\3\63\3\63")
        buf.write("\3\63\5\63\u01bf\n\63\3\64\3\64\3\64\5\64\u01c4\n\64\3")
        buf.write("\65\3\65\5\65\u01c8\n\65\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\66\5\66\u01d1\n\66\3\67\3\67\3\67\38\38\58\u01d8\n")
        buf.write("8\39\39\39\39\3:\3:\3:\3;\3;\3;\3;\3;\5;\u01e6\n;\3<\3")
        buf.write("<\3<\3=\3=\3=\3=\3>\3>\3>\3>\5>\u01f3\n>\3?\3?\3?\3?\3")
        buf.write("?\5?\u01fa\n?\3@\3@\3@\3A\3A\3A\5A\u0202\nA\3B\3B\3B\5")
        buf.write("B\u0207\nB\3B\2\5^`bC\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfh")
        buf.write("jlnprtvxz|~\u0080\u0082\2\3\3\2\b\n\2\u0202\2\u0084\3")
        buf.write("\2\2\2\4\u0088\3\2\2\2\6\u008f\3\2\2\2\b\u0095\3\2\2\2")
        buf.write("\n\u0097\3\2\2\2\f\u009c\3\2\2\2\16\u00a4\3\2\2\2\20\u00ab")
        buf.write("\3\2\2\2\22\u00ad\3\2\2\2\24\u00b7\3\2\2\2\26\u00bb\3")
        buf.write("\2\2\2\30\u00ca\3\2\2\2\32\u00cc\3\2\2\2\34\u00ce\3\2")
        buf.write("\2\2\36\u00d1\3\2\2\2 \u00d8\3\2\2\2\"\u00dc\3\2\2\2$")
        buf.write("\u00e3\3\2\2\2&\u00e5\3\2\2\2(\u00e8\3\2\2\2*\u00ec\3")
        buf.write("\2\2\2,\u00f4\3\2\2\2.\u00f6\3\2\2\2\60\u00fc\3\2\2\2")
        buf.write("\62\u0107\3\2\2\2\64\u0109\3\2\2\2\66\u010c\3\2\2\28\u0113")
        buf.write("\3\2\2\2:\u0115\3\2\2\2<\u0118\3\2\2\2>\u011c\3\2\2\2")
        buf.write("@\u0121\3\2\2\2B\u0129\3\2\2\2D\u012f\3\2\2\2F\u0131\3")
        buf.write("\2\2\2H\u013b\3\2\2\2J\u013d\3\2\2\2L\u0146\3\2\2\2N\u0149")
        buf.write("\3\2\2\2P\u014c\3\2\2\2R\u0153\3\2\2\2T\u0156\3\2\2\2")
        buf.write("V\u0160\3\2\2\2X\u0166\3\2\2\2Z\u016d\3\2\2\2\\\u018c")
        buf.write("\3\2\2\2^\u018e\3\2\2\2`\u019c\3\2\2\2b\u01aa\3\2\2\2")
        buf.write("d\u01be\3\2\2\2f\u01c3\3\2\2\2h\u01c7\3\2\2\2j\u01d0\3")
        buf.write("\2\2\2l\u01d2\3\2\2\2n\u01d7\3\2\2\2p\u01d9\3\2\2\2r\u01dd")
        buf.write("\3\2\2\2t\u01e5\3\2\2\2v\u01e7\3\2\2\2x\u01ea\3\2\2\2")
        buf.write("z\u01f2\3\2\2\2|\u01f9\3\2\2\2~\u01fb\3\2\2\2\u0080\u0201")
        buf.write("\3\2\2\2\u0082\u0206\3\2\2\2\u0084\u0085\5\u0080A\2\u0085")
        buf.write("\u0086\5\4\3\2\u0086\u0087\7\2\2\3\u0087\3\3\2\2\2\u0088")
        buf.write("\u0089\5\b\5\2\u0089\u008a\5\6\4\2\u008a\5\3\2\2\2\u008b")
        buf.write("\u008c\5\b\5\2\u008c\u008d\5\6\4\2\u008d\u0090\3\2\2\2")
        buf.write("\u008e\u0090\3\2\2\2\u008f\u008b\3\2\2\2\u008f\u008e\3")
        buf.write("\2\2\2\u0090\7\3\2\2\2\u0091\u0096\5\n\6\2\u0092\u0093")
        buf.write("\5\30\r\2\u0093\u0094\5~@\2\u0094\u0096\3\2\2\2\u0095")
        buf.write("\u0091\3\2\2\2\u0095\u0092\3\2\2\2\u0096\t\3\2\2\2\u0097")
        buf.write("\u0098\7\16\2\2\u0098\u0099\7/\2\2\u0099\u009a\5\f\7\2")
        buf.write("\u009a\u009b\5\24\13\2\u009b\13\3\2\2\2\u009c\u009d\7")
        buf.write("+\2\2\u009d\u009e\5\16\b\2\u009e\u009f\7,\2\2\u009f\r")
        buf.write("\3\2\2\2\u00a0\u00a1\5\22\n\2\u00a1\u00a2\5\20\t\2\u00a2")
        buf.write("\u00a5\3\2\2\2\u00a3\u00a5\3\2\2\2\u00a4\u00a0\3\2\2\2")
        buf.write("\u00a4\u00a3\3\2\2\2\u00a5\17\3\2\2\2\u00a6\u00a7\7*\2")
        buf.write("\2\u00a7\u00a8\5\22\n\2\u00a8\u00a9\5\20\t\2\u00a9\u00ac")
        buf.write("\3\2\2\2\u00aa\u00ac\3\2\2\2\u00ab\u00a6\3\2\2\2\u00ab")
        buf.write("\u00aa\3\2\2\2\u00ac\21\3\2\2\2\u00ad\u00ae\5\32\16\2")
        buf.write("\u00ae\u00b1\7/\2\2\u00af\u00b2\5 \21\2\u00b0\u00b2\3")
        buf.write("\2\2\2\u00b1\u00af\3\2\2\2\u00b1\u00b0\3\2\2\2\u00b2\23")
        buf.write("\3\2\2\2\u00b3\u00b8\5~@\2\u00b4\u00b5\5\u0080A\2\u00b5")
        buf.write("\u00b6\5\26\f\2\u00b6\u00b8\3\2\2\2\u00b7\u00b3\3\2\2")
        buf.write("\2\u00b7\u00b4\3\2\2\2\u00b8\25\3\2\2\2\u00b9\u00bc\5")
        buf.write("P)\2\u00ba\u00bc\5T+\2\u00bb\u00b9\3\2\2\2\u00bb\u00ba")
        buf.write("\3\2\2\2\u00bc\27\3\2\2\2\u00bd\u00c0\5\32\16\2\u00be")
        buf.write("\u00c0\7\r\2\2\u00bf\u00bd\3\2\2\2\u00bf\u00be\3\2\2\2")
        buf.write("\u00c0\u00c1\3\2\2\2\u00c1\u00c4\7/\2\2\u00c2\u00c5\5")
        buf.write("\34\17\2\u00c3\u00c5\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c4")
        buf.write("\u00c3\3\2\2\2\u00c5\u00cb\3\2\2\2\u00c6\u00c7\7\f\2\2")
        buf.write("\u00c7\u00c8\7/\2\2\u00c8\u00cb\5\34\17\2\u00c9\u00cb")
        buf.write("\5\36\20\2\u00ca\u00bf\3\2\2\2\u00ca\u00c6\3\2\2\2\u00ca")
        buf.write("\u00c9\3\2\2\2\u00cb\31\3\2\2\2\u00cc\u00cd\t\2\2\2\u00cd")
        buf.write("\33\3\2\2\2\u00ce\u00cf\7!\2\2\u00cf\u00d0\5Z.\2\u00d0")
        buf.write("\35\3\2\2\2\u00d1\u00d2\5\32\16\2\u00d2\u00d3\7/\2\2\u00d3")
        buf.write("\u00d6\5 \21\2\u00d4\u00d7\5&\24\2\u00d5\u00d7\3\2\2\2")
        buf.write("\u00d6\u00d4\3\2\2\2\u00d6\u00d5\3\2\2\2\u00d7\37\3\2")
        buf.write("\2\2\u00d8\u00d9\7-\2\2\u00d9\u00da\5\"\22\2\u00da\u00db")
        buf.write("\7.\2\2\u00db!\3\2\2\2\u00dc\u00dd\7\3\2\2\u00dd\u00de")
        buf.write("\5$\23\2\u00de#\3\2\2\2\u00df\u00e0\7*\2\2\u00e0\u00e1")
        buf.write("\7\3\2\2\u00e1\u00e4\5$\23\2\u00e2\u00e4\3\2\2\2\u00e3")
        buf.write("\u00df\3\2\2\2\u00e3\u00e2\3\2\2\2\u00e4%\3\2\2\2\u00e5")
        buf.write("\u00e6\7!\2\2\u00e6\u00e7\5(\25\2\u00e7\'\3\2\2\2\u00e8")
        buf.write("\u00e9\7-\2\2\u00e9\u00ea\5*\26\2\u00ea\u00eb\7.\2\2\u00eb")
        buf.write(")\3\2\2\2\u00ec\u00ed\5.\30\2\u00ed\u00ee\5,\27\2\u00ee")
        buf.write("+\3\2\2\2\u00ef\u00f0\7*\2\2\u00f0\u00f1\5.\30\2\u00f1")
        buf.write("\u00f2\5,\27\2\u00f2\u00f5\3\2\2\2\u00f3\u00f5\3\2\2\2")
        buf.write("\u00f4\u00ef\3\2\2\2\u00f4\u00f3\3\2\2\2\u00f5-\3\2\2")
        buf.write("\2\u00f6\u00f7\5Z.\2\u00f7/\3\2\2\2\u00f8\u00fd\7\3\2")
        buf.write("\2\u00f9\u00fd\7\4\2\2\u00fa\u00fd\7\5\2\2\u00fb\u00fd")
        buf.write("\5(\25\2\u00fc\u00f8\3\2\2\2\u00fc\u00f9\3\2\2\2\u00fc")
        buf.write("\u00fa\3\2\2\2\u00fc\u00fb\3\2\2\2\u00fd\61\3\2\2\2\u00fe")
        buf.write("\u0108\5\64\33\2\u00ff\u0108\5\66\34\2\u0100\u0108\5<")
        buf.write("\37\2\u0101\u0108\5J&\2\u0102\u0108\5L\'\2\u0103\u0108")
        buf.write("\5N(\2\u0104\u0108\5P)\2\u0105\u0108\5R*\2\u0106\u0108")
        buf.write("\5T+\2\u0107\u00fe\3\2\2\2\u0107\u00ff\3\2\2\2\u0107\u0100")
        buf.write("\3\2\2\2\u0107\u0101\3\2\2\2\u0107\u0102\3\2\2\2\u0107")
        buf.write("\u0103\3\2\2\2\u0107\u0104\3\2\2\2\u0107\u0105\3\2\2\2")
        buf.write("\u0107\u0106\3\2\2\2\u0108\63\3\2\2\2\u0109\u010a\5\30")
        buf.write("\r\2\u010a\u010b\5~@\2\u010b\65\3\2\2\2\u010c\u010d\5")
        buf.write("8\35\2\u010d\u010e\7!\2\2\u010e\u010f\5Z.\2\u010f\u0110")
        buf.write("\5~@\2\u0110\67\3\2\2\2\u0111\u0114\7/\2\2\u0112\u0114")
        buf.write("\5:\36\2\u0113\u0111\3\2\2\2\u0113\u0112\3\2\2\2\u0114")
        buf.write("9\3\2\2\2\u0115\u0116\7/\2\2\u0116\u0117\5p9\2\u0117;")
        buf.write("\3\2\2\2\u0118\u0119\5> \2\u0119\u011a\5B\"\2\u011a\u011b")
        buf.write("\5H%\2\u011b=\3\2\2\2\u011c\u011d\7\24\2\2\u011d\u011e")
        buf.write("\5@!\2\u011e\u011f\5\u0080A\2\u011f\u0120\5\62\32\2\u0120")
        buf.write("?\3\2\2\2\u0121\u0122\7+\2\2\u0122\u0123\5Z.\2\u0123\u0124")
        buf.write("\7,\2\2\u0124A\3\2\2\2\u0125\u0126\5F$\2\u0126\u0127\5")
        buf.write("D#\2\u0127\u012a\3\2\2\2\u0128\u012a\3\2\2\2\u0129\u0125")
        buf.write("\3\2\2\2\u0129\u0128\3\2\2\2\u012aC\3\2\2\2\u012b\u012c")
        buf.write("\5F$\2\u012c\u012d\5D#\2\u012d\u0130\3\2\2\2\u012e\u0130")
        buf.write("\3\2\2\2\u012f\u012b\3\2\2\2\u012f\u012e\3\2\2\2\u0130")
        buf.write("E\3\2\2\2\u0131\u0132\7\26\2\2\u0132\u0133\5@!\2\u0133")
        buf.write("\u0134\5\u0080A\2\u0134\u0135\5\62\32\2\u0135G\3\2\2\2")
        buf.write("\u0136\u0137\7\25\2\2\u0137\u0138\5\u0080A\2\u0138\u0139")
        buf.write("\5\62\32\2\u0139\u013c\3\2\2\2\u013a\u013c\3\2\2\2\u013b")
        buf.write("\u0136\3\2\2\2\u013b\u013a\3\2\2\2\u013cI\3\2\2\2\u013d")
        buf.write("\u013e\7\17\2\2\u013e\u013f\7/\2\2\u013f\u0140\7\20\2")
        buf.write("\2\u0140\u0141\5Z.\2\u0141\u0142\7\21\2\2\u0142\u0143")
        buf.write("\5Z.\2\u0143\u0144\5\u0080A\2\u0144\u0145\5\62\32\2\u0145")
        buf.write("K\3\2\2\2\u0146\u0147\7\22\2\2\u0147\u0148\5~@\2\u0148")
        buf.write("M\3\2\2\2\u0149\u014a\7\23\2\2\u014a\u014b\5~@\2\u014b")
        buf.write("O\3\2\2\2\u014c\u014f\7\13\2\2\u014d\u0150\5Z.\2\u014e")
        buf.write("\u0150\3\2\2\2\u014f\u014d\3\2\2\2\u014f\u014e\3\2\2\2")
        buf.write("\u0150\u0151\3\2\2\2\u0151\u0152\5~@\2\u0152Q\3\2\2\2")
        buf.write("\u0153\u0154\5v<\2\u0154\u0155\5~@\2\u0155S\3\2\2\2\u0156")
        buf.write("\u0157\7\27\2\2\u0157\u0158\5~@\2\u0158\u0159\5V,\2\u0159")
        buf.write("\u015a\7\30\2\2\u015a\u015b\5~@\2\u015bU\3\2\2\2\u015c")
        buf.write("\u015d\5\62\32\2\u015d\u015e\5X-\2\u015e\u0161\3\2\2\2")
        buf.write("\u015f\u0161\3\2\2\2\u0160\u015c\3\2\2\2\u0160\u015f\3")
        buf.write("\2\2\2\u0161W\3\2\2\2\u0162\u0163\5\62\32\2\u0163\u0164")
        buf.write("\5X-\2\u0164\u0167\3\2\2\2\u0165\u0167\3\2\2\2\u0166\u0162")
        buf.write("\3\2\2\2\u0166\u0165\3\2\2\2\u0167Y\3\2\2\2\u0168\u0169")
        buf.write("\5\\/\2\u0169\u016a\7(\2\2\u016a\u016b\5\\/\2\u016b\u016e")
        buf.write("\3\2\2\2\u016c\u016e\5\\/\2\u016d\u0168\3\2\2\2\u016d")
        buf.write("\u016c\3\2\2\2\u016e[\3\2\2\2\u016f\u0170\5^\60\2\u0170")
        buf.write("\u0171\7\"\2\2\u0171\u0172\5^\60\2\u0172\u018d\3\2\2\2")
        buf.write("\u0173\u0174\5^\60\2\u0174\u0175\7)\2\2\u0175\u0176\5")
        buf.write("^\60\2\u0176\u018d\3\2\2\2\u0177\u0178\5^\60\2\u0178\u0179")
        buf.write("\7#\2\2\u0179\u017a\5^\60\2\u017a\u018d\3\2\2\2\u017b")
        buf.write("\u017c\5^\60\2\u017c\u017d\7$\2\2\u017d\u017e\5^\60\2")
        buf.write("\u017e\u018d\3\2\2\2\u017f\u0180\5^\60\2\u0180\u0181\7")
        buf.write("%\2\2\u0181\u0182\5^\60\2\u0182\u018d\3\2\2\2\u0183\u0184")
        buf.write("\5^\60\2\u0184\u0185\7&\2\2\u0185\u0186\5^\60\2\u0186")
        buf.write("\u018d\3\2\2\2\u0187\u0188\5^\60\2\u0188\u0189\7\'\2\2")
        buf.write("\u0189\u018a\5^\60\2\u018a\u018d\3\2\2\2\u018b\u018d\5")
        buf.write("^\60\2\u018c\u016f\3\2\2\2\u018c\u0173\3\2\2\2\u018c\u0177")
        buf.write("\3\2\2\2\u018c\u017b\3\2\2\2\u018c\u017f\3\2\2\2\u018c")
        buf.write("\u0183\3\2\2\2\u018c\u0187\3\2\2\2\u018c\u018b\3\2\2\2")
        buf.write("\u018d]\3\2\2\2\u018e\u018f\b\60\1\2\u018f\u0190\5`\61")
        buf.write("\2\u0190\u0199\3\2\2\2\u0191\u0192\f\5\2\2\u0192\u0193")
        buf.write("\7\32\2\2\u0193\u0198\5`\61\2\u0194\u0195\f\4\2\2\u0195")
        buf.write("\u0196\7\33\2\2\u0196\u0198\5`\61\2\u0197\u0191\3\2\2")
        buf.write("\2\u0197\u0194\3\2\2\2\u0198\u019b\3\2\2\2\u0199\u0197")
        buf.write("\3\2\2\2\u0199\u019a\3\2\2\2\u019a_\3\2\2\2\u019b\u0199")
        buf.write("\3\2\2\2\u019c\u019d\b\61\1\2\u019d\u019e\5b\62\2\u019e")
        buf.write("\u01a7\3\2\2\2\u019f\u01a0\f\5\2\2\u01a0\u01a1\7\34\2")
        buf.write("\2\u01a1\u01a6\5b\62\2\u01a2\u01a3\f\4\2\2\u01a3\u01a4")
        buf.write("\7\35\2\2\u01a4\u01a6\5b\62\2\u01a5\u019f\3\2\2\2\u01a5")
        buf.write("\u01a2\3\2\2\2\u01a6\u01a9\3\2\2\2\u01a7\u01a5\3\2\2\2")
        buf.write("\u01a7\u01a8\3\2\2\2\u01a8a\3\2\2\2\u01a9\u01a7\3\2\2")
        buf.write("\2\u01aa\u01ab\b\62\1\2\u01ab\u01ac\5d\63\2\u01ac\u01b8")
        buf.write("\3\2\2\2\u01ad\u01ae\f\6\2\2\u01ae\u01af\7\36\2\2\u01af")
        buf.write("\u01b7\5d\63\2\u01b0\u01b1\f\5\2\2\u01b1\u01b2\7\37\2")
        buf.write("\2\u01b2\u01b7\5d\63\2\u01b3\u01b4\f\4\2\2\u01b4\u01b5")
        buf.write("\7 \2\2\u01b5\u01b7\5d\63\2\u01b6\u01ad\3\2\2\2\u01b6")
        buf.write("\u01b0\3\2\2\2\u01b6\u01b3\3\2\2\2\u01b7\u01ba\3\2\2\2")
        buf.write("\u01b8\u01b6\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9c\3\2\2")
        buf.write("\2\u01ba\u01b8\3\2\2\2\u01bb\u01bc\7\31\2\2\u01bc\u01bf")
        buf.write("\5d\63\2\u01bd\u01bf\5f\64\2\u01be\u01bb\3\2\2\2\u01be")
        buf.write("\u01bd\3\2\2\2\u01bfe\3\2\2\2\u01c0\u01c1\7\35\2\2\u01c1")
        buf.write("\u01c4\5f\64\2\u01c2\u01c4\5h\65\2\u01c3\u01c0\3\2\2\2")
        buf.write("\u01c3\u01c2\3\2\2\2\u01c4g\3\2\2\2\u01c5\u01c8\5l\67")
        buf.write("\2\u01c6\u01c8\5j\66\2\u01c7\u01c5\3\2\2\2\u01c7\u01c6")
        buf.write("\3\2\2\2\u01c8i\3\2\2\2\u01c9\u01d1\5v<\2\u01ca\u01d1")
        buf.write("\7/\2\2\u01cb\u01d1\5\60\31\2\u01cc\u01cd\7+\2\2\u01cd")
        buf.write("\u01ce\5Z.\2\u01ce\u01cf\7,\2\2\u01cf\u01d1\3\2\2\2\u01d0")
        buf.write("\u01c9\3\2\2\2\u01d0\u01ca\3\2\2\2\u01d0\u01cb\3\2\2\2")
        buf.write("\u01d0\u01cc\3\2\2\2\u01d1k\3\2\2\2\u01d2\u01d3\5n8\2")
        buf.write("\u01d3\u01d4\5p9\2\u01d4m\3\2\2\2\u01d5\u01d8\7/\2\2\u01d6")
        buf.write("\u01d8\5v<\2\u01d7\u01d5\3\2\2\2\u01d7\u01d6\3\2\2\2\u01d8")
        buf.write("o\3\2\2\2\u01d9\u01da\7-\2\2\u01da\u01db\5r:\2\u01db\u01dc")
        buf.write("\7.\2\2\u01dcq\3\2\2\2\u01dd\u01de\5Z.\2\u01de\u01df\5")
        buf.write("t;\2\u01dfs\3\2\2\2\u01e0\u01e1\7*\2\2\u01e1\u01e2\5Z")
        buf.write(".\2\u01e2\u01e3\5t;\2\u01e3\u01e6\3\2\2\2\u01e4\u01e6")
        buf.write("\3\2\2\2\u01e5\u01e0\3\2\2\2\u01e5\u01e4\3\2\2\2\u01e6")
        buf.write("u\3\2\2\2\u01e7\u01e8\7/\2\2\u01e8\u01e9\5x=\2\u01e9w")
        buf.write("\3\2\2\2\u01ea\u01eb\7+\2\2\u01eb\u01ec\5z>\2\u01ec\u01ed")
        buf.write("\7,\2\2\u01edy\3\2\2\2\u01ee\u01ef\5Z.\2\u01ef\u01f0\5")
        buf.write("|?\2\u01f0\u01f3\3\2\2\2\u01f1\u01f3\3\2\2\2\u01f2\u01ee")
        buf.write("\3\2\2\2\u01f2\u01f1\3\2\2\2\u01f3{\3\2\2\2\u01f4\u01f5")
        buf.write("\7*\2\2\u01f5\u01f6\5Z.\2\u01f6\u01f7\5|?\2\u01f7\u01fa")
        buf.write("\3\2\2\2\u01f8\u01fa\3\2\2\2\u01f9\u01f4\3\2\2\2\u01f9")
        buf.write("\u01f8\3\2\2\2\u01fa}\3\2\2\2\u01fb\u01fc\7\60\2\2\u01fc")
        buf.write("\u01fd\5\u0082B\2\u01fd\177\3\2\2\2\u01fe\u01ff\7\60\2")
        buf.write("\2\u01ff\u0202\5\u0082B\2\u0200\u0202\3\2\2\2\u0201\u01fe")
        buf.write("\3\2\2\2\u0201\u0200\3\2\2\2\u0202\u0081\3\2\2\2\u0203")
        buf.write("\u0204\7\60\2\2\u0204\u0207\5\u0082B\2\u0205\u0207\3\2")
        buf.write("\2\2\u0206\u0203\3\2\2\2\u0206\u0205\3\2\2\2\u0207\u0083")
        buf.write("\3\2\2\2*\u008f\u0095\u00a4\u00ab\u00b1\u00b7\u00bb\u00bf")
        buf.write("\u00c4\u00ca\u00d6\u00e3\u00f4\u00fc\u0107\u0113\u0129")
        buf.write("\u012f\u013b\u014f\u0160\u0166\u016d\u018c\u0197\u0199")
        buf.write("\u01a5\u01a7\u01b6\u01b8\u01be\u01c3\u01c7\u01d0\u01d7")
        buf.write("\u01e5\u01f2\u01f9\u0201\u0206")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'true'", "'false'", "'number'", "'bool'", "'string'", 
                     "'return'", "'var'", "'dynamic'", "'func'", "'for'", 
                     "'until'", "'by'", "'break'", "'continue'", "'if'", 
                     "'else'", "'elif'", "'begin'", "'end'", "'not'", "'and'", 
                     "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", "'<-'", 
                     "'='", "'!='", "'<'", "'>'", "'<='", "'>='", "'...'", 
                     "'=='", "','", "'('", "')'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "NUMLIT", "BOOLLIT", "STRINGLIT", "TRUE", 
                      "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", "VAR", 
                      "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
                      "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", 
                      "NOT", "AND", "OR", "ADDOP", "SUBOP", "MULOP", "DIVOP", 
                      "MODOP", "ASSIGNOP", "EQUALOP", "DIFFOP", "SMALLEROP", 
                      "GREATEROP", "SEQOP", "GEQOP", "ELLIPOP", "DOUBLEEQOP", 
                      "COMMA", "LRB", "RRB", "LSQB", "RSQB", "IDENTIFIER", 
                      "LINEBREAK", "COMMENT", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_decllist = 1
    RULE_decllisttail = 2
    RULE_decl = 3
    RULE_func_decl = 4
    RULE_param_decl = 5
    RULE_paramlist = 6
    RULE_paramlisttail = 7
    RULE_param = 8
    RULE_func_decl_end = 9
    RULE_func_statement = 10
    RULE_var_decl = 11
    RULE_typ = 12
    RULE_initialization = 13
    RULE_array_decl = 14
    RULE_dimensionlist = 15
    RULE_numlitlist = 16
    RULE_numlitlisttail = 17
    RULE_array_init = 18
    RULE_arraylit = 19
    RULE_array_decl_elelist = 20
    RULE_array_decl_elelisttail = 21
    RULE_array_decl_ele = 22
    RULE_literals = 23
    RULE_statement = 24
    RULE_var_decl_statement = 25
    RULE_assign_statement = 26
    RULE_lhs = 27
    RULE_array_ele = 28
    RULE_if_statement = 29
    RULE_ifpart = 30
    RULE_exprclause = 31
    RULE_eliflist = 32
    RULE_eliflisttail = 33
    RULE_elifpart = 34
    RULE_elsepart = 35
    RULE_for_statement = 36
    RULE_break_statement = 37
    RULE_continue_statement = 38
    RULE_return_statement = 39
    RULE_function_call_statement = 40
    RULE_block_statement = 41
    RULE_statementlist = 42
    RULE_statementlisttail = 43
    RULE_expr = 44
    RULE_lv8_expr = 45
    RULE_lv7_expr = 46
    RULE_lv6_expr = 47
    RULE_lv5_expr = 48
    RULE_lv4_expr = 49
    RULE_lv3_expr = 50
    RULE_lv2_expr = 51
    RULE_lv1_expr = 52
    RULE_array_indexing = 53
    RULE_array_expression = 54
    RULE_index_operator = 55
    RULE_exprlist = 56
    RULE_exprlisttail = 57
    RULE_function_call = 58
    RULE_args = 59
    RULE_argslist = 60
    RULE_argslisttail = 61
    RULE_linebreaklist = 62
    RULE_nullablelinebreaklist = 63
    RULE_linebreaklisttail = 64

    ruleNames =  [ "program", "decllist", "decllisttail", "decl", "func_decl", 
                   "param_decl", "paramlist", "paramlisttail", "param", 
                   "func_decl_end", "func_statement", "var_decl", "typ", 
                   "initialization", "array_decl", "dimensionlist", "numlitlist", 
                   "numlitlisttail", "array_init", "arraylit", "array_decl_elelist", 
                   "array_decl_elelisttail", "array_decl_ele", "literals", 
                   "statement", "var_decl_statement", "assign_statement", 
                   "lhs", "array_ele", "if_statement", "ifpart", "exprclause", 
                   "eliflist", "eliflisttail", "elifpart", "elsepart", "for_statement", 
                   "break_statement", "continue_statement", "return_statement", 
                   "function_call_statement", "block_statement", "statementlist", 
                   "statementlisttail", "expr", "lv8_expr", "lv7_expr", 
                   "lv6_expr", "lv5_expr", "lv4_expr", "lv3_expr", "lv2_expr", 
                   "lv1_expr", "array_indexing", "array_expression", "index_operator", 
                   "exprlist", "exprlisttail", "function_call", "args", 
                   "argslist", "argslisttail", "linebreaklist", "nullablelinebreaklist", 
                   "linebreaklisttail" ]

    EOF = Token.EOF
    NUMLIT=1
    BOOLLIT=2
    STRINGLIT=3
    TRUE=4
    FALSE=5
    NUMBER=6
    BOOL=7
    STRING=8
    RETURN=9
    VAR=10
    DYNAMIC=11
    FUNC=12
    FOR=13
    UNTIL=14
    BY=15
    BREAK=16
    CONTINUE=17
    IF=18
    ELSE=19
    ELIF=20
    BEGIN=21
    END=22
    NOT=23
    AND=24
    OR=25
    ADDOP=26
    SUBOP=27
    MULOP=28
    DIVOP=29
    MODOP=30
    ASSIGNOP=31
    EQUALOP=32
    DIFFOP=33
    SMALLEROP=34
    GREATEROP=35
    SEQOP=36
    GEQOP=37
    ELLIPOP=38
    DOUBLEEQOP=39
    COMMA=40
    LRB=41
    RRB=42
    LSQB=43
    RSQB=44
    IDENTIFIER=45
    LINEBREAK=46
    COMMENT=47
    WS=48
    ERROR_CHAR=49
    ILLEGAL_ESCAPE=50
    UNCLOSE_STRING=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nullablelinebreaklist(self):
            return self.getTypedRuleContext(ZCodeParser.NullablelinebreaklistContext,0)


        def decllist(self):
            return self.getTypedRuleContext(ZCodeParser.DecllistContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.nullablelinebreaklist()
            self.state = 131
            self.decllist()
            self.state = 132
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(ZCodeParser.DeclContext,0)


        def decllisttail(self):
            return self.getTypedRuleContext(ZCodeParser.DecllisttailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decllist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecllist" ):
                return visitor.visitDecllist(self)
            else:
                return visitor.visitChildren(self)




    def decllist(self):

        localctx = ZCodeParser.DecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decllist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.decl()
            self.state = 135
            self.decllisttail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecllisttailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(ZCodeParser.DeclContext,0)


        def decllisttail(self):
            return self.getTypedRuleContext(ZCodeParser.DecllisttailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decllisttail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecllisttail" ):
                return visitor.visitDecllisttail(self)
            else:
                return visitor.visitChildren(self)




    def decllisttail(self):

        localctx = ZCodeParser.DecllisttailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decllisttail)
        try:
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.decl()
                self.state = 138
                self.decllisttail()
                pass
            elif token in [ZCodeParser.EOF]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Func_declContext,0)


        def var_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Var_declContext,0)


        def linebreaklist(self):
            return self.getTypedRuleContext(ZCodeParser.LinebreaklistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_decl)
        try:
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.func_decl()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.var_decl()
                self.state = 145
                self.linebreaklist()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def param_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Param_declContext,0)


        def func_decl_end(self):
            return self.getTypedRuleContext(ZCodeParser.Func_decl_endContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = ZCodeParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(ZCodeParser.FUNC)
            self.state = 150
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 151
            self.param_decl()
            self.state = 152
            self.func_decl_end()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LRB(self):
            return self.getToken(ZCodeParser.LRB, 0)

        def paramlist(self):
            return self.getTypedRuleContext(ZCodeParser.ParamlistContext,0)


        def RRB(self):
            return self.getToken(ZCodeParser.RRB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_param_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_decl" ):
                return visitor.visitParam_decl(self)
            else:
                return visitor.visitChildren(self)




    def param_decl(self):

        localctx = ZCodeParser.Param_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_param_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(ZCodeParser.LRB)
            self.state = 155
            self.paramlist()
            self.state = 156
            self.match(ZCodeParser.RRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(ZCodeParser.ParamContext,0)


        def paramlisttail(self):
            return self.getTypedRuleContext(ZCodeParser.ParamlisttailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = ZCodeParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_paramlist)
        try:
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.param()
                self.state = 159
                self.paramlisttail()
                pass
            elif token in [ZCodeParser.RRB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlisttailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def param(self):
            return self.getTypedRuleContext(ZCodeParser.ParamContext,0)


        def paramlisttail(self):
            return self.getTypedRuleContext(ZCodeParser.ParamlisttailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramlisttail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlisttail" ):
                return visitor.visitParamlisttail(self)
            else:
                return visitor.visitChildren(self)




    def paramlisttail(self):

        localctx = ZCodeParser.ParamlisttailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_paramlisttail)
        try:
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.match(ZCodeParser.COMMA)
                self.state = 165
                self.param()
                self.state = 166
                self.paramlisttail()
                pass
            elif token in [ZCodeParser.RRB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(ZCodeParser.TypContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def dimensionlist(self):
            return self.getTypedRuleContext(ZCodeParser.DimensionlistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = ZCodeParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.typ()
            self.state = 172
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LSQB]:
                self.state = 173
                self.dimensionlist()
                pass
            elif token in [ZCodeParser.COMMA, ZCodeParser.RRB]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_decl_endContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def linebreaklist(self):
            return self.getTypedRuleContext(ZCodeParser.LinebreaklistContext,0)


        def nullablelinebreaklist(self):
            return self.getTypedRuleContext(ZCodeParser.NullablelinebreaklistContext,0)


        def func_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Func_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_decl_end

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl_end" ):
                return visitor.visitFunc_decl_end(self)
            else:
                return visitor.visitChildren(self)




    def func_decl_end(self):

        localctx = ZCodeParser.Func_decl_endContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_func_decl_end)
        try:
            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.linebreaklist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.nullablelinebreaklist()
                self.state = 179
                self.func_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def return_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statementContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_statement" ):
                return visitor.visitFunc_statement(self)
            else:
                return visitor.visitChildren(self)




    def func_statement(self):

        localctx = ZCodeParser.Func_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_func_statement)
        try:
            self.state = 185
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.return_statement()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.block_statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def typ(self):
            return self.getTypedRuleContext(ZCodeParser.TypContext,0)


        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def initialization(self):
            return self.getTypedRuleContext(ZCodeParser.InitializationContext,0)


        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def array_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Array_declContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = ZCodeParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_var_decl)
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                    self.state = 187
                    self.typ()
                    pass
                elif token in [ZCodeParser.DYNAMIC]:
                    self.state = 188
                    self.match(ZCodeParser.DYNAMIC)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 191
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 194
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.ASSIGNOP]:
                    self.state = 192
                    self.initialization()
                    pass
                elif token in [ZCodeParser.LINEBREAK]:
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 196
                self.match(ZCodeParser.VAR)
                self.state = 197
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 198
                self.initialization()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 199
                self.array_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = ZCodeParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitializationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGNOP(self):
            return self.getToken(ZCodeParser.ASSIGNOP, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_initialization

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitialization" ):
                return visitor.visitInitialization(self)
            else:
                return visitor.visitChildren(self)




    def initialization(self):

        localctx = ZCodeParser.InitializationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_initialization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(ZCodeParser.ASSIGNOP)
            self.state = 205
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(ZCodeParser.TypContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def dimensionlist(self):
            return self.getTypedRuleContext(ZCodeParser.DimensionlistContext,0)


        def array_init(self):
            return self.getTypedRuleContext(ZCodeParser.Array_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_decl" ):
                return visitor.visitArray_decl(self)
            else:
                return visitor.visitChildren(self)




    def array_decl(self):

        localctx = ZCodeParser.Array_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_array_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.typ()
            self.state = 208
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 209
            self.dimensionlist()
            self.state = 212
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ASSIGNOP]:
                self.state = 210
                self.array_init()
                pass
            elif token in [ZCodeParser.LINEBREAK]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSQB(self):
            return self.getToken(ZCodeParser.LSQB, 0)

        def numlitlist(self):
            return self.getTypedRuleContext(ZCodeParser.NumlitlistContext,0)


        def RSQB(self):
            return self.getToken(ZCodeParser.RSQB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_dimensionlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimensionlist" ):
                return visitor.visitDimensionlist(self)
            else:
                return visitor.visitChildren(self)




    def dimensionlist(self):

        localctx = ZCodeParser.DimensionlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_dimensionlist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(ZCodeParser.LSQB)
            self.state = 215
            self.numlitlist()
            self.state = 216
            self.match(ZCodeParser.RSQB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumlitlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMLIT(self):
            return self.getToken(ZCodeParser.NUMLIT, 0)

        def numlitlisttail(self):
            return self.getTypedRuleContext(ZCodeParser.NumlitlisttailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_numlitlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumlitlist" ):
                return visitor.visitNumlitlist(self)
            else:
                return visitor.visitChildren(self)




    def numlitlist(self):

        localctx = ZCodeParser.NumlitlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_numlitlist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(ZCodeParser.NUMLIT)
            self.state = 219
            self.numlitlisttail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumlitlisttailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def NUMLIT(self):
            return self.getToken(ZCodeParser.NUMLIT, 0)

        def numlitlisttail(self):
            return self.getTypedRuleContext(ZCodeParser.NumlitlisttailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_numlitlisttail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumlitlisttail" ):
                return visitor.visitNumlitlisttail(self)
            else:
                return visitor.visitChildren(self)




    def numlitlisttail(self):

        localctx = ZCodeParser.NumlitlisttailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_numlitlisttail)
        try:
            self.state = 225
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.match(ZCodeParser.COMMA)
                self.state = 222
                self.match(ZCodeParser.NUMLIT)
                self.state = 223
                self.numlitlisttail()
                pass
            elif token in [ZCodeParser.RSQB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGNOP(self):
            return self.getToken(ZCodeParser.ASSIGNOP, 0)

        def arraylit(self):
            return self.getTypedRuleContext(ZCodeParser.ArraylitContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_init" ):
                return visitor.visitArray_init(self)
            else:
                return visitor.visitChildren(self)




    def array_init(self):

        localctx = ZCodeParser.Array_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_array_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(ZCodeParser.ASSIGNOP)
            self.state = 228
            self.arraylit()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraylitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSQB(self):
            return self.getToken(ZCodeParser.LSQB, 0)

        def array_decl_elelist(self):
            return self.getTypedRuleContext(ZCodeParser.Array_decl_elelistContext,0)


        def RSQB(self):
            return self.getToken(ZCodeParser.RSQB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arraylit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraylit" ):
                return visitor.visitArraylit(self)
            else:
                return visitor.visitChildren(self)




    def arraylit(self):

        localctx = ZCodeParser.ArraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_arraylit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(ZCodeParser.LSQB)
            self.state = 231
            self.array_decl_elelist()
            self.state = 232
            self.match(ZCodeParser.RSQB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_decl_elelistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_decl_ele(self):
            return self.getTypedRuleContext(ZCodeParser.Array_decl_eleContext,0)


        def array_decl_elelisttail(self):
            return self.getTypedRuleContext(ZCodeParser.Array_decl_elelisttailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_decl_elelist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_decl_elelist" ):
                return visitor.visitArray_decl_elelist(self)
            else:
                return visitor.visitChildren(self)




    def array_decl_elelist(self):

        localctx = ZCodeParser.Array_decl_elelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_array_decl_elelist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.array_decl_ele()
            self.state = 235
            self.array_decl_elelisttail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_decl_elelisttailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def array_decl_ele(self):
            return self.getTypedRuleContext(ZCodeParser.Array_decl_eleContext,0)


        def array_decl_elelisttail(self):
            return self.getTypedRuleContext(ZCodeParser.Array_decl_elelisttailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_decl_elelisttail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_decl_elelisttail" ):
                return visitor.visitArray_decl_elelisttail(self)
            else:
                return visitor.visitChildren(self)




    def array_decl_elelisttail(self):

        localctx = ZCodeParser.Array_decl_elelisttailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_array_decl_elelisttail)
        try:
            self.state = 242
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.match(ZCodeParser.COMMA)
                self.state = 238
                self.array_decl_ele()
                self.state = 239
                self.array_decl_elelisttail()
                pass
            elif token in [ZCodeParser.RSQB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_decl_eleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_decl_ele

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_decl_ele" ):
                return visitor.visitArray_decl_ele(self)
            else:
                return visitor.visitChildren(self)




    def array_decl_ele(self):

        localctx = ZCodeParser.Array_decl_eleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_array_decl_ele)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMLIT(self):
            return self.getToken(ZCodeParser.NUMLIT, 0)

        def BOOLLIT(self):
            return self.getToken(ZCodeParser.BOOLLIT, 0)

        def STRINGLIT(self):
            return self.getToken(ZCodeParser.STRINGLIT, 0)

        def arraylit(self):
            return self.getTypedRuleContext(ZCodeParser.ArraylitContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_literals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)




    def literals(self):

        localctx = ZCodeParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_literals)
        try:
            self.state = 250
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.match(ZCodeParser.NUMLIT)
                pass
            elif token in [ZCodeParser.BOOLLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.match(ZCodeParser.BOOLLIT)
                pass
            elif token in [ZCodeParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 248
                self.match(ZCodeParser.STRINGLIT)
                pass
            elif token in [ZCodeParser.LSQB]:
                self.enterOuterAlt(localctx, 4)
                self.state = 249
                self.arraylit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Var_decl_statementContext,0)


        def assign_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Assign_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(ZCodeParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(ZCodeParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Continue_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statementContext,0)


        def function_call_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Function_call_statementContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_statement)
        try:
            self.state = 261
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.var_decl_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
                self.assign_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 254
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 255
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 256
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 257
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 258
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 259
                self.function_call_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 260
                self.block_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Var_declContext,0)


        def linebreaklist(self):
            return self.getTypedRuleContext(ZCodeParser.LinebreaklistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_var_decl_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl_statement" ):
                return visitor.visitVar_decl_statement(self)
            else:
                return visitor.visitChildren(self)




    def var_decl_statement(self):

        localctx = ZCodeParser.Var_decl_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_var_decl_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.var_decl()
            self.state = 264
            self.linebreaklist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(ZCodeParser.LhsContext,0)


        def ASSIGNOP(self):
            return self.getToken(ZCodeParser.ASSIGNOP, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def linebreaklist(self):
            return self.getTypedRuleContext(ZCodeParser.LinebreaklistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assign_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_statement" ):
                return visitor.visitAssign_statement(self)
            else:
                return visitor.visitChildren(self)




    def assign_statement(self):

        localctx = ZCodeParser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.lhs()
            self.state = 267
            self.match(ZCodeParser.ASSIGNOP)
            self.state = 268
            self.expr()
            self.state = 269
            self.linebreaklist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def array_ele(self):
            return self.getTypedRuleContext(ZCodeParser.Array_eleContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_lhs)
        try:
            self.state = 273
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 272
                self.array_ele()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_eleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def index_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_ele

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_ele" ):
                return visitor.visitArray_ele(self)
            else:
                return visitor.visitChildren(self)




    def array_ele(self):

        localctx = ZCodeParser.Array_eleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_array_ele)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 276
            self.index_operator()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifpart(self):
            return self.getTypedRuleContext(ZCodeParser.IfpartContext,0)


        def eliflist(self):
            return self.getTypedRuleContext(ZCodeParser.EliflistContext,0)


        def elsepart(self):
            return self.getTypedRuleContext(ZCodeParser.ElsepartContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = ZCodeParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.ifpart()
            self.state = 279
            self.eliflist()
            self.state = 280
            self.elsepart()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfpartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def exprclause(self):
            return self.getTypedRuleContext(ZCodeParser.ExprclauseContext,0)


        def nullablelinebreaklist(self):
            return self.getTypedRuleContext(ZCodeParser.NullablelinebreaklistContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_ifpart

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfpart" ):
                return visitor.visitIfpart(self)
            else:
                return visitor.visitChildren(self)




    def ifpart(self):

        localctx = ZCodeParser.IfpartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_ifpart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(ZCodeParser.IF)
            self.state = 283
            self.exprclause()
            self.state = 284
            self.nullablelinebreaklist()
            self.state = 285
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprclauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LRB(self):
            return self.getToken(ZCodeParser.LRB, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RRB(self):
            return self.getToken(ZCodeParser.RRB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exprclause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprclause" ):
                return visitor.visitExprclause(self)
            else:
                return visitor.visitChildren(self)




    def exprclause(self):

        localctx = ZCodeParser.ExprclauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_exprclause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(ZCodeParser.LRB)
            self.state = 288
            self.expr()
            self.state = 289
            self.match(ZCodeParser.RRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EliflistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elifpart(self):
            return self.getTypedRuleContext(ZCodeParser.ElifpartContext,0)


        def eliflisttail(self):
            return self.getTypedRuleContext(ZCodeParser.EliflisttailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_eliflist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEliflist" ):
                return visitor.visitEliflist(self)
            else:
                return visitor.visitChildren(self)




    def eliflist(self):

        localctx = ZCodeParser.EliflistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_eliflist)
        try:
            self.state = 295
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.elifpart()
                self.state = 292
                self.eliflisttail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EliflisttailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elifpart(self):
            return self.getTypedRuleContext(ZCodeParser.ElifpartContext,0)


        def eliflisttail(self):
            return self.getTypedRuleContext(ZCodeParser.EliflisttailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_eliflisttail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEliflisttail" ):
                return visitor.visitEliflisttail(self)
            else:
                return visitor.visitChildren(self)




    def eliflisttail(self):

        localctx = ZCodeParser.EliflisttailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_eliflisttail)
        try:
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self.elifpart()
                self.state = 298
                self.eliflisttail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifpartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def exprclause(self):
            return self.getTypedRuleContext(ZCodeParser.ExprclauseContext,0)


        def nullablelinebreaklist(self):
            return self.getTypedRuleContext(ZCodeParser.NullablelinebreaklistContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elifpart

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifpart" ):
                return visitor.visitElifpart(self)
            else:
                return visitor.visitChildren(self)




    def elifpart(self):

        localctx = ZCodeParser.ElifpartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_elifpart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(ZCodeParser.ELIF)
            self.state = 304
            self.exprclause()
            self.state = 305
            self.nullablelinebreaklist()
            self.state = 306
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElsepartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def nullablelinebreaklist(self):
            return self.getTypedRuleContext(ZCodeParser.NullablelinebreaklistContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elsepart

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElsepart" ):
                return visitor.visitElsepart(self)
            else:
                return visitor.visitChildren(self)




    def elsepart(self):

        localctx = ZCodeParser.ElsepartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_elsepart)
        try:
            self.state = 313
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 308
                self.match(ZCodeParser.ELSE)
                self.state = 309
                self.nullablelinebreaklist()
                self.state = 310
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def nullablelinebreaklist(self):
            return self.getTypedRuleContext(ZCodeParser.NullablelinebreaklistContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = ZCodeParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(ZCodeParser.FOR)
            self.state = 316
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 317
            self.match(ZCodeParser.UNTIL)
            self.state = 318
            self.expr()
            self.state = 319
            self.match(ZCodeParser.BY)
            self.state = 320
            self.expr()
            self.state = 321
            self.nullablelinebreaklist()
            self.state = 322
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def linebreaklist(self):
            return self.getTypedRuleContext(ZCodeParser.LinebreaklistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = ZCodeParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(ZCodeParser.BREAK)
            self.state = 325
            self.linebreaklist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def linebreaklist(self):
            return self.getTypedRuleContext(ZCodeParser.LinebreaklistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = ZCodeParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.match(ZCodeParser.CONTINUE)
            self.state = 328
            self.linebreaklist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def linebreaklist(self):
            return self.getTypedRuleContext(ZCodeParser.LinebreaklistContext,0)


        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = ZCodeParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.match(ZCodeParser.RETURN)
            self.state = 333
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMLIT, ZCodeParser.BOOLLIT, ZCodeParser.STRINGLIT, ZCodeParser.NOT, ZCodeParser.SUBOP, ZCodeParser.LRB, ZCodeParser.LSQB, ZCodeParser.IDENTIFIER]:
                self.state = 331
                self.expr()
                pass
            elif token in [ZCodeParser.LINEBREAK]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 335
            self.linebreaklist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_call(self):
            return self.getTypedRuleContext(ZCodeParser.Function_callContext,0)


        def linebreaklist(self):
            return self.getTypedRuleContext(ZCodeParser.LinebreaklistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call_statement" ):
                return visitor.visitFunction_call_statement(self)
            else:
                return visitor.visitChildren(self)




    def function_call_statement(self):

        localctx = ZCodeParser.Function_call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_function_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.function_call()
            self.state = 338
            self.linebreaklist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def linebreaklist(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.LinebreaklistContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.LinebreaklistContext,i)


        def statementlist(self):
            return self.getTypedRuleContext(ZCodeParser.StatementlistContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_block_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = ZCodeParser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_block_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.match(ZCodeParser.BEGIN)
            self.state = 341
            self.linebreaklist()
            self.state = 342
            self.statementlist()
            self.state = 343
            self.match(ZCodeParser.END)
            self.state = 344
            self.linebreaklist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def statementlisttail(self):
            return self.getTypedRuleContext(ZCodeParser.StatementlisttailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statementlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementlist" ):
                return visitor.visitStatementlist(self)
            else:
                return visitor.visitChildren(self)




    def statementlist(self):

        localctx = ZCodeParser.StatementlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_statementlist)
        try:
            self.state = 350
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                self.statement()
                self.state = 347
                self.statementlisttail()
                pass
            elif token in [ZCodeParser.END]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementlisttailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def statementlisttail(self):
            return self.getTypedRuleContext(ZCodeParser.StatementlisttailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statementlisttail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementlisttail" ):
                return visitor.visitStatementlisttail(self)
            else:
                return visitor.visitChildren(self)




    def statementlisttail(self):

        localctx = ZCodeParser.StatementlisttailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_statementlisttail)
        try:
            self.state = 356
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 352
                self.statement()
                self.state = 353
                self.statementlisttail()
                pass
            elif token in [ZCodeParser.END]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lv8_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Lv8_exprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Lv8_exprContext,i)


        def ELLIPOP(self):
            return self.getToken(ZCodeParser.ELLIPOP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ZCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_expr)
        try:
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 358
                self.lv8_expr()
                self.state = 359
                self.match(ZCodeParser.ELLIPOP)
                self.state = 360
                self.lv8_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 362
                self.lv8_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lv8_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lv7_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Lv7_exprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Lv7_exprContext,i)


        def EQUALOP(self):
            return self.getToken(ZCodeParser.EQUALOP, 0)

        def DOUBLEEQOP(self):
            return self.getToken(ZCodeParser.DOUBLEEQOP, 0)

        def DIFFOP(self):
            return self.getToken(ZCodeParser.DIFFOP, 0)

        def SMALLEROP(self):
            return self.getToken(ZCodeParser.SMALLEROP, 0)

        def GREATEROP(self):
            return self.getToken(ZCodeParser.GREATEROP, 0)

        def SEQOP(self):
            return self.getToken(ZCodeParser.SEQOP, 0)

        def GEQOP(self):
            return self.getToken(ZCodeParser.GEQOP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_lv8_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLv8_expr" ):
                return visitor.visitLv8_expr(self)
            else:
                return visitor.visitChildren(self)




    def lv8_expr(self):

        localctx = ZCodeParser.Lv8_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_lv8_expr)
        try:
            self.state = 394
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 365
                self.lv7_expr(0)
                self.state = 366
                self.match(ZCodeParser.EQUALOP)
                self.state = 367
                self.lv7_expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 369
                self.lv7_expr(0)
                self.state = 370
                self.match(ZCodeParser.DOUBLEEQOP)
                self.state = 371
                self.lv7_expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 373
                self.lv7_expr(0)
                self.state = 374
                self.match(ZCodeParser.DIFFOP)
                self.state = 375
                self.lv7_expr(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 377
                self.lv7_expr(0)
                self.state = 378
                self.match(ZCodeParser.SMALLEROP)
                self.state = 379
                self.lv7_expr(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 381
                self.lv7_expr(0)
                self.state = 382
                self.match(ZCodeParser.GREATEROP)
                self.state = 383
                self.lv7_expr(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 385
                self.lv7_expr(0)
                self.state = 386
                self.match(ZCodeParser.SEQOP)
                self.state = 387
                self.lv7_expr(0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 389
                self.lv7_expr(0)
                self.state = 390
                self.match(ZCodeParser.GEQOP)
                self.state = 391
                self.lv7_expr(0)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 393
                self.lv7_expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lv7_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lv6_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Lv6_exprContext,0)


        def lv7_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Lv7_exprContext,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_lv7_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLv7_expr" ):
                return visitor.visitLv7_expr(self)
            else:
                return visitor.visitChildren(self)



    def lv7_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Lv7_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_lv7_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.lv6_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 407
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 405
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.Lv7_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lv7_expr)
                        self.state = 399
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 400
                        self.match(ZCodeParser.AND)
                        self.state = 401
                        self.lv6_expr(0)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.Lv7_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lv7_expr)
                        self.state = 402
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 403
                        self.match(ZCodeParser.OR)
                        self.state = 404
                        self.lv6_expr(0)
                        pass

             
                self.state = 409
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Lv6_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lv5_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Lv5_exprContext,0)


        def lv6_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Lv6_exprContext,0)


        def ADDOP(self):
            return self.getToken(ZCodeParser.ADDOP, 0)

        def SUBOP(self):
            return self.getToken(ZCodeParser.SUBOP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_lv6_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLv6_expr" ):
                return visitor.visitLv6_expr(self)
            else:
                return visitor.visitChildren(self)



    def lv6_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Lv6_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_lv6_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.lv5_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 421
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 419
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.Lv6_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lv6_expr)
                        self.state = 413
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 414
                        self.match(ZCodeParser.ADDOP)
                        self.state = 415
                        self.lv5_expr(0)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.Lv6_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lv6_expr)
                        self.state = 416
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 417
                        self.match(ZCodeParser.SUBOP)
                        self.state = 418
                        self.lv5_expr(0)
                        pass

             
                self.state = 423
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Lv5_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lv4_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Lv4_exprContext,0)


        def lv5_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Lv5_exprContext,0)


        def MULOP(self):
            return self.getToken(ZCodeParser.MULOP, 0)

        def DIVOP(self):
            return self.getToken(ZCodeParser.DIVOP, 0)

        def MODOP(self):
            return self.getToken(ZCodeParser.MODOP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_lv5_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLv5_expr" ):
                return visitor.visitLv5_expr(self)
            else:
                return visitor.visitChildren(self)



    def lv5_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Lv5_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 96
        self.enterRecursionRule(localctx, 96, self.RULE_lv5_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self.lv4_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 438
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 436
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.Lv5_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lv5_expr)
                        self.state = 427
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 428
                        self.match(ZCodeParser.MULOP)
                        self.state = 429
                        self.lv4_expr()
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.Lv5_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lv5_expr)
                        self.state = 430
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 431
                        self.match(ZCodeParser.DIVOP)
                        self.state = 432
                        self.lv4_expr()
                        pass

                    elif la_ == 3:
                        localctx = ZCodeParser.Lv5_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lv5_expr)
                        self.state = 433
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 434
                        self.match(ZCodeParser.MODOP)
                        self.state = 435
                        self.lv4_expr()
                        pass

             
                self.state = 440
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Lv4_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def lv4_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Lv4_exprContext,0)


        def lv3_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Lv3_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_lv4_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLv4_expr" ):
                return visitor.visitLv4_expr(self)
            else:
                return visitor.visitChildren(self)




    def lv4_expr(self):

        localctx = ZCodeParser.Lv4_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_lv4_expr)
        try:
            self.state = 444
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 441
                self.match(ZCodeParser.NOT)
                self.state = 442
                self.lv4_expr()
                pass
            elif token in [ZCodeParser.NUMLIT, ZCodeParser.BOOLLIT, ZCodeParser.STRINGLIT, ZCodeParser.SUBOP, ZCodeParser.LRB, ZCodeParser.LSQB, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 443
                self.lv3_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lv3_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUBOP(self):
            return self.getToken(ZCodeParser.SUBOP, 0)

        def lv3_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Lv3_exprContext,0)


        def lv2_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Lv2_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_lv3_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLv3_expr" ):
                return visitor.visitLv3_expr(self)
            else:
                return visitor.visitChildren(self)




    def lv3_expr(self):

        localctx = ZCodeParser.Lv3_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_lv3_expr)
        try:
            self.state = 449
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUBOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 446
                self.match(ZCodeParser.SUBOP)
                self.state = 447
                self.lv3_expr()
                pass
            elif token in [ZCodeParser.NUMLIT, ZCodeParser.BOOLLIT, ZCodeParser.STRINGLIT, ZCodeParser.LRB, ZCodeParser.LSQB, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 448
                self.lv2_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lv2_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_indexing(self):
            return self.getTypedRuleContext(ZCodeParser.Array_indexingContext,0)


        def lv1_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Lv1_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_lv2_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLv2_expr" ):
                return visitor.visitLv2_expr(self)
            else:
                return visitor.visitChildren(self)




    def lv2_expr(self):

        localctx = ZCodeParser.Lv2_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_lv2_expr)
        try:
            self.state = 453
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 451
                self.array_indexing()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 452
                self.lv1_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lv1_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_call(self):
            return self.getTypedRuleContext(ZCodeParser.Function_callContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def literals(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralsContext,0)


        def LRB(self):
            return self.getToken(ZCodeParser.LRB, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RRB(self):
            return self.getToken(ZCodeParser.RRB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_lv1_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLv1_expr" ):
                return visitor.visitLv1_expr(self)
            else:
                return visitor.visitChildren(self)




    def lv1_expr(self):

        localctx = ZCodeParser.Lv1_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_lv1_expr)
        try:
            self.state = 462
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 455
                self.function_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 456
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 457
                self.literals()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 458
                self.match(ZCodeParser.LRB)
                self.state = 459
                self.expr()
                self.state = 460
                self.match(ZCodeParser.RRB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_indexingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Array_expressionContext,0)


        def index_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_indexing

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_indexing" ):
                return visitor.visitArray_indexing(self)
            else:
                return visitor.visitChildren(self)




    def array_indexing(self):

        localctx = ZCodeParser.Array_indexingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_array_indexing)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 464
            self.array_expression()
            self.state = 465
            self.index_operator()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def function_call(self):
            return self.getTypedRuleContext(ZCodeParser.Function_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_expression" ):
                return visitor.visitArray_expression(self)
            else:
                return visitor.visitChildren(self)




    def array_expression(self):

        localctx = ZCodeParser.Array_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_array_expression)
        try:
            self.state = 469
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 467
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 468
                self.function_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSQB(self):
            return self.getToken(ZCodeParser.LSQB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(ZCodeParser.ExprlistContext,0)


        def RSQB(self):
            return self.getToken(ZCodeParser.RSQB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_index_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operator" ):
                return visitor.visitIndex_operator(self)
            else:
                return visitor.visitChildren(self)




    def index_operator(self):

        localctx = ZCodeParser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_index_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self.match(ZCodeParser.LSQB)
            self.state = 472
            self.exprlist()
            self.state = 473
            self.match(ZCodeParser.RSQB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def exprlisttail(self):
            return self.getTypedRuleContext(ZCodeParser.ExprlisttailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exprlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlist" ):
                return visitor.visitExprlist(self)
            else:
                return visitor.visitChildren(self)




    def exprlist(self):

        localctx = ZCodeParser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_exprlist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
            self.expr()
            self.state = 476
            self.exprlisttail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlisttailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def exprlisttail(self):
            return self.getTypedRuleContext(ZCodeParser.ExprlisttailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exprlisttail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlisttail" ):
                return visitor.visitExprlisttail(self)
            else:
                return visitor.visitChildren(self)




    def exprlisttail(self):

        localctx = ZCodeParser.ExprlisttailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_exprlisttail)
        try:
            self.state = 483
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 478
                self.match(ZCodeParser.COMMA)
                self.state = 479
                self.expr()
                self.state = 480
                self.exprlisttail()
                pass
            elif token in [ZCodeParser.RSQB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def args(self):
            return self.getTypedRuleContext(ZCodeParser.ArgsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = ZCodeParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_function_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 486
            self.args()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LRB(self):
            return self.getToken(ZCodeParser.LRB, 0)

        def argslist(self):
            return self.getTypedRuleContext(ZCodeParser.ArgslistContext,0)


        def RRB(self):
            return self.getToken(ZCodeParser.RRB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_args

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = ZCodeParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_args)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
            self.match(ZCodeParser.LRB)
            self.state = 489
            self.argslist()
            self.state = 490
            self.match(ZCodeParser.RRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgslistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def argslisttail(self):
            return self.getTypedRuleContext(ZCodeParser.ArgslisttailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argslist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgslist" ):
                return visitor.visitArgslist(self)
            else:
                return visitor.visitChildren(self)




    def argslist(self):

        localctx = ZCodeParser.ArgslistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_argslist)
        try:
            self.state = 496
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMLIT, ZCodeParser.BOOLLIT, ZCodeParser.STRINGLIT, ZCodeParser.NOT, ZCodeParser.SUBOP, ZCodeParser.LRB, ZCodeParser.LSQB, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 492
                self.expr()
                self.state = 493
                self.argslisttail()
                pass
            elif token in [ZCodeParser.RRB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgslisttailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def argslisttail(self):
            return self.getTypedRuleContext(ZCodeParser.ArgslisttailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argslisttail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgslisttail" ):
                return visitor.visitArgslisttail(self)
            else:
                return visitor.visitChildren(self)




    def argslisttail(self):

        localctx = ZCodeParser.ArgslisttailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_argslisttail)
        try:
            self.state = 503
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 498
                self.match(ZCodeParser.COMMA)
                self.state = 499
                self.expr()
                self.state = 500
                self.argslisttail()
                pass
            elif token in [ZCodeParser.RRB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LinebreaklistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LINEBREAK(self):
            return self.getToken(ZCodeParser.LINEBREAK, 0)

        def linebreaklisttail(self):
            return self.getTypedRuleContext(ZCodeParser.LinebreaklisttailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_linebreaklist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLinebreaklist" ):
                return visitor.visitLinebreaklist(self)
            else:
                return visitor.visitChildren(self)




    def linebreaklist(self):

        localctx = ZCodeParser.LinebreaklistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_linebreaklist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 505
            self.match(ZCodeParser.LINEBREAK)
            self.state = 506
            self.linebreaklisttail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NullablelinebreaklistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LINEBREAK(self):
            return self.getToken(ZCodeParser.LINEBREAK, 0)

        def linebreaklisttail(self):
            return self.getTypedRuleContext(ZCodeParser.LinebreaklisttailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_nullablelinebreaklist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullablelinebreaklist" ):
                return visitor.visitNullablelinebreaklist(self)
            else:
                return visitor.visitChildren(self)




    def nullablelinebreaklist(self):

        localctx = ZCodeParser.NullablelinebreaklistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_nullablelinebreaklist)
        try:
            self.state = 511
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LINEBREAK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 508
                self.match(ZCodeParser.LINEBREAK)
                self.state = 509
                self.linebreaklisttail()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FUNC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LinebreaklisttailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LINEBREAK(self):
            return self.getToken(ZCodeParser.LINEBREAK, 0)

        def linebreaklisttail(self):
            return self.getTypedRuleContext(ZCodeParser.LinebreaklisttailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_linebreaklisttail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLinebreaklisttail" ):
                return visitor.visitLinebreaklisttail(self)
            else:
                return visitor.visitChildren(self)




    def linebreaklisttail(self):

        localctx = ZCodeParser.LinebreaklisttailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_linebreaklisttail)
        try:
            self.state = 516
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LINEBREAK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 513
                self.match(ZCodeParser.LINEBREAK)
                self.state = 514
                self.linebreaklisttail()
                pass
            elif token in [ZCodeParser.EOF, ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FUNC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.ELSE, ZCodeParser.ELIF, ZCodeParser.BEGIN, ZCodeParser.END, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[46] = self.lv7_expr_sempred
        self._predicates[47] = self.lv6_expr_sempred
        self._predicates[48] = self.lv5_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def lv7_expr_sempred(self, localctx:Lv7_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def lv6_expr_sempred(self, localctx:Lv6_exprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def lv5_expr_sempred(self, localctx:Lv5_exprContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         




