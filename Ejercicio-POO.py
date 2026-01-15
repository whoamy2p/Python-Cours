"""
🧩 EJERCICIO 1 – Sistema de empleados (Herencia + Polimorfismo)
Contexto

Una empresa tiene distintos tipos de empleados.

Clases base
    - Empleado
    - atributos: nombre, dni, salario_base
    - método: calcular_salario() → polimórfico

Clases hijas
    - EmpleadoTiempoCompleto
    - EmpleadoPorHoras
    - EmpleadoComision

Reglas
    - Tiempo completo: salario fijo
    - Por horas: salario = horas_trabajadas x tarifa
    - Comisión: salario = salario_base + comisión

Tarea
    - Crea una lista con distintos empleados
    - Recorre la lista y calcula el salario sin usar if/else
    - Usa polimorfismo correctamente

    
🧩 EJERCICIO 2 – Sistema bancario (Encapsulamiento fuerte)
Contexto

Un banco maneja cuentas de usuarios.

Clase
    - CuentaBancaria
    - atributos privados
    - saldo
    - número de cuenta

métodos:
    - depositar()
    - retirar()
    - consultar_saldo()

Reglas
    - No se puede retirar más dinero del disponible
    - El saldo NO debe modificarse directamente
    - El número de cuenta no puede cambiar

Tarea
    - Intenta modificar el saldo desde fuera (y evita que funcione)
    - Usa getters/setters solo si es necesario

    
🧩 EJERCICIO 3 – Carrito de compras (Composición + Polimorfismo)
Contexto

Una tienda vende distintos tipos de productos.

Clases
    - Producto (base)
    - ProductoDigital
    - ProductoFisico

Reglas
    - Digital → no tiene costo de envío
    - Físico → costo de envío depende del peso

Clase adicional
    - Carrito
        - contiene una lista de productos
        - método total_pagar()

Restricción
    - El carrito NO debe saber qué tipo de producto es
    - Cada producto decide su precio final

    
🧩 EJERCICIO 4 – Sistema de autenticación (POO realista)
Contexto

Sistema con distintos tipos de usuarios.

Clases
    - Usuario (base)
    - Admin
    - Cliente

Reglas
    - Todos pueden iniciar sesión
    - Solo Admin puede eliminar usuarios
    - Cliente solo puede ver su perfil

Tarea
    - Implementa métodos con el mismo nombre pero comportamiento distinto
    - Usa polimorfismo, no validaciones por tipo

    
🧩 EJERCICIO 5 – Sensores (Abstracción + Herencia)
Contexto

Un sistema recibe datos de sensores.

Clase abstracta
    - Sensor
    - método abstracto: leer_dato()

Clases hijas
    - SensorTemperatura
    - SensorHumedad
    - SensorPresion

Tarea
    - Simula lecturas diferentes
    - Almacena sensores en una lista
    - Llama al mismo método sin importar el tipo

    
🧩 EJERCICIO 6 – Juego simple (Encapsulamiento + Estado)
Contexto

Juego con personajes.

Clase
    - Personaje
    - atributos privados: vida, energía
    - métodos:
    - atacar()
    - recibir_daño()        
    - curar()

Reglas
    - La vida nunca puede ser negativa
    - Si energía llega a 0, no puede atacar
    - Nadie puede modificar vida directamente
"""
