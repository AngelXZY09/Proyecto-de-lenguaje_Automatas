# Generated from Lenguaje.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LenguajeParser import LenguajeParser
else:
    from LenguajeParser import LenguajeParser

# This class defines a complete listener for a parse tree produced by LenguajeParser.
class LenguajeListener(ParseTreeListener):

    # Enter a parse tree produced by LenguajeParser#programa.
    def enterPrograma(self, ctx:LenguajeParser.ProgramaContext):
        pass

    # Exit a parse tree produced by LenguajeParser#programa.
    def exitPrograma(self, ctx:LenguajeParser.ProgramaContext):
        pass


    # Enter a parse tree produced by LenguajeParser#funcion.
    def enterFuncion(self, ctx:LenguajeParser.FuncionContext):
        pass

    # Exit a parse tree produced by LenguajeParser#funcion.
    def exitFuncion(self, ctx:LenguajeParser.FuncionContext):
        pass


    # Enter a parse tree produced by LenguajeParser#parametros.
    def enterParametros(self, ctx:LenguajeParser.ParametrosContext):
        pass

    # Exit a parse tree produced by LenguajeParser#parametros.
    def exitParametros(self, ctx:LenguajeParser.ParametrosContext):
        pass


    # Enter a parse tree produced by LenguajeParser#bloque.
    def enterBloque(self, ctx:LenguajeParser.BloqueContext):
        pass

    # Exit a parse tree produced by LenguajeParser#bloque.
    def exitBloque(self, ctx:LenguajeParser.BloqueContext):
        pass


    # Enter a parse tree produced by LenguajeParser#sentencia.
    def enterSentencia(self, ctx:LenguajeParser.SentenciaContext):
        pass

    # Exit a parse tree produced by LenguajeParser#sentencia.
    def exitSentencia(self, ctx:LenguajeParser.SentenciaContext):
        pass


    # Enter a parse tree produced by LenguajeParser#tarea.
    def enterTarea(self, ctx:LenguajeParser.TareaContext):
        pass

    # Exit a parse tree produced by LenguajeParser#tarea.
    def exitTarea(self, ctx:LenguajeParser.TareaContext):
        pass


    # Enter a parse tree produced by LenguajeParser#declaracion.
    def enterDeclaracion(self, ctx:LenguajeParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by LenguajeParser#declaracion.
    def exitDeclaracion(self, ctx:LenguajeParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by LenguajeParser#siEntonces.
    def enterSiEntonces(self, ctx:LenguajeParser.SiEntoncesContext):
        pass

    # Exit a parse tree produced by LenguajeParser#siEntonces.
    def exitSiEntonces(self, ctx:LenguajeParser.SiEntoncesContext):
        pass


    # Enter a parse tree produced by LenguajeParser#sinoEntonces.
    def enterSinoEntonces(self, ctx:LenguajeParser.SinoEntoncesContext):
        pass

    # Exit a parse tree produced by LenguajeParser#sinoEntonces.
    def exitSinoEntonces(self, ctx:LenguajeParser.SinoEntoncesContext):
        pass


    # Enter a parse tree produced by LenguajeParser#imprimir.
    def enterImprimir(self, ctx:LenguajeParser.ImprimirContext):
        pass

    # Exit a parse tree produced by LenguajeParser#imprimir.
    def exitImprimir(self, ctx:LenguajeParser.ImprimirContext):
        pass


    # Enter a parse tree produced by LenguajeParser#mientras.
    def enterMientras(self, ctx:LenguajeParser.MientrasContext):
        pass

    # Exit a parse tree produced by LenguajeParser#mientras.
    def exitMientras(self, ctx:LenguajeParser.MientrasContext):
        pass


    # Enter a parse tree produced by LenguajeParser#asignacion.
    def enterAsignacion(self, ctx:LenguajeParser.AsignacionContext):
        pass

    # Exit a parse tree produced by LenguajeParser#asignacion.
    def exitAsignacion(self, ctx:LenguajeParser.AsignacionContext):
        pass


    # Enter a parse tree produced by LenguajeParser#para.
    def enterPara(self, ctx:LenguajeParser.ParaContext):
        pass

    # Exit a parse tree produced by LenguajeParser#para.
    def exitPara(self, ctx:LenguajeParser.ParaContext):
        pass


    # Enter a parse tree produced by LenguajeParser#repetirCiclo.
    def enterRepetirCiclo(self, ctx:LenguajeParser.RepetirCicloContext):
        pass

    # Exit a parse tree produced by LenguajeParser#repetirCiclo.
    def exitRepetirCiclo(self, ctx:LenguajeParser.RepetirCicloContext):
        pass


    # Enter a parse tree produced by LenguajeParser#llamadaFuncion.
    def enterLlamadaFuncion(self, ctx:LenguajeParser.LlamadaFuncionContext):
        pass

    # Exit a parse tree produced by LenguajeParser#llamadaFuncion.
    def exitLlamadaFuncion(self, ctx:LenguajeParser.LlamadaFuncionContext):
        pass


    # Enter a parse tree produced by LenguajeParser#argumentos.
    def enterArgumentos(self, ctx:LenguajeParser.ArgumentosContext):
        pass

    # Exit a parse tree produced by LenguajeParser#argumentos.
    def exitArgumentos(self, ctx:LenguajeParser.ArgumentosContext):
        pass


    # Enter a parse tree produced by LenguajeParser#expresion.
    def enterExpresion(self, ctx:LenguajeParser.ExpresionContext):
        pass

    # Exit a parse tree produced by LenguajeParser#expresion.
    def exitExpresion(self, ctx:LenguajeParser.ExpresionContext):
        pass


    # Enter a parse tree produced by LenguajeParser#primary.
    def enterPrimary(self, ctx:LenguajeParser.PrimaryContext):
        pass

    # Exit a parse tree produced by LenguajeParser#primary.
    def exitPrimary(self, ctx:LenguajeParser.PrimaryContext):
        pass


    # Enter a parse tree produced by LenguajeParser#lista.
    def enterLista(self, ctx:LenguajeParser.ListaContext):
        pass

    # Exit a parse tree produced by LenguajeParser#lista.
    def exitLista(self, ctx:LenguajeParser.ListaContext):
        pass


    # Enter a parse tree produced by LenguajeParser#matriz.
    def enterMatriz(self, ctx:LenguajeParser.MatrizContext):
        pass

    # Exit a parse tree produced by LenguajeParser#matriz.
    def exitMatriz(self, ctx:LenguajeParser.MatrizContext):
        pass


    # Enter a parse tree produced by LenguajeParser#operator.
    def enterOperator(self, ctx:LenguajeParser.OperatorContext):
        pass

    # Exit a parse tree produced by LenguajeParser#operator.
    def exitOperator(self, ctx:LenguajeParser.OperatorContext):
        pass


