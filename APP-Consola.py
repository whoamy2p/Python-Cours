
"""
Tienda Pizeria Online

Usuario
| - Email
| - password
| - Name
├── Cliente
| - Ver_carta ()
| - Agregar_carrito ()
| - Pagar ()
└── Empleado
    | - Puesto
    | - Horario
    | - Turno
    | - Calcular salario ()
    ├── EmpleadoTiempoCompleto
    ├── EmpleadoPorHoras
    └── EmpleadoPorTurno

Producto (abstracta)
| - Nombre
| - Precio
├── Pizza
├── Bebida
└── Combo

Carrito
| - Lista_productos ()
| - Agregar_produto ()
| - Total ()
Pago
| - Pato_total
Autenticacion
| - login
| - register
| - Validar email
| - Validar password

"""
from functools import wraps
from abc import ABC, abstractmethod
import pdb

# Clase de errores


class AutenticacionError (Exception):
    def __init__(self, mensaje = "Autenticación Invalida", codigo = None):
        super().__init__(mensaje)
        self.codigo = codigo
    
    def es_crtico (self):
        error = None
        
        match self.codigo:
            case 400:   # Error 400 critico: Email invalido
                error = 400
            case 420:   # Error 420 critico: Password invalido
                error = 420
            case 430:
                error = 430
            case _:
                error = None
        
        return error

class PermisionError (AutenticacionError):
    def __init__(self, mensaje = "Permisos denegados", codigo = None):
        super().__init__(mensaje, codigo)

class ProductoError (Exception):
    def __init__(self, *args):
        self.mensaje = None
        super().__init__(*self.mensaje)
    
    def Stock (self):
        pass

class BDError (Exception):
    def __init__(self, message_bd = "Base de datos vacia", codigo = None):
        super().__init__(message_bd)
        self.codigo = codigo
    
    # Error 250 base de datos vacia
    def critico_BD (self):
        return  self.codigo if self.codigo == 250 else None

# Clase de logica del negocio ------------------------------------------------

class Autenticacion:
    def __init__(self, bd_users):
        self.Estado = None
        self.nombre_usuario = None
        self.role = None

        self.bd_users = bd_users

    # query = [dni, email, password]
    def Login (self, query):
        # pdb.set_trace ()
        if self.Validar_usuario(query[0]):
            # try:
            if self.Validar_email (query[1]) and self.Validar_password (query[2]):
                data_user = self.bd_users.Leer ()[query[0]]
                if query[1] != data_user["email"] or query[2] != data_user["password"]:
                    return None # Usuario o contraseña incorrectas
                    
                self.Estado = True
                self.nombre_usuario = data_user["name"]
                self.role = data_user["role"]

            # except AutenticacionError as a:
            #     print ("Error ", a.es_crtico (),": ", a)
        
        else:
            return False
        
        return True

    def Logout (self):
        self.Estado = None
        self.nombre_usuario = None

        return 

    # Registramos al usuario si no esta en la base de datos
    def Register (self, query):
        if not self.Validar_usuario (query[0]):
            try:
                if self.Validar_email (query[2]) and self.Validar_password (query[3]):
                    self.bd_users.Agregar (query)
                    return True
            except AutenticacionError as a:
                print ("Error ", a.es_crtico (),": ", a)    
            except BDError as b:
                print ("Error ", b.critico_BD (),": ", b)
            
        return f"Usuario {query[1]} ya esta registrado"
    
    # Valida si el usuario esta en la base de datos
    def Validar_usuario (self, dni):
        if dni in self.bd_users.Leer ().keys ():
            return True
        
        return False

    @staticmethod  # decordar que permite crear una funcion independiente de la clase
    def require_admin (func):
        @wraps (func)
        def wrappers (self, *args, **kwargs):
            if self.auth.role != "Admin" or self.auth.role is None:
                raise PermisionError ("No tiene permisos de Admin", 100) 
                
            return func (self, *args, **kwargs)
        return wrappers
    
    # Requiere login para ciertas cosas a nivel de cliente
    @staticmethod
    def require_login (func):
        @wraps (func)
        def wrappers (self, *args, **kwargs):
            if self.auth.Estado is None:
                raise PermisionError ("No ha iniciado session", 110)
            
            return func (self, *args, **kwargs)
        return wrappers


    def Validar_password (self, password):
        especiales = "!#$%&/()=?¡¿*+-[]{}-_"

        if len (password) < 8:
            raise AutenticacionError ("La contraseña debe tener al menos 8 caracteres", 420)
        
        if not any (c in password for c in especiales):
            raise AutenticacionError ("La contraseña debe contener un carácter especial", 422)
        
        if password.isspace ():
            raise AutenticacionError ("La contraseña no puede contener espacios")

        return True

        
    #  controlar este error de validacion de email
    def Validar_email (self, email):
        dominios = ["@gmail.com", "@hotmail.com", "@microsoft.com", "@yahoo.com", "@outlook.com"]
        if not any (email.endswith (domain) for domain in dominios):
            raise AutenticacionError (f"Usuario {email} Invalido", 400)
        
        return True
           

