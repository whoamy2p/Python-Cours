"""
Nivel Básico (20 ejercicios)

- Extraer solo los números de "Edad: 25 años"
- Obtener solo las vocales de "murciélago"
- Capturar solo los nombres de "Juan Pérez, María López"
- Extraer el dominio de "usuario@gmail.com" (sin @ ni .com)
- Obtener solo el día de fechas como "2024-01-15"
- Capturar solo el código postal de "CP: 28001"
- Extraer solo las iniciales de "Ana María"
- Obtener solo la hora de "Hora: 14:30" (sin minutos)
- Capturar solo las palabras entre comillas dobles
- Extraer solo los hashtags de "#python #aprendizaje" (sin #)
- Obtener solo el precio de "$1200" (sin $)
- Capturar solo la extensión de "documento.pdf"
- Extraer solo el año de "Copyright 2024"
- Obtener solo el usuario de "telegram: @usuario123"
- Capturar solo las primeras 3 letras de "abcdef"
- Extraer solo el código de "(ABC-123)"
- Obtener solo el nombre del archivo de "ruta/archivo.txt"
- Capturar solo las consonantes de "hola mundo"
- Extraer solo la temperatura de "Temp: 25°C"
- Obtener solo la palabra antes de "es" en "Python es genial"

Nivel Intermedio (10 ejercicios)

- Extraer solo los números pares de una lista de números
- Capturar solo palabras que comiencen con vocal
- Obtener solo las direcciones IP de un texto (solo los octetos)
- Extraer solo las etiquetas HTML de "<p>texto</p>" (sin <>)
- Capturar solo las palabras palíndromas de 3 letras
- Obtener solo los identificadores de variables de código Python
- Extraer solo los números decimales pero sin el punto
- Capturar solo los encabezados Markdown (# Título)
- Obtener solo las fechas en formato dd/mm/aaaa (solo día y mes)
- Extraer solo las palabras que tengan letras repetidas consecutivas
"""


"""
Ejercicio 1

Extrae solo números de teléfono con este formato:
-> (XXX) XXX-XXXX
"Llámanos al (123) 456-7890 o al (999) 000-1111. Código: (12) 345-6789"

Ejercicio 2

- Extrae usuarios que cumplan:
- solo letras y números
- mínimo 4 caracteres
- empiezan con letra

"Usuarios: Ana12, 9luis, tom, Maria99, _root, Pedro1"

# Ejercicio 3

- Extrae nombres de archivo que:
- terminen en .pdf
- tengan letras, números o guiones bajos

"Docs: reporte_final.pdf, data-2024.pdf, imagen.png, 123file.pdf"

# Ejercicio 4

Extrae horas válidas en formato: HH:MM
(00–23 horas, 00–59 minutos)

"Reuniones: 09:30, 25:61, 18:45, 7:05, 00:00"

# Ejercicio 5

Extrae códigos que tengan:  AAA-999
- 3 letras mayúsculas
- guion
- 3 números

"Productos: TV-123, ABC-999, car-456, XYZ-001, AAA-12"

"""

"""
Ejercicio 6

Extrae fechas válidas en formato DD/MM/AAAA.
- Días: 01–31
- Meses: 01–12
- Año: 4 dígitos

texto = "Fechas: 12/05/2023, 31/13/2024, 01/01/2020, 32/12/2022"
# Resultado esperado: ['12/05/2023', '01/01/2020']

Ejercicio 7

Extrae hashtags válidos de Twitter:
- Empiezan con #
- Solo letras, números o guiones bajos
- Al menos 2 caracteres después de #

texto = "Posts: #Python, #AI_2026, #1data, #x, #hola_mundo"
# Resultado esperado: ['#Python', '#AI_2026', '#1data', '#hola_mundo']

Ejercicio 8

- Extrae direcciones de email simples:
- Letras, números, puntos o guiones antes de @
- Dominio con letras y punto
- Extensión de 2–4 letras

texto = "Emails: juan@gmail.com, ana@outlook, pedro_123@mail.co, invalid@domain, root@abc.xyz"
# Resultado esperado: ['juan@gmail.com', 'pedro_123@mail.co', 'root@abc.xyz']

Ejercicio 9

- Extrae códigos alfanuméricos de producto:
- Formato: 2 letras mayúsculas + 4 números
- Ejemplo: AB1234

texto = "Inventario: AB1234, XY5678, aa1234, Z9X8Y7"
# Resultado esperado: ['AB1234', 'XY5678']

Ejercicio 10
- Extrae URLs simples:
- Comienzan con http:// o https://
- Dominio con letras, números, puntos o guiones
- Opcionalmente terminan con / o /algo

texto = "Enlaces: http://google.com, https://github.com/whoamy2p, ftp://server.com, https://site.org/"
# Resultado esperado: ['http://google.com', 'https://github.com/whoamy2p', 'https://site.org/'
"""

