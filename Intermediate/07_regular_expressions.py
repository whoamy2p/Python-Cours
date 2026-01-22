
# RegEx

"""
Una RegEx, o expresión regular, es una secuencia de caracteres que forma un patrón de búsqueda.

Function	        Description
- re.search()	    busca y devuelve la 1ra coincidencia en la cadena y devuelve un objeto Match si hay una coincidencia.
- re.match()	    Busca coincidencia solo al inicio
- re.findall()	    Devuelve una lista que contiene todas las coincidencias.
- re.finditer()	    Iterador de coincidencias
- re.sub()	        Busca y reeemplaza el texto en eleccion, Devulve nuevo string
- re.split()	    Devuelve una lista donde la cadena se ha dividido en cada coincidencia:
"""

"""  OBJETOS DE COINCIDENCIAS -> SEARCH <-
.span()    devuelve una tupla que contiene las posiciones de inicio y fin de la coincidencia.
.string    devuelve la cadena pasada a la función.
.group()   devuelve la parte de la cadena donde hubo una coincidencia.
"""

""" SECUENCIAS ESPECIALES
Clase	Significado
\d	    Dígito (0-9)
\D	    No dígito (0-9)
\w	    Letras + números + _     ->   (a-z, A-Z, 0-9, _)
\W	    No \w
\s	    Espacio
\S	    No espacio
\b      Limite de palabra (mas estricto la expresion)
"""

"""
Character	Description	                                                                  Example
[]	        Un conjunto de caracteres	                                                  "[a-m]"	
\	        Signals a special sequence (can also be used to escape special characters)	  "\d"	
.	        Cualquier carácter (excepto el carácter de nueva línea)	                      "he..o"	
^	        Empíeza con	(texto)                                                           "^hello"	
$	        Termina con	 (texto)                                                          "planet$"	
*	        Cero o más ocurrencias	                                                      "he.*o"	
+	        Uno o mas ocurrencias	                                                      "he.+o"	
?	        Cero o una ocurrencia                                                         "he.?o"	
{n} | {n,m}	Exactamente el número especificado de ocurrencias	                          "he.{2}o"	
|	        Cualquiera o	                                                              "falls|stays"	
()	        Captura y grupo solo lo que esta dentro del parentesis
"""

"""
Set	        Description	
[arn]	    Devuelve una coincidencia donde uno de los caracteres especificados (a, r o n) está presente	
[a-n]	    Devuelve una coincidencia para cualquier carácter en minúscula, alfabéticamente entre a y n	
[^arn]	    Devuelve una coincidencia para cualquier carácter EXCEPTO a, r y n	
[0123]	    Devuelve una coincidencia donde cualquiera de los dígitos especificados (0, 1, 2 o 3) está presente	
[0-9]	    Devuelve una coincidencia para cualquier dígito entre 0 y 9 	
[0-5][0-9]	Devuelve una coincidencia para cualquier número de dos dígitos entre 00 y 59
[a-zA-Z]	Devuelve una coincidencia para cualquier carácter alfabético entre a y z, en minúscula o en mayúscula.	
[+]	        En conjuntos, +, *, ., |, (), $,{} no tienen un significado especial, por lo que [+] significa: devolver una coincidencia para cualquier carácter + en la cadena
"""


""" 🔥 FLAGS (MODIFICADORES)
Flag	Uso
re.I	Ignorar mayúsculas
re.M	Multilínea
re.S	El punto incluye salto
re.X	Regex comentado
"""

"""
NOTA: OJO  --> \ <--

Sí.
Cuando usas \(, \. , \+, etc.
estás diciendo literalmente:

👉 “Este símbolo ya no es especial.
Trátalo como un carácter normal.”
"""

"""
OJO:  

Usar \b hace que tu patrón sea más estricto: no solo debe coincidir con la forma que definiste, sino que también tiene que estar aislado (con espacios, caracteres especiales o inicio/final de cadena) para que se capture.
Sin \b, el patrón solo se fija en la forma y captura coincidencias incluso si están pegadas a otras letras o números.
"""