class BaseDato (ABC):
    def __init__(self):
        self._db = {
            "74296543":{
                "name": "Isaias Cesar Quintana Errazabal",
                "email": "cesar@gmail.com",
                "password": "Cesar&2001",
                "role": "Admin"
            }
        }

        self._dbProductos = {
            "Pizza Peperoni": {
                "precio": 22.50,
                "stock": 10,
                "categoria": "Alimento"
            }
        }
    
    # query = [dni, name, email, password]
    @abstractmethod
    def Agregar (self, query):
        pass
    
    @abstractmethod
    def Leer (self):
        pass
    
    @abstractmethod
    def Actualizar (self):
        pass

    @abstractmethod
    def Eliminar (self):
        pass

class BD_Usuarios (BaseDato):
    def __init__(self):
        super().__init__()
    
    # query = [dni, name, email, password, role]
    def Agregar (self, query):
        dni, name, email, password, role = query        
        self._db[dni] = {"name": name, "email": email, "password":password, "role": role}
        return name

    def Leer (self):
        return self._db

    def Actualizar (self, query):
        if self._db:
            raise BDError ("Base de Datos vacia", 250)
        
        if Autenticacion.Validar_usuario (query[0]):
            self._db[query[0]].update ({
                "name" : query [1],
                "password" : query[3],
            })

            return (query[0], query[1], query[3])


    def Eliminar (self, key):
        del self._db[key]

        return self._db[key]["name"]

class BD_productos (BaseDato):
    def __init__(self, auth):
        super().__init__()
        self.auth = auth

    # query = [producto, precio, stock, cateogoria]
    @Autenticacion.require_admin
    def Agregar (self, query):
        self._dbProductos[query[0]] = {
            "precio": query[1],
            "stok": query[2],
            "categoria": query[3]
        }

        return query[0]
        
    @Autenticacion.require_admin
    def Leer (self):
        return self._dbProductos

    @Autenticacion.require_admin
    def Actualizar (self, query):
        if not self._dbProductos:
            raise BDError ("Base de datos Vacia", 250)
        
        if self.validar_producto (query[0]):
            self._dbProductos[query[0]].update ({
                "precio": query[1], 
                "stock": query[2]
            })

            return query[0]

    @Autenticacion.require_admin
    def Eliminar (self, key):
        if self.validar_producto (key):
            del self._dbProductos[key]
            return key

        return False

    def validar_producto (self, producto):
        if producto in self._dbProductos.keys ():
            return True
        
        return False
    
class AdminController:
    def __init__(self, bd_usuarios, auth):
        self.bd_usuarios = bd_usuarios
        self.auth = auth

    @Autenticacion.require_admin
    def Agregar (self, query):
        if self.auth.Validar_email (query[2]) and self.auth.Validar_password (query[3]):
            return self.bd_usuarios.Agregar (query)

    @Autenticacion.require_admin
    def Actualizar (self, query):
        if self.auth.Validar_email (query[1]) and self.auth.Validar_password (query[2]):
            return self.bd_usuarios.Actualizar (query)


    @Autenticacion.require_admin
    def Eliminar (self, key):
        return self.bd_usuarios.Eliminar (key)

class Usuario:
    def __init__(self, auth):
        self.nombre = auth.nombre_usuario
        self.estado = auth.Estado

class Cliente (Usuario):
    def __init__ (self, auth ,bd_productos, pago):
        super ().__init__ (auth)
        self._bd_productos = bd_productos._dbProductos
        self.auth = auth
        self.pago = pago
    
    def Ver_carta (self):
        return ((p, self._bd_productos[p]["precio"], self._bd_productos[p]["categoria"]) for p in self._bd_productos)
            
    
    @Autenticacion.require_login
    def Agregar_carrito (self, producto):
        data = self.pago.carrito.Agregar_producto (producto, self._bd_productos[producto].get ("precio", 0))
        return data
    
    @Autenticacion.require_login
    def Pagar (self):
        return self.pago.Pago_Total ()


