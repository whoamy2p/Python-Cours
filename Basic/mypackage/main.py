
from my_module import MAtematica, usuario

print (MAtematica.Suma (3, 7))

def login ():
    email = input ("INgrese su email: ")

    for k in usuario.values ():
        if email in k.values ():
            print ("usuario autenticado")
            return
    
    print ("Usuario no autenticado")

login ()