"""
Importante saber 
--> lookbehind <-- mira hacia atrás
(?<!X) →  “Antes de aquí, NO debe estar X”
(?<=X) → “Antes de aquí, SÍ debe estar X”

--> lookahead <-- mira hacia adelante
(?!X) →  “Después de aquí NO debe venir X”
(?=X) →  “Después de aquí SÍ debe venir X”

(?:X) -> Agrupa sin capturar -> no crea grupo para extraer luego
"""

# -------------------------------------------------- EJEMPLOS

import re

texto = """Hola mundo. el
Mi pimer el numero de la suerte el es 945-659
"""

# busca coincidencia en todo el texto devulve objeto "re.match" sino "None"
var = re.search ("mundo.", texto)

print (var)            # Devuelve objeto re.match
print (var.span ())    # Devuelve el rango de la palabra buscada -> (5, 11)
print (var.start ())   # Devulve la posicion donde empieza
print (var.end ())     # Devuelve la posicion donde termina
print (var.group ())   # Devulve la palabra buscada -> "mundo"

# devuelve "re.match" si empieza con la palabra buscada sino "None"
var1 = re.match ("Hola", texto)

# findall () y finditer () hacen lo mismo, buscan coincidencia en toda la cadena
var2 = re.findall ("el", texto)   # Devulve lista
var3 = re.finditer ("el", texto)  # Devuelve objeto iterador match

# re.sub (busca, reemplaza, texto)  # Devuelve nuevo string
texto = "Me gusta el café. El café es rico."
var = re.sub ("café", "te", texto)

# re.split (separador, texto) : Devuelve una lista 
texto = "Manzana,Pera,Naranja"
var4 = re.split (",", texto)

## -------------------------------- Insertando expresion regulares -------------------------------------

# El punto representa CUALQUIER caracter (excepto nueva línea)
re.findall("a.c", "abc axc a c a-c app")  # ['abc', 'axc', 'a c', 'a-c']
# Encuentra: a + CUALQUIER CARACTER + c

# ^ significa "empieza con"
re.findall("^Hola", "Hola mundo")    # ['Hola'] ✓
re.findall("^Hola", "Dice Hola")     # [] ✗ (no empieza con Hola)

# $ significa "termina con"
re.findall("mundo$", "Hola mundo")   # ['mundo'] ✓
re.findall("mundo$", "mundo feliz")  # [] ✗ (no termina con mundo)

# * significa * = 0 o más veces
re.findall("ab*c", "ac abc abbc abbbc")    # ['ac', 'abc', 'abbc', 'abbbc']
# Encuentra: a + (b cero o más veces) + c

# + significa + = 1 o más veces (debe aparecer al menos 1)
re.findall("ab+c", "ac abc abbc abbbc")   # ['abc', 'abbc', 'abbbc']  

# ? significa ? = 0 o 1 vez , opcional
re.findall("ab?c", "ac abc abbc")    # ['ac', 'abc']  (NOTA: 'abbc' NO está porque tiene 2 'b')

# {} significa   {n} = exactamente n veces  ;  {n,m} = entre n y m veces
re.findall("a{3}", "aa aaa aaaa")    # ['aaa', 'aaa'] (de 'aaaa' toma solo 3)
re.findall("a{2,4}", "a aa aaa aaaa aaaaa")  # ['aa', 'aaa', 'aaaa', 'aaaa'] (entre 2 y 4 'a')

# | significa "esto O aquello"
re.findall("gato|perro", "tengo un gato y un perro")   # ['gato', 'perro']  (encuentra gato O perro)

# () agrupa y captura
resultado = re.search("(ab)+", "ababab")
print(resultado.group())  # 'ababab' (todo el match)
print(resultado.group(1)) # 'ab' (lo que capturó el grupo)