
var = {
    123456: {
        "name": "Isaias", 
        "email": "cesar@gmail.com",
        "password":"1234", 
        "role": "admin"
    }
}

print ([var[123456][data] for data in var[123456] if data in ["name", "role"]])

def es_crtico (codigo):
    error = None
        
    match codigo:
        case 400:   # Error 400 critico: Email invalido
            error = 400
        case 420:   # Error 420 critico: Password invalido
            error = 420
        case _:
            error = None
        
    return error

# print (es_crtico (4200))

def Validar_password (password):
    especiales = "!#$%&/()=?¡¿*+-[]{}-_"

    if len (password) < 8:
        return "La contraseña debe tener al menos 8 caracteres"
        
    if not any (c in password for c in especiales):
        return "La contraseña debe tener un carácter especial"
        
    if password.isspace ():
        return "La contraseña no puede contener espacios"

    return True

# print (Validar_password ("cesar2001"))



dic = {
    "ceviche":{
        "total":20
    }
}

# print (dic["ceviche"]["total"])

sueldos = [("Cocinero", 116.66), ("Meseros", 83.33), ("Contador", 150)]

# sueldos = [("Cocinero", 3500),("Meseros", 2500),("Contador", 4500)
# ]

role = "Cocinero"
dias = 30

var = map (lambda x: round (x[1] * dias), filter (lambda x: x[0] == role, sueldos))
d = list (var)[0]
print (d)

suel = 0
for k, v in sueldos:
    if role in k:
        suel = v

print (suel)