class Empleado (Usuario):
    def __init__(self, auth):
        super().__init__(auth)
    
    @Autenticacion.require_admin
    def Calcular_salario (self):
        pass

class EmpleadoTC (Empleado):
    def __init__(self, auth, bd_usuarios):
        super().__init__(auth)
        self.auth = auth
        self._bd_usuarios = bd_usuarios._db
        self.sueldos = [("Cocinero", 116.66), ("Meseros", 83.33), ("Contador", 150)]
    
    @Autenticacion.require_admin
    def Calcular_salario_individual (self, dni, dias = 30):
        if self.auth.Validar_usuario (dni):
            nombre, role = [self._bd_usuarios[dni][data] for data in self._bd_usuarios[dni] if data in ["name", "role"]]

            dinero = list (map(lambda x: round (x[1] * dias), filter (lambda x: x[0] == role, self.sueldos)))[0]

            return (nombre, role, dinero)

        return False # si el usuario no esta en la base de datos
    
    @Autenticacion.require_admin
    def Calcular_salario_grupal (self):
        pagos_empleados = []
        for key, value in self._bd_usuarios.items ():
            if value["role"] in ["Cocinero", "Meseros", "Contador"]:
                dinero = list (map(lambda x: round (x[1] * 30), filter (lambda x: x[0] == value["role"], self.sueldos)))[0]

                pagos_empleados.append ((value["name"], dinero))

        return pagos_empleados


class EmpleadoPH (Empleado):
    def __init__(self, auth, bd_usuarios):
        super().__init__(auth)
        self.auth = auth
        self._bd_usuarios = bd_usuarios._db
        self.sueldos = [("Cocinero", 116.66), ("Meseros", 83.33), ("Contador", 150)]
    
    @Autenticacion.require_admin
    def Calcular_salario_individual (self, dni, dias = 3, horas = 3):
        if self.auth.Validar_usuario (dni):
            nombre, role = [self._bd_usuarios[dni][data] for data in self._bd_usuarios[dni] if data in ["name", "role"]]

            dinero = list (map(lambda x: round (x[1] * round((dias * horas) / 24)), filter (lambda x: x[0] == role, self.sueldos)))[0]

            return (nombre, role, dinero)

        return False # si el usuario no esta en la base de datos
    

class Producto:
    def __init__(self, bd_productos):
        self._bd_producto = bd_productos

    def Agregar_producto (self, query): # query = [producto, precio, stock, categoria]
        return self._bd_producto.Agregar (query)
    
    def Eliminar_producto (self, key):
        return self._bd_producto.Eliminar (key)

    def Editar_producto (self, query):
        return self._bd_producto.Actualizar (query)

class carrito:
    def __init__(self):
        self.car = {}

    @staticmethod
    def contador ():
        cantidad = 0
        while True:
            recibido = yield cantidad

            cantidad += recibido

    def Agregar_producto (self, producto, precio):
        cuenta = self.contador ()
        next (cuenta)
        if not self.existe_producto (producto):
            self.car[producto] = {"total_p": precio}
        
        self.car[producto].update ({"total_p":precio * cuenta.send (1)})
        return producto
        

    def Total (self):
        total = 0
        for value in self.car.values ():
            total += value["total_p"]
        
        self.car["Total"] = total
        return self.car
    
    def existe_producto (self, producto):
        if producto in self.car.keys ():
            return True
        
        return False

class Pago:
    def __init__(self, carrito):
        self.carrito = carrito

    def Pago_Total (self):
        data = self.carrito.Total ()
        return data["Total"]


# role = [Admin, User, Cocinero, Contador, Mesero]

#  GUI -----------------GUI

def input_user (q = None):
    if q in ["Register", "Agregar"]: 
        try:
            dni = input ("N° DNI: ")
            name = input ("Nombre de Usuario: ").title ()
            email = input ("Email: ").lower ()
            password = input ("Password: ")
            role = input ("Rol: ")
        except ValueError as e:
            print (e, "Datos no permitidos")
        
        return [dni, name, email, password, role]
    
    if q in ["Actualizar", "Login"]:
        try:
            dni = input ("N° DNI: ")
            email = input ("Email: ").lower ()
            password = input ("Password: ")
        except ValueError as e:
            print (e, "Datos no permitidos")
            
        return  [dni, email, password]
    
    # Eliminar
    dni = input ("N° DNI: ")
    return dni

