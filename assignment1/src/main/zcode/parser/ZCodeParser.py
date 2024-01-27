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
        buf.write("\u0200\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4\u008e\n\4\3\5\3\5\3\5")
        buf.write("\3\5\5\5\u0094\n\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\5\b\u00a3\n\b\3\t\3\t\3\t\3\t\3\t\5\t")
        buf.write("\u00aa\n\t\3\n\3\n\3\n\3\n\5\n\u00b0\n\n\3\13\3\13\3\13")
        buf.write("\3\13\5\13\u00b6\n\13\3\f\3\f\5\f\u00ba\n\f\3\r\3\r\5")
        buf.write("\r\u00be\n\r\3\r\3\r\3\r\5\r\u00c3\n\r\3\r\3\r\3\r\3\r")
        buf.write("\5\r\u00c9\n\r\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\5\23\u00e0\n\23\3\24\3\24\3\24\3\25\3\25\3")
        buf.write("\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\5\27")
        buf.write("\u00f1\n\27\3\30\3\30\5\30\u00f5\n\30\3\31\3\31\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u0102\n\32")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35\5\35")
        buf.write("\u010e\n\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3")
        buf.write("\37\3 \3 \3 \3 \3!\3!\3!\3!\5!\u0121\n!\3\"\3\"\3\"\3")
        buf.write("\"\5\"\u0127\n\"\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\5$\u0133")
        buf.write("\n$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3")
        buf.write("(\3(\3(\5(\u0147\n(\3(\3(\3)\3)\3)\3*\3*\3*\3*\3*\3*\3")
        buf.write("+\3+\3+\3+\5+\u0158\n+\3,\3,\3,\3,\5,\u015e\n,\3-\3-\3")
        buf.write("-\3-\3-\5-\u0165\n-\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\5")
        buf.write(".\u0184\n.\3/\3/\3/\3/\3/\3/\3/\3/\3/\7/\u018f\n/\f/\16")
        buf.write("/\u0192\13/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write("\60\7\60\u019d\n\60\f\60\16\60\u01a0\13\60\3\61\3\61\3")
        buf.write("\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\7\61")
        buf.write("\u01ae\n\61\f\61\16\61\u01b1\13\61\3\62\3\62\3\62\5\62")
        buf.write("\u01b6\n\62\3\63\3\63\3\63\5\63\u01bb\n\63\3\64\3\64\5")
        buf.write("\64\u01bf\n\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\5\65")
        buf.write("\u01c8\n\65\3\66\3\66\3\66\3\67\3\67\5\67\u01cf\n\67\3")
        buf.write("8\38\38\38\39\39\39\3:\3:\3:\3:\3:\5:\u01dd\n:\3;\3;\3")
        buf.write(";\3<\3<\3<\3<\3=\3=\3=\3=\5=\u01ea\n=\3>\3>\3>\3>\3>\5")
        buf.write(">\u01f1\n>\3?\3?\3?\3@\3@\3@\5@\u01f9\n@\3A\3A\3A\5A\u01fe")
        buf.write("\nA\3A\2\5\\^`B\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(" \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprt")
        buf.write("vxz|~\u0080\2\4\3\2\b\n\3\2\3\5\2\u01f7\2\u0082\3\2\2")
        buf.write("\2\4\u0086\3\2\2\2\6\u008d\3\2\2\2\b\u0093\3\2\2\2\n\u0095")
        buf.write("\3\2\2\2\f\u009a\3\2\2\2\16\u00a2\3\2\2\2\20\u00a9\3\2")
        buf.write("\2\2\22\u00ab\3\2\2\2\24\u00b5\3\2\2\2\26\u00b9\3\2\2")
        buf.write("\2\30\u00c8\3\2\2\2\32\u00ca\3\2\2\2\34\u00cc\3\2\2\2")
        buf.write("\36\u00cf\3\2\2\2 \u00d4\3\2\2\2\"\u00d8\3\2\2\2$\u00df")
        buf.write("\3\2\2\2&\u00e1\3\2\2\2(\u00e4\3\2\2\2*\u00e8\3\2\2\2")
        buf.write(",\u00f0\3\2\2\2.\u00f4\3\2\2\2\60\u00f6\3\2\2\2\62\u0101")
        buf.write("\3\2\2\2\64\u0103\3\2\2\2\66\u0106\3\2\2\28\u010d\3\2")
        buf.write("\2\2:\u010f\3\2\2\2<\u0113\3\2\2\2>\u0118\3\2\2\2@\u0120")
        buf.write("\3\2\2\2B\u0126\3\2\2\2D\u0128\3\2\2\2F\u0132\3\2\2\2")
        buf.write("H\u0134\3\2\2\2J\u013d\3\2\2\2L\u0140\3\2\2\2N\u0143\3")
        buf.write("\2\2\2P\u014a\3\2\2\2R\u014d\3\2\2\2T\u0157\3\2\2\2V\u015d")
        buf.write("\3\2\2\2X\u0164\3\2\2\2Z\u0183\3\2\2\2\\\u0185\3\2\2\2")
        buf.write("^\u0193\3\2\2\2`\u01a1\3\2\2\2b\u01b5\3\2\2\2d\u01ba\3")
        buf.write("\2\2\2f\u01be\3\2\2\2h\u01c7\3\2\2\2j\u01c9\3\2\2\2l\u01ce")
        buf.write("\3\2\2\2n\u01d0\3\2\2\2p\u01d4\3\2\2\2r\u01dc\3\2\2\2")
        buf.write("t\u01de\3\2\2\2v\u01e1\3\2\2\2x\u01e9\3\2\2\2z\u01f0\3")
        buf.write("\2\2\2|\u01f2\3\2\2\2~\u01f8\3\2\2\2\u0080\u01fd\3\2\2")
        buf.write("\2\u0082\u0083\5~@\2\u0083\u0084\5\4\3\2\u0084\u0085\7")
        buf.write("\2\2\3\u0085\3\3\2\2\2\u0086\u0087\5\b\5\2\u0087\u0088")
        buf.write("\5\6\4\2\u0088\5\3\2\2\2\u0089\u008a\5\b\5\2\u008a\u008b")
        buf.write("\5\6\4\2\u008b\u008e\3\2\2\2\u008c\u008e\3\2\2\2\u008d")
        buf.write("\u0089\3\2\2\2\u008d\u008c\3\2\2\2\u008e\7\3\2\2\2\u008f")
        buf.write("\u0094\5\n\6\2\u0090\u0091\5\30\r\2\u0091\u0092\5|?\2")
        buf.write("\u0092\u0094\3\2\2\2\u0093\u008f\3\2\2\2\u0093\u0090\3")
        buf.write("\2\2\2\u0094\t\3\2\2\2\u0095\u0096\7\16\2\2\u0096\u0097")
        buf.write("\7/\2\2\u0097\u0098\5\f\7\2\u0098\u0099\5\24\13\2\u0099")
        buf.write("\13\3\2\2\2\u009a\u009b\7+\2\2\u009b\u009c\5\16\b\2\u009c")
        buf.write("\u009d\7,\2\2\u009d\r\3\2\2\2\u009e\u009f\5\22\n\2\u009f")
        buf.write("\u00a0\5\20\t\2\u00a0\u00a3\3\2\2\2\u00a1\u00a3\3\2\2")
        buf.write("\2\u00a2\u009e\3\2\2\2\u00a2\u00a1\3\2\2\2\u00a3\17\3")
        buf.write("\2\2\2\u00a4\u00a5\7*\2\2\u00a5\u00a6\5\22\n\2\u00a6\u00a7")
        buf.write("\5\20\t\2\u00a7\u00aa\3\2\2\2\u00a8\u00aa\3\2\2\2\u00a9")
        buf.write("\u00a4\3\2\2\2\u00a9\u00a8\3\2\2\2\u00aa\21\3\2\2\2\u00ab")
        buf.write("\u00ac\5\32\16\2\u00ac\u00af\7/\2\2\u00ad\u00b0\5 \21")
        buf.write("\2\u00ae\u00b0\3\2\2\2\u00af\u00ad\3\2\2\2\u00af\u00ae")
        buf.write("\3\2\2\2\u00b0\23\3\2\2\2\u00b1\u00b6\5|?\2\u00b2\u00b3")
        buf.write("\5~@\2\u00b3\u00b4\5\26\f\2\u00b4\u00b6\3\2\2\2\u00b5")
        buf.write("\u00b1\3\2\2\2\u00b5\u00b2\3\2\2\2\u00b6\25\3\2\2\2\u00b7")
        buf.write("\u00ba\5N(\2\u00b8\u00ba\5R*\2\u00b9\u00b7\3\2\2\2\u00b9")
        buf.write("\u00b8\3\2\2\2\u00ba\27\3\2\2\2\u00bb\u00be\5\32\16\2")
        buf.write("\u00bc\u00be\7\r\2\2\u00bd\u00bb\3\2\2\2\u00bd\u00bc\3")
        buf.write("\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00c2\7/\2\2\u00c0\u00c3")
        buf.write("\5\34\17\2\u00c1\u00c3\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c2")
        buf.write("\u00c1\3\2\2\2\u00c3\u00c9\3\2\2\2\u00c4\u00c5\7\f\2\2")
        buf.write("\u00c5\u00c6\7/\2\2\u00c6\u00c9\5\34\17\2\u00c7\u00c9")
        buf.write("\5\36\20\2\u00c8\u00bd\3\2\2\2\u00c8\u00c4\3\2\2\2\u00c8")
        buf.write("\u00c7\3\2\2\2\u00c9\31\3\2\2\2\u00ca\u00cb\t\2\2\2\u00cb")
        buf.write("\33\3\2\2\2\u00cc\u00cd\7!\2\2\u00cd\u00ce\5X-\2\u00ce")
        buf.write("\35\3\2\2\2\u00cf\u00d0\5\32\16\2\u00d0\u00d1\7/\2\2\u00d1")
        buf.write("\u00d2\5 \21\2\u00d2\u00d3\5&\24\2\u00d3\37\3\2\2\2\u00d4")
        buf.write("\u00d5\7-\2\2\u00d5\u00d6\5\"\22\2\u00d6\u00d7\7.\2\2")
        buf.write("\u00d7!\3\2\2\2\u00d8\u00d9\7\3\2\2\u00d9\u00da\5$\23")
        buf.write("\2\u00da#\3\2\2\2\u00db\u00dc\7*\2\2\u00dc\u00dd\7\3\2")
        buf.write("\2\u00dd\u00e0\5$\23\2\u00de\u00e0\3\2\2\2\u00df\u00db")
        buf.write("\3\2\2\2\u00df\u00de\3\2\2\2\u00e0%\3\2\2\2\u00e1\u00e2")
        buf.write("\7!\2\2\u00e2\u00e3\5(\25\2\u00e3\'\3\2\2\2\u00e4\u00e5")
        buf.write("\7-\2\2\u00e5\u00e6\5*\26\2\u00e6\u00e7\7.\2\2\u00e7)")
        buf.write("\3\2\2\2\u00e8\u00e9\5.\30\2\u00e9\u00ea\5,\27\2\u00ea")
        buf.write("+\3\2\2\2\u00eb\u00ec\7*\2\2\u00ec\u00ed\5.\30\2\u00ed")
        buf.write("\u00ee\5,\27\2\u00ee\u00f1\3\2\2\2\u00ef\u00f1\3\2\2\2")
        buf.write("\u00f0\u00eb\3\2\2\2\u00f0\u00ef\3\2\2\2\u00f1-\3\2\2")
        buf.write("\2\u00f2\u00f5\5X-\2\u00f3\u00f5\5(\25\2\u00f4\u00f2\3")
        buf.write("\2\2\2\u00f4\u00f3\3\2\2\2\u00f5/\3\2\2\2\u00f6\u00f7")
        buf.write("\t\3\2\2\u00f7\61\3\2\2\2\u00f8\u0102\5\64\33\2\u00f9")
        buf.write("\u0102\5\66\34\2\u00fa\u0102\5:\36\2\u00fb\u0102\5H%\2")
        buf.write("\u00fc\u0102\5J&\2\u00fd\u0102\5L\'\2\u00fe\u0102\5N(")
        buf.write("\2\u00ff\u0102\5P)\2\u0100\u0102\5R*\2\u0101\u00f8\3\2")
        buf.write("\2\2\u0101\u00f9\3\2\2\2\u0101\u00fa\3\2\2\2\u0101\u00fb")
        buf.write("\3\2\2\2\u0101\u00fc\3\2\2\2\u0101\u00fd\3\2\2\2\u0101")
        buf.write("\u00fe\3\2\2\2\u0101\u00ff\3\2\2\2\u0101\u0100\3\2\2\2")
        buf.write("\u0102\63\3\2\2\2\u0103\u0104\5\30\r\2\u0104\u0105\5|")
        buf.write("?\2\u0105\65\3\2\2\2\u0106\u0107\58\35\2\u0107\u0108\7")
        buf.write("!\2\2\u0108\u0109\5X-\2\u0109\u010a\5|?\2\u010a\67\3\2")
        buf.write("\2\2\u010b\u010e\7/\2\2\u010c\u010e\5j\66\2\u010d\u010b")
        buf.write("\3\2\2\2\u010d\u010c\3\2\2\2\u010e9\3\2\2\2\u010f\u0110")
        buf.write("\5<\37\2\u0110\u0111\5@!\2\u0111\u0112\5F$\2\u0112;\3")
        buf.write("\2\2\2\u0113\u0114\7\24\2\2\u0114\u0115\5> \2\u0115\u0116")
        buf.write("\5~@\2\u0116\u0117\5\62\32\2\u0117=\3\2\2\2\u0118\u0119")
        buf.write("\7+\2\2\u0119\u011a\5X-\2\u011a\u011b\7,\2\2\u011b?\3")
        buf.write("\2\2\2\u011c\u011d\5D#\2\u011d\u011e\5B\"\2\u011e\u0121")
        buf.write("\3\2\2\2\u011f\u0121\3\2\2\2\u0120\u011c\3\2\2\2\u0120")
        buf.write("\u011f\3\2\2\2\u0121A\3\2\2\2\u0122\u0123\5D#\2\u0123")
        buf.write("\u0124\5B\"\2\u0124\u0127\3\2\2\2\u0125\u0127\3\2\2\2")
        buf.write("\u0126\u0122\3\2\2\2\u0126\u0125\3\2\2\2\u0127C\3\2\2")
        buf.write("\2\u0128\u0129\7\26\2\2\u0129\u012a\5> \2\u012a\u012b")
        buf.write("\5~@\2\u012b\u012c\5\62\32\2\u012cE\3\2\2\2\u012d\u012e")
        buf.write("\7\25\2\2\u012e\u012f\5~@\2\u012f\u0130\5\62\32\2\u0130")
        buf.write("\u0133\3\2\2\2\u0131\u0133\3\2\2\2\u0132\u012d\3\2\2\2")
        buf.write("\u0132\u0131\3\2\2\2\u0133G\3\2\2\2\u0134\u0135\7\17\2")
        buf.write("\2\u0135\u0136\7/\2\2\u0136\u0137\7\20\2\2\u0137\u0138")
        buf.write("\5X-\2\u0138\u0139\7\21\2\2\u0139\u013a\5X-\2\u013a\u013b")
        buf.write("\5~@\2\u013b\u013c\5\62\32\2\u013cI\3\2\2\2\u013d\u013e")
        buf.write("\7\22\2\2\u013e\u013f\5|?\2\u013fK\3\2\2\2\u0140\u0141")
        buf.write("\7\23\2\2\u0141\u0142\5|?\2\u0142M\3\2\2\2\u0143\u0146")
        buf.write("\7\13\2\2\u0144\u0147\5X-\2\u0145\u0147\3\2\2\2\u0146")
        buf.write("\u0144\3\2\2\2\u0146\u0145\3\2\2\2\u0147\u0148\3\2\2\2")
        buf.write("\u0148\u0149\5|?\2\u0149O\3\2\2\2\u014a\u014b\5t;\2\u014b")
        buf.write("\u014c\5|?\2\u014cQ\3\2\2\2\u014d\u014e\7\27\2\2\u014e")
        buf.write("\u014f\5|?\2\u014f\u0150\5T+\2\u0150\u0151\7\30\2\2\u0151")
        buf.write("\u0152\5|?\2\u0152S\3\2\2\2\u0153\u0154\5\62\32\2\u0154")
        buf.write("\u0155\5V,\2\u0155\u0158\3\2\2\2\u0156\u0158\3\2\2\2\u0157")
        buf.write("\u0153\3\2\2\2\u0157\u0156\3\2\2\2\u0158U\3\2\2\2\u0159")
        buf.write("\u015a\5\62\32\2\u015a\u015b\5V,\2\u015b\u015e\3\2\2\2")
        buf.write("\u015c\u015e\3\2\2\2\u015d\u0159\3\2\2\2\u015d\u015c\3")
        buf.write("\2\2\2\u015eW\3\2\2\2\u015f\u0160\5Z.\2\u0160\u0161\7")
        buf.write("(\2\2\u0161\u0162\5Z.\2\u0162\u0165\3\2\2\2\u0163\u0165")
        buf.write("\5Z.\2\u0164\u015f\3\2\2\2\u0164\u0163\3\2\2\2\u0165Y")
        buf.write("\3\2\2\2\u0166\u0167\5\\/\2\u0167\u0168\7\"\2\2\u0168")
        buf.write("\u0169\5\\/\2\u0169\u0184\3\2\2\2\u016a\u016b\5\\/\2\u016b")
        buf.write("\u016c\7)\2\2\u016c\u016d\5\\/\2\u016d\u0184\3\2\2\2\u016e")
        buf.write("\u016f\5\\/\2\u016f\u0170\7#\2\2\u0170\u0171\5\\/\2\u0171")
        buf.write("\u0184\3\2\2\2\u0172\u0173\5\\/\2\u0173\u0174\7$\2\2\u0174")
        buf.write("\u0175\5\\/\2\u0175\u0184\3\2\2\2\u0176\u0177\5\\/\2\u0177")
        buf.write("\u0178\7%\2\2\u0178\u0179\5\\/\2\u0179\u0184\3\2\2\2\u017a")
        buf.write("\u017b\5\\/\2\u017b\u017c\7&\2\2\u017c\u017d\5\\/\2\u017d")
        buf.write("\u0184\3\2\2\2\u017e\u017f\5\\/\2\u017f\u0180\7\'\2\2")
        buf.write("\u0180\u0181\5\\/\2\u0181\u0184\3\2\2\2\u0182\u0184\5")
        buf.write("\\/\2\u0183\u0166\3\2\2\2\u0183\u016a\3\2\2\2\u0183\u016e")
        buf.write("\3\2\2\2\u0183\u0172\3\2\2\2\u0183\u0176\3\2\2\2\u0183")
        buf.write("\u017a\3\2\2\2\u0183\u017e\3\2\2\2\u0183\u0182\3\2\2\2")
        buf.write("\u0184[\3\2\2\2\u0185\u0186\b/\1\2\u0186\u0187\5^\60\2")
        buf.write("\u0187\u0190\3\2\2\2\u0188\u0189\f\5\2\2\u0189\u018a\7")
        buf.write("\32\2\2\u018a\u018f\5^\60\2\u018b\u018c\f\4\2\2\u018c")
        buf.write("\u018d\7\33\2\2\u018d\u018f\5^\60\2\u018e\u0188\3\2\2")
        buf.write("\2\u018e\u018b\3\2\2\2\u018f\u0192\3\2\2\2\u0190\u018e")
        buf.write("\3\2\2\2\u0190\u0191\3\2\2\2\u0191]\3\2\2\2\u0192\u0190")
        buf.write("\3\2\2\2\u0193\u0194\b\60\1\2\u0194\u0195\5`\61\2\u0195")
        buf.write("\u019e\3\2\2\2\u0196\u0197\f\5\2\2\u0197\u0198\7\34\2")
        buf.write("\2\u0198\u019d\5`\61\2\u0199\u019a\f\4\2\2\u019a\u019b")
        buf.write("\7\35\2\2\u019b\u019d\5`\61\2\u019c\u0196\3\2\2\2\u019c")
        buf.write("\u0199\3\2\2\2\u019d\u01a0\3\2\2\2\u019e\u019c\3\2\2\2")
        buf.write("\u019e\u019f\3\2\2\2\u019f_\3\2\2\2\u01a0\u019e\3\2\2")
        buf.write("\2\u01a1\u01a2\b\61\1\2\u01a2\u01a3\5b\62\2\u01a3\u01af")
        buf.write("\3\2\2\2\u01a4\u01a5\f\6\2\2\u01a5\u01a6\7\36\2\2\u01a6")
        buf.write("\u01ae\5b\62\2\u01a7\u01a8\f\5\2\2\u01a8\u01a9\7\37\2")
        buf.write("\2\u01a9\u01ae\5b\62\2\u01aa\u01ab\f\4\2\2\u01ab\u01ac")
        buf.write("\7 \2\2\u01ac\u01ae\5b\62\2\u01ad\u01a4\3\2\2\2\u01ad")
        buf.write("\u01a7\3\2\2\2\u01ad\u01aa\3\2\2\2\u01ae\u01b1\3\2\2\2")
        buf.write("\u01af\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0a\3\2\2")
        buf.write("\2\u01b1\u01af\3\2\2\2\u01b2\u01b3\7\31\2\2\u01b3\u01b6")
        buf.write("\5b\62\2\u01b4\u01b6\5d\63\2\u01b5\u01b2\3\2\2\2\u01b5")
        buf.write("\u01b4\3\2\2\2\u01b6c\3\2\2\2\u01b7\u01b8\7\35\2\2\u01b8")
        buf.write("\u01bb\5d\63\2\u01b9\u01bb\5f\64\2\u01ba\u01b7\3\2\2\2")
        buf.write("\u01ba\u01b9\3\2\2\2\u01bbe\3\2\2\2\u01bc\u01bf\5j\66")
        buf.write("\2\u01bd\u01bf\5h\65\2\u01be\u01bc\3\2\2\2\u01be\u01bd")
        buf.write("\3\2\2\2\u01bfg\3\2\2\2\u01c0\u01c8\5t;\2\u01c1\u01c8")
        buf.write("\7/\2\2\u01c2\u01c8\5\60\31\2\u01c3\u01c4\7+\2\2\u01c4")
        buf.write("\u01c5\5X-\2\u01c5\u01c6\7,\2\2\u01c6\u01c8\3\2\2\2\u01c7")
        buf.write("\u01c0\3\2\2\2\u01c7\u01c1\3\2\2\2\u01c7\u01c2\3\2\2\2")
        buf.write("\u01c7\u01c3\3\2\2\2\u01c8i\3\2\2\2\u01c9\u01ca\5l\67")
        buf.write("\2\u01ca\u01cb\5n8\2\u01cbk\3\2\2\2\u01cc\u01cf\7/\2\2")
        buf.write("\u01cd\u01cf\5t;\2\u01ce\u01cc\3\2\2\2\u01ce\u01cd\3\2")
        buf.write("\2\2\u01cfm\3\2\2\2\u01d0\u01d1\7-\2\2\u01d1\u01d2\5p")
        buf.write("9\2\u01d2\u01d3\7.\2\2\u01d3o\3\2\2\2\u01d4\u01d5\5X-")
        buf.write("\2\u01d5\u01d6\5r:\2\u01d6q\3\2\2\2\u01d7\u01d8\7*\2\2")
        buf.write("\u01d8\u01d9\5X-\2\u01d9\u01da\5r:\2\u01da\u01dd\3\2\2")
        buf.write("\2\u01db\u01dd\3\2\2\2\u01dc\u01d7\3\2\2\2\u01dc\u01db")
        buf.write("\3\2\2\2\u01dds\3\2\2\2\u01de\u01df\7/\2\2\u01df\u01e0")
        buf.write("\5v<\2\u01e0u\3\2\2\2\u01e1\u01e2\7+\2\2\u01e2\u01e3\5")
        buf.write("x=\2\u01e3\u01e4\7,\2\2\u01e4w\3\2\2\2\u01e5\u01e6\5X")
        buf.write("-\2\u01e6\u01e7\5z>\2\u01e7\u01ea\3\2\2\2\u01e8\u01ea")
        buf.write("\3\2\2\2\u01e9\u01e5\3\2\2\2\u01e9\u01e8\3\2\2\2\u01ea")
        buf.write("y\3\2\2\2\u01eb\u01ec\7*\2\2\u01ec\u01ed\5X-\2\u01ed\u01ee")
        buf.write("\5z>\2\u01ee\u01f1\3\2\2\2\u01ef\u01f1\3\2\2\2\u01f0\u01eb")
        buf.write("\3\2\2\2\u01f0\u01ef\3\2\2\2\u01f1{\3\2\2\2\u01f2\u01f3")
        buf.write("\7\60\2\2\u01f3\u01f4\5\u0080A\2\u01f4}\3\2\2\2\u01f5")
        buf.write("\u01f6\7\60\2\2\u01f6\u01f9\5\u0080A\2\u01f7\u01f9\3\2")
        buf.write("\2\2\u01f8\u01f5\3\2\2\2\u01f8\u01f7\3\2\2\2\u01f9\177")
        buf.write("\3\2\2\2\u01fa\u01fb\7\60\2\2\u01fb\u01fe\5\u0080A\2\u01fc")
        buf.write("\u01fe\3\2\2\2\u01fd\u01fa\3\2\2\2\u01fd\u01fc\3\2\2\2")
        buf.write("\u01fe\u0081\3\2\2\2)\u008d\u0093\u00a2\u00a9\u00af\u00b5")
        buf.write("\u00b9\u00bd\u00c2\u00c8\u00df\u00f0\u00f4\u0101\u010d")
        buf.write("\u0120\u0126\u0132\u0146\u0157\u015d\u0164\u0183\u018e")
        buf.write("\u0190\u019c\u019e\u01ad\u01af\u01b5\u01ba\u01be\u01c7")
        buf.write("\u01ce\u01dc\u01e9\u01f0\u01f8\u01fd")
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
                     "'=='", "','", "'('", "')'", "'['", "']'", "<INVALID>", 
                     "'\n'" ]

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
    RULE_if_statement = 28
    RULE_ifpart = 29
    RULE_exprclause = 30
    RULE_eliflist = 31
    RULE_eliflisttail = 32
    RULE_elifpart = 33
    RULE_elsepart = 34
    RULE_for_statement = 35
    RULE_break_statement = 36
    RULE_continue_statement = 37
    RULE_return_statement = 38
    RULE_function_call_statement = 39
    RULE_block_statement = 40
    RULE_statementlist = 41
    RULE_statementlisttail = 42
    RULE_expr = 43
    RULE_lv8_expr = 44
    RULE_lv7_expr = 45
    RULE_lv6_expr = 46
    RULE_lv5_expr = 47
    RULE_lv4_expr = 48
    RULE_lv3_expr = 49
    RULE_lv2_expr = 50
    RULE_lv1_expr = 51
    RULE_array_indexing = 52
    RULE_array_expression = 53
    RULE_index_operator = 54
    RULE_exprlist = 55
    RULE_exprlisttail = 56
    RULE_function_call = 57
    RULE_args = 58
    RULE_argslist = 59
    RULE_argslisttail = 60
    RULE_linebreaklist = 61
    RULE_nullablelinebreaklist = 62
    RULE_linebreaklisttail = 63

    ruleNames =  [ "program", "decllist", "decllisttail", "decl", "func_decl", 
                   "param_decl", "paramlist", "paramlisttail", "param", 
                   "func_decl_end", "func_statement", "var_decl", "typ", 
                   "initialization", "array_decl", "dimensionlist", "numlitlist", 
                   "numlitlisttail", "array_init", "arraylit", "array_decl_elelist", 
                   "array_decl_elelisttail", "array_decl_ele", "literals", 
                   "statement", "var_decl_statement", "assign_statement", 
                   "lhs", "if_statement", "ifpart", "exprclause", "eliflist", 
                   "eliflisttail", "elifpart", "elsepart", "for_statement", 
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
            self.state = 128
            self.nullablelinebreaklist()
            self.state = 129
            self.decllist()
            self.state = 130
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
            self.state = 132
            self.decl()
            self.state = 133
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
            self.state = 139
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.decl()
                self.state = 136
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
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.func_decl()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.var_decl()
                self.state = 143
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
            self.state = 147
            self.match(ZCodeParser.FUNC)
            self.state = 148
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 149
            self.param_decl()
            self.state = 150
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
            self.state = 152
            self.match(ZCodeParser.LRB)
            self.state = 153
            self.paramlist()
            self.state = 154
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
            self.state = 160
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.param()
                self.state = 157
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
            self.state = 167
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.match(ZCodeParser.COMMA)
                self.state = 163
                self.param()
                self.state = 164
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
            self.state = 169
            self.typ()
            self.state = 170
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 173
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LSQB]:
                self.state = 171
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
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.linebreaklist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self.nullablelinebreaklist()
                self.state = 177
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
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.return_statement()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
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
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                    self.state = 185
                    self.typ()
                    pass
                elif token in [ZCodeParser.DYNAMIC]:
                    self.state = 186
                    self.match(ZCodeParser.DYNAMIC)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 189
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 192
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.ASSIGNOP]:
                    self.state = 190
                    self.initialization()
                    pass
                elif token in [ZCodeParser.LINEBREAK]:
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.match(ZCodeParser.VAR)
                self.state = 195
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 196
                self.initialization()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 197
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
            self.state = 200
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
            self.state = 202
            self.match(ZCodeParser.ASSIGNOP)
            self.state = 203
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
            self.state = 205
            self.typ()
            self.state = 206
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 207
            self.dimensionlist()
            self.state = 208
            self.array_init()
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
            self.state = 210
            self.match(ZCodeParser.LSQB)
            self.state = 211
            self.numlitlist()
            self.state = 212
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
            self.state = 214
            self.match(ZCodeParser.NUMLIT)
            self.state = 215
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
            self.state = 221
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.match(ZCodeParser.COMMA)
                self.state = 218
                self.match(ZCodeParser.NUMLIT)
                self.state = 219
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
            self.state = 223
            self.match(ZCodeParser.ASSIGNOP)
            self.state = 224
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
            self.state = 226
            self.match(ZCodeParser.LSQB)
            self.state = 227
            self.array_decl_elelist()
            self.state = 228
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
            self.state = 230
            self.array_decl_ele()
            self.state = 231
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
            self.state = 238
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.match(ZCodeParser.COMMA)
                self.state = 234
                self.array_decl_ele()
                self.state = 235
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


        def arraylit(self):
            return self.getTypedRuleContext(ZCodeParser.ArraylitContext,0)


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
            self.state = 242
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMLIT, ZCodeParser.BOOLLIT, ZCodeParser.STRINGLIT, ZCodeParser.NOT, ZCodeParser.SUBOP, ZCodeParser.LRB, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.expr()
                pass
            elif token in [ZCodeParser.LSQB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMLIT) | (1 << ZCodeParser.BOOLLIT) | (1 << ZCodeParser.STRINGLIT))) != 0)):
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
            self.state = 255
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.var_decl_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.assign_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 248
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 249
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 250
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 251
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 252
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 253
                self.function_call_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 254
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
            self.state = 257
            self.var_decl()
            self.state = 258
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
            self.state = 260
            self.lhs()
            self.state = 261
            self.match(ZCodeParser.ASSIGNOP)
            self.state = 262
            self.expr()
            self.state = 263
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

        def array_indexing(self):
            return self.getTypedRuleContext(ZCodeParser.Array_indexingContext,0)


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
            self.state = 267
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 266
                self.array_indexing()
                pass


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
        self.enterRule(localctx, 56, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.ifpart()
            self.state = 270
            self.eliflist()
            self.state = 271
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
        self.enterRule(localctx, 58, self.RULE_ifpart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(ZCodeParser.IF)
            self.state = 274
            self.exprclause()
            self.state = 275
            self.nullablelinebreaklist()
            self.state = 276
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
        self.enterRule(localctx, 60, self.RULE_exprclause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(ZCodeParser.LRB)
            self.state = 279
            self.expr()
            self.state = 280
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
        self.enterRule(localctx, 62, self.RULE_eliflist)
        try:
            self.state = 286
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                self.elifpart()
                self.state = 283
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
        self.enterRule(localctx, 64, self.RULE_eliflisttail)
        try:
            self.state = 292
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 288
                self.elifpart()
                self.state = 289
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
        self.enterRule(localctx, 66, self.RULE_elifpart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.match(ZCodeParser.ELIF)
            self.state = 295
            self.exprclause()
            self.state = 296
            self.nullablelinebreaklist()
            self.state = 297
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
        self.enterRule(localctx, 68, self.RULE_elsepart)
        try:
            self.state = 304
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.match(ZCodeParser.ELSE)
                self.state = 300
                self.nullablelinebreaklist()
                self.state = 301
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
        self.enterRule(localctx, 70, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(ZCodeParser.FOR)
            self.state = 307
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 308
            self.match(ZCodeParser.UNTIL)
            self.state = 309
            self.expr()
            self.state = 310
            self.match(ZCodeParser.BY)
            self.state = 311
            self.expr()
            self.state = 312
            self.nullablelinebreaklist()
            self.state = 313
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
        self.enterRule(localctx, 72, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(ZCodeParser.BREAK)
            self.state = 316
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
        self.enterRule(localctx, 74, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(ZCodeParser.CONTINUE)
            self.state = 319
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
        self.enterRule(localctx, 76, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.match(ZCodeParser.RETURN)
            self.state = 324
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMLIT, ZCodeParser.BOOLLIT, ZCodeParser.STRINGLIT, ZCodeParser.NOT, ZCodeParser.SUBOP, ZCodeParser.LRB, ZCodeParser.IDENTIFIER]:
                self.state = 322
                self.expr()
                pass
            elif token in [ZCodeParser.LINEBREAK]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 326
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
        self.enterRule(localctx, 78, self.RULE_function_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.function_call()
            self.state = 329
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
        self.enterRule(localctx, 80, self.RULE_block_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(ZCodeParser.BEGIN)
            self.state = 332
            self.linebreaklist()
            self.state = 333
            self.statementlist()
            self.state = 334
            self.match(ZCodeParser.END)
            self.state = 335
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
        self.enterRule(localctx, 82, self.RULE_statementlist)
        try:
            self.state = 341
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.statement()
                self.state = 338
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
        self.enterRule(localctx, 84, self.RULE_statementlisttail)
        try:
            self.state = 347
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.statement()
                self.state = 344
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
        self.enterRule(localctx, 86, self.RULE_expr)
        try:
            self.state = 354
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 349
                self.lv8_expr()
                self.state = 350
                self.match(ZCodeParser.ELLIPOP)
                self.state = 351
                self.lv8_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 353
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
        self.enterRule(localctx, 88, self.RULE_lv8_expr)
        try:
            self.state = 385
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.lv7_expr(0)
                self.state = 357
                self.match(ZCodeParser.EQUALOP)
                self.state = 358
                self.lv7_expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 360
                self.lv7_expr(0)
                self.state = 361
                self.match(ZCodeParser.DOUBLEEQOP)
                self.state = 362
                self.lv7_expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 364
                self.lv7_expr(0)
                self.state = 365
                self.match(ZCodeParser.DIFFOP)
                self.state = 366
                self.lv7_expr(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 368
                self.lv7_expr(0)
                self.state = 369
                self.match(ZCodeParser.SMALLEROP)
                self.state = 370
                self.lv7_expr(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 372
                self.lv7_expr(0)
                self.state = 373
                self.match(ZCodeParser.GREATEROP)
                self.state = 374
                self.lv7_expr(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 376
                self.lv7_expr(0)
                self.state = 377
                self.match(ZCodeParser.SEQOP)
                self.state = 378
                self.lv7_expr(0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 380
                self.lv7_expr(0)
                self.state = 381
                self.match(ZCodeParser.GEQOP)
                self.state = 382
                self.lv7_expr(0)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 384
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
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_lv7_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.lv6_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 398
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 396
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.Lv7_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lv7_expr)
                        self.state = 390
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 391
                        self.match(ZCodeParser.AND)
                        self.state = 392
                        self.lv6_expr(0)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.Lv7_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lv7_expr)
                        self.state = 393
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 394
                        self.match(ZCodeParser.OR)
                        self.state = 395
                        self.lv6_expr(0)
                        pass

             
                self.state = 400
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

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
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_lv6_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.lv5_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 412
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 410
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.Lv6_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lv6_expr)
                        self.state = 404
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 405
                        self.match(ZCodeParser.ADDOP)
                        self.state = 406
                        self.lv5_expr(0)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.Lv6_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lv6_expr)
                        self.state = 407
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 408
                        self.match(ZCodeParser.SUBOP)
                        self.state = 409
                        self.lv5_expr(0)
                        pass

             
                self.state = 414
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_lv5_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.lv4_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 429
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 427
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.Lv5_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lv5_expr)
                        self.state = 418
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 419
                        self.match(ZCodeParser.MULOP)
                        self.state = 420
                        self.lv4_expr()
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.Lv5_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lv5_expr)
                        self.state = 421
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 422
                        self.match(ZCodeParser.DIVOP)
                        self.state = 423
                        self.lv4_expr()
                        pass

                    elif la_ == 3:
                        localctx = ZCodeParser.Lv5_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lv5_expr)
                        self.state = 424
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 425
                        self.match(ZCodeParser.MODOP)
                        self.state = 426
                        self.lv4_expr()
                        pass

             
                self.state = 431
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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
        self.enterRule(localctx, 96, self.RULE_lv4_expr)
        try:
            self.state = 435
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 432
                self.match(ZCodeParser.NOT)
                self.state = 433
                self.lv4_expr()
                pass
            elif token in [ZCodeParser.NUMLIT, ZCodeParser.BOOLLIT, ZCodeParser.STRINGLIT, ZCodeParser.SUBOP, ZCodeParser.LRB, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 434
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
        self.enterRule(localctx, 98, self.RULE_lv3_expr)
        try:
            self.state = 440
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUBOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 437
                self.match(ZCodeParser.SUBOP)
                self.state = 438
                self.lv3_expr()
                pass
            elif token in [ZCodeParser.NUMLIT, ZCodeParser.BOOLLIT, ZCodeParser.STRINGLIT, ZCodeParser.LRB, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 439
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
        self.enterRule(localctx, 100, self.RULE_lv2_expr)
        try:
            self.state = 444
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 442
                self.array_indexing()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 443
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
        self.enterRule(localctx, 102, self.RULE_lv1_expr)
        try:
            self.state = 453
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 446
                self.function_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 447
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 448
                self.literals()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 449
                self.match(ZCodeParser.LRB)
                self.state = 450
                self.expr()
                self.state = 451
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
        self.enterRule(localctx, 104, self.RULE_array_indexing)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
            self.array_expression()
            self.state = 456
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
        self.enterRule(localctx, 106, self.RULE_array_expression)
        try:
            self.state = 460
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 458
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 459
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
        self.enterRule(localctx, 108, self.RULE_index_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.match(ZCodeParser.LSQB)
            self.state = 463
            self.exprlist()
            self.state = 464
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
        self.enterRule(localctx, 110, self.RULE_exprlist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self.expr()
            self.state = 467
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
        self.enterRule(localctx, 112, self.RULE_exprlisttail)
        try:
            self.state = 474
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 469
                self.match(ZCodeParser.COMMA)
                self.state = 470
                self.expr()
                self.state = 471
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
        self.enterRule(localctx, 114, self.RULE_function_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 477
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
        self.enterRule(localctx, 116, self.RULE_args)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
            self.match(ZCodeParser.LRB)
            self.state = 480
            self.argslist()
            self.state = 481
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
        self.enterRule(localctx, 118, self.RULE_argslist)
        try:
            self.state = 487
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMLIT, ZCodeParser.BOOLLIT, ZCodeParser.STRINGLIT, ZCodeParser.NOT, ZCodeParser.SUBOP, ZCodeParser.LRB, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 483
                self.expr()
                self.state = 484
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
        self.enterRule(localctx, 120, self.RULE_argslisttail)
        try:
            self.state = 494
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 489
                self.match(ZCodeParser.COMMA)
                self.state = 490
                self.expr()
                self.state = 491
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
        self.enterRule(localctx, 122, self.RULE_linebreaklist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 496
            self.match(ZCodeParser.LINEBREAK)
            self.state = 497
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
        self.enterRule(localctx, 124, self.RULE_nullablelinebreaklist)
        try:
            self.state = 502
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LINEBREAK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 499
                self.match(ZCodeParser.LINEBREAK)
                self.state = 500
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
        self.enterRule(localctx, 126, self.RULE_linebreaklisttail)
        try:
            self.state = 507
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LINEBREAK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 504
                self.match(ZCodeParser.LINEBREAK)
                self.state = 505
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
        self._predicates[45] = self.lv7_expr_sempred
        self._predicates[46] = self.lv6_expr_sempred
        self._predicates[47] = self.lv5_expr_sempred
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
         