# ----------------------- REFERENCIAS RÁPIDAS RE 1

"""
Ejercicio 11 – Extraer números de teléfono

- Formato: (XXX) XXX-XXXX
- Solo números entre paréntesis y separados por guion

texto = "Llámanos al (123) 456-7890 o al (999) 000-1111. Código: (12) 345-6789"
# Salida esperada: ['(123) 456-7890', '(999) 000-1111']


Ejercicio 12 – Extraer códigos postales

- Solo números de 5 dígitos
- Por ejemplo: 12345

texto = "Direcciones: Lima 15001, Cusco 08002, Arequipa 0400, Piura 20001"
# Salida esperada: ['15001', '08002', '20001']


Ejercicio 13 – Extraer nombres de usuario

- Empiezan con letra
- Solo letras y números
- Mínimo 4 caracteres

texto = "Usuarios: Ana12, 9luis, tom, Maria99, _root, Pedro1"
# Salida esperada: ['Ana12', 'Maria99', 'Pedro1']


Ejercicio 14 – Extraer nombres de archivos

- Terminen en .txt o .csv
- Pueden tener letras, números o guiones bajos

texto = "Archivos: data_final.txt, reporte_2024.csv, imagen.png, resumen.docx"
# Salida esperada: ['data_final.txt', 'reporte_2024.csv']


Ejercicio 15 – Extraer horas en formato HH:MM

- Horas: 00–23
- Minutos: 00–59

texto = "Reuniones: 09:30, 25:61, 18:45, 7:05, 00:00"
# Salida esperada: ['09:30', '18:45', '00:00']

"""

# ----------------------- REFERENCIAS RÁPIDAS RE 2

"""
Ejercicio 16 – Extraer números de tarjetas simples

- Formato: XXXX-XXXX-XXXX-XXXX (solo números)
- Ejemplo válido: 1234-5678-9012-3456

texto = "Tarjetas: 1234-5678-9012-3456, 0000-1111-2222-333, 4321-8765-0000-9999"
# Salida esperada: ['1234-5678-9012-3456', '4321-8765-0000-9999']


Ejercicio 17 – Extraer códigos de productos con guion

- Formato: AAA-999
- 3 letras mayúsculas + guion + 3 números

texto = "Productos: TV-123, ABC-999, car-456, XYZ-001, AAA-12"
# Salida esperada: ['ABC-999', 'XYZ-001']


Ejercicio 18 – Extraer direcciones IPv4

- Formato: X.X.X.X
- Cada octeto: 0–255 (puedes simplificar con 0–999 para regex intermedio)

texto = "Redes: 192.168.1.1, 256.100.0.1, 10.0.0.5, 123.456.78.90"
# Salida esperada: ['192.168.1.1', '10.0.0.5']


Ejercicio 19 – Extraer números de serie

- Formato: 2 letras + 2 números + 2 letras + 2 números
- Ejemplo: AB12CD34

texto = "Series: AB12CD34, XY99ZZ00, 12AB34CD, A1B2C3D4"
# Salida esperada: ['AB12CD34', 'XY99ZZ00']


Ejercicio 20 – Extraer etiquetas HTML simples

- Etiquetas como <div>, <p>, <h1>
- Solo abrir etiquetas (sin atributos por ahora)

texto = "<div>Hola</div><p>Texto</p><span>Otro</span><h1>Título</h1>"
# Salida esperada: ['<div>', '<p>', '<span>', '<h1>']
"""