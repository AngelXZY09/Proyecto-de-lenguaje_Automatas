from antlr4 import *
from LenguajeLexer import LenguajeLexer
from LenguajeParser import LenguajeParser
from LenguajeListener import LenguajeListener
from prueba4 import TraducPyCode

def main():
    for file_name in ['PruebaIf.prueba']:
        with open(file_name, 'r') as fileope:
            file_content = fileope.read()
        
        lexer = LenguajeLexer(InputStream(file_content))
        stream = CommonTokenStream(lexer)
        parser = LenguajeParser(stream)
        tree = parser.programa()

        # Aplica el listener
        listener = TraducPyCode()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        # Imprime el árbol sintáctico
        print(tree.toStringTree(recog=parser))

        # Imprime el código Python generado
        print(f"Código Python generado para {file_name}:")
        print(listener.get_python_code())

if __name__ == '__main__':
    main()