# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=14711

### Tuples ### son inmutables

# Definición

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

# Acceso a elementos y búsqueda

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Brais"))
print(my_tuple.index("Moure"))

# Concatenación

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

# Subtuplas

print(my_sum_tuple[3:6])

# Desempaquetar
(a, b, c, *d) = my_tuple
print (a)
