# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=34583

### Modules ###

from math import pi as PI_VALUE
import math
from mypackage.my_module import Validar_email



print(math.pi)
print(math.pow(2, 8))


print(PI_VALUE)

print (Validar_email ("cesar@gmail.com")) # True


"""
🧠 REGLA DE ORO DE MÓDULOS
    📌 Un módulo = una responsabilidad

Ejemplo:

- auth.py → autenticación
- db.py → base de datos
- utils.py → helpers
- models.py → clases
"""

"""
proyecto/
│
├── main.py          -> Modulo
├── usuarios.py      -> Modulo
├── productos.py     -> Modulo
└── utils.py         -> Modulo

# - ------------------ Paquete ---------------
tienda/
│
├── __init__.py   # Indica que es un paquete (conjunto  de modulos)
├── carrito.py
├── producto.py
└── usuario.py


"""


"""
¿Qué es orquestación?

Orquestación es:

👉 El código que coordina, conecta y dirige
👉 a las clases y módulos para que trabajen juntas
👉 sin contener lógica de negocio

En palabras simples:

Es el “director de orquesta” 🎼
No toca instrumentos, solo indica quién entra, cuándo y con qué.

-------------------------------------------------------------------------------

3️⃣ Regla de oro (muy importante)

🧠 La orquestación puede conocer a todos
🔒 Pero nadie debe conocer a la orquestación
"""