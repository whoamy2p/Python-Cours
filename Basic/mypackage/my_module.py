
# MOUDLOS

class MAtematica:
    def Suma (a, b):
        return a + b
 
    def resta (a, b):
        return a - b
    
    def multiplicacion (a, b):
        return a * b
    
    def calculadora (string):
        var = eval (string)
        return var

usuario = {
    "ICEQ": {
        "name": "Isaias Cesar Quintana Errazabal",
        "email": "cesarquintanaerrazabal@gmail.com",
        "alias": ["Kriptom", "whoamy", "zeus"],
        "Student": False,
        "age": 23
    },
    "ANMO": {
        "name": "Abigail Nayely Martinez Osoario",
        "email": "abigail@gmail.com",
        "alias": ["Kriptom", "whoamy", "zeus"],
        "Student": False,
        "age": 23
    },
    "KVNB": {
        "name": "Kristhel Vivian Nolasco Borja",
        "email": "kristhel@gmail.com",
        "alias": ["Kriptom", "whoamy", "zeus"],
        "Student": False,
        "age": 23
    },
    "OJAC": {
        "name": "Oriana Jheria Armas carrera",
        "email": "oriana@gmail.com",
        "alias": ["Kriptom", "whoamy", "zeus"],
        "Student": False,
        "age": 23
    }
}


def Validar_email (email):
    if email.endswith ("@gmail.com"):
        return True