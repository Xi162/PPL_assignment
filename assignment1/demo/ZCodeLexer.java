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
		TYPE=1, NUMLIT=2, BOOLLIT=3, STRINGLIT=4, TRUE=5, FALSE=6, NUMBER=7, BOOL=8, 
		STRING=9, RETURN=10, VAR=11, DYNAMIC=12, FUNC=13, FOR=14, UNTIL=15, BY=16, 
		BREAK=17, CONTINUE=18, IF=19, ELSE=20, ELIF=21, BEGIN=22, END=23, NOT=24, 
		AND=25, OR=26, ADDOP=27, SUBOP=28, MULOP=29, DIVOP=30, MODOP=31, ASSIGNOP=32, 
		EQUALOP=33, DIFFOP=34, SMALLEROP=35, GREATEROP=36, SEQOP=37, GEQOP=38, 
		ELLIPOP=39, DOUBLEEQOP=40, COMMA=41, LRB=42, RRB=43, LSQB=44, RSQB=45, 
		IDENTIFIER=46, LINEBREAK=47, COMMENT=48, WS=49;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"TYPE", "NUMLIT", "BOOLLIT", "STRINGLIT", "TRUE", "FALSE", "NUMBER", 
			"BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", 
			"BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", 
			"AND", "OR", "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", "ASSIGNOP", 
			"EQUALOP", "DIFFOP", "SMALLEROP", "GREATEROP", "SEQOP", "GEQOP", "ELLIPOP", 
			"DOUBLEEQOP", "COMMA", "LRB", "RRB", "LSQB", "RSQB", "IDENTIFIER", "DIGIT", 
			"LINEBREAK", "COMMENT", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, "'true'", "'false'", "'number'", "'bool'", 
			"'string'", "'return'", "'var'", "'dynamic'", "'func'", "'for'", "'until'", 
			"'by'", "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
			"'end'", "'not'", "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", 
			"'<-'", "'='", "'!='", "'<'", "'>'", "'<='", "'>='", "'...'", "'=='", 
			"','", "'('", "')'", "'['", "']'", null, "'\n'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "TYPE", "NUMLIT", "BOOLLIT", "STRINGLIT", "TRUE", "FALSE", "NUMBER", 
			"BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", 
			"BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", 
			"AND", "OR", "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", "ASSIGNOP", 
			"EQUALOP", "DIFFOP", "SMALLEROP", "GREATEROP", "SEQOP", "GEQOP", "ELLIPOP", 
			"DOUBLEEQOP", "COMMA", "LRB", "RRB", "LSQB", "RSQB", "IDENTIFIER", "LINEBREAK", 
			"COMMENT", "WS"
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\63\u0163\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t"+
		" \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t"+
		"+\4,\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\3\2"+
		"\3\2\3\2\5\2k\n\2\3\3\6\3n\n\3\r\3\16\3o\3\3\3\3\7\3t\n\3\f\3\16\3w\13"+
		"\3\5\3y\n\3\3\3\3\3\5\3}\n\3\3\3\7\3\u0080\n\3\f\3\16\3\u0083\13\3\5\3"+
		"\u0085\n\3\3\4\3\4\5\4\u0089\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3"+
		"\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5\u009d\n\5\f\5\16\5\u00a0\13\5\3"+
		"\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b"+
		"\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13"+
		"\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3"+
		"\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3"+
		"\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3"+
		"\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3"+
		"\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3"+
		"\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\35\3"+
		"\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3"+
		"&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3(\3)\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3"+
		".\3/\3/\7/\u0147\n/\f/\16/\u014a\13/\3\60\3\60\3\61\3\61\3\62\3\62\3\62"+
		"\7\62\u0153\n\62\f\62\16\62\u0156\13\62\3\62\5\62\u0159\n\62\3\62\3\62"+
		"\3\63\6\63\u015e\n\63\r\63\16\63\u015f\3\63\3\63\3\u0154\2\64\3\3\5\4"+
		"\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22"+
		"#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C"+
		"#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\2a\61c\62e\63\3\2\n\4\2GGgg\4\2--//\5"+
		"\2$$))^^\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\3\3\f\f\5\2\n\13\16\17\"\""+
		"\2\u0176\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2"+
		"\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27"+
		"\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2"+
		"\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2"+
		"\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2"+
		"\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2"+
		"\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S"+
		"\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2a\3\2"+
		"\2\2\2c\3\2\2\2\2e\3\2\2\2\3j\3\2\2\2\5m\3\2\2\2\7\u0088\3\2\2\2\t\u008a"+
		"\3\2\2\2\13\u00a3\3\2\2\2\r\u00a8\3\2\2\2\17\u00ae\3\2\2\2\21\u00b5\3"+
		"\2\2\2\23\u00ba\3\2\2\2\25\u00c1\3\2\2\2\27\u00c8\3\2\2\2\31\u00cc\3\2"+
		"\2\2\33\u00d4\3\2\2\2\35\u00d9\3\2\2\2\37\u00dd\3\2\2\2!\u00e3\3\2\2\2"+
		"#\u00e6\3\2\2\2%\u00ec\3\2\2\2\'\u00f5\3\2\2\2)\u00f8\3\2\2\2+\u00fd\3"+
		"\2\2\2-\u0102\3\2\2\2/\u0108\3\2\2\2\61\u010c\3\2\2\2\63\u0110\3\2\2\2"+
		"\65\u0114\3\2\2\2\67\u0117\3\2\2\29\u0119\3\2\2\2;\u011b\3\2\2\2=\u011d"+
		"\3\2\2\2?\u011f\3\2\2\2A\u0121\3\2\2\2C\u0124\3\2\2\2E\u0126\3\2\2\2G"+
		"\u0129\3\2\2\2I\u012b\3\2\2\2K\u012d\3\2\2\2M\u0130\3\2\2\2O\u0133\3\2"+
		"\2\2Q\u0137\3\2\2\2S\u013a\3\2\2\2U\u013c\3\2\2\2W\u013e\3\2\2\2Y\u0140"+
		"\3\2\2\2[\u0142\3\2\2\2]\u0144\3\2\2\2_\u014b\3\2\2\2a\u014d\3\2\2\2c"+
		"\u014f\3\2\2\2e\u015d\3\2\2\2gk\5\17\b\2hk\5\21\t\2ik\5\23\n\2jg\3\2\2"+
		"\2jh\3\2\2\2ji\3\2\2\2k\4\3\2\2\2ln\5_\60\2ml\3\2\2\2no\3\2\2\2om\3\2"+
		"\2\2op\3\2\2\2px\3\2\2\2qu\7\60\2\2rt\5_\60\2sr\3\2\2\2tw\3\2\2\2us\3"+
		"\2\2\2uv\3\2\2\2vy\3\2\2\2wu\3\2\2\2xq\3\2\2\2xy\3\2\2\2y\u0084\3\2\2"+
		"\2z|\t\2\2\2{}\t\3\2\2|{\3\2\2\2|}\3\2\2\2}\u0081\3\2\2\2~\u0080\5_\60"+
		"\2\177~\3\2\2\2\u0080\u0083\3\2\2\2\u0081\177\3\2\2\2\u0081\u0082\3\2"+
		"\2\2\u0082\u0085\3\2\2\2\u0083\u0081\3\2\2\2\u0084z\3\2\2\2\u0084\u0085"+
		"\3\2\2\2\u0085\6\3\2\2\2\u0086\u0089\5\13\6\2\u0087\u0089\5\r\7\2\u0088"+
		"\u0086\3\2\2\2\u0088\u0087\3\2\2\2\u0089\b\3\2\2\2\u008a\u009e\7$\2\2"+
		"\u008b\u008c\7^\2\2\u008c\u009d\7d\2\2\u008d\u008e\7^\2\2\u008e\u009d"+
		"\7h\2\2\u008f\u0090\7^\2\2\u0090\u009d\7t\2\2\u0091\u0092\7^\2\2\u0092"+
		"\u009d\7p\2\2\u0093\u0094\7^\2\2\u0094\u009d\7v\2\2\u0095\u0096\7^\2\2"+
		"\u0096\u009d\7)\2\2\u0097\u0098\7^\2\2\u0098\u009d\7^\2\2\u0099\u009a"+
		"\7)\2\2\u009a\u009d\7$\2\2\u009b\u009d\n\4\2\2\u009c\u008b\3\2\2\2\u009c"+
		"\u008d\3\2\2\2\u009c\u008f\3\2\2\2\u009c\u0091\3\2\2\2\u009c\u0093\3\2"+
		"\2\2\u009c\u0095\3\2\2\2\u009c\u0097\3\2\2\2\u009c\u0099\3\2\2\2\u009c"+
		"\u009b\3\2\2\2\u009d\u00a0\3\2\2\2\u009e\u009c\3\2\2\2\u009e\u009f\3\2"+
		"\2\2\u009f\u00a1\3\2\2\2\u00a0\u009e\3\2\2\2\u00a1\u00a2\7$\2\2\u00a2"+
		"\n\3\2\2\2\u00a3\u00a4\7v\2\2\u00a4\u00a5\7t\2\2\u00a5\u00a6\7w\2\2\u00a6"+
		"\u00a7\7g\2\2\u00a7\f\3\2\2\2\u00a8\u00a9\7h\2\2\u00a9\u00aa\7c\2\2\u00aa"+
		"\u00ab\7n\2\2\u00ab\u00ac\7u\2\2\u00ac\u00ad\7g\2\2\u00ad\16\3\2\2\2\u00ae"+
		"\u00af\7p\2\2\u00af\u00b0\7w\2\2\u00b0\u00b1\7o\2\2\u00b1\u00b2\7d\2\2"+
		"\u00b2\u00b3\7g\2\2\u00b3\u00b4\7t\2\2\u00b4\20\3\2\2\2\u00b5\u00b6\7"+
		"d\2\2\u00b6\u00b7\7q\2\2\u00b7\u00b8\7q\2\2\u00b8\u00b9\7n\2\2\u00b9\22"+
		"\3\2\2\2\u00ba\u00bb\7u\2\2\u00bb\u00bc\7v\2\2\u00bc\u00bd\7t\2\2\u00bd"+
		"\u00be\7k\2\2\u00be\u00bf\7p\2\2\u00bf\u00c0\7i\2\2\u00c0\24\3\2\2\2\u00c1"+
		"\u00c2\7t\2\2\u00c2\u00c3\7g\2\2\u00c3\u00c4\7v\2\2\u00c4\u00c5\7w\2\2"+
		"\u00c5\u00c6\7t\2\2\u00c6\u00c7\7p\2\2\u00c7\26\3\2\2\2\u00c8\u00c9\7"+
		"x\2\2\u00c9\u00ca\7c\2\2\u00ca\u00cb\7t\2\2\u00cb\30\3\2\2\2\u00cc\u00cd"+
		"\7f\2\2\u00cd\u00ce\7{\2\2\u00ce\u00cf\7p\2\2\u00cf\u00d0\7c\2\2\u00d0"+
		"\u00d1\7o\2\2\u00d1\u00d2\7k\2\2\u00d2\u00d3\7e\2\2\u00d3\32\3\2\2\2\u00d4"+
		"\u00d5\7h\2\2\u00d5\u00d6\7w\2\2\u00d6\u00d7\7p\2\2\u00d7\u00d8\7e\2\2"+
		"\u00d8\34\3\2\2\2\u00d9\u00da\7h\2\2\u00da\u00db\7q\2\2\u00db\u00dc\7"+
		"t\2\2\u00dc\36\3\2\2\2\u00dd\u00de\7w\2\2\u00de\u00df\7p\2\2\u00df\u00e0"+
		"\7v\2\2\u00e0\u00e1\7k\2\2\u00e1\u00e2\7n\2\2\u00e2 \3\2\2\2\u00e3\u00e4"+
		"\7d\2\2\u00e4\u00e5\7{\2\2\u00e5\"\3\2\2\2\u00e6\u00e7\7d\2\2\u00e7\u00e8"+
		"\7t\2\2\u00e8\u00e9\7g\2\2\u00e9\u00ea\7c\2\2\u00ea\u00eb\7m\2\2\u00eb"+
		"$\3\2\2\2\u00ec\u00ed\7e\2\2\u00ed\u00ee\7q\2\2\u00ee\u00ef\7p\2\2\u00ef"+
		"\u00f0\7v\2\2\u00f0\u00f1\7k\2\2\u00f1\u00f2\7p\2\2\u00f2\u00f3\7w\2\2"+
		"\u00f3\u00f4\7g\2\2\u00f4&\3\2\2\2\u00f5\u00f6\7k\2\2\u00f6\u00f7\7h\2"+
		"\2\u00f7(\3\2\2\2\u00f8\u00f9\7g\2\2\u00f9\u00fa\7n\2\2\u00fa\u00fb\7"+
		"u\2\2\u00fb\u00fc\7g\2\2\u00fc*\3\2\2\2\u00fd\u00fe\7g\2\2\u00fe\u00ff"+
		"\7n\2\2\u00ff\u0100\7k\2\2\u0100\u0101\7h\2\2\u0101,\3\2\2\2\u0102\u0103"+
		"\7d\2\2\u0103\u0104\7g\2\2\u0104\u0105\7i\2\2\u0105\u0106\7k\2\2\u0106"+
		"\u0107\7p\2\2\u0107.\3\2\2\2\u0108\u0109\7g\2\2\u0109\u010a\7p\2\2\u010a"+
		"\u010b\7f\2\2\u010b\60\3\2\2\2\u010c\u010d\7p\2\2\u010d\u010e\7q\2\2\u010e"+
		"\u010f\7v\2\2\u010f\62\3\2\2\2\u0110\u0111\7c\2\2\u0111\u0112\7p\2\2\u0112"+
		"\u0113\7f\2\2\u0113\64\3\2\2\2\u0114\u0115\7q\2\2\u0115\u0116\7t\2\2\u0116"+
		"\66\3\2\2\2\u0117\u0118\7-\2\2\u01188\3\2\2\2\u0119\u011a\7/\2\2\u011a"+
		":\3\2\2\2\u011b\u011c\7,\2\2\u011c<\3\2\2\2\u011d\u011e\7\61\2\2\u011e"+
		">\3\2\2\2\u011f\u0120\7\'\2\2\u0120@\3\2\2\2\u0121\u0122\7>\2\2\u0122"+
		"\u0123\7/\2\2\u0123B\3\2\2\2\u0124\u0125\7?\2\2\u0125D\3\2\2\2\u0126\u0127"+
		"\7#\2\2\u0127\u0128\7?\2\2\u0128F\3\2\2\2\u0129\u012a\7>\2\2\u012aH\3"+
		"\2\2\2\u012b\u012c\7@\2\2\u012cJ\3\2\2\2\u012d\u012e\7>\2\2\u012e\u012f"+
		"\7?\2\2\u012fL\3\2\2\2\u0130\u0131\7@\2\2\u0131\u0132\7?\2\2\u0132N\3"+
		"\2\2\2\u0133\u0134\7\60\2\2\u0134\u0135\7\60\2\2\u0135\u0136\7\60\2\2"+
		"\u0136P\3\2\2\2\u0137\u0138\7?\2\2\u0138\u0139\7?\2\2\u0139R\3\2\2\2\u013a"+
		"\u013b\7.\2\2\u013bT\3\2\2\2\u013c\u013d\7*\2\2\u013dV\3\2\2\2\u013e\u013f"+
		"\7+\2\2\u013fX\3\2\2\2\u0140\u0141\7]\2\2\u0141Z\3\2\2\2\u0142\u0143\7"+
		"_\2\2\u0143\\\3\2\2\2\u0144\u0148\t\5\2\2\u0145\u0147\t\6\2\2\u0146\u0145"+
		"\3\2\2\2\u0147\u014a\3\2\2\2\u0148\u0146\3\2\2\2\u0148\u0149\3\2\2\2\u0149"+
		"^\3\2\2\2\u014a\u0148\3\2\2\2\u014b\u014c\t\7\2\2\u014c`\3\2\2\2\u014d"+
		"\u014e\7\f\2\2\u014eb\3\2\2\2\u014f\u0150\7%\2\2\u0150\u0154\7%\2\2\u0151"+
		"\u0153\13\2\2\2\u0152\u0151\3\2\2\2\u0153\u0156\3\2\2\2\u0154\u0155\3"+
		"\2\2\2\u0154\u0152\3\2\2\2\u0155\u0158\3\2\2\2\u0156\u0154\3\2\2\2\u0157"+
		"\u0159\t\b\2\2\u0158\u0157\3\2\2\2\u0159\u015a\3\2\2\2\u015a\u015b\b\62"+
		"\2\2\u015bd\3\2\2\2\u015c\u015e\t\t\2\2\u015d\u015c\3\2\2\2\u015e\u015f"+
		"\3\2\2\2\u015f\u015d\3\2\2\2\u015f\u0160\3\2\2\2\u0160\u0161\3\2\2\2\u0161"+
		"\u0162\b\63\2\2\u0162f\3\2\2\2\21\2joux|\u0081\u0084\u0088\u009c\u009e"+
		"\u0148\u0154\u0158\u015f\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}