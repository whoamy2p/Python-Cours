import re

"""
Ejercicio 22 – Extraer palabras que empiecen con mayúscula
Empiezan con letra mayúscula
Luego solo letras minúsculas
Mínimo 3 letras en total
"""

text = "Nombres: Ana, juan, Pedro, Lu, Carlos, mAria"
print (re.findall (r"\b[A-Z][a-z]{2,}\b", text))


"""
Ejercicio 23 – Extraer fechas en formato AAAA-MM-DD
Año: 4 dígitos
Mes: 01–12
Día: 01–31 (no necesitas validar meses exactos)
"""
text = "Fechas: 2024-01-15, 2023-13-01, 2025-12-31, 20-05-10"
print (re.findall (r"\b\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01])\b", text))

"""
Ejercicio 24 – Extraer nombres de variables estilo Python

Empiezan con letra o _
Luego letras, números o _
No pueden empezar con número
"""

text = "Vars: _total, suma1, 2dato, valor_max, $error, temp"
print (re.findall (r"\b[a-zA-Z_]\w+\b", text, re.I))

"""
Ejercicio 25 – Extraer etiquetas HTML con contenido

Captura etiquetas simples con su contenido
Formato: <tag>contenido</tag>
Sin atributos por ahora
"""
text = "<p>Hola</p><div>Texto</div><span>123</span><h1>Título</h1>"
print (re.findall (r"<[a-z0-9]+>\w+</[a-z0-9]+>", text))


