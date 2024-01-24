grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}


// syntax
program: function_decl | function_def | var_decl;
function_decl: FUNC IDENTIFIER param_list LINEBREAK;
param_list: LRB param_decl  (COMMA param_decl) RRB 
			| LRB RRB;
param_decl: TYPE IDENTIFIER;
function_def: function_decl LINEBREAK BEGIN statement_list END LINEBREAK;
statement_list: (statement)*;
statement: IDENTIFIER ASSIGNOP expr;
expr: NUMLIT | BOOLLIT | STRINGLIT;
//array_ele: IDENTIFIER LSQB  RSQB


// Lexer
TYPE: NUMBER | BOOL | STRING;
NUMLIT: DIGIT+ ('.' DIGIT*)? ([eE] [+-]? DIGIT+)?;
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
MINOP: '-';
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
fragment ESC: ('\\' 'b' | '\\' 'f' | '\\' 'r' | '\\' 'n' | '\\' 't' | '\\' '\'' | '\\' '\\');

LINEBREAK: '\n';
COMMENT: '#' '#' .*? '\n' -> skip; //skip comments
WS : [ \t\r\b\f]+ -> skip ; // skip spaces, tabs, newlines
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;