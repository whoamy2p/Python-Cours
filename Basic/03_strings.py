# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=8643

### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

# Formateo

name, surname, age = "Brais", "Moure", 35
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaqueado de caracteres

language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse

reversed_language = language[::-1]
print(reversed_language)

# Funciones del lenguaje
texto = "  Hola es mundo como estas  "

texto.lower()       # todo a minuscula
texto.upper()       # todo a mayuscula
texto.title()       # cada palabra con mayuscula
texto.capitalize()  # primera letra mayuscula
texto.swapcase()    # cambia mayusculas por minusculas y viceversa

texto.find("es")        #    (posición) (-1 si no existe)
texto.rfind("es")       #    (posición) (-1 si no existe)
texto.index("es")       #    (error si no existe)
texto.count("o")        #    devulve la cantidad de veces que aparece

email = " cesarquintana@gmail.com"
email.strip(" ")       #  elimina caracter y espacio al inicio y final
email.lstrip(" cesar")      #  elimina caracter y espacio al inicio
email.rstrip(".com")      #  elimina caracter y espacio al final

lista = ["Cesar", "Quintana", "Errazabal"]
texto.replace("mundo", "Python")  # reemplaza texto
texto.split(" ")                 # convierte string en lista
",".join(lista)                # convierte lista en string

texto.startswith("arch")   # True
texto.endswith(".txt")     # True

"123".isdigit()        # True
"abc".isalpha()        # True
"abc123".isalnum()     # True
" ".isspace()          # True
"Hola".istitle()       # True
"hola".islower()       # True
"HOLA".isupper()       # True
