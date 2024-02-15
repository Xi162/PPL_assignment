grammar ZCode;

// syntax
program: nullablelinebreaklist decllist EOF;
decllist: decl decllisttail;
decllisttail: decl decllisttail | ;
decl: func_decl | var_decl linebreaklist;

// function declarations
func_decl: FUNC IDENTIFIER param_decl func_decl_end;
param_decl: LRB paramlist RRB;
paramlist: param paramlisttail | ;
paramlisttail: COMMA param paramlisttail | ;
param: typ IDENTIFIER (dimensionlist | );
func_decl_end: linebreaklist
			| nullablelinebreaklist func_statement;
func_statement: return_statement
				| block_statement;

// variable declarations
var_decl: (typ | DYNAMIC) IDENTIFIER (initialization | )
		| VAR IDENTIFIER initialization
		| array_decl;
typ: NUMBER | BOOL | STRING;
initialization: ASSIGNOP expr;

// array declarations
array_decl: typ IDENTIFIER dimensionlist (array_init | );
dimensionlist: LSQB numlitlist RSQB;
numlitlist: NUMLIT numlitlisttail;
numlitlisttail: COMMA NUMLIT numlitlisttail | ;
array_init: ASSIGNOP arraylit;
arraylit: LSQB array_decl_elelist RSQB;
array_decl_elelist: array_decl_ele array_decl_elelisttail;
array_decl_elelisttail: COMMA array_decl_ele array_decl_elelisttail | ;
array_decl_ele: expr | arraylit;
literals: NUMLIT | BOOLLIT | STRINGLIT;

// statement
statement: var_decl_statement
		| assign_statement
		| if_statement
		| for_statement
		| break_statement
		| continue_statement
		| return_statement
		| function_call_statement
		| block_statement;
// var declaration statement
var_decl_statement: var_decl linebreaklist;

// assign statement
assign_statement: lhs ASSIGNOP expr linebreaklist;
lhs: IDENTIFIER | array_ele;
array_ele: IDENTIFIER index_operator;

// if statement
if_statement: ifpart eliflist elsepart;
ifpart: IF exprclause nullablelinebreaklist statement;
exprclause: LRB expr RRB;
eliflist: elifpart eliflisttail | ;
eliflisttail: elifpart eliflisttail | ;
elifpart: ELIF exprclause nullablelinebreaklist statement;
elsepart: (ELSE nullablelinebreaklist statement) | ;

// for statement
for_statement: FOR IDENTIFIER UNTIL expr BY expr nullablelinebreaklist statement;

// break statement
break_statement: BREAK linebreaklist;

// continue statement
continue_statement: CONTINUE linebreaklist;

// return statement
return_statement: RETURN (expr | ) linebreaklist;

// function call statement
function_call_statement: function_call linebreaklist;

// block statement
block_statement: BEGIN linebreaklist statementlist END linebreaklist;
statementlist: statement statementlisttail | ;
statementlisttail: statement statementlisttail | ;

// expression
expr: lv8_expr ELLIPOP lv8_expr
	| lv8_expr;
lv8_expr: lv7_expr EQUALOP lv7_expr
		| lv7_expr DOUBLEEQOP lv7_expr
		| lv7_expr DIFFOP lv7_expr
		| lv7_expr SMALLEROP lv7_expr
		| lv7_expr GREATEROP lv7_expr
		| lv7_expr SEQOP lv7_expr
		| lv7_expr GEQOP lv7_expr
		| lv7_expr;

lv7_expr: lv7_expr AND lv6_expr
		| lv7_expr OR lv6_expr
		| lv6_expr;

lv6_expr: lv6_expr ADDOP lv5_expr
		| lv6_expr SUBOP lv5_expr
		| lv5_expr;

lv5_expr: lv5_expr MULOP lv4_expr
		| lv5_expr DIVOP lv4_expr
		| lv5_expr MODOP lv4_expr
		| lv4_expr;

lv4_expr: NOT lv4_expr
		| lv3_expr;

lv3_expr: SUBOP lv3_expr
		| lv2_expr;

lv2_expr: array_indexing
		| lv1_expr;

lv1_expr: function_call
		| IDENTIFIER
		| literals
		| LRB expr RRB;

// index operator
array_indexing: array_expression index_operator;
array_expression: IDENTIFIER | function_call;
index_operator: LSQB exprlist RSQB;
exprlist: expr exprlisttail;
exprlisttail: COMMA expr exprlisttail | ;

// function call
function_call: IDENTIFIER args;
args: LRB argslist RRB;
argslist: expr argslisttail | ;
argslisttail: COMMA expr argslisttail | ;

//list of linebreaks
linebreaklist: LINEBREAK linebreaklisttail;
nullablelinebreaklist: LINEBREAK linebreaklisttail | ;
linebreaklisttail: LINEBREAK linebreaklisttail | ;


// Lexer
NUMLIT: DIGIT+ ('.' DIGIT*)? ([eE] [+-]? DIGIT+)?;
BOOLLIT: TRUE | FALSE;
STRINGLIT: '"' (ESC | ~('\\' | '"' | '\n' | '\r'))* '"';
TRUE: 'true';
FALSE: 'false';
NUMBER: 'number';
BOOL: 'bool';
STRING: 'string';
RETURN: 'return';
VAR: 'var';
DYNAMIC: 'dynamic';
FUNC: 'func';
FOR: 'for';
UNTIL: 'until';
BY: 'by';
BREAK: 'break';
CONTINUE: 'continue';
IF: 'if';
ELSE: 'else';
ELIF: 'elif';
BEGIN: 'begin';
END: 'end';
NOT: 'not';
AND: 'and';
OR: 'or';
ADDOP: '+';
SUBOP: '-';
MULOP: '*';
DIVOP: '/';
MODOP: '%';
ASSIGNOP: '<-';
EQUALOP: '=';
DIFFOP: '!=';
SMALLEROP: '<';
GREATEROP: '>';
SEQOP: '<=';
GEQOP: '>=';
ELLIPOP: '...';
DOUBLEEQOP: '==';
COMMA: ',';
LRB: '(';
RRB: ')';
LSQB: '[';
RSQB: ']';
IDENTIFIER: [_A-Za-z] [_A-Za-z0-9]*;
fragment DIGIT: [0-9];
fragment BACKSPACEESC: '\\' 'b';
fragment FORMFEEDESC: '\\' 'f';
fragment CARRETURNESC: '\\' 'r';
fragment NEWLINEESC: '\\' 'n';
fragment TABESC: '\\' 't';
fragment SQUOTEESC: '\\' '\'';
fragment BACKLASHESC: '\\' '\\';
fragment DQUOTEESC: '\'' '"';
fragment ESC: (BACKSPACEESC | FORMFEEDESC | CARRETURNESC | NEWLINEESC | TABESC | SQUOTEESC | BACKLASHESC | DQUOTEESC);

LINEBREAK: '\n' | '\r' | '\r' '\n';
COMMENT: '#' '#' (~('\n' | '\r'))* (EOF | ) -> skip; //skip comments
WS : [ \t\b\f]+ -> skip ; // skip spaces, tabs, newlines