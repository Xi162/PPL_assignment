// Generated from ZCode.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ZCodeParser}.
 */
public interface ZCodeListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(ZCodeParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(ZCodeParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#decllist}.
	 * @param ctx the parse tree
	 */
	void enterDecllist(ZCodeParser.DecllistContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#decllist}.
	 * @param ctx the parse tree
	 */
	void exitDecllist(ZCodeParser.DecllistContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#decllisttail}.
	 * @param ctx the parse tree
	 */
	void enterDecllisttail(ZCodeParser.DecllisttailContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#decllisttail}.
	 * @param ctx the parse tree
	 */
	void exitDecllisttail(ZCodeParser.DecllisttailContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#decl}.
	 * @param ctx the parse tree
	 */
	void enterDecl(ZCodeParser.DeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#decl}.
	 * @param ctx the parse tree
	 */
	void exitDecl(ZCodeParser.DeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#func_decl}.
	 * @param ctx the parse tree
	 */
	void enterFunc_decl(ZCodeParser.Func_declContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#func_decl}.
	 * @param ctx the parse tree
	 */
	void exitFunc_decl(ZCodeParser.Func_declContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#param_decl}.
	 * @param ctx the parse tree
	 */
	void enterParam_decl(ZCodeParser.Param_declContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#param_decl}.
	 * @param ctx the parse tree
	 */
	void exitParam_decl(ZCodeParser.Param_declContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#paramlist}.
	 * @param ctx the parse tree
	 */
	void enterParamlist(ZCodeParser.ParamlistContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#paramlist}.
	 * @param ctx the parse tree
	 */
	void exitParamlist(ZCodeParser.ParamlistContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#paramlisttail}.
	 * @param ctx the parse tree
	 */
	void enterParamlisttail(ZCodeParser.ParamlisttailContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#paramlisttail}.
	 * @param ctx the parse tree
	 */
	void exitParamlisttail(ZCodeParser.ParamlisttailContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#param}.
	 * @param ctx the parse tree
	 */
	void enterParam(ZCodeParser.ParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#param}.
	 * @param ctx the parse tree
	 */
	void exitParam(ZCodeParser.ParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#func_decl_end}.
	 * @param ctx the parse tree
	 */
	void enterFunc_decl_end(ZCodeParser.Func_decl_endContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#func_decl_end}.
	 * @param ctx the parse tree
	 */
	void exitFunc_decl_end(ZCodeParser.Func_decl_endContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#func_statement}.
	 * @param ctx the parse tree
	 */
	void enterFunc_statement(ZCodeParser.Func_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#func_statement}.
	 * @param ctx the parse tree
	 */
	void exitFunc_statement(ZCodeParser.Func_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#var_decl}.
	 * @param ctx the parse tree
	 */
	void enterVar_decl(ZCodeParser.Var_declContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#var_decl}.
	 * @param ctx the parse tree
	 */
	void exitVar_decl(ZCodeParser.Var_declContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#typ}.
	 * @param ctx the parse tree
	 */
	void enterTyp(ZCodeParser.TypContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#typ}.
	 * @param ctx the parse tree
	 */
	void exitTyp(ZCodeParser.TypContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#initialization}.
	 * @param ctx the parse tree
	 */
	void enterInitialization(ZCodeParser.InitializationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#initialization}.
	 * @param ctx the parse tree
	 */
	void exitInitialization(ZCodeParser.InitializationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#array_decl}.
	 * @param ctx the parse tree
	 */
	void enterArray_decl(ZCodeParser.Array_declContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#array_decl}.
	 * @param ctx the parse tree
	 */
	void exitArray_decl(ZCodeParser.Array_declContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#dimensionlist}.
	 * @param ctx the parse tree
	 */
	void enterDimensionlist(ZCodeParser.DimensionlistContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#dimensionlist}.
	 * @param ctx the parse tree
	 */
	void exitDimensionlist(ZCodeParser.DimensionlistContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#numlitlist}.
	 * @param ctx the parse tree
	 */
	void enterNumlitlist(ZCodeParser.NumlitlistContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#numlitlist}.
	 * @param ctx the parse tree
	 */
	void exitNumlitlist(ZCodeParser.NumlitlistContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#numlitlisttail}.
	 * @param ctx the parse tree
	 */
	void enterNumlitlisttail(ZCodeParser.NumlitlisttailContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#numlitlisttail}.
	 * @param ctx the parse tree
	 */
	void exitNumlitlisttail(ZCodeParser.NumlitlisttailContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#array_init}.
	 * @param ctx the parse tree
	 */
	void enterArray_init(ZCodeParser.Array_initContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#array_init}.
	 * @param ctx the parse tree
	 */
	void exitArray_init(ZCodeParser.Array_initContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#arraylit}.
	 * @param ctx the parse tree
	 */
	void enterArraylit(ZCodeParser.ArraylitContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#arraylit}.
	 * @param ctx the parse tree
	 */
	void exitArraylit(ZCodeParser.ArraylitContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#array_decl_elelist}.
	 * @param ctx the parse tree
	 */
	void enterArray_decl_elelist(ZCodeParser.Array_decl_elelistContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#array_decl_elelist}.
	 * @param ctx the parse tree
	 */
	void exitArray_decl_elelist(ZCodeParser.Array_decl_elelistContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#array_decl_elelisttail}.
	 * @param ctx the parse tree
	 */
	void enterArray_decl_elelisttail(ZCodeParser.Array_decl_elelisttailContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#array_decl_elelisttail}.
	 * @param ctx the parse tree
	 */
	void exitArray_decl_elelisttail(ZCodeParser.Array_decl_elelisttailContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#array_decl_ele}.
	 * @param ctx the parse tree
	 */
	void enterArray_decl_ele(ZCodeParser.Array_decl_eleContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#array_decl_ele}.
	 * @param ctx the parse tree
	 */
	void exitArray_decl_ele(ZCodeParser.Array_decl_eleContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#literals}.
	 * @param ctx the parse tree
	 */
	void enterLiterals(ZCodeParser.LiteralsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#literals}.
	 * @param ctx the parse tree
	 */
	void exitLiterals(ZCodeParser.LiteralsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(ZCodeParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(ZCodeParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#var_decl_statement}.
	 * @param ctx the parse tree
	 */
	void enterVar_decl_statement(ZCodeParser.Var_decl_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#var_decl_statement}.
	 * @param ctx the parse tree
	 */
	void exitVar_decl_statement(ZCodeParser.Var_decl_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#assign_statement}.
	 * @param ctx the parse tree
	 */
	void enterAssign_statement(ZCodeParser.Assign_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#assign_statement}.
	 * @param ctx the parse tree
	 */
	void exitAssign_statement(ZCodeParser.Assign_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#lhs}.
	 * @param ctx the parse tree
	 */
	void enterLhs(ZCodeParser.LhsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#lhs}.
	 * @param ctx the parse tree
	 */
	void exitLhs(ZCodeParser.LhsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#array_ele}.
	 * @param ctx the parse tree
	 */
	void enterArray_ele(ZCodeParser.Array_eleContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#array_ele}.
	 * @param ctx the parse tree
	 */
	void exitArray_ele(ZCodeParser.Array_eleContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#if_statement}.
	 * @param ctx the parse tree
	 */
	void enterIf_statement(ZCodeParser.If_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#if_statement}.
	 * @param ctx the parse tree
	 */
	void exitIf_statement(ZCodeParser.If_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#ifpart}.
	 * @param ctx the parse tree
	 */
	void enterIfpart(ZCodeParser.IfpartContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#ifpart}.
	 * @param ctx the parse tree
	 */
	void exitIfpart(ZCodeParser.IfpartContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#exprclause}.
	 * @param ctx the parse tree
	 */
	void enterExprclause(ZCodeParser.ExprclauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#exprclause}.
	 * @param ctx the parse tree
	 */
	void exitExprclause(ZCodeParser.ExprclauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#eliflist}.
	 * @param ctx the parse tree
	 */
	void enterEliflist(ZCodeParser.EliflistContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#eliflist}.
	 * @param ctx the parse tree
	 */
	void exitEliflist(ZCodeParser.EliflistContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#eliflisttail}.
	 * @param ctx the parse tree
	 */
	void enterEliflisttail(ZCodeParser.EliflisttailContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#eliflisttail}.
	 * @param ctx the parse tree
	 */
	void exitEliflisttail(ZCodeParser.EliflisttailContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#elifpart}.
	 * @param ctx the parse tree
	 */
	void enterElifpart(ZCodeParser.ElifpartContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#elifpart}.
	 * @param ctx the parse tree
	 */
	void exitElifpart(ZCodeParser.ElifpartContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#elsepart}.
	 * @param ctx the parse tree
	 */
	void enterElsepart(ZCodeParser.ElsepartContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#elsepart}.
	 * @param ctx the parse tree
	 */
	void exitElsepart(ZCodeParser.ElsepartContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#for_statement}.
	 * @param ctx the parse tree
	 */
	void enterFor_statement(ZCodeParser.For_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#for_statement}.
	 * @param ctx the parse tree
	 */
	void exitFor_statement(ZCodeParser.For_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#break_statement}.
	 * @param ctx the parse tree
	 */
	void enterBreak_statement(ZCodeParser.Break_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#break_statement}.
	 * @param ctx the parse tree
	 */
	void exitBreak_statement(ZCodeParser.Break_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#continue_statement}.
	 * @param ctx the parse tree
	 */
	void enterContinue_statement(ZCodeParser.Continue_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#continue_statement}.
	 * @param ctx the parse tree
	 */
	void exitContinue_statement(ZCodeParser.Continue_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#return_statement}.
	 * @param ctx the parse tree
	 */
	void enterReturn_statement(ZCodeParser.Return_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#return_statement}.
	 * @param ctx the parse tree
	 */
	void exitReturn_statement(ZCodeParser.Return_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#function_call_statement}.
	 * @param ctx the parse tree
	 */
	void enterFunction_call_statement(ZCodeParser.Function_call_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#function_call_statement}.
	 * @param ctx the parse tree
	 */
	void exitFunction_call_statement(ZCodeParser.Function_call_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#block_statement}.
	 * @param ctx the parse tree
	 */
	void enterBlock_statement(ZCodeParser.Block_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#block_statement}.
	 * @param ctx the parse tree
	 */
	void exitBlock_statement(ZCodeParser.Block_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#statementlist}.
	 * @param ctx the parse tree
	 */
	void enterStatementlist(ZCodeParser.StatementlistContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#statementlist}.
	 * @param ctx the parse tree
	 */
	void exitStatementlist(ZCodeParser.StatementlistContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#statementlisttail}.
	 * @param ctx the parse tree
	 */
	void enterStatementlisttail(ZCodeParser.StatementlisttailContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#statementlisttail}.
	 * @param ctx the parse tree
	 */
	void exitStatementlisttail(ZCodeParser.StatementlisttailContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(ZCodeParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(ZCodeParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#lv8_expr}.
	 * @param ctx the parse tree
	 */
	void enterLv8_expr(ZCodeParser.Lv8_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#lv8_expr}.
	 * @param ctx the parse tree
	 */
	void exitLv8_expr(ZCodeParser.Lv8_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#lv7_expr}.
	 * @param ctx the parse tree
	 */
	void enterLv7_expr(ZCodeParser.Lv7_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#lv7_expr}.
	 * @param ctx the parse tree
	 */
	void exitLv7_expr(ZCodeParser.Lv7_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#lv6_expr}.
	 * @param ctx the parse tree
	 */
	void enterLv6_expr(ZCodeParser.Lv6_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#lv6_expr}.
	 * @param ctx the parse tree
	 */
	void exitLv6_expr(ZCodeParser.Lv6_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#lv5_expr}.
	 * @param ctx the parse tree
	 */
	void enterLv5_expr(ZCodeParser.Lv5_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#lv5_expr}.
	 * @param ctx the parse tree
	 */
	void exitLv5_expr(ZCodeParser.Lv5_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#lv4_expr}.
	 * @param ctx the parse tree
	 */
	void enterLv4_expr(ZCodeParser.Lv4_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#lv4_expr}.
	 * @param ctx the parse tree
	 */
	void exitLv4_expr(ZCodeParser.Lv4_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#lv3_expr}.
	 * @param ctx the parse tree
	 */
	void enterLv3_expr(ZCodeParser.Lv3_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#lv3_expr}.
	 * @param ctx the parse tree
	 */
	void exitLv3_expr(ZCodeParser.Lv3_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#lv2_expr}.
	 * @param ctx the parse tree
	 */
	void enterLv2_expr(ZCodeParser.Lv2_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#lv2_expr}.
	 * @param ctx the parse tree
	 */
	void exitLv2_expr(ZCodeParser.Lv2_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#lv1_expr}.
	 * @param ctx the parse tree
	 */
	void enterLv1_expr(ZCodeParser.Lv1_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#lv1_expr}.
	 * @param ctx the parse tree
	 */
	void exitLv1_expr(ZCodeParser.Lv1_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#array_indexing}.
	 * @param ctx the parse tree
	 */
	void enterArray_indexing(ZCodeParser.Array_indexingContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#array_indexing}.
	 * @param ctx the parse tree
	 */
	void exitArray_indexing(ZCodeParser.Array_indexingContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#array_expression}.
	 * @param ctx the parse tree
	 */
	void enterArray_expression(ZCodeParser.Array_expressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#array_expression}.
	 * @param ctx the parse tree
	 */
	void exitArray_expression(ZCodeParser.Array_expressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#index_operator}.
	 * @param ctx the parse tree
	 */
	void enterIndex_operator(ZCodeParser.Index_operatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#index_operator}.
	 * @param ctx the parse tree
	 */
	void exitIndex_operator(ZCodeParser.Index_operatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#exprlist}.
	 * @param ctx the parse tree
	 */
	void enterExprlist(ZCodeParser.ExprlistContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#exprlist}.
	 * @param ctx the parse tree
	 */
	void exitExprlist(ZCodeParser.ExprlistContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#exprlisttail}.
	 * @param ctx the parse tree
	 */
	void enterExprlisttail(ZCodeParser.ExprlisttailContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#exprlisttail}.
	 * @param ctx the parse tree
	 */
	void exitExprlisttail(ZCodeParser.ExprlisttailContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#function_call}.
	 * @param ctx the parse tree
	 */
	void enterFunction_call(ZCodeParser.Function_callContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#function_call}.
	 * @param ctx the parse tree
	 */
	void exitFunction_call(ZCodeParser.Function_callContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#args}.
	 * @param ctx the parse tree
	 */
	void enterArgs(ZCodeParser.ArgsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#args}.
	 * @param ctx the parse tree
	 */
	void exitArgs(ZCodeParser.ArgsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#argslist}.
	 * @param ctx the parse tree
	 */
	void enterArgslist(ZCodeParser.ArgslistContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#argslist}.
	 * @param ctx the parse tree
	 */
	void exitArgslist(ZCodeParser.ArgslistContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#argslisttail}.
	 * @param ctx the parse tree
	 */
	void enterArgslisttail(ZCodeParser.ArgslisttailContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#argslisttail}.
	 * @param ctx the parse tree
	 */
	void exitArgslisttail(ZCodeParser.ArgslisttailContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#linebreaklist}.
	 * @param ctx the parse tree
	 */
	void enterLinebreaklist(ZCodeParser.LinebreaklistContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#linebreaklist}.
	 * @param ctx the parse tree
	 */
	void exitLinebreaklist(ZCodeParser.LinebreaklistContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#nullablelinebreaklist}.
	 * @param ctx the parse tree
	 */
	void enterNullablelinebreaklist(ZCodeParser.NullablelinebreaklistContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#nullablelinebreaklist}.
	 * @param ctx the parse tree
	 */
	void exitNullablelinebreaklist(ZCodeParser.NullablelinebreaklistContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#linebreaklisttail}.
	 * @param ctx the parse tree
	 */
	void enterLinebreaklisttail(ZCodeParser.LinebreaklisttailContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#linebreaklisttail}.
	 * @param ctx the parse tree
	 */
	void exitLinebreaklisttail(ZCodeParser.LinebreaklisttailContext ctx);
}