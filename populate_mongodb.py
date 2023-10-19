import pymongo

# Conexión a la base de datos MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["api_db"]

# Crear las categorías "Chofer" y "Pasajero"
categorias = db["core_categoria"]
categorias_data = [
    {
        "idCategoria": "1",
        "nombre": "Chofer",
        "descripcion": "Alumno inscrito como chofer en la aplicación, para atender a solicitudes de pasajeros",
    },
    {
        "idCategoria": "2",
        "nombre": "Pasajero",
        "descripcion": "Alumno inscrito como pasajero en la aplicación, para solicitar servicio de locomoción a alumno chofer",
    }
]

categorias.insert_many(categorias_data)

# Crear usuarios
usuarios = db["core_usuario"]
usuarios_data = [
    {
        "rut": "16111111-1",
        "correo": "juan.perez@duocuc.cl",
        "contrasennia": "juanperez",
        "nombre": "Juan",
        "apellidoPaterno": "Pérez",
        "apellidoMaterno": "Pérez",
        "fechaNacimiento": "01/01/1990",
        "carrera": "Ingeniería en Informática",
        "sede": "Antonio Varas",
        "idCategoria": "1",  # Asignar la categoría "Chofer"
        "categoria": "Chofer",
        "isActive": True,
        "patenteVehiculo": "AB123CD",
        "patente": "AB123CD",
    },
    {
        "rut": "16222222-2",
        "correo": "maria.rodriguez@duocuc.cl",
        "contrasennia": "mariarodriguez",        
        "nombre": "María",
        "apellidoPaterno": "Rodríguez",
        "apellidoMaterno": "Rodríguez",
        "fechaNacimiento": "02/02/1991",
        "carrera": "Gastronomía",
        "sede": "Antonio Varas",
        "idCategoria": "1",  # Asignar la categoría "Chofer"
        "categoria": "Chofer",
        "isActive": True,
        "patenteVehiculo": "XY987ZA",
        "patente": "XY987ZA",
    },
    {
        "rut": "16333333-3",
        "correo": "carlos.sanchez@duocuc.cl",
        "contrasennia": "carlossanchez", 
        "nombre": "Carlos",
        "apellidoPaterno": "Sánchez",
        "apellidoMaterno": "Sánchez",
        "fechaNacimiento": "03/03/1992",
        "carrera": "Administración de Redes y Telecomunicaciones",
        "sede": "Plaza Oeste",
        "idCategoria": "1",  # Asignar la categoría "Chofer"
        "categoria": "Chofer",
        "isActive": False,
        "patenteVehiculo": "LM456OP",
        "patente": "LM456OP",
    },
    {
        "rut": "16444444-4",
        "correo": "laura.fernandez@duocuc.cl",
        "contrasennia": "laurafernandez", 
        "nombre": "Laura",
        "apellidoPaterno": "Fernández",
        "apellidoMaterno": "Fernández",
        "fechaNacimiento": "04/04/1993",
        "carrera": "Turismo",
        "sede": "Antonio Varas",
        "idCategoria": "1",  # Asignar la categoría "Chofer"
        "categoria": "Chofer",
        "isActive": False,
        "patenteVehiculo": "PQ789RS",
        "patente": "PQ789RS",
    },
    {
        "rut": "16555555-5",
        "correo": "pedro.gomez@duocuc.cl",
        "contrasennia": "pedrogomez", 
        "nombre": "Pedro",
        "apellidoPaterno": "Gómez",
        "apellidoMaterno": "Gómez",
        "fechaNacimiento": "05/05/1994",
        "carrera": "Auditoría",
        "sede": "Maipú",
        "idCategoria": "2",  # Asignar la categoría "Pasajero"
        "categoria": "Pasajero",
    },
    {
        "rut": "16666666-6",
        "correo": "javiera.lopez@duocuc.cl",
        "contrasennia": "javieralopez", 
        "nombre": "Javiera",
        "apellidoPaterno": "López",
        "apellidoMaterno": "López",
        "fechaNacimiento": "06/06/1995",
        "carrera": "Ingeniería en Marketing Digital",
        "sede": "Maipú",
        "idCategoria": "2",  # Asignar la categoría "Pasajero"
        "categoria": "Pasajero",
    },
    {
        "rut": "16777777-7",
        "correo": "martin.torres@duocuc.cl",
        "contrasennia": "martintorres", 
        "nombre": "Martín",
        "apellidoPaterno": "Torres",
        "apellidoMaterno": "Torres",
        "fechaNacimiento": "07/07/1996",
        "carrera": "Ingeniería en Gestión Logística",
        "sede": "Padre Alonso de Ovalle",
        "idCategoria": "1",  # Asignar la categoría "Chofer"
        "categoria": "Chofer",
        "isActive": True,
        "patenteVehiculo": "JK321UW",
        "patente": "JK321UW",
    },
    {
        "rut": "16888888-8",
        "correo": "carmen.ruiz@duocuc.cl",
        "contrasennia": "carmenruiz", 
        "nombre": "Carmen",
        "apellidoPaterno": "Ruiz",
        "apellidoMaterno": "Ruiz",
        "fechaNacimiento": "08/08/1997",
        "carrera": "Ingeniería en Gestión Logística",
        "sede": "Padre Alonso de Ovalle",
        "idCategoria": "2",  # Asignar la categoría "Pasajero"
        "categoria": "Pasajero",
    },
    {
        "rut": "16999999-9",
        "correo": "javier.garcia@duocuc.cl",
        "contrasennia": "javiergarcia", 
        "nombre": "Javier",
        "apellidoPaterno": "García",
        "apellidoMaterno": "García",
        "fechaNacimiento": "09/09/1998",
        "carrera": "Ingeniería en Prevención de Riesgos",
        "sede": "San Bernardo",
        "idCategoria": "2",  # Asignar la categoría "Pasajero"
        "categoria": "Pasajero",
        "isActive": False,
    },
]

usuarios.insert_many(usuarios_data)

# Crear vehículos
vehiculos = db["core_vehiculo"]
vehiculos_data = [
    {
        "patenteVehiculo": "AB123CD",
        "marca": "Marca1",
        "modelo": "Modelo1",
        "annio": 2020,
        "color": "Rojo",
        "capacidadPasajeros": 5,
    },
    {
        "patenteVehiculo": "XY987ZA",
        "marca": "Marca2",
        "modelo": "Modelo2",
        "annio": 2021,
        "color": "Azul",
        "capacidadPasajeros": 4,
    },
    {
        "patenteVehiculo": "LM456OP",
        "marca": "Marca3",
        "modelo": "Modelo3",
        "annio": 2019,
        "color": "Verde",
        "capacidadPasajeros": 6,
    },
    {
        "patenteVehiculo": "PQ789RS",
        "marca": "Marca4",
        "modelo": "Modelo4",
        "annio": 2022,
        "color": "Amarillo",
        "capacidadPasajeros": 4,
    },
    {
        "patenteVehiculo": "JK321UW",
        "marca": "Marca5",
        "modelo": "Modelo5",
        "annio": 2018,
        "color": "Blanco",
        "capacidadPasajeros": 5,
    },
]

vehiculos.insert_many(vehiculos_data)

# Cerrar la conexión a MongoDB
client.close()
