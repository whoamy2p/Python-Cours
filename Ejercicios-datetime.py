"""
Docstring for Hello-Python.Ejercicios-datetime

🧠 EJERCICIO 1 — Fecha de vencimiento simple

Nivel: Intermedio bajo

Enunciado
- Pide al usuario una fecha en formato: dd/mm/yyyy
- Luego:
    - conviértela a datetime
    - suma 45 días
    - muestra la fecha de vencimiento en formato: yyyy-mm-dd


📌 Practicas:
- strptime
- strftime
- timedelta


🧠 EJERCICIO 2 — ¿Cuántos días faltan?

Nivel: Intermedio

Enunciado
Pide una fecha futura al usuario y muestra:
cuántos días faltan desde hoy
si la fecha ya pasó, mostrar un mensaje adecuado

📌 Practicas:
- comparación de fechas
- resta de datetime
- .days


🧠 EJERCICIO 3 — Ejecución cada X minutos

Nivel: Intermedio

Enunciado
 Simula un script que:
 se ejecuta cada 10 minutos
 imprime la hora de ejecución
 se detiene después de 5 ejecuciones

Reglas
- Usa datetime y timedelta
- NO uses sleep(600) directo
- Controla el número de ejecuciones



🧠 EJERCICIO 4 — Validación de expiración

Nivel: Intermedio

Enunciado
 Simula un token que:
 se crea ahora
 expira en 3 minutos
 cada 30 segundos verifica:
 si sigue válido
 o si ya expiró

Reglas
- Usa datetime.now()
- Usa timedelta
- Usa sleep(30)
- Detén el script cuando expire

📌 Practicas:
- comparación de fechas
- loops controlados
- expiración simple
"""

# AVANZADOS  -**************

"""
🧠 EJERCICIO 1 — Ventana deslizante de actividad (Security)

Nivel: Intermedio–alto

Enunciado
Tienes una lista de eventos de conexión con timestamps (string).
Debes detectar si en cualquier ventana de 5 minutos ocurren más de 10 eventos.

Datos de entrada
eventos = [
    "2026-01-16 10:00:00",
    "2026-01-16 10:00:30",
    "2026-01-16 10:01:10",
    ...
]

Reglas
- Convierte strings → datetime
- Usa timedelta
- NO uses librerías externas
- Detecta la primera ventana sospechosa
- Imprime inicio y fin de la ventana

📌 Esto simula:
- detección de fuerza bruta / anomalías



🧠 EJERCICIO 2 — Scheduler preciso sin acumulación de error

Nivel: Alto

Enunciado
Crea un scheduler que:
se ejecute exactamente cada 30 minutos
aunque la tarea dure tiempo variable
no use sleep(1800) directamente

Requisitos
- Usa datetime y timedelta
- Calcula la próxima ejecución basada en reloj real
- Soporta que la tarea dure más de 30 segundos

📌 Esto es:
- calidad de código de producción


🧠 EJERCICIO 3 — Token con expiración renovable

Nivel: Intermedio–alto

Enunciado
Implementa un sistema de tokens que:
expiran a los 15 minutos
si el token se usa antes de expirar, se renueva automáticamente
si expira, se invalida

Reglas
- Usa datetime.now()
- Usa timedelta
- No uses time.time()
- Simula varios accesos en distintos tiempos

📌 Esto es exactamente:
- cómo funcionan sesiones reales


🧠 EJERCICIO 4 — Correlación de eventos entre dispositivos

Nivel: Alto

Enunciado
Tienes eventos enviados por varios equipos:

eventos = [
    ("PC-01", "2026-01-16 10:00:01"),
    ("PC-02", "2026-01-16 10:00:03"),
    ("PC-01", "2026-01-16 10:02:10"),
    ("PC-03", "2026-01-16 10:04:55"),
]


Debes detectar si 3 dispositivos distintos reportan eventos dentro de una ventana de 2 minutos.

Reglas
- Convertir a datetime
- Usar timedelta
- No usar sets directamente para resolverlo (piensa bien)
- Imprimir la ventana detectada y los dispositivos

📌 Esto simula:
- detección distribuida / incidentes coordinados




🧠 Reglas generales (muy importante)

- Para TODOS los ejercicios:
- Nada de while True infinitos sin control
- Nada de variables globales sucias
- Código legible
- Manejo correcto de fechas

🎯 Cómo te recomiendo abordarlos

1️⃣ Convierte todo a datetime
2️⃣ Piensa en intervalos, no en instantes
3️⃣ Usa timedelta como herramienta principal
4️⃣ Imagina que es código de producción, no de tarea
"""
