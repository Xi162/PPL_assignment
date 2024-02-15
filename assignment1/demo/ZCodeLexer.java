// Generated from ZCode.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class ZCodeLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		NUMLIT=1, BOOLLIT=2, STRINGLIT=3, TRUE=4, FALSE=5, NUMBER=6, BOOL=7, STRING=8, 
		RETURN=9, VAR=10, DYNAMIC=11, FUNC=12, FOR=13, UNTIL=14, BY=15, BREAK=16, 
		CONTINUE=17, IF=18, ELSE=19, ELIF=20, BEGIN=21, END=22, NOT=23, AND=24, 
		OR=25, ADDOP=26, SUBOP=27, MULOP=28, DIVOP=29, MODOP=30, ASSIGNOP=31, 
		EQUALOP=32, DIFFOP=33, SMALLEROP=34, GREATEROP=35, SEQOP=36, GEQOP=37, 
		ELLIPOP=38, DOUBLEEQOP=39, COMMA=40, LRB=41, RRB=42, LSQB=43, RSQB=44, 
		IDENTIFIER=45, LINEBREAK=46, COMMENT=47, WS=48;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"NUMLIT", "BOOLLIT", "STRINGLIT", "TRUE", "FALSE", "NUMBER", "BOOL", 
			"STRING", "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
			"CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", 
			"ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", "ASSIGNOP", "EQUALOP", "DIFFOP", 
			"SMALLEROP", "GREATEROP", "SEQOP", "GEQOP", "ELLIPOP", "DOUBLEEQOP", 
			"COMMA", "LRB", "RRB", "LSQB", "RSQB", "IDENTIFIER", "DIGIT", "BACKSPACEESC", 
			"FORMFEEDESC", "CARRETURNESC", "NEWLINEESC", "TABESC", "SQUOTEESC", "BACKLASHESC", 
			"DQUOTEESC", "ESC", "LINEBREAK", "COMMENT", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, "'true'", "'false'", "'number'", "'bool'", "'string'", 
			"'return'", "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
			"'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", "'end'", 
			"'not'", "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", "'<-'", 
			"'='", "'!='", "'<'", "'>'", "'<='", "'>='", "'...'", "'=='", "','", 
			"'('", "')'", "'['", "']'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "NUMLIT", "BOOLLIT", "STRINGLIT", "TRUE", "FALSE", "NUMBER", "BOOL", 
			"STRING", "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
			"CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", 
			"ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", "ASSIGNOP", "EQUALOP", "DIFFOP", 
			"SMALLEROP", "GREATEROP", "SEQOP", "GEQOP", "ELLIPOP", "DOUBLEEQOP", 
			"COMMA", "LRB", "RRB", "LSQB", "RSQB", "IDENTIFIER", "LINEBREAK", "COMMENT", 
			"WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public ZCodeLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "ZCode.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\62\u0184\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t"+
		" \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t"+
		"+\4,\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64"+
		"\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\3\2\6\2y\n"+
		"\2\r\2\16\2z\3\2\3\2\7\2\177\n\2\f\2\16\2\u0082\13\2\5\2\u0084\n\2\3\2"+
		"\3\2\5\2\u0088\n\2\3\2\6\2\u008b\n\2\r\2\16\2\u008c\5\2\u008f\n\2\3\3"+
		"\3\3\5\3\u0093\n\3\3\4\3\4\3\4\7\4\u0098\n\4\f\4\16\4\u009b\13\4\3\4\3"+
		"\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7"+
		"\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3"+
		"\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r"+
		"\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3"+
		"\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3"+
		"\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3"+
		"\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3"+
		"\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3"+
		"\35\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3%\3%\3"+
		"%\3&\3&\3&\3\'\3\'\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3"+
		".\7.\u0142\n.\f.\16.\u0145\13.\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3\62"+
		"\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66"+
		"\3\67\3\67\3\67\38\38\38\38\38\38\38\38\58\u0169\n8\39\39\39\59\u016e"+
		"\n9\3:\3:\3:\7:\u0173\n:\f:\16:\u0176\13:\3:\3:\5:\u017a\n:\3:\3:\3;\6"+
		";\u017f\n;\r;\16;\u0180\3;\3;\2\2<\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n"+
		"\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30"+
		"/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.["+
		"/]\2_\2a\2c\2e\2g\2i\2k\2m\2o\2q\60s\61u\62\3\2\n\4\2GGgg\4\2--//\6\2"+
		"\f\f\17\17$$^^\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\4\2\f\f\17\17\5\2\n\13"+
		"\16\16\"\"\2\u018e\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13"+
		"\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2"+
		"\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2"+
		"!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3"+
		"\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2"+
		"\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E"+
		"\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2"+
		"\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2q\3\2\2\2"+
		"\2s\3\2\2\2\2u\3\2\2\2\3x\3\2\2\2\5\u0092\3\2\2\2\7\u0094\3\2\2\2\t\u009e"+
		"\3\2\2\2\13\u00a3\3\2\2\2\r\u00a9\3\2\2\2\17\u00b0\3\2\2\2\21\u00b5\3"+
		"\2\2\2\23\u00bc\3\2\2\2\25\u00c3\3\2\2\2\27\u00c7\3\2\2\2\31\u00cf\3\2"+
		"\2\2\33\u00d4\3\2\2\2\35\u00d8\3\2\2\2\37\u00de\3\2\2\2!\u00e1\3\2\2\2"+
		"#\u00e7\3\2\2\2%\u00f0\3\2\2\2\'\u00f3\3\2\2\2)\u00f8\3\2\2\2+\u00fd\3"+
		"\2\2\2-\u0103\3\2\2\2/\u0107\3\2\2\2\61\u010b\3\2\2\2\63\u010f\3\2\2\2"+
		"\65\u0112\3\2\2\2\67\u0114\3\2\2\29\u0116\3\2\2\2;\u0118\3\2\2\2=\u011a"+
		"\3\2\2\2?\u011c\3\2\2\2A\u011f\3\2\2\2C\u0121\3\2\2\2E\u0124\3\2\2\2G"+
		"\u0126\3\2\2\2I\u0128\3\2\2\2K\u012b\3\2\2\2M\u012e\3\2\2\2O\u0132\3\2"+
		"\2\2Q\u0135\3\2\2\2S\u0137\3\2\2\2U\u0139\3\2\2\2W\u013b\3\2\2\2Y\u013d"+
		"\3\2\2\2[\u013f\3\2\2\2]\u0146\3\2\2\2_\u0148\3\2\2\2a\u014b\3\2\2\2c"+
		"\u014e\3\2\2\2e\u0151\3\2\2\2g\u0154\3\2\2\2i\u0157\3\2\2\2k\u015a\3\2"+
		"\2\2m\u015d\3\2\2\2o\u0168\3\2\2\2q\u016d\3\2\2\2s\u016f\3\2\2\2u\u017e"+
		"\3\2\2\2wy\5]/\2xw\3\2\2\2yz\3\2\2\2zx\3\2\2\2z{\3\2\2\2{\u0083\3\2\2"+
		"\2|\u0080\7\60\2\2}\177\5]/\2~}\3\2\2\2\177\u0082\3\2\2\2\u0080~\3\2\2"+
		"\2\u0080\u0081\3\2\2\2\u0081\u0084\3\2\2\2\u0082\u0080\3\2\2\2\u0083|"+
		"\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u008e\3\2\2\2\u0085\u0087\t\2\2\2\u0086"+
		"\u0088\t\3\2\2\u0087\u0086\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u008a\3\2"+
		"\2\2\u0089\u008b\5]/\2\u008a\u0089\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008a"+
		"\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u008f\3\2\2\2\u008e\u0085\3\2\2\2\u008e"+
		"\u008f\3\2\2\2\u008f\4\3\2\2\2\u0090\u0093\5\t\5\2\u0091\u0093\5\13\6"+
		"\2\u0092\u0090\3\2\2\2\u0092\u0091\3\2\2\2\u0093\6\3\2\2\2\u0094\u0099"+
		"\7$\2\2\u0095\u0098\5o8\2\u0096\u0098\n\4\2\2\u0097\u0095\3\2\2\2\u0097"+
		"\u0096\3\2\2\2\u0098\u009b\3\2\2\2\u0099\u0097\3\2\2\2\u0099\u009a\3\2"+
		"\2\2\u009a\u009c\3\2\2\2\u009b\u0099\3\2\2\2\u009c\u009d\7$\2\2\u009d"+
		"\b\3\2\2\2\u009e\u009f\7v\2\2\u009f\u00a0\7t\2\2\u00a0\u00a1\7w\2\2\u00a1"+
		"\u00a2\7g\2\2\u00a2\n\3\2\2\2\u00a3\u00a4\7h\2\2\u00a4\u00a5\7c\2\2\u00a5"+
		"\u00a6\7n\2\2\u00a6\u00a7\7u\2\2\u00a7\u00a8\7g\2\2\u00a8\f\3\2\2\2\u00a9"+
		"\u00aa\7p\2\2\u00aa\u00ab\7w\2\2\u00ab\u00ac\7o\2\2\u00ac\u00ad\7d\2\2"+
		"\u00ad\u00ae\7g\2\2\u00ae\u00af\7t\2\2\u00af\16\3\2\2\2\u00b0\u00b1\7"+
		"d\2\2\u00b1\u00b2\7q\2\2\u00b2\u00b3\7q\2\2\u00b3\u00b4\7n\2\2\u00b4\20"+
		"\3\2\2\2\u00b5\u00b6\7u\2\2\u00b6\u00b7\7v\2\2\u00b7\u00b8\7t\2\2\u00b8"+
		"\u00b9\7k\2\2\u00b9\u00ba\7p\2\2\u00ba\u00bb\7i\2\2\u00bb\22\3\2\2\2\u00bc"+
		"\u00bd\7t\2\2\u00bd\u00be\7g\2\2\u00be\u00bf\7v\2\2\u00bf\u00c0\7w\2\2"+
		"\u00c0\u00c1\7t\2\2\u00c1\u00c2\7p\2\2\u00c2\24\3\2\2\2\u00c3\u00c4\7"+
		"x\2\2\u00c4\u00c5\7c\2\2\u00c5\u00c6\7t\2\2\u00c6\26\3\2\2\2\u00c7\u00c8"+
		"\7f\2\2\u00c8\u00c9\7{\2\2\u00c9\u00ca\7p\2\2\u00ca\u00cb\7c\2\2\u00cb"+
		"\u00cc\7o\2\2\u00cc\u00cd\7k\2\2\u00cd\u00ce\7e\2\2\u00ce\30\3\2\2\2\u00cf"+
		"\u00d0\7h\2\2\u00d0\u00d1\7w\2\2\u00d1\u00d2\7p\2\2\u00d2\u00d3\7e\2\2"+
		"\u00d3\32\3\2\2\2\u00d4\u00d5\7h\2\2\u00d5\u00d6\7q\2\2\u00d6\u00d7\7"+
		"t\2\2\u00d7\34\3\2\2\2\u00d8\u00d9\7w\2\2\u00d9\u00da\7p\2\2\u00da\u00db"+
		"\7v\2\2\u00db\u00dc\7k\2\2\u00dc\u00dd\7n\2\2\u00dd\36\3\2\2\2\u00de\u00df"+
		"\7d\2\2\u00df\u00e0\7{\2\2\u00e0 \3\2\2\2\u00e1\u00e2\7d\2\2\u00e2\u00e3"+
		"\7t\2\2\u00e3\u00e4\7g\2\2\u00e4\u00e5\7c\2\2\u00e5\u00e6\7m\2\2\u00e6"+
		"\"\3\2\2\2\u00e7\u00e8\7e\2\2\u00e8\u00e9\7q\2\2\u00e9\u00ea\7p\2\2\u00ea"+
		"\u00eb\7v\2\2\u00eb\u00ec\7k\2\2\u00ec\u00ed\7p\2\2\u00ed\u00ee\7w\2\2"+
		"\u00ee\u00ef\7g\2\2\u00ef$\3\2\2\2\u00f0\u00f1\7k\2\2\u00f1\u00f2\7h\2"+
		"\2\u00f2&\3\2\2\2\u00f3\u00f4\7g\2\2\u00f4\u00f5\7n\2\2\u00f5\u00f6\7"+
		"u\2\2\u00f6\u00f7\7g\2\2\u00f7(\3\2\2\2\u00f8\u00f9\7g\2\2\u00f9\u00fa"+
		"\7n\2\2\u00fa\u00fb\7k\2\2\u00fb\u00fc\7h\2\2\u00fc*\3\2\2\2\u00fd\u00fe"+
		"\7d\2\2\u00fe\u00ff\7g\2\2\u00ff\u0100\7i\2\2\u0100\u0101\7k\2\2\u0101"+
		"\u0102\7p\2\2\u0102,\3\2\2\2\u0103\u0104\7g\2\2\u0104\u0105\7p\2\2\u0105"+
		"\u0106\7f\2\2\u0106.\3\2\2\2\u0107\u0108\7p\2\2\u0108\u0109\7q\2\2\u0109"+
		"\u010a\7v\2\2\u010a\60\3\2\2\2\u010b\u010c\7c\2\2\u010c\u010d\7p\2\2\u010d"+
		"\u010e\7f\2\2\u010e\62\3\2\2\2\u010f\u0110\7q\2\2\u0110\u0111\7t\2\2\u0111"+
		"\64\3\2\2\2\u0112\u0113\7-\2\2\u0113\66\3\2\2\2\u0114\u0115\7/\2\2\u0115"+
		"8\3\2\2\2\u0116\u0117\7,\2\2\u0117:\3\2\2\2\u0118\u0119\7\61\2\2\u0119"+
		"<\3\2\2\2\u011a\u011b\7\'\2\2\u011b>\3\2\2\2\u011c\u011d\7>\2\2\u011d"+
		"\u011e\7/\2\2\u011e@\3\2\2\2\u011f\u0120\7?\2\2\u0120B\3\2\2\2\u0121\u0122"+
		"\7#\2\2\u0122\u0123\7?\2\2\u0123D\3\2\2\2\u0124\u0125\7>\2\2\u0125F\3"+
		"\2\2\2\u0126\u0127\7@\2\2\u0127H\3\2\2\2\u0128\u0129\7>\2\2\u0129\u012a"+
		"\7?\2\2\u012aJ\3\2\2\2\u012b\u012c\7@\2\2\u012c\u012d\7?\2\2\u012dL\3"+
		"\2\2\2\u012e\u012f\7\60\2\2\u012f\u0130\7\60\2\2\u0130\u0131\7\60\2\2"+
		"\u0131N\3\2\2\2\u0132\u0133\7?\2\2\u0133\u0134\7?\2\2\u0134P\3\2\2\2\u0135"+
		"\u0136\7.\2\2\u0136R\3\2\2\2\u0137\u0138\7*\2\2\u0138T\3\2\2\2\u0139\u013a"+
		"\7+\2\2\u013aV\3\2\2\2\u013b\u013c\7]\2\2\u013cX\3\2\2\2\u013d\u013e\7"+
		"_\2\2\u013eZ\3\2\2\2\u013f\u0143\t\5\2\2\u0140\u0142\t\6\2\2\u0141\u0140"+
		"\3\2\2\2\u0142\u0145\3\2\2\2\u0143\u0141\3\2\2\2\u0143\u0144\3\2\2\2\u0144"+
		"\\\3\2\2\2\u0145\u0143\3\2\2\2\u0146\u0147\t\7\2\2\u0147^\3\2\2\2\u0148"+
		"\u0149\7^\2\2\u0149\u014a\7d\2\2\u014a`\3\2\2\2\u014b\u014c\7^\2\2\u014c"+
		"\u014d\7h\2\2\u014db\3\2\2\2\u014e\u014f\7^\2\2\u014f\u0150\7t\2\2\u0150"+
		"d\3\2\2\2\u0151\u0152\7^\2\2\u0152\u0153\7p\2\2\u0153f\3\2\2\2\u0154\u0155"+
		"\7^\2\2\u0155\u0156\7v\2\2\u0156h\3\2\2\2\u0157\u0158\7^\2\2\u0158\u0159"+
		"\7)\2\2\u0159j\3\2\2\2\u015a\u015b\7^\2\2\u015b\u015c\7^\2\2\u015cl\3"+
		"\2\2\2\u015d\u015e\7)\2\2\u015e\u015f\7$\2\2\u015fn\3\2\2\2\u0160\u0169"+
		"\5_\60\2\u0161\u0169\5a\61\2\u0162\u0169\5c\62\2\u0163\u0169\5e\63\2\u0164"+
		"\u0169\5g\64\2\u0165\u0169\5i\65\2\u0166\u0169\5k\66\2\u0167\u0169\5m"+
		"\67\2\u0168\u0160\3\2\2\2\u0168\u0161\3\2\2\2\u0168\u0162\3\2\2\2\u0168"+
		"\u0163\3\2\2\2\u0168\u0164\3\2\2\2\u0168\u0165\3\2\2\2\u0168\u0166\3\2"+
		"\2\2\u0168\u0167\3\2\2\2\u0169p\3\2\2\2\u016a\u016e\t\b\2\2\u016b\u016c"+
		"\7\17\2\2\u016c\u016e\7\f\2\2\u016d\u016a\3\2\2\2\u016d\u016b\3\2\2\2"+
		"\u016er\3\2\2\2\u016f\u0170\7%\2\2\u0170\u0174\7%\2\2\u0171\u0173\n\b"+
		"\2\2\u0172\u0171\3\2\2\2\u0173\u0176\3\2\2\2\u0174\u0172\3\2\2\2\u0174"+
		"\u0175\3\2\2\2\u0175\u0179\3\2\2\2\u0176\u0174\3\2\2\2\u0177\u017a\7\2"+
		"\2\3\u0178\u017a\3\2\2\2\u0179\u0177\3\2\2\2\u0179\u0178\3\2\2\2\u017a"+
		"\u017b\3\2\2\2\u017b\u017c\b:\2\2\u017ct\3\2\2\2\u017d\u017f\t\t\2\2\u017e"+
		"\u017d\3\2\2\2\u017f\u0180\3\2\2\2\u0180\u017e\3\2\2\2\u0180\u0181\3\2"+
		"\2\2\u0181\u0182\3\2\2\2\u0182\u0183\b;\2\2\u0183v\3\2\2\2\22\2z\u0080"+
		"\u0083\u0087\u008c\u008e\u0092\u0097\u0099\u0143\u0168\u016d\u0174\u0179"+
		"\u0180\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}