"""
Docstring for Hello-Python.Ejercicio-SQL
"""

# ORDER BY
"""
EJERCICIO 1

📌 Encuentra todas las películas ordenadas por título de A a Z
👉 Debes usar: SELECT + ORDER BY

EJERCICIO 2

📌 Encuentra todas las películas dirigidas por "Brad Bird" y ordénalas por año (de más antigua a más nueva)
👉 Debes usar: WHERE + ORDER BY

EJERCICIO 3

📌 Encuentra todas las películas que NO fueron dirigidas por "Jhon Lasseter" y ordénalas por director
Debes usar: WHERE, != o NOT, ORDER BY

EJERCICIO 4

📌 Encuentra todas las películas que empiecen con "Toy" y ordénalas por año descendente

⚠️ Pista:
Todavía no hemos visto LIKE, así que por ahora hazlo solo con lo que sabes:
👉 Usa WHERE con condiciones simples (title = ... o OR)

"""

# LIMIT
"""

📝 EJERCICIO 1

📌 Muestra solo las 4 primeras películas ordenadas por título

📝 EJERCICIO 2

📌 Muestra las 3 películas más nuevas (por año)

📝 EJERCICIO 3

📌 Muestra solo 2 películas dirigidas por "Andrew Stanton"

📝 EJERCICIO 4

📌 Muestra la película más larga de todas

⚠️ Pista:
Ordena por duración descendente y usa LIMIT 1.
"""

#  BETWEEN & IN
"""
🔹 Ejercicio 1

Muestra el título, año y rating de las películas que sean del año entre 2000 y 2010, ordenadas por año.

🔹 Ejercicio 2

Muestra todas las películas dirigidas por:
"Pete Docter", "Brad Bird", "Andrew Stanton"
Muestra título y director, ordenadas por director.

🔹 Ejercicio 3

Muestra las películas con rating entre 7.0 y 8.0, mostrando título y rating, ordenadas por rating descendente.

🔹 Ejercicio 4

Muestra las películas que:
Sean de "USA" o "Mexico" (usa IN) Y tengan duración entre 95 y 115 minutos
Muestra título, país y duración.

🔹 Ejercicio 5

Muestra las películas que NO fueron dirigidas por:
"John Lasseter", "Josh Cooley"
Muestra título y director.
"""

# LIKE & IS NULL / IS NOT NULL
"""
🟡 Ejercicio 1

Mostrar el título y director de todas las películas cuyo título comience con la letra “S” y que sí tengan director registrado.

🟡 Ejercicio 2

Mostrar el título, año y rating de las películas cuyo título contenga la palabra “Star” y cuyo rating esté entre 7.5 y 9.0.

🟡 Ejercicio 3

Mostrar todas las películas que no tengan país registrado y cuyo título termine en “Man”.

🟡 Ejercicio 4

Mostrar título, director y país de las películas donde:
El nombre del director empiece con “B” Y el país no esté vacío
Ordenar por título en orden alfabético.

🟡 Ejercicio 5 (difícil 🔥)

Mostrar título, año, director y rating de las películas donde:
El título contenga la letra “o” en cualquier parte
El director no esté vacío
El rating no sea NULL
El año esté entre 2005 y 2020

Mostrar solo las 5 más recientes.
"""
