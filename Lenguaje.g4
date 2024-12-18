grammar Lenguaje;

// Lexer rules;

//Funcion
FUNCION: 'Hacer';
NAMEF: [a-zA-Z_][a-zA-Z0-9_]*;
VARIABLE: [a-zA-Z_][a-zA-Z0-9_]*;

//Imprimir
IMPRIMIR: '-Escribir';

//Principal
MAIN: '-Tarea-';

//Variables
INT: 'numero';
NUMBER: [0-9]+ ('.' [0-9]+)?;
STRING: 'texto';
ORACION: '"' .*? '"';

BOOLEAN: 'verdadero_falso';
CHAR: 'inicial_nombre';

//Operators
MENOS: '-';
MULT: '*';
EQUALS: '=';
MAS: '+';
DIV: '/';
PORCENTAJE: '%';
MAYORIGUAL: '-MayorOigual';
IGUAL: '-Igual';
MENORIGUAL: '-MenorOigual';
MENOR: '-Menor';
MAYOR: '-Mayor';
POW: '^';
SQRT: '-Raíz';

//Agrupacion
LPAREN: '(';
RPAREN: ')';
LCORCHE: '[';
RCORCHE: ']';
LLLAVE: '{';
RLLAVE: '}';
PUNTOYCOMA: ';';
COMA: ',';

//ciclo
IF: '-Si';
ELSE: '-Sino';

// Estructuras de control
MIENTRAS: '-mientras';
PARA: '-para';

// Ciclo FOR
FOR: '-repetir';

// Listas y matrices
LISTA: 'lista';

// Skip whitespaces and newlines
WS: [ \t\r\n]+ -> skip;

//Parser rules

programa: (funcion)* tarea;
funcion: FUNCION NAMEF LPAREN (parametros)? RPAREN LLLAVE bloque RLLAVE;
parametros: NAMEF (COMA NAMEF)*;
bloque:(sentencia)+;
sentencia: siEntonces | declaracion | asignacion | mientras | para | repetirCiclo | imprimir | llamadaFuncion;
tarea: MAIN LLLAVE sentencia* RLLAVE;

declaracion: (BOOLEAN | INT | STRING | SQRT | LISTA) NAMEF EQUALS expresion PUNTOYCOMA;
siEntonces: IF LPAREN expresion RPAREN LLLAVE bloque RLLAVE (sinoEntonces)?;
sinoEntonces: ELSE LLLAVE bloque RLLAVE;
imprimir: IMPRIMIR LPAREN expresion RPAREN PUNTOYCOMA;
mientras: MIENTRAS LPAREN expresion RPAREN bloque;
asignacion: NAMEF EQUALS expresion PUNTOYCOMA;
para: PARA LPAREN asignacion expresion PUNTOYCOMA asignacion RPAREN bloque;
repetirCiclo: FOR NUMBER 'veces' LLLAVE bloque RLLAVE;
llamadaFuncion: '--' NAMEF LPAREN argumentos? RPAREN;
argumentos: expresion (COMA expresion)*;
expresion: primary (operator primary)*;
primary: NUMBER | ORACION | BOOLEAN | NAMEF | lista | matriz | LPAREN expresion RPAREN;
lista: LCORCHE (expresion (COMA expresion)*)? RCORCHE;
matriz: LCORCHE (lista (COMA lista)*)? RCORCHE;
operator: MAS | MENOS | MULT | DIV | PORCENTAJE | POW | IGUAL | MENOR | MAYOR | MENORIGUAL | MAYORIGUAL;






