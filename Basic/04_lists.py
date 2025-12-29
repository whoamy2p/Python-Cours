# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=10872

### Lists ###

# Definición

my_list = list()
my_other_list = []

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Brais", "Moure"]

print(type(my_list))
print(type(my_other_list))

# Acceso a elementos y búsqueda

print(my_other_list[0])
print(my_other_list[-4])

age, height, *name = my_other_list  # comodin unpacking
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

# Concatenación

print(my_list + my_other_list)

# Funciones y metodos para listas


lista = ["Cesar", 23, 1.70, "peru"]
lista1 = [1, 2, 3]

lista.append("Ingeniero")  # Agregar al final
lista.insert(1, "Rojo")    # Agregar en posición específica

lista.remove("Cesar")      # Eliminar elemento por valor
print(lista.pop(2))         # Elimina el ultimo elemento, con parametro el indice indicado
lista.clear ()            # Limpia toda la lista

print(lista.count(23))    # cuenta la cantidad de vces que repite
print(lista.index("peru"))  # Devulve la posicion del elemento

listax = lista.copy ()   # copia el contenido
lista.extend (lista1)    # Combina dos iterables
lista.reverse ()  # invierte el contenido de un iterable
lista.sort ()   # Ordena el contenido de un iterable
print (sorted (lista))  # Ordena el contenido de la lista  -> devuelve una nueva lista


del my_list[2]
print(my_list)


