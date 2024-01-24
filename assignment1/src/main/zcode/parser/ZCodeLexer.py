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
        buf.write("\u0179\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\3\2\6\2o\n\2\r\2\16\2p\3\2\3")
        buf.write("\2\7\2u\n\2\f\2\16\2x\13\2\5\2z\n\2\3\2\3\2\5\2~\n\2\3")
        buf.write("\2\6\2\u0081\n\2\r\2\16\2\u0082\5\2\u0085\n\2\3\3\3\3")
        buf.write("\5\3\u0089\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4\u009d\n\4\f\4\16")
        buf.write("\4\u00a0\13\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37")
        buf.write("\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3%\3%\3%")
        buf.write("\3&\3&\3&\3\'\3\'\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3+\3+\3")
        buf.write(",\3,\3-\3-\3.\3.\7.\u0147\n.\f.\16.\u014a\13.\3/\3/\3")
        buf.write("\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\60\5\60\u015c\n\60\3\61\3\61\3\62\3\62\3")
        buf.write("\62\7\62\u0163\n\62\f\62\16\62\u0166\13\62\3\62\3\62\3")
        buf.write("\62\3\62\3\63\6\63\u016d\n\63\r\63\16\63\u016e\3\63\3")
        buf.write("\63\3\64\3\64\3\64\3\65\3\65\3\66\3\66\3\u0164\2\67\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[/]\2_\2a\60c\61e\62g\63i\64k\65\3\2\t\4\2GGg")
        buf.write("g\4\2--//\5\2$$))^^\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;")
        buf.write("\5\2\n\13\16\17\"\"\2\u018f\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write("\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2")
        buf.write("g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\3n\3\2\2\2\5\u0088\3\2")
        buf.write("\2\2\7\u008a\3\2\2\2\t\u00a3\3\2\2\2\13\u00a8\3\2\2\2")
        buf.write("\r\u00ae\3\2\2\2\17\u00b5\3\2\2\2\21\u00ba\3\2\2\2\23")
        buf.write("\u00c1\3\2\2\2\25\u00c8\3\2\2\2\27\u00cc\3\2\2\2\31\u00d4")
        buf.write("\3\2\2\2\33\u00d9\3\2\2\2\35\u00dd\3\2\2\2\37\u00e3\3")
        buf.write("\2\2\2!\u00e6\3\2\2\2#\u00ec\3\2\2\2%\u00f5\3\2\2\2\'")
        buf.write("\u00f8\3\2\2\2)\u00fd\3\2\2\2+\u0102\3\2\2\2-\u0108\3")
        buf.write("\2\2\2/\u010c\3\2\2\2\61\u0110\3\2\2\2\63\u0114\3\2\2")
        buf.write("\2\65\u0117\3\2\2\2\67\u0119\3\2\2\29\u011b\3\2\2\2;\u011d")
        buf.write("\3\2\2\2=\u011f\3\2\2\2?\u0121\3\2\2\2A\u0124\3\2\2\2")
        buf.write("C\u0126\3\2\2\2E\u0129\3\2\2\2G\u012b\3\2\2\2I\u012d\3")
        buf.write("\2\2\2K\u0130\3\2\2\2M\u0133\3\2\2\2O\u0137\3\2\2\2Q\u013a")
        buf.write("\3\2\2\2S\u013c\3\2\2\2U\u013e\3\2\2\2W\u0140\3\2\2\2")
        buf.write("Y\u0142\3\2\2\2[\u0144\3\2\2\2]\u014b\3\2\2\2_\u015b\3")
        buf.write("\2\2\2a\u015d\3\2\2\2c\u015f\3\2\2\2e\u016c\3\2\2\2g\u0172")
        buf.write("\3\2\2\2i\u0175\3\2\2\2k\u0177\3\2\2\2mo\5]/\2nm\3\2\2")
        buf.write("\2op\3\2\2\2pn\3\2\2\2pq\3\2\2\2qy\3\2\2\2rv\7\60\2\2")
        buf.write("su\5]/\2ts\3\2\2\2ux\3\2\2\2vt\3\2\2\2vw\3\2\2\2wz\3\2")
        buf.write("\2\2xv\3\2\2\2yr\3\2\2\2yz\3\2\2\2z\u0084\3\2\2\2{}\t")
        buf.write("\2\2\2|~\t\3\2\2}|\3\2\2\2}~\3\2\2\2~\u0080\3\2\2\2\177")
        buf.write("\u0081\5]/\2\u0080\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082")
        buf.write("\u0080\3\2\2\2\u0082\u0083\3\2\2\2\u0083\u0085\3\2\2\2")
        buf.write("\u0084{\3\2\2\2\u0084\u0085\3\2\2\2\u0085\4\3\2\2\2\u0086")
        buf.write("\u0089\5\t\5\2\u0087\u0089\5\13\6\2\u0088\u0086\3\2\2")
        buf.write("\2\u0088\u0087\3\2\2\2\u0089\6\3\2\2\2\u008a\u009e\7$")
        buf.write("\2\2\u008b\u008c\7^\2\2\u008c\u009d\7d\2\2\u008d\u008e")
        buf.write("\7^\2\2\u008e\u009d\7h\2\2\u008f\u0090\7^\2\2\u0090\u009d")
        buf.write("\7t\2\2\u0091\u0092\7^\2\2\u0092\u009d\7p\2\2\u0093\u0094")
        buf.write("\7^\2\2\u0094\u009d\7v\2\2\u0095\u0096\7^\2\2\u0096\u009d")
        buf.write("\7)\2\2\u0097\u0098\7^\2\2\u0098\u009d\7^\2\2\u0099\u009a")
        buf.write("\7)\2\2\u009a\u009d\7$\2\2\u009b\u009d\n\4\2\2\u009c\u008b")
        buf.write("\3\2\2\2\u009c\u008d\3\2\2\2\u009c\u008f\3\2\2\2\u009c")
        buf.write("\u0091\3\2\2\2\u009c\u0093\3\2\2\2\u009c\u0095\3\2\2\2")
        buf.write("\u009c\u0097\3\2\2\2\u009c\u0099\3\2\2\2\u009c\u009b\3")
        buf.write("\2\2\2\u009d\u00a0\3\2\2\2\u009e\u009c\3\2\2\2\u009e\u009f")
        buf.write("\3\2\2\2\u009f\u00a1\3\2\2\2\u00a0\u009e\3\2\2\2\u00a1")
        buf.write("\u00a2\7$\2\2\u00a2\b\3\2\2\2\u00a3\u00a4\7v\2\2\u00a4")
        buf.write("\u00a5\7t\2\2\u00a5\u00a6\7w\2\2\u00a6\u00a7\7g\2\2\u00a7")
        buf.write("\n\3\2\2\2\u00a8\u00a9\7h\2\2\u00a9\u00aa\7c\2\2\u00aa")
        buf.write("\u00ab\7n\2\2\u00ab\u00ac\7u\2\2\u00ac\u00ad\7g\2\2\u00ad")
        buf.write("\f\3\2\2\2\u00ae\u00af\7p\2\2\u00af\u00b0\7w\2\2\u00b0")
        buf.write("\u00b1\7o\2\2\u00b1\u00b2\7d\2\2\u00b2\u00b3\7g\2\2\u00b3")
        buf.write("\u00b4\7t\2\2\u00b4\16\3\2\2\2\u00b5\u00b6\7d\2\2\u00b6")
        buf.write("\u00b7\7q\2\2\u00b7\u00b8\7q\2\2\u00b8\u00b9\7n\2\2\u00b9")
        buf.write("\20\3\2\2\2\u00ba\u00bb\7u\2\2\u00bb\u00bc\7v\2\2\u00bc")
        buf.write("\u00bd\7t\2\2\u00bd\u00be\7k\2\2\u00be\u00bf\7p\2\2\u00bf")
        buf.write("\u00c0\7i\2\2\u00c0\22\3\2\2\2\u00c1\u00c2\7t\2\2\u00c2")
        buf.write("\u00c3\7g\2\2\u00c3\u00c4\7v\2\2\u00c4\u00c5\7w\2\2\u00c5")
        buf.write("\u00c6\7t\2\2\u00c6\u00c7\7p\2\2\u00c7\24\3\2\2\2\u00c8")
        buf.write("\u00c9\7x\2\2\u00c9\u00ca\7c\2\2\u00ca\u00cb\7t\2\2\u00cb")
        buf.write("\26\3\2\2\2\u00cc\u00cd\7f\2\2\u00cd\u00ce\7{\2\2\u00ce")
        buf.write("\u00cf\7p\2\2\u00cf\u00d0\7c\2\2\u00d0\u00d1\7o\2\2\u00d1")
        buf.write("\u00d2\7k\2\2\u00d2\u00d3\7e\2\2\u00d3\30\3\2\2\2\u00d4")
        buf.write("\u00d5\7h\2\2\u00d5\u00d6\7w\2\2\u00d6\u00d7\7p\2\2\u00d7")
        buf.write("\u00d8\7e\2\2\u00d8\32\3\2\2\2\u00d9\u00da\7h\2\2\u00da")
        buf.write("\u00db\7q\2\2\u00db\u00dc\7t\2\2\u00dc\34\3\2\2\2\u00dd")
        buf.write("\u00de\7w\2\2\u00de\u00df\7p\2\2\u00df\u00e0\7v\2\2\u00e0")
        buf.write("\u00e1\7k\2\2\u00e1\u00e2\7n\2\2\u00e2\36\3\2\2\2\u00e3")
        buf.write("\u00e4\7d\2\2\u00e4\u00e5\7{\2\2\u00e5 \3\2\2\2\u00e6")
        buf.write("\u00e7\7d\2\2\u00e7\u00e8\7t\2\2\u00e8\u00e9\7g\2\2\u00e9")
        buf.write("\u00ea\7c\2\2\u00ea\u00eb\7m\2\2\u00eb\"\3\2\2\2\u00ec")
        buf.write("\u00ed\7e\2\2\u00ed\u00ee\7q\2\2\u00ee\u00ef\7p\2\2\u00ef")
        buf.write("\u00f0\7v\2\2\u00f0\u00f1\7k\2\2\u00f1\u00f2\7p\2\2\u00f2")
        buf.write("\u00f3\7w\2\2\u00f3\u00f4\7g\2\2\u00f4$\3\2\2\2\u00f5")
        buf.write("\u00f6\7k\2\2\u00f6\u00f7\7h\2\2\u00f7&\3\2\2\2\u00f8")
        buf.write("\u00f9\7g\2\2\u00f9\u00fa\7n\2\2\u00fa\u00fb\7u\2\2\u00fb")
        buf.write("\u00fc\7g\2\2\u00fc(\3\2\2\2\u00fd\u00fe\7g\2\2\u00fe")
        buf.write("\u00ff\7n\2\2\u00ff\u0100\7k\2\2\u0100\u0101\7h\2\2\u0101")
        buf.write("*\3\2\2\2\u0102\u0103\7d\2\2\u0103\u0104\7g\2\2\u0104")
        buf.write("\u0105\7i\2\2\u0105\u0106\7k\2\2\u0106\u0107\7p\2\2\u0107")
        buf.write(",\3\2\2\2\u0108\u0109\7g\2\2\u0109\u010a\7p\2\2\u010a")
        buf.write("\u010b\7f\2\2\u010b.\3\2\2\2\u010c\u010d\7p\2\2\u010d")
        buf.write("\u010e\7q\2\2\u010e\u010f\7v\2\2\u010f\60\3\2\2\2\u0110")
        buf.write("\u0111\7c\2\2\u0111\u0112\7p\2\2\u0112\u0113\7f\2\2\u0113")
        buf.write("\62\3\2\2\2\u0114\u0115\7q\2\2\u0115\u0116\7t\2\2\u0116")
        buf.write("\64\3\2\2\2\u0117\u0118\7-\2\2\u0118\66\3\2\2\2\u0119")
        buf.write("\u011a\7/\2\2\u011a8\3\2\2\2\u011b\u011c\7,\2\2\u011c")
        buf.write(":\3\2\2\2\u011d\u011e\7\61\2\2\u011e<\3\2\2\2\u011f\u0120")
        buf.write("\7\'\2\2\u0120>\3\2\2\2\u0121\u0122\7>\2\2\u0122\u0123")
        buf.write("\7/\2\2\u0123@\3\2\2\2\u0124\u0125\7?\2\2\u0125B\3\2\2")
        buf.write("\2\u0126\u0127\7#\2\2\u0127\u0128\7?\2\2\u0128D\3\2\2")
        buf.write("\2\u0129\u012a\7>\2\2\u012aF\3\2\2\2\u012b\u012c\7@\2")
        buf.write("\2\u012cH\3\2\2\2\u012d\u012e\7>\2\2\u012e\u012f\7?\2")
        buf.write("\2\u012fJ\3\2\2\2\u0130\u0131\7@\2\2\u0131\u0132\7?\2")
        buf.write("\2\u0132L\3\2\2\2\u0133\u0134\7\60\2\2\u0134\u0135\7\60")
        buf.write("\2\2\u0135\u0136\7\60\2\2\u0136N\3\2\2\2\u0137\u0138\7")
        buf.write("?\2\2\u0138\u0139\7?\2\2\u0139P\3\2\2\2\u013a\u013b\7")
        buf.write(".\2\2\u013bR\3\2\2\2\u013c\u013d\7*\2\2\u013dT\3\2\2\2")
        buf.write("\u013e\u013f\7+\2\2\u013fV\3\2\2\2\u0140\u0141\7]\2\2")
        buf.write("\u0141X\3\2\2\2\u0142\u0143\7_\2\2\u0143Z\3\2\2\2\u0144")
        buf.write("\u0148\t\5\2\2\u0145\u0147\t\6\2\2\u0146\u0145\3\2\2\2")
        buf.write("\u0147\u014a\3\2\2\2\u0148\u0146\3\2\2\2\u0148\u0149\3")
        buf.write("\2\2\2\u0149\\\3\2\2\2\u014a\u0148\3\2\2\2\u014b\u014c")
        buf.write("\t\7\2\2\u014c^\3\2\2\2\u014d\u014e\7^\2\2\u014e\u015c")
        buf.write("\7d\2\2\u014f\u0150\7^\2\2\u0150\u015c\7h\2\2\u0151\u0152")
        buf.write("\7^\2\2\u0152\u015c\7t\2\2\u0153\u0154\7^\2\2\u0154\u015c")
        buf.write("\7p\2\2\u0155\u0156\7^\2\2\u0156\u015c\7v\2\2\u0157\u0158")
        buf.write("\7^\2\2\u0158\u015c\7)\2\2\u0159\u015a\7^\2\2\u015a\u015c")
        buf.write("\7^\2\2\u015b\u014d\3\2\2\2\u015b\u014f\3\2\2\2\u015b")
        buf.write("\u0151\3\2\2\2\u015b\u0153\3\2\2\2\u015b\u0155\3\2\2\2")
        buf.write("\u015b\u0157\3\2\2\2\u015b\u0159\3\2\2\2\u015c`\3\2\2")
        buf.write("\2\u015d\u015e\7\f\2\2\u015eb\3\2\2\2\u015f\u0160\7%\2")
        buf.write("\2\u0160\u0164\7%\2\2\u0161\u0163\13\2\2\2\u0162\u0161")
        buf.write("\3\2\2\2\u0163\u0166\3\2\2\2\u0164\u0165\3\2\2\2\u0164")
        buf.write("\u0162\3\2\2\2\u0165\u0167\3\2\2\2\u0166\u0164\3\2\2\2")
        buf.write("\u0167\u0168\7\f\2\2\u0168\u0169\3\2\2\2\u0169\u016a\b")
        buf.write("\62\2\2\u016ad\3\2\2\2\u016b\u016d\t\b\2\2\u016c\u016b")
        buf.write("\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u016c\3\2\2\2\u016e")
        buf.write("\u016f\3\2\2\2\u016f\u0170\3\2\2\2\u0170\u0171\b\63\2")
        buf.write("\2\u0171f\3\2\2\2\u0172\u0173\13\2\2\2\u0173\u0174\b\64")
        buf.write("\3\2\u0174h\3\2\2\2\u0175\u0176\13\2\2\2\u0176j\3\2\2")
        buf.write("\2\u0177\u0178\13\2\2\2\u0178l\3\2\2\2\20\2pvy}\u0082")
        buf.write("\u0084\u0088\u009c\u009e\u0148\u015b\u0164\u016e\4\b\2")
        buf.write("\2\3\64\2")
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
    MINOP = 27
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
    UNCLOSE_STRING = 50
    ILLEGAL_ESCAPE = 51

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
            "END", "NOT", "AND", "OR", "ADDOP", "MINOP", "MULOP", "DIVOP", 
            "MODOP", "ASSIGNOP", "EQUALOP", "DIFFOP", "SMALLEROP", "GREATEROP", 
            "SEQOP", "GEQOP", "ELLIPOP", "DOUBLEEQOP", "COMMA", "LRB", "RRB", 
            "LSQB", "RSQB", "IDENTIFIER", "LINEBREAK", "COMMENT", "WS", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "NUMLIT", "BOOLLIT", "STRINGLIT", "TRUE", "FALSE", "NUMBER", 
                  "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", "FUNC", 
                  "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", 
                  "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "ADDOP", "MINOP", 
                  "MULOP", "DIVOP", "MODOP", "ASSIGNOP", "EQUALOP", "DIFFOP", 
                  "SMALLEROP", "GREATEROP", "SEQOP", "GEQOP", "ELLIPOP", 
                  "DOUBLEEQOP", "COMMA", "LRB", "RRB", "LSQB", "RSQB", "IDENTIFIER", 
                  "DIGIT", "ESC", "LINEBREAK", "COMMENT", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[50] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


