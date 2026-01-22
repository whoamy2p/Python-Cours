
#  -------------- SQLite 3 ----------------------------

# Tipos de datos

"""
OJO: SQLIte no tiene tipo booleano se repsentan con 0 y 1

NULL     : Valor Nulo
INTEGER  : Entero (positivo / negativo)
REAL     : Numero Decimal (float)
TEXT     : Texto
BLOB     : Datos binarios (imágenes, pdf, audio, etc.)
"""

# Operadores artiméticos

"""
+    : Suma
-    : Resta
*    : Multiplicación
/    : División
%    : Módulo
**   : Exponente
"""

# Operadores de comparación

"""
=           : Igual que
!= o <>     : Distinto que
>           : Mayor que
<           : Menor que
>=          : Mayor o igual que
<=          : Menor o igual que
"""

# Operadores lógicos

"""
AND         : Y
OR          : O
NOT         : NO
"""

# Operadores especiales

"""
BETWEEN     : Entre un rango de valores
IN          : Dentro de una lista de valores
LIKE        : Coincide con un patrón
IS NULL     : Es nulo
"""

#  -----------------------------------------------------

# CREATE TABLE -> En toda tabla debe de haber su PRIMARY KEY

"""
CREATE TABLE nombre_tabla (
    columna1 TIPO_DATO,
    columna2 TIPO_DATO,
    columna3 TIPO_DATO
)
"""
# PRIMARY KEY -> Clave primaria (Identificador único)
# AUTOINCREMENT -> Incrementa automáticamente el valor de la clave primaria
# NOT NULL -> No permite valores nulos (columnas nulos)
# UNIQUE -> No permite valores duplicados en la columna
# DEFAULT -> Valor por defecto si no se especifica ningún valor
# CHECK (expresion math) -> Restringe los valores que se pueden insertar en una columna

# Ejercicios

# Crear una tabla
"""
CREATE TABLE Nombre_tabla (
	"id" INTEGER PRIMARY KEY AUTOINCREMENT,
	"Nombres" TEXT,
	"Edad" INTEGER CHECK (Edad > 0),
	"Email" TEXT UNIQUE NOT NULL,
	"Password" TEXT NOT NULL,
	"Active" INTEGER DEFAULT 1
);

"""

# INsertar datos en la tabla

"""
INSERT INTO Nombre_tabla
VALUES (
    NULL,
	"Isaias Cesar Quintana Errazabal",
	23,
	"cesar@gmail.com",
	"Cesar123",
	0
);

# envias a columnas especificas y/o por lote (que no tenge NOT NULL)

INSERT INTO Nombre_tabla ("Edad", "Email", "Password")
VALUES (23, "cesar@gmail.com", "Cesar123"),
        (22, "juan@gmail.com", "Juan123");
        (25, "maria@gmail.com", "Maria123");
"""

# Leer datos de la tabla

"""
SELECT * FROM Nombre_tabla   # Leer todos los datos de la tabla
SELECT columna1, columna2 FROM tabla;  # Leer datos específicos de la tabla

SELECT * FROM Nombre_tabla WHERE columna > 18 AND active = 1;  # Filtrar datos con condiciones (AND : indica ambas de cumplen)

SELECT * FROM Nombre_tabla ORDER BY columna DESC;  # Ordenar los datos por edad de forma descendente
"""

# Actualizar datos en la tabla

"""
UPDATE Nombre_tabla
SET columna1 = valor1, columna2 = valor2, ....
WHERE condicion;
"""

# Eliminar datos en la tabla

"""
DELETE FROM tabla
WHERE condicion;
"""


# OTROS

"""
BETWEEN  : Filtrar valores entre un rango específico
IN       : Filtrar valores dentro de una lista específica
NOT      : Excluir valores que cumplan una condición
"""

