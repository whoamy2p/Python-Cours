
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ruta_txt = BASE_DIR / "Intermediate" / "my_file.txt"


def Leer ():
    with open (ruta_txt, "r", encoding="utf-8") as file:
        line = file.readlines ()
        mayor = 0
        for k in range (len (line)):
            new = len(line[k].replace ("\t\t", " ").split (" ")[0])
            if mayor < new:
                mayor = new

        file.seek (0)

        print ("-"*21)
        print ("  Alumno \tNotas")
        print ("-"*21)

        for lines in file:
            text = lines.replace ("\t\t", " ").strip ('\n').split (" ")
            cantidad = len (text[0])
            if cantidad <= mayor:
                print (" "*(mayor-cantidad) + text[0] + '\t' + str (text[1]))
        
        print ("-"*21)
    

def Escribir (cantidad):
    with open (ruta_txt, "w", encoding="utf-8") as file:
        for _ in range (cantidad):
            nombre = input ("nombre~: ")
            nota = float (input ("Nota~: "))
            file.write (nombre + '\t\t' + str(nota) +'\n')

def Actualizar (alumno):
    with open (ruta_txt, "r", encoding="utf-8") as file:
        lineas = file.readlines ()

    with open (ruta_txt, "w", encoding="utf-8") as file:
        for linea in lineas:
            if alumno in linea:
                nota = float (input ("nueva nota: "))
                file.write (alumno + '\t\t' + str(nota) + '\n')
                continue
            
            file.write (linea)


def Eliminar(alumno):
    with open(ruta_txt, "r", encoding="utf-8") as file:
        lineas = file.readlines()

    with open(ruta_txt, "w", encoding="utf-8") as file:
        for linea in lineas:
            print (linea)
            if alumno not in linea.lower():
                file.write(linea)

        
def main ():
    print ("""SISTEMA CRUD DE NOTAS""")

    while True:
        print ("""
            1. Rellenar datos
            2. Leer datos
            3. Actualizar datos
            4. Eliminar datos
            5. Salir
        """)

        opcion = int (input ("opcion: "))
        match opcion:
            case 1:
                cantidad = int (input ("Cantidad de alumnos: "))
                Escribir (cantidad)
            case 2:
                Leer ()
            case 3:
                alumno = input ("Nombre de alumno: ")
                Actualizar (alumno)
            case 4:
                alumno = input ("Nombre de alumno: ")
                Eliminar (alumno)
            case 5:
                break
            case _:
                print ("Opcion no disponible")

if __name__ == "__main__":
    main ()