def input_productos (q = None):
    if q == "Agregar":
        try:
            producto = input ("Producto: ").title ()
            precio = float(input ("Precio: "))
            stock = int(input ("Stock: "))
            categoria = input ("Categoria [Alimento, Bebdida]: ")
        except ValueError as e:
            print (e, "Datos no permitidos")
        
        return [producto, precio, stock, categoria]
    
    producto = input ("Producto: ").title ()
    return producto


def Controller_opciones ():
    controller = True
    while controller:
        try:
            opcion = int (input ("Seleccione una opción 0 salir: "))
            if opcion == 0:
                break
        except ValueError as e:
            print (e, "No se permite Letras")
            continue
        else: 
            controller = False
    
    return opcion

def GUI_Autenticacion (auth):
    print ("""
        AUTENTICACION DE USUARIO
    """)

    while True:
        print ("""\n
            1. Iniciar session
            2. Registrarse
            3. Cerrar session
            4. Salir\n
        """)

        # query = [dni, name, email, password, role]
        opcion = Controller_opciones ()
        
        match opcion:
            case 1:
                query = input_user (q = "Login")
                try:
                    if auth.Login (query):
                        print ("Inicio de session exitoso .....!")
                except AutenticacionError as a:
                    print ("Error ", a.es_crtico (),": ", a)
                    continue
            case 2:
                query = input_user (q = "Register")
                if auth.Register (query):
                    print ("Registro de usuario existoso")
            case 3:
                auth.Logout ()
                print ("Cerrando session")
            case 4:
                break
            case _:
                print ("\nOpcion no disponible, Intentelo nuevamente\n")


def GUI_Cliente (auth, bd_productos, pago):
    # pdb.set_trace ()
    cliente = Cliente (auth, bd_productos, pago)

    print ("""\n
        PIZERIA IQGEOSPATIAL TECHNOLOGY
    \n""")

    while True:
        print ("""\n
            1. Ver carta
            2. Agregar carrito
            3. Pagar
            4. Salir\n
        """)

        opcion = Controller_opciones ()
        match opcion:
            case 1:
                # producto, precio, categoria
                print ("Producto\t precio\t categoria")
                for d in cliente.Ver_carta ():
                    for k in d:
                        print (k, end="\t\t")
            case 2:
                while True:
                    producto = input ("Nombre del Producto a consumir (S: Termina): ").title ()
                    if producto == "S":
                        break
                    
                    try:
                        cliente.Agregar_carrito (producto)
                    except AutenticacionError as a:
                        print (f"Error {a.codigo}: ", a)
                        continue
            case 3:
                try:
                    cliente.Pagar ()
                except AutenticacionError as a:
                    print (f"Error {a.codigo}: ", a)
                    continue
            case 4:
                break
            case _:
                print ("\nOpcion no disponible, Intentelo nuevamente\n")

