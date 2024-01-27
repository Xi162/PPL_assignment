# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decllist.
    def visitDecllist(self, ctx:ZCodeParser.DecllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decllisttail.
    def visitDecllisttail(self, ctx:ZCodeParser.DecllisttailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl.
    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_decl.
    def visitFunc_decl(self, ctx:ZCodeParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param_decl.
    def visitParam_decl(self, ctx:ZCodeParser.Param_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramlist.
    def visitParamlist(self, ctx:ZCodeParser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramlisttail.
    def visitParamlisttail(self, ctx:ZCodeParser.ParamlisttailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param.
    def visitParam(self, ctx:ZCodeParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_decl_end.
    def visitFunc_decl_end(self, ctx:ZCodeParser.Func_decl_endContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_statement.
    def visitFunc_statement(self, ctx:ZCodeParser.Func_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#var_decl.
    def visitVar_decl(self, ctx:ZCodeParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#typ.
    def visitTyp(self, ctx:ZCodeParser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#initialization.
    def visitInitialization(self, ctx:ZCodeParser.InitializationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_decl.
    def visitArray_decl(self, ctx:ZCodeParser.Array_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#dimensionlist.
    def visitDimensionlist(self, ctx:ZCodeParser.DimensionlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#numlitlist.
    def visitNumlitlist(self, ctx:ZCodeParser.NumlitlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#numlitlisttail.
    def visitNumlitlisttail(self, ctx:ZCodeParser.NumlitlisttailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_init.
    def visitArray_init(self, ctx:ZCodeParser.Array_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arraylit.
    def visitArraylit(self, ctx:ZCodeParser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_decl_elelist.
    def visitArray_decl_elelist(self, ctx:ZCodeParser.Array_decl_elelistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_decl_elelisttail.
    def visitArray_decl_elelisttail(self, ctx:ZCodeParser.Array_decl_elelisttailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_decl_ele.
    def visitArray_decl_ele(self, ctx:ZCodeParser.Array_decl_eleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#literals.
    def visitLiterals(self, ctx:ZCodeParser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#statement.
    def visitStatement(self, ctx:ZCodeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#var_decl_statement.
    def visitVar_decl_statement(self, ctx:ZCodeParser.Var_decl_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assign_statement.
    def visitAssign_statement(self, ctx:ZCodeParser.Assign_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#lhs.
    def visitLhs(self, ctx:ZCodeParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#if_statement.
    def visitIf_statement(self, ctx:ZCodeParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ifpart.
    def visitIfpart(self, ctx:ZCodeParser.IfpartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exprclause.
    def visitExprclause(self, ctx:ZCodeParser.ExprclauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#eliflist.
    def visitEliflist(self, ctx:ZCodeParser.EliflistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#eliflisttail.
    def visitEliflisttail(self, ctx:ZCodeParser.EliflisttailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elifpart.
    def visitElifpart(self, ctx:ZCodeParser.ElifpartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elsepart.
    def visitElsepart(self, ctx:ZCodeParser.ElsepartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#for_statement.
    def visitFor_statement(self, ctx:ZCodeParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#break_statement.
    def visitBreak_statement(self, ctx:ZCodeParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#continue_statement.
    def visitContinue_statement(self, ctx:ZCodeParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#return_statement.
    def visitReturn_statement(self, ctx:ZCodeParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function_call_statement.
    def visitFunction_call_statement(self, ctx:ZCodeParser.Function_call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#block_statement.
    def visitBlock_statement(self, ctx:ZCodeParser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#statementlist.
    def visitStatementlist(self, ctx:ZCodeParser.StatementlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#statementlisttail.
    def visitStatementlisttail(self, ctx:ZCodeParser.StatementlisttailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr.
    def visitExpr(self, ctx:ZCodeParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#lv8_expr.
    def visitLv8_expr(self, ctx:ZCodeParser.Lv8_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#lv7_expr.
    def visitLv7_expr(self, ctx:ZCodeParser.Lv7_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#lv6_expr.
    def visitLv6_expr(self, ctx:ZCodeParser.Lv6_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#lv5_expr.
    def visitLv5_expr(self, ctx:ZCodeParser.Lv5_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#lv4_expr.
    def visitLv4_expr(self, ctx:ZCodeParser.Lv4_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#lv3_expr.
    def visitLv3_expr(self, ctx:ZCodeParser.Lv3_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#lv2_expr.
    def visitLv2_expr(self, ctx:ZCodeParser.Lv2_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#lv1_expr.
    def visitLv1_expr(self, ctx:ZCodeParser.Lv1_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_indexing.
    def visitArray_indexing(self, ctx:ZCodeParser.Array_indexingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_expression.
    def visitArray_expression(self, ctx:ZCodeParser.Array_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#index_operator.
    def visitIndex_operator(self, ctx:ZCodeParser.Index_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exprlist.
    def visitExprlist(self, ctx:ZCodeParser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exprlisttail.
    def visitExprlisttail(self, ctx:ZCodeParser.ExprlisttailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function_call.
    def visitFunction_call(self, ctx:ZCodeParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#args.
    def visitArgs(self, ctx:ZCodeParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#argslist.
    def visitArgslist(self, ctx:ZCodeParser.ArgslistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#argslisttail.
    def visitArgslisttail(self, ctx:ZCodeParser.ArgslisttailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#linebreaklist.
    def visitLinebreaklist(self, ctx:ZCodeParser.LinebreaklistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#nullablelinebreaklist.
    def visitNullablelinebreaklist(self, ctx:ZCodeParser.NullablelinebreaklistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#linebreaklisttail.
    def visitLinebreaklisttail(self, ctx:ZCodeParser.LinebreaklisttailContext):
        return self.visitChildren(ctx)



del ZCodeParser