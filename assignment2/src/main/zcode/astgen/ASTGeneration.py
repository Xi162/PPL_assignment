from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *


class ASTGeneration(ZCodeVisitor):

    def visitProgram(self, ctx: ZCodeParser.ProgramContext):
        return Program(ctx.decllist().accept(self))
    
    def visitDecllist(self, ctx: ZCodeParser.DecllistContext):
        return [ctx.decl().accept(self)] + ctx.decllisttail().accept(self)
    
    def visitDecllisttail(self, ctx: ZCodeParser.DecllisttailContext):
        if ctx.decl():
            return [ctx.decl().accept(self)] + ctx.decllisttail().accept(self)
        else:
            return []
        
    def visitDecl(self, ctx: ZCodeParser.DeclContext):
        if ctx.var_decl():
            return ctx.var_decl().accept(self)
        else:
            return ctx.func_decl().accept(self)
        
    def visitVar_decl(self, ctx: ZCodeParser.Var_declContext):
        if ctx.array_decl():
            return ctx.array_decl().accept(self)
        typ = None
        modifier = None
        init = None
        if ctx.typ():
            typ = ctx.typ().accept(self)
        elif ctx.DYNAMIC():
            modifier = ctx.DYNAMIC().getText()
        elif ctx.VAR():
            modifier = ctx.VAR().getText()
        if ctx.initialization():
            init = ctx.initialization().accept(self)
        return VarDecl(Id(ctx.IDENTIFIER().getText()), typ, modifier, init)
    
    def visitArray_decl(self, ctx: ZCodeParser.Array_declContext):
        typ = ctx.typ().accept(self)
        if not ctx.array_init():
            return VarDecl(Id(ctx.IDENTIFIER().getText()), ArrayType(ctx.dimensionlist().accept(self), typ))
        return VarDecl(Id(ctx.IDENTIFIER().getText()), ArrayType(ctx.dimensionlist().accept(self), typ), None, ctx.array_init().accept(self))
    
    def visitDimensionlist(self, ctx: ZCodeParser.DimensionlistContext):
        return ctx.numlitlist().accept(self)
    
    def visitNumlitlist(self, ctx: ZCodeParser.NumlitlistContext):
        return [float(ctx.NUMLIT().getText())] + ctx.numlitlisttail().accept(self)
    
    def visitNumlitlisttail(self, ctx: ZCodeParser.NumlitlisttailContext):
        if ctx.NUMLIT():
            return [float(ctx.NUMLIT().getText())] + ctx.numlitlisttail().accept(self)
        else:
            return []
        
    def visitArray_init(self, ctx: ZCodeParser.Array_initContext):
        return ctx.arraylit().accept(self)
    
    def visitArraylit(self, ctx: ZCodeParser.ArraylitContext):
        return ArrayLiteral(ctx.array_decl_elelist().accept(self))
    
    def visitArray_decl_elelist(self, ctx: ZCodeParser.Array_decl_elelistContext):
        if ctx.array_decl_ele():
            return [ctx.array_decl_ele().accept(self)] + ctx.array_decl_elelisttail().accept(self)
        else:
            return []
        
    def visitArray_decl_elelisttail(self, ctx: ZCodeParser.Array_decl_elelisttailContext):
        if ctx.array_decl_ele():
            return [ctx.array_decl_ele().accept(self)] + ctx.array_decl_elelisttail().accept(self)
        else:
            return []
        
    def visitArray_decl_ele(self, ctx: ZCodeParser.Array_decl_eleContext):
        return ctx.expr().accept(self)
    
    def visitInitialization(self, ctx: ZCodeParser.InitializationContext):
        return ctx.expr().accept(self)
    
    def visitTyp(self, ctx: ZCodeParser.TypContext):
        if ctx.NUMBER():
            return NumberType()
        elif ctx.BOOL():
            return BoolType()
        elif ctx.STRING():
            return StringType()
        
    def visitExpr(self, ctx: ZCodeParser.ExprContext):
        if ctx.ELLIPOP():
            return BinaryOp(ctx.ELLIPOP().getText(), ctx.lv8_expr(0).accept(self), ctx.lv8_expr(1).accept(self))
        else:
            return ctx.lv8_expr(0).accept(self)
        
    def visitLv8_expr(self, ctx: ZCodeParser.Lv8_exprContext):
        if ctx.EQUALOP():
            return BinaryOp(ctx.EQUALOP().getText(), ctx.lv7_expr(0).accept(self), ctx.lv7_expr(1).accept(self))
        elif ctx.DOUBLEEQOP():
            return BinaryOp(ctx.DOUBLEEQOP().getText(), ctx.lv7_expr(0).accept(self), ctx.lv7_expr(1).accept(self))
        elif ctx.DIFFOP():
            return BinaryOp(ctx.DIFFOP().getText(), ctx.lv7_expr(0).accept(self), ctx.lv7_expr(1).accept(self))
        elif ctx.SMALLEROP():
            return BinaryOp(ctx.SMALLEROP().getText(), ctx.lv7_expr(0).accept(self), ctx.lv7_expr(1).accept(self))
        elif ctx.GREATEROP():
            return BinaryOp(ctx.GREATEROP().getText(), ctx.lv7_expr(0).accept(self), ctx.lv7_expr(1).accept(self))
        elif ctx.SEQOP():
            return BinaryOp(ctx.SEQOP().getText(), ctx.lv7_expr(0).accept(self), ctx.lv7_expr(1).accept(self))
        elif ctx.GEQOP():
            return BinaryOp(ctx.GEQOP().getText(), ctx.lv7_expr(0).accept(self), ctx.lv7_expr(1).accept(self))
        else:
            return ctx.lv7_expr(0).accept(self)
        
    def visitLv7_expr(self, ctx: ZCodeParser.Lv7_exprContext):
        if ctx.AND():
            return BinaryOp(ctx.AND().getText(), ctx.lv7_expr().accept(self), ctx.lv6_expr().accept(self))
        elif ctx.OR():
            return BinaryOp(ctx.OR().getText(), ctx.lv7_expr().accept(self), ctx.lv6_expr().accept(self))
        else:
            return ctx.lv6_expr().accept(self)
        
    def visitLv6_expr(self, ctx: ZCodeParser.Lv6_exprContext):
        if ctx.ADDOP():
            return BinaryOp(ctx.ADDOP().getText(), ctx.lv6_expr().accept(self), ctx.lv5_expr().accept(self))
        elif ctx.SUBOP():
            return BinaryOp(ctx.SUBOP().getText(), ctx.lv6_expr().accept(self), ctx.lv5_expr().accept(self))
        else:
            return ctx.lv5_expr().accept(self)
        
    def visitLv5_expr(self, ctx: ZCodeParser.Lv5_exprContext):
        if ctx.MULOP():
            return BinaryOp(ctx.MULOP().getText(), ctx.lv5_expr().accept(self), ctx.lv4_expr().accept(self))
        elif ctx.DIVOP():
            return BinaryOp(ctx.DIVOP().getText(), ctx.lv5_expr().accept(self), ctx.lv4_expr().accept(self))
        elif ctx.MODOP():
            return BinaryOp(ctx.MODOP().getText(), ctx.lv5_expr().accept(self), ctx.lv4_expr().accept(self))
        else:
            return ctx.lv4_expr().accept(self)
        
    def visitLv4_expr(self, ctx: ZCodeParser.Lv4_exprContext):
        if ctx.NOT():
            return UnaryOp(ctx.NOT().getText(), ctx.lv4_expr().accept(self))
        else:
            return ctx.lv3_expr().accept(self)
        
    def visitLv3_expr(self, ctx: ZCodeParser.Lv3_exprContext):
        if ctx.SUBOP():
            return UnaryOp(ctx.SUBOP().getText(), ctx.lv3_expr().accept(self))
        else:
            return ctx.lv2_expr().accept(self)
    
    def visitLv2_expr(self, ctx: ZCodeParser.Lv2_exprContext):
        if ctx.array_indexing():
            return ctx.array_indexing().accept(self)
        else:
            return ctx.lv1_expr().accept(self)
        
    def visitLv1_expr(self, ctx: ZCodeParser.Lv1_exprContext):
        if ctx.function_call():
            return ctx.function_call().accept(self)
        elif ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        elif ctx.literals():
            return ctx.literals().accept(self)
        else:
            return ctx.expr().accept(self)
        
    def visitLiterals(self, ctx: ZCodeParser.LiteralsContext):
        if ctx.NUMLIT():
            return NumberLiteral(float(ctx.NUMLIT().getText()))
        elif ctx.BOOLLIT():
            return BooleanLiteral(ctx.BOOLLIT().getText() == "true")
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        else:
            return ctx.arraylit().accept(self)
        
    def visitArray_indexing(self, ctx: ZCodeParser.Array_indexingContext):
        return ArrayCell(ctx.array_expression().accept(self), ctx.index_operator().accept(self))
    
    def visitArray_expression(self, ctx: ZCodeParser.Array_expressionContext):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        return ctx.function_call().accept(self)
    
    def visitIndex_operator(self, ctx: ZCodeParser.Index_operatorContext):
        return ctx.exprlist().accept(self)
    
    def visitExprlist(self, ctx: ZCodeParser.ExprlistContext):
        return [ctx.expr().accept(self)] + ctx.exprlisttail().accept(self)
    
    def visitExprlisttail(self, ctx: ZCodeParser.ExprlisttailContext):
        if ctx.expr():
            return [ctx.expr().accept(self)] + ctx.exprlisttail().accept(self)
        else:
            return []
        
    def visitFunction_call(self, ctx: ZCodeParser.Function_callContext):
        return CallExpr(Id(ctx.IDENTIFIER().getText()), ctx.args().accept(self))
    
    def visitArgs(self, ctx: ZCodeParser.ArgsContext):
        return ctx.argslist().accept(self)
    
    def visitArgslist(self, ctx: ZCodeParser.ArgslistContext):
        if ctx.expr():
            return [ctx.expr().accept(self)] + ctx.argslisttail().accept(self)
        else:
            return []
        
    def visitArgslisttail(self, ctx: ZCodeParser.ArgslisttailContext):
        if ctx.expr():
            return [ctx.expr().accept(self)] + ctx.argslisttail().accept(self)
        else:
            return []
        
    def visitFunc_decl(self, ctx: ZCodeParser.Func_declContext):
        return FuncDecl(Id(ctx.IDENTIFIER().getText()), ctx.param_decl().accept(self), ctx.func_decl_end().accept(self))
    
    def visitParam_decl(self, ctx: ZCodeParser.Param_declContext):
        return ctx.paramlist().accept(self)
    
    def visitParamlist(self, ctx: ZCodeParser.ParamlistContext):
        if ctx.param():
            return [ctx.param().accept(self)] + ctx.paramlisttail().accept(self)
        else:
            return []
        
    def visitParamlisttail(self, ctx: ZCodeParser.ParamlisttailContext):
        if ctx.param():
            return [ctx.param().accept(self)] + ctx.paramlisttail().accept(self)
        else:
            return []
        
    def visitParam(self, ctx: ZCodeParser.ParamContext):
        typ = ctx.typ().accept(self)
        if ctx.dimensionlist():
            return VarDecl(Id(ctx.IDENTIFIER().getText()), ArrayType(ctx.dimensionlist().accept(self), typ))
        return VarDecl(Id(ctx.IDENTIFIER().getText()), typ)
    
    def visitFunc_decl_end(self, ctx: ZCodeParser.Func_decl_endContext):
        if ctx.func_statement():
            return ctx.func_statement().accept(self)
        return None
    
    def visitFunc_statement(self, ctx: ZCodeParser.Func_statementContext):
        if ctx.return_statement():
            return ctx.return_statement().accept(self)
        else:
            return ctx.block_statement().accept(self)
        
    def visitReturn_statement(self, ctx: ZCodeParser.Return_statementContext):
        if ctx.expr():
            return Return(ctx.expr().accept(self))
        return Return()
    
    def visitBlock_statement(self, ctx: ZCodeParser.Block_statementContext):
        return Block(ctx.statementlist().accept(self))
    
    def visitStatementlist(self, ctx: ZCodeParser.StatementlistContext):
        if ctx.statement():
            return [ctx.statement().accept(self)] + ctx.statementlisttail().accept(self)
        else:
            return []
        
    def visitStatementlisttail(self, ctx: ZCodeParser.StatementlisttailContext):
        if ctx.statement():
            return [ctx.statement().accept(self)] + ctx.statementlisttail().accept(self)
        else:
            return []
        
    def visitStatement(self, ctx: ZCodeParser.StatementContext):
        if ctx.var_decl_statement():
            return ctx.var_decl_statement().accept(self)
        elif ctx.assign_statement():
            return ctx.assign_statement().accept(self)
        elif ctx.if_statement():
            return ctx.if_statement().accept(self)
        elif ctx.for_statement():
            return ctx.for_statement().accept(self)
        elif ctx.break_statement():
            return ctx.break_statement().accept(self)
        elif ctx.continue_statement():
            return ctx.continue_statement().accept(self)
        elif ctx.return_statement():
            return ctx.return_statement().accept(self)
        elif ctx.function_call_statement():
            return ctx.function_call_statement().accept(self)
        else:
            return ctx.block_statement().accept(self)
        
    def visitVar_decl_statement(self, ctx: ZCodeParser.Var_decl_statementContext):
        return ctx.var_decl().accept(self)
    
    def visitAssign_statement(self, ctx: ZCodeParser.Assign_statementContext):
        return Assign(ctx.lhs().accept(self), ctx.expr().accept(self))
    
    def visitLhs(self, ctx: ZCodeParser.LhsContext):
        if ctx.array_ele():
            return ctx.array_ele().accept(self)
        return Id(ctx.IDENTIFIER().getText())
    
    def visitArray_ele(self, ctx: ZCodeParser.Array_eleContext):
        return ArrayCell(Id(ctx.IDENTIFIER().getText()), ctx.index_operator().accept(self))
    
    def visitFor_statement(self, ctx: ZCodeParser.For_statementContext):
        return For(Id(ctx.IDENTIFIER().getText()), ctx.expr(0).accept(self), ctx.expr(1).accept(self), ctx.statement().accept(self))
    
    def visitBreak_statement(self, ctx: ZCodeParser.Break_statementContext):
        return Break()
    
    def visitContinue_statement(self, ctx: ZCodeParser.Continue_statementContext):
        return Continue()
    
    def visitFunction_call_statement(self, ctx: ZCodeParser.Function_call_statementContext):
        func_expr = ctx.function_call().accept(self)
        return CallStmt(func_expr.name, func_expr.args)
    
    def visitIf_statement(self, ctx: ZCodeParser.If_statementContext):
        ifclause = ctx.ifpart().accept(self)
        eliflist = ctx.eliflist().accept(self)
        elsestmt = ctx.elsepart().accept(self)
        return If(ifclause[0], ifclause[1], eliflist, elsestmt)
    
    def visitIfpart(self, ctx: ZCodeParser.IfpartContext):
        return (ctx.exprclause().accept(self), ctx.statement().accept(self))
    
    def visitExprclause(self, ctx: ZCodeParser.ExprclauseContext):
        return ctx.expr().accept(self)
    
    def visitEliflist(self, ctx: ZCodeParser.EliflistContext):
        if ctx.elifpart():
            return [ctx.elifpart().accept(self)] + ctx.eliflisttail().accept(self)
        else:
            return []
        
    def visitEliflisttail(self, ctx: ZCodeParser.EliflisttailContext):
        if ctx.elifpart():
            return [ctx.elifpart().accept(self)] + ctx.eliflisttail().accept(self)
        else:
            return []
        
    def visitElifpart(self, ctx: ZCodeParser.ElifpartContext):
        return (ctx.exprclause().accept(self), ctx.statement().accept(self))
    
    def visitElsepart(self, ctx: ZCodeParser.ElsepartContext):
        if ctx.statement():
            return ctx.statement().accept(self)
        return None
        
    