class Amdin:
    def __init__(self, producto, empleadoTC, empleadoPH, admincontroller):
        self.producto = producto
        self.empleadoTC = empleadoTC
        self.empleadoPH = empleadoPH
        self.admincontroller = admincontroller

        self.GUI_Admin ()


    def GUI_Admin (self):
        print ("""\n
            GESTOR DE ADMINISTRADOR
        \n""")

        while True:
            print ("""\n
                1. Gestionar Productos
                2. Gestionar Usuarios (clientes / empleados)
                3. Calculo de salario Empleados
                4. Salir\n
            """)

            opcion = Controller_opciones ()
            match opcion:
                case 1:
                    try:
                        self.Gestion_producto ()
                    except PermisionError as p:
                        print (f"Error {p.codigo}: ", p)
                        continue
                case 2:
                    try:
                        self.Gestion_usuario ()
                    except AutenticacionError as a:
                        print (f"Error {a.codigo}: ", a)
                        continue
                case 3:
                    try:
                        self.Gestion_salario ()
                    except PermisionError as p:
                        print (f"Error {p.codigo}: ", p)
                        continue
                case 4:
                    break
                case _:
                    print ("\nOpcion no disponible, Intentelo nuevamente\n")
    
    def Gestion_producto (self):
        print ("""\n
            GESTiION DE PRODUCTOS
        \n""")  

        while True:
            print ("""\n
                1. Agregar prodcuto
                2. Actualizar producto
                3. Eliminar producto
                4. Salir\n
            """)

            opcion = Controller_opciones ()  
            match opcion:
                case 1:  # query = [producto, precio, stock, categoria]
                    query = input_productos (q="Agregar")
                    data = self.producto.Agregar_producto (query)
                    print (f"\nProducto {data} Agregado\n")

                case 2:
                    query = input_productos (q="Agregar")
                    data = self.producto.Editar_producto (query)
                    print (f"\nProducto {data} Actualizado\n") 
                case 3:
                    key = input_productos ()
                    data = self.producto.Eliminar_producto (key)
                    print (f"\nProducto {data} Eliminado\n") 
                case 4:
                    break
                case _:
                    print ("\nOpcion no disponible, Intentelo nuevamente\n")


    def Gestion_usuario (self):
        print ("""\n
            GESTION DE USUARIOS
        \n""")

        while True:
            print ("""\n
                1. Agregar Usuario
                2. Actualizar usuario
                3. Eliminar usuario
                4. Salir\n
            """)

            opcion = Controller_opciones ()
            match opcion:
                case 1:
                    print ("Rol:  ['Cocinero', 'Meseros', 'Contador']")
                    query = input_user (q = "Agregar")
                    usr = self.admincontroller.Agregar (query) 
                    print (f"\nUsuario {usr} Agregado con exito .. !\n")
                case 2:
                    print ("Rol:  ['Cocinero', 'Meseros', 'Contador']")
                    query = input_user (q = "Actualizar")
                    try:
                        usr = self.admincontroller.Actualizar (query) 
                    except BDError as b:
                        print (f"Error {b.codigo}: ", b)
                    print (f"\nUsuario {usr[0]} Actualizado con exito .. !")
                    print (f"""
                        nuevo nombre: {usr[1]}
                        password: {usr[2]}
                    \n""")
                case 3:
                    key = input_user ()
                    usr = self.admincontroller.Eliminar (key)
                    print (f"\nUsuario {usr} Eliminado con exito .. !\n")
                case 4:
                    break
                case _:
                    print ("\nOpcion no disponible, Intentelo nuevamente\n") 

    
    def Gestion_salario (self):
        print ("""\n
            GESTION DE SALARIOS
        \n""")

        while True:
            print ("""\n
                1. Salario por Tiempo completo individual
                2. Salario por Teimpo completo grupo
                3. Salario por Horas Inidividual
                4. Salir\n
            """)

            opcion = Controller_opciones ()
            match opcion:
                case 1:
                    dni = input_user ()
                    s = self.empleadoTC.Calcular_salario_individual (dni)
                    # nombre, rol y dinero
                    print (f"""\n
                        Sr. {s[0]}
                        Area: {s[1]}
                        Sueldo: S/. {s[2]}
                    \n""")
                case 2:
                    s = self.empleadoTC.Calcular_salario_grupal ()
                    print ("\nLISTA DE EMPLEADOS Y SUELDOS")
                    for (name, sueldo) in s:
                        print (f"- {name}    S/.{sueldo}")

                case 3:
                    dni = input_user ()
                    dias = int (input ("N de dias trabajados: "))
                    horas = float (input ("N Horas trabajadas: "))
                    s = self.empleadoPH.Calcular_salario_individual (dni, dias, horas)
                    print (f"""\n
                        Sr. {s[0]}
                        Area: {s[1]}
                        Sueldo: S/. {s[2]}
                    \n""")
                case 4:
                    break
                case _:
                    print ("\nOpcion no disponible, Intentelo nuevamente\n")

        

def main ():
    bd_usuario = BD_Usuarios ()
    auth = Autenticacion (bd_usuario)
    bd_productos = BD_productos (auth)

    print ("\nPIZZERIA IQGEOSAPTIAL TECHNOLOGY\n")

    while True:
        print ("""
            1. Autenticación
            2. GUI de Usuario
            3. GUI de Administrador
            4. Salir
        """)
        opcion = Controller_opciones ()
        match opcion:
            case 1:
                GUI_Autenticacion (auth)
            case 2:
                carro = carrito ()
                pago = Pago (carro)
                GUI_Cliente (auth, bd_productos, pago)
            case 3:
                producto = Producto (bd_productos)
                empleadoTC = EmpleadoTC (auth, bd_usuario)
                empleadoPH = EmpleadoPH (auth, bd_usuario)
                admincontroller = AdminController (bd_usuario, auth)

                admin = Amdin (producto, empleadoTC, empleadoPH, admincontroller)
                admin
            case 4:
                break
            case _:
                print ("\nOpcion no disponible, Intentelo nuevamente\n")


if __name__ == "__main__":
    main ()
