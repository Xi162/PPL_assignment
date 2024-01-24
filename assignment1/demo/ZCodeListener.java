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
	 * Enter a parse tree produced by {@link ZCodeParser#function_decl}.
	 * @param ctx the parse tree
	 */
	void enterFunction_decl(ZCodeParser.Function_declContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#function_decl}.
	 * @param ctx the parse tree
	 */
	void exitFunction_decl(ZCodeParser.Function_declContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#param_list}.
	 * @param ctx the parse tree
	 */
	void enterParam_list(ZCodeParser.Param_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#param_list}.
	 * @param ctx the parse tree
	 */
	void exitParam_list(ZCodeParser.Param_listContext ctx);
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
	 * Enter a parse tree produced by {@link ZCodeParser#function_def}.
	 * @param ctx the parse tree
	 */
	void enterFunction_def(ZCodeParser.Function_defContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#function_def}.
	 * @param ctx the parse tree
	 */
	void exitFunction_def(ZCodeParser.Function_defContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#function_decl_statement}.
	 * @param ctx the parse tree
	 */
	void enterFunction_decl_statement(ZCodeParser.Function_decl_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#function_decl_statement}.
	 * @param ctx the parse tree
	 */
	void exitFunction_decl_statement(ZCodeParser.Function_decl_statementContext ctx);
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
	 * Enter a parse tree produced by {@link ZCodeParser#array_index}.
	 * @param ctx the parse tree
	 */
	void enterArray_index(ZCodeParser.Array_indexContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#array_index}.
	 * @param ctx the parse tree
	 */
	void exitArray_index(ZCodeParser.Array_indexContext ctx);
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
}