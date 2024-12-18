from LenguajeListener import LenguajeListener
from LenguajeParser import LenguajeParser

class TraducPyCode(LenguajeListener):
    def __init__(self):
        self.result = []  # Almacena el código Python generado
        self.indent_level = 0  # Controla la indentación

    def add_line(self, line):
        """Agrega una línea al resultado con la indentación adecuada."""
        self.result.append("    " * self.indent_level + line)

        # Enter a parse tree produced by LenguajeParser#programa.
    def enterPrograma(self, ctx:LenguajeParser.ProgramaContext):
        pass

    # Exit a parse tree produced by LenguajeParser#programa.
    def exitPrograma(self, ctx:LenguajeParser.ProgramaContext):
        # Unir todas las partes generadas
        self.python_code = "\n".join(self.result)
        self.create_python_file()

    def create_python_file(self):
        """Crea un archivo .py con el nombre del main del programa y escribe el código Python generado."""
        main_function_name = "Tarea"  # Nombre del main del programa
        file_name = f"{main_function_name}.py"
        with open(file_name, 'w') as file:
            file.write(self.python_code)

    def process_expression(self, ctx):
        """Procesa una expresión y traduce los operadores personalizados."""
        if ctx.getChildCount() == 1:  # Nodo hoja: número, variable, texto, etc.
            return ctx.getChild(0).getText()
        elif ctx.getChildCount() >= 3:  # Expresión con operador (binary operation)
            left = self.process_expression(ctx.getChild(0))
            operator = self.translate_operator(ctx.getChild(1).getText())
            right = self.process_expression(ctx.getChild(2))
            return f"({left} {operator} {right})"
        elif ctx.lista():  # Si es una lista
            return self.get_vector(ctx.lista())
        elif ctx.matriz():  # Si es una matriz
            return self.get_matrix(ctx.matriz())
        else:
            return ctx.getText()

    def translate_operator(self, operator):
        """Traduce operadores personalizados al equivalente en Python."""
        operator_map = {
            "-Igual": "==",
            "-MayorOigual": ">=",
            "-MenorOigual": "<=",
            "-Mayor": ">",
            "-Menor": "<",
            "-": "-",
            "+": "+",
            "*": "*",
            "/": "/",
            "%": "%",
            "^": "**",
            "-raíz": "** 0.5",  # Interpretación de raíz
        }
        return operator_map.get(operator, operator)  # Retorna el operador traducido

    # Enter a parse tree produced by LenguajeParser#funcion.
    def enterFuncion(self, ctx:LenguajeParser.FuncionContext):
        nombre = ctx.NAMEF().getText()
        parametros = ctx.parametros().getText() if ctx.parametros() else ""
        self.add_line(f"def {nombre}({parametros}):")
        self.indent_level += 1

    # Exit a parse tree produced by LenguajeParser#funcion.
    def exitFuncion(self, ctx:LenguajeParser.FuncionContext):
        self.indent_level -= 1
        self.add_line("")  # Agregar una línea en blanco al final de la función


    # Enter a parse tree produced by LenguajeParser#parametros.
    def enterParametros(self, ctx:LenguajeParser.ParametrosContext):
        pass

    # Exit a parse tree produced by LenguajeParser#parametros.
    def exitParametros(self, ctx:LenguajeParser.ParametrosContext):
        pass


    # Enter a parse tree produced by LenguajeParser#bloque.
    def enterBloque(self, ctx:LenguajeParser.BloqueContext):
        self.indent_level += 1  # Aumentar la indentación al entrar en un bloque

    # Exit a parse tree produced by LenguajeParser#bloque.
    def exitBloque(self, ctx:LenguajeParser.BloqueContext):
        self.indent_level -= 1  # Disminuir la indentación al salir de un bloque


    # Enter a parse tree produced by LenguajeParser#tarea.
    def enterTarea(self, ctx:LenguajeParser.TareaContext):
        self.add_line('if __name__ == "__main__":')
        self.indent_level =0   # Aumentar la indentación al entrar en una tarea
        self.indent_level += 1

    # Exit a parse tree produced by LenguajeParser#tarea.
    def exitTarea(self, ctx:LenguajeParser.TareaContext):
        self.indent_level -= 1  # Disminuir la indentación al salir de una tarea


    # Enter a parse tree produced by LenguajeParser#sentencia.
    def enterSentencia(self, ctx:LenguajeParser.SentenciaContext):
        pass

    # Exit a parse tree produced by LenguajeParser#sentencia.
    def exitSentencia(self, ctx:LenguajeParser.SentenciaContext):
        pass


    # Enter a parse tree produced by LenguajeParser#declaracion.
    def enterDeclaracion(self, ctx:LenguajeParser.DeclaracionContext):
        Tipo = ctx.getChild(0).getText()
        nombre = ctx.NAMEF().getText()
        valor = self.process_expression(ctx.expresion())
        print(Tipo,nombre,valor,"dx")
        if Tipo == "-Raíz":
            self.add_line(f"{nombre} = {valor} ** 0.5")
        elif Tipo == "lista":
            self.add_line(f"{nombre} = {valor}")
        else:
            self.add_line(f"{nombre} = {valor}")

    # Exit a parse tree produced by LenguajeParser#declaracion.
    def exitDeclaracion(self, ctx:LenguajeParser.DeclaracionContext):
        pass


    def enterAsignacion(self, ctx:LenguajeParser.AsignacionContext):
        if ctx.getChild(0).getText() in ["numero", "texto", "verdadero_falso", "inicial_nombre","repetir"]:
            nombre = ctx.getChild(1).getText()  # Corregir para obtener el nombre de la variable
        else:
            nombre = ctx.getChild(0).getText()  # Corregir para obtener el nombre de la variable
        valor = ctx.expresion().getText()
        if valor == "verdadero":
            self.add_line(f"{nombre} = True")
        else:
            self.add_line(f"{nombre} = {valor}")


    # Exit a parse tree produced by LenguajeParser#asignacion.
    def exitAsignacion(self, ctx:LenguajeParser.AsignacionContext):
        pass

    # Enter a parse tree produced by LenguajeParser#siEntonces.
    def enterSiEntonces(self, ctx:LenguajeParser.SiEntoncesContext):
        condicion = self.process_expression(ctx.expresion())
        self.add_line(f"if {condicion}:")
        self.indent_level += 1

    # Exit a parse tree produced by LenguajeParser#siEntonces.
    def exitSiEntonces(self, ctx:LenguajeParser.SiEntoncesContext):
        self.indent_level -= 1

    # Enter a parse tree produced by LenguajeParser#sinoEntonces.
    def enterSinoEntonces(self, ctx:LenguajeParser.SinoEntoncesContext):
        self.indent_level -= 1
        if ctx.ELSE():
            self.add_line("else:")
            self.indent_level += 1

    # Exit a parse tree produced by LenguajeParser#sinoEntonces.
    def exitSinoEntonces(self, ctx:LenguajeParser.SinoEntoncesContext):
        self.indent_level -= 1

    # Enter a parse tree produced by LenguajeParser#imprimir.
    def enterImprimir(self, ctx:LenguajeParser.ImprimirContext):
        pass

    # Exit a parse tree produced by LenguajeParser#imprimir.
    def exitImprimir(self, ctx:LenguajeParser.ImprimirContext):
        expresion = ctx.expresion().getText()
        # Reemplazar concatenaciones con '+' por comas en la función print
        partes = expresion.replace("+", ",")
        self.add_line(f"print({partes})")


    # Enter a parse tree produced by LenguajeParser#mientras.
    def enterMientras(self, ctx:LenguajeParser.MientrasContext):
        condicion = self.process_expression(ctx.expresion())
        self.add_line(f"while {condicion}:")
        self.indent_level += 1

    # Exit a parse tree produced by LenguajeParser#mientras.
    def exitMientras(self, ctx:LenguajeParser.MientrasContext):
        self.indent_level -= 1


    # Enter a parse tree produced by LenguajeParser#para.
    def enterPara(self, ctx:LenguajeParser.ParaContext):
        pass

    # Exit a parse tree produced by LenguajeParser#para.
    def exitPara(self, ctx:LenguajeParser.ParaContext):
        # Traducción de un bucle `para`
        inicializacion = ctx.asignacion(0).getText()
        condicion = ctx.expresion().getText()
        incremento = ctx.asignacion(1).getText()
        self.add_line(f"for {inicializacion}; {condicion}; {incremento}:")
        self.indent_level += 1

    # Enter a parse tree produced by LenguajeParser#repetirCiclo.
    def enterRepetirCiclo(self, ctx:LenguajeParser.RepetirCicloContext):
        veces = ctx.NUMBER().getText()
        self.add_line(f"for _ in range({veces}):")
        self.indent_level += 1

    # Exit a parse tree produced by LenguajeParser#repetirCiclo.
    def exitRepetirCiclo(self, ctx:LenguajeParser.RepetirCicloContext):
        self.indent_level -= 1

    # Enter a parse tree produced by LenguajeParser#llamadaFuncion.
    def enterLlamadaFuncion(self, ctx:LenguajeParser.LlamadaFuncionContext):
        nombre = ctx.NAMEF().getText()
        argumentos = ctx.argumentos().getText() if ctx.argumentos() else ""
        self.add_line(f"{nombre}({argumentos})")

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


    # Enter a parse tree produced by LenguajeParser#operator.
    def enterOperator(self, ctx:LenguajeParser.OperatorContext):
        pass

    # Exit a parse tree produced by LenguajeParser#operator.
    def exitOperator(self, ctx:LenguajeParser.OperatorContext):
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

    def get_vector(self, ctx):
        """Obtiene un vector (lista) del contexto."""
        return "[" + ", ".join(self.process_expression(child) for child in ctx.expresion()) + "]"

    def get_matrix(self, ctx):
        """Obtiene una matriz (lista de listas) del contexto."""
        return "[" + ", ".join(self.get_vector(row) for row in ctx.lista()) + "]"
    
    def get_python_code(self):
        """Devuelve el código Python generado."""
        return self.python_code