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
			"COMMA", "LRB", "RRB", "LSQB", "RSQB", "IDENTIFIER", "DIGIT", "LINEBREAK", 
			"COMMENT", "WS"
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
			"'('", "')'", "'['", "']'", null, "'\n'"
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\62\u015c\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t"+
		" \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t"+
		"+\4,\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\3\2\6\2g\n\2\r"+
		"\2\16\2h\3\2\3\2\7\2m\n\2\f\2\16\2p\13\2\5\2r\n\2\3\2\3\2\5\2v\n\2\3\2"+
		"\7\2y\n\2\f\2\16\2|\13\2\5\2~\n\2\3\3\3\3\5\3\u0082\n\3\3\4\3\4\3\4\3"+
		"\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4\u0096\n"+
		"\4\f\4\16\4\u0099\13\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6"+
		"\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3"+
		"\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f"+
		"\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17"+
		"\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22"+
		"\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24"+
		"\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27"+
		"\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32"+
		"\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3\""+
		"\3\"\3\"\3#\3#\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3\'\3(\3(\3(\3)\3)"+
		"\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\7.\u0140\n.\f.\16.\u0143\13.\3/\3/\3\60"+
		"\3\60\3\61\3\61\3\61\7\61\u014c\n\61\f\61\16\61\u014f\13\61\3\61\5\61"+
		"\u0152\n\61\3\61\3\61\3\62\6\62\u0157\n\62\r\62\16\62\u0158\3\62\3\62"+
		"\3\u014d\2\63\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16"+
		"\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34"+
		"\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\2_\60a\61c\62\3\2\n"+
		"\4\2GGgg\4\2--//\5\2$$))^^\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\3\3\f\f\5"+
		"\2\n\13\16\17\"\"\2\u016d\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2"+
		"\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2"+
		"\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3"+
		"\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2"+
		"\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67"+
		"\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2"+
		"\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2"+
		"\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2_"+
		"\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\3f\3\2\2\2\5\u0081\3\2\2\2\7\u0083\3\2"+
		"\2\2\t\u009c\3\2\2\2\13\u00a1\3\2\2\2\r\u00a7\3\2\2\2\17\u00ae\3\2\2\2"+
		"\21\u00b3\3\2\2\2\23\u00ba\3\2\2\2\25\u00c1\3\2\2\2\27\u00c5\3\2\2\2\31"+
		"\u00cd\3\2\2\2\33\u00d2\3\2\2\2\35\u00d6\3\2\2\2\37\u00dc\3\2\2\2!\u00df"+
		"\3\2\2\2#\u00e5\3\2\2\2%\u00ee\3\2\2\2\'\u00f1\3\2\2\2)\u00f6\3\2\2\2"+
		"+\u00fb\3\2\2\2-\u0101\3\2\2\2/\u0105\3\2\2\2\61\u0109\3\2\2\2\63\u010d"+
		"\3\2\2\2\65\u0110\3\2\2\2\67\u0112\3\2\2\29\u0114\3\2\2\2;\u0116\3\2\2"+
		"\2=\u0118\3\2\2\2?\u011a\3\2\2\2A\u011d\3\2\2\2C\u011f\3\2\2\2E\u0122"+
		"\3\2\2\2G\u0124\3\2\2\2I\u0126\3\2\2\2K\u0129\3\2\2\2M\u012c\3\2\2\2O"+
		"\u0130\3\2\2\2Q\u0133\3\2\2\2S\u0135\3\2\2\2U\u0137\3\2\2\2W\u0139\3\2"+
		"\2\2Y\u013b\3\2\2\2[\u013d\3\2\2\2]\u0144\3\2\2\2_\u0146\3\2\2\2a\u0148"+
		"\3\2\2\2c\u0156\3\2\2\2eg\5]/\2fe\3\2\2\2gh\3\2\2\2hf\3\2\2\2hi\3\2\2"+
		"\2iq\3\2\2\2jn\7\60\2\2km\5]/\2lk\3\2\2\2mp\3\2\2\2nl\3\2\2\2no\3\2\2"+
		"\2or\3\2\2\2pn\3\2\2\2qj\3\2\2\2qr\3\2\2\2r}\3\2\2\2su\t\2\2\2tv\t\3\2"+
		"\2ut\3\2\2\2uv\3\2\2\2vz\3\2\2\2wy\5]/\2xw\3\2\2\2y|\3\2\2\2zx\3\2\2\2"+
		"z{\3\2\2\2{~\3\2\2\2|z\3\2\2\2}s\3\2\2\2}~\3\2\2\2~\4\3\2\2\2\177\u0082"+
		"\5\t\5\2\u0080\u0082\5\13\6\2\u0081\177\3\2\2\2\u0081\u0080\3\2\2\2\u0082"+
		"\6\3\2\2\2\u0083\u0097\7$\2\2\u0084\u0085\7^\2\2\u0085\u0096\7d\2\2\u0086"+
		"\u0087\7^\2\2\u0087\u0096\7h\2\2\u0088\u0089\7^\2\2\u0089\u0096\7t\2\2"+
		"\u008a\u008b\7^\2\2\u008b\u0096\7p\2\2\u008c\u008d\7^\2\2\u008d\u0096"+
		"\7v\2\2\u008e\u008f\7^\2\2\u008f\u0096\7)\2\2\u0090\u0091\7^\2\2\u0091"+
		"\u0096\7^\2\2\u0092\u0093\7)\2\2\u0093\u0096\7$\2\2\u0094\u0096\n\4\2"+
		"\2\u0095\u0084\3\2\2\2\u0095\u0086\3\2\2\2\u0095\u0088\3\2\2\2\u0095\u008a"+
		"\3\2\2\2\u0095\u008c\3\2\2\2\u0095\u008e\3\2\2\2\u0095\u0090\3\2\2\2\u0095"+
		"\u0092\3\2\2\2\u0095\u0094\3\2\2\2\u0096\u0099\3\2\2\2\u0097\u0095\3\2"+
		"\2\2\u0097\u0098\3\2\2\2\u0098\u009a\3\2\2\2\u0099\u0097\3\2\2\2\u009a"+
		"\u009b\7$\2\2\u009b\b\3\2\2\2\u009c\u009d\7v\2\2\u009d\u009e\7t\2\2\u009e"+
		"\u009f\7w\2\2\u009f\u00a0\7g\2\2\u00a0\n\3\2\2\2\u00a1\u00a2\7h\2\2\u00a2"+
		"\u00a3\7c\2\2\u00a3\u00a4\7n\2\2\u00a4\u00a5\7u\2\2\u00a5\u00a6\7g\2\2"+
		"\u00a6\f\3\2\2\2\u00a7\u00a8\7p\2\2\u00a8\u00a9\7w\2\2\u00a9\u00aa\7o"+
		"\2\2\u00aa\u00ab\7d\2\2\u00ab\u00ac\7g\2\2\u00ac\u00ad\7t\2\2\u00ad\16"+
		"\3\2\2\2\u00ae\u00af\7d\2\2\u00af\u00b0\7q\2\2\u00b0\u00b1\7q\2\2\u00b1"+
		"\u00b2\7n\2\2\u00b2\20\3\2\2\2\u00b3\u00b4\7u\2\2\u00b4\u00b5\7v\2\2\u00b5"+
		"\u00b6\7t\2\2\u00b6\u00b7\7k\2\2\u00b7\u00b8\7p\2\2\u00b8\u00b9\7i\2\2"+
		"\u00b9\22\3\2\2\2\u00ba\u00bb\7t\2\2\u00bb\u00bc\7g\2\2\u00bc\u00bd\7"+
		"v\2\2\u00bd\u00be\7w\2\2\u00be\u00bf\7t\2\2\u00bf\u00c0\7p\2\2\u00c0\24"+
		"\3\2\2\2\u00c1\u00c2\7x\2\2\u00c2\u00c3\7c\2\2\u00c3\u00c4\7t\2\2\u00c4"+
		"\26\3\2\2\2\u00c5\u00c6\7f\2\2\u00c6\u00c7\7{\2\2\u00c7\u00c8\7p\2\2\u00c8"+
		"\u00c9\7c\2\2\u00c9\u00ca\7o\2\2\u00ca\u00cb\7k\2\2\u00cb\u00cc\7e\2\2"+
		"\u00cc\30\3\2\2\2\u00cd\u00ce\7h\2\2\u00ce\u00cf\7w\2\2\u00cf\u00d0\7"+
		"p\2\2\u00d0\u00d1\7e\2\2\u00d1\32\3\2\2\2\u00d2\u00d3\7h\2\2\u00d3\u00d4"+
		"\7q\2\2\u00d4\u00d5\7t\2\2\u00d5\34\3\2\2\2\u00d6\u00d7\7w\2\2\u00d7\u00d8"+
		"\7p\2\2\u00d8\u00d9\7v\2\2\u00d9\u00da\7k\2\2\u00da\u00db\7n\2\2\u00db"+
		"\36\3\2\2\2\u00dc\u00dd\7d\2\2\u00dd\u00de\7{\2\2\u00de \3\2\2\2\u00df"+
		"\u00e0\7d\2\2\u00e0\u00e1\7t\2\2\u00e1\u00e2\7g\2\2\u00e2\u00e3\7c\2\2"+
		"\u00e3\u00e4\7m\2\2\u00e4\"\3\2\2\2\u00e5\u00e6\7e\2\2\u00e6\u00e7\7q"+
		"\2\2\u00e7\u00e8\7p\2\2\u00e8\u00e9\7v\2\2\u00e9\u00ea\7k\2\2\u00ea\u00eb"+
		"\7p\2\2\u00eb\u00ec\7w\2\2\u00ec\u00ed\7g\2\2\u00ed$\3\2\2\2\u00ee\u00ef"+
		"\7k\2\2\u00ef\u00f0\7h\2\2\u00f0&\3\2\2\2\u00f1\u00f2\7g\2\2\u00f2\u00f3"+
		"\7n\2\2\u00f3\u00f4\7u\2\2\u00f4\u00f5\7g\2\2\u00f5(\3\2\2\2\u00f6\u00f7"+
		"\7g\2\2\u00f7\u00f8\7n\2\2\u00f8\u00f9\7k\2\2\u00f9\u00fa\7h\2\2\u00fa"+
		"*\3\2\2\2\u00fb\u00fc\7d\2\2\u00fc\u00fd\7g\2\2\u00fd\u00fe\7i\2\2\u00fe"+
		"\u00ff\7k\2\2\u00ff\u0100\7p\2\2\u0100,\3\2\2\2\u0101\u0102\7g\2\2\u0102"+
		"\u0103\7p\2\2\u0103\u0104\7f\2\2\u0104.\3\2\2\2\u0105\u0106\7p\2\2\u0106"+
		"\u0107\7q\2\2\u0107\u0108\7v\2\2\u0108\60\3\2\2\2\u0109\u010a\7c\2\2\u010a"+
		"\u010b\7p\2\2\u010b\u010c\7f\2\2\u010c\62\3\2\2\2\u010d\u010e\7q\2\2\u010e"+
		"\u010f\7t\2\2\u010f\64\3\2\2\2\u0110\u0111\7-\2\2\u0111\66\3\2\2\2\u0112"+
		"\u0113\7/\2\2\u01138\3\2\2\2\u0114\u0115\7,\2\2\u0115:\3\2\2\2\u0116\u0117"+
		"\7\61\2\2\u0117<\3\2\2\2\u0118\u0119\7\'\2\2\u0119>\3\2\2\2\u011a\u011b"+
		"\7>\2\2\u011b\u011c\7/\2\2\u011c@\3\2\2\2\u011d\u011e\7?\2\2\u011eB\3"+
		"\2\2\2\u011f\u0120\7#\2\2\u0120\u0121\7?\2\2\u0121D\3\2\2\2\u0122\u0123"+
		"\7>\2\2\u0123F\3\2\2\2\u0124\u0125\7@\2\2\u0125H\3\2\2\2\u0126\u0127\7"+
		">\2\2\u0127\u0128\7?\2\2\u0128J\3\2\2\2\u0129\u012a\7@\2\2\u012a\u012b"+
		"\7?\2\2\u012bL\3\2\2\2\u012c\u012d\7\60\2\2\u012d\u012e\7\60\2\2\u012e"+
		"\u012f\7\60\2\2\u012fN\3\2\2\2\u0130\u0131\7?\2\2\u0131\u0132\7?\2\2\u0132"+
		"P\3\2\2\2\u0133\u0134\7.\2\2\u0134R\3\2\2\2\u0135\u0136\7*\2\2\u0136T"+
		"\3\2\2\2\u0137\u0138\7+\2\2\u0138V\3\2\2\2\u0139\u013a\7]\2\2\u013aX\3"+
		"\2\2\2\u013b\u013c\7_\2\2\u013cZ\3\2\2\2\u013d\u0141\t\5\2\2\u013e\u0140"+
		"\t\6\2\2\u013f\u013e\3\2\2\2\u0140\u0143\3\2\2\2\u0141\u013f\3\2\2\2\u0141"+
		"\u0142\3\2\2\2\u0142\\\3\2\2\2\u0143\u0141\3\2\2\2\u0144\u0145\t\7\2\2"+
		"\u0145^\3\2\2\2\u0146\u0147\7\f\2\2\u0147`\3\2\2\2\u0148\u0149\7%\2\2"+
		"\u0149\u014d\7%\2\2\u014a\u014c\13\2\2\2\u014b\u014a\3\2\2\2\u014c\u014f"+
		"\3\2\2\2\u014d\u014e\3\2\2\2\u014d\u014b\3\2\2\2\u014e\u0151\3\2\2\2\u014f"+
		"\u014d\3\2\2\2\u0150\u0152\t\b\2\2\u0151\u0150\3\2\2\2\u0152\u0153\3\2"+
		"\2\2\u0153\u0154\b\61\2\2\u0154b\3\2\2\2\u0155\u0157\t\t\2\2\u0156\u0155"+
		"\3\2\2\2\u0157\u0158\3\2\2\2\u0158\u0156\3\2\2\2\u0158\u0159\3\2\2\2\u0159"+
		"\u015a\3\2\2\2\u015a\u015b\b\62\2\2\u015bd\3\2\2\2\20\2hnquz}\u0081\u0095"+
		"\u0097\u0141\u014d\u0151\u0158\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}