# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=2938

### Tipos de Variables ###

texto = "hola como estas"   # String
num = 45                    # Integer
decimal = 3.14              # float
booleano = True             # Booleano
none = None                 # NoneType
complex_num = 3 + 1j        # Complex


# Concatenación de variables en un print
print(texto, num, booleano)
print("Este es el valor de:", num)

# Algunas funciones del sistema
print(len(texto))

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Brais", "Moure", 'MoureDev', 35
print("Me llamo:", name, surname, ". Mi edad es:",
      age, ". Y mi alias es:", alias)

# Inputs / entrada de texto
name = input('¿Cuál es tu nombre? ')
age = input('¿Cuántos años tienes? ')
print(name)
print(age)

# Cambiamos su tipo
name = 35
age = "Brais"
print(name)
print(age)
