grammar ZCode;

// syntax
program: (function_decl_statement | function_def | var_decl_statement)+;
function_decl: FUNC IDENTIFIER param_list;
param_list: LRB (param_decl  (COMMA param_decl)*)? RRB;
param_decl: TYPE IDENTIFIER (LSQB NUMLIT (COMMA NUMLIT)* RSQB)? ;
function_def: function_decl (LINEBREAK)* statement;
function_decl_statement: function_decl LINEBREAK+;
// TODO: statement (2)
statement: var_decl_statement
		| assign_statement
		| if_statement
		| for_statement
		| break_statement
		| continue_statement
		| return_statement
		| function_call_statement
		| block_statement;
var_decl_statement: (TYPE | DYNAMIC) IDENTIFIER (ASSIGNOP expr)? LINEBREAK+
		| VAR IDENTIFIER ASSIGNOP expr LINEBREAK+
		| TYPE IDENTIFIER LSQB NUMLIT (COMMA NUMLIT)* RSQB (ASSIGNOP arraylit)? LINEBREAK+;
assign_statement: (IDENTIFIER | array_index) ASSIGNOP expr LINEBREAK+;
if_statement: IF LRB expr RRB (LINEBREAK)* statement (ELIF LRB expr RRB (LINEBREAK)* statement)* (ELSE (LINEBREAK)* statement)?;
for_statement: FOR IDENTIFIER UNTIL expr BY expr LINEBREAK+ statement;
break_statement: BREAK LINEBREAK+;
continue_statement: CONTINUE LINEBREAK+;
return_statement: RETURN expr? LINEBREAK+;
function_call_statement: function_call LINEBREAK+;
block_statement: BEGIN LINEBREAK + (statement)* END LINEBREAK+;

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

lv2_expr: array_index
		| lv1_expr;

lv1_expr: function_call
		| IDENTIFIER
		| NUMLIT
		| BOOLLIT
		| STRINGLIT
		| LRB expr RRB;
arraylit: LSQB (array_ele (COMMA array_ele)*)? RSQB;
array_ele: arraylit | expr;
array_index: (IDENTIFIER | function_call) LSQB expr (COMMA expr)* RSQB;
function_call: IDENTIFIER LRB (expr (COMMA expr)*)? RRB;



// Lexer
TYPE: NUMBER | BOOL | STRING;
NUMLIT: DIGIT+ ('.' DIGIT*)? ([eE] [+-]? DIGIT*)?;
BOOLLIT: TRUE | FALSE;
STRINGLIT: '"' ('\\' 'b' | '\\' 'f' | '\\' 'r' | '\\' 'n' | '\\' 't' | '\\' '\'' | '\\' '\\' | '\'' '"' | ~('\\' | '\'' | '"'))* '"';
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

LINEBREAK: '\n';
COMMENT: '#' '#' .*? ('\n' | EOF) -> skip; //skip comments
WS : [ \t\r\b\f]+ -> skip ; // skip spaces, tabs, newlines