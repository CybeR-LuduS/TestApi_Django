import pymongo

# Conexión a la base de datos MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["api_db"]

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
        "carrera": "Ingeniería en Informática",
        "sede": "Antonio Varas",
        "categoria": "Chofer",
        "patenteVehiculo": "AB123CD",
        "marcaVehiculo": "Marca1",
        "modeloVehiculo": "Modelo1",
        "colorVehiculo": "Rojo",
    },
    {
        "rut": "16222222-2",
        "correo": "maria.rodriguez@duocuc.cl",
        "contrasennia": "mariarodriguez",
        "nombre": "María",
        "apellidoPaterno": "Rodríguez",
        "apellidoMaterno": "Rodríguez",
        "carrera": "Gastronomía",
        "sede": "Antonio Varas",
        "categoria": "Chofer",
        "patenteVehiculo": "XY987ZA",
        "marcaVehiculo": "Marca2",
        "modeloVehiculo": "Modelo2",
        "colorVehiculo": "Azul",
    },
    {
        "rut": "16333333-3",
        "correo": "carlos.sanchez@duocuc.cl",
        "contrasennia": "carlossanchez",
        "nombre": "Carlos",
        "apellidoPaterno": "Sánchez",
        "apellidoMaterno": "Sánchez",
        "carrera": "Administración de Redes y Telecomunicaciones",
        "sede": "Plaza Oeste",
        "categoria": "Chofer",
        "patenteVehiculo": "LM456OP",
        "marcaVehiculo": "Marca3",
        "modeloVehiculo": "Modelo3",
        "colorVehiculo": "Verde",
    },
    {
        "rut": "16444444-4",
        "correo": "laura.fernandez@duocuc.cl",
        "contrasennia": "laurafernandez",
        "nombre": "Laura",
        "apellidoPaterno": "Fernández",
        "apellidoMaterno": "Fernández",
        "carrera": "Turismo",
        "sede": "Antonio Varas",
        "categoria": "Chofer",
        "patenteVehiculo": "PQ789RS",
        "marcaVehiculo": "Marca4",
        "modeloVehiculo": "Modelo4",
        "colorVehiculo": "Amarillo",
    },
    {
        "rut": "16555555-5",
        "correo": "pedro.gomez@duocuc.cl",
        "contrasennia": "pedrogomez",
        "nombre": "Pedro",
        "apellidoPaterno": "Gómez",
        "apellidoMaterno": "Gómez",
        "carrera": "Auditoría",
        "sede": "Maipú",
        "categoria": "Pasajero",
    },
    {
        "rut": "16666666-6",
        "correo": "javiera.lopez@duocuc.cl",
        "contrasennia": "javieralopez",
        "nombre": "Javiera",
        "apellidoPaterno": "López",
        "apellidoMaterno": "López",
        "carrera": "Ingeniería en Marketing Digital",
        "sede": "Maipú",
        "categoria": "Pasajero",
    },
    {
        "rut": "16777777-7",
        "correo": "martin.torres@duocuc.cl",
        "contrasennia": "martintorres",
        "nombre": "Martín",
        "apellidoPaterno": "Torres",
        "apellidoMaterno": "Torres",
        "carrera": "Ingeniería en Gestión Logística",
        "sede": "Padre Alonso de Ovalle",
        "categoria": "Chofer",
        "patenteVehiculo": "JK321UW",
        "marcaVehiculo": "Marca5",
        "modeloVehiculo": "Modelo5",
        "colorVehiculo": "Blanco",
    },
    {
        "rut": "16888888-8",
        "correo": "carmen.ruiz@duocuc.cl",
        "contrasennia": "carmenruiz",
        "nombre": "Carmen",
        "apellidoPaterno": "Ruiz",
        "apellidoMaterno": "Ruiz",
        "carrera": "Ingeniería en Gestión Logística",
        "sede": "Padre Alonso de Ovalle",
        "categoria": "Pasajero",
    },
    {
        "rut": "16999999-9",
        "correo": "javier.garcia@duocuc.cl",
        "contrasennia": "javiergarcia",
        "nombre": "Javier",
        "apellidoPaterno": "García",
        "apellidoMaterno": "García",
        "carrera": "Ingeniería en Prevención de Riesgos",
        "sede": "San Bernardo",
        "categoria": "Pasajero",
    },
    {
        "rut": "17000000-0",
        "correo": "mart.orellana@duocuc.cl",
        "contrasennia": "martinorellana",
        "nombre": "Martín",
        "apellidoPaterno": "Orellana",
        "apellidoMaterno": "Orellana",
        "carrera": "Ingeniería en Informática",
        "sede": "Antonio Varas",
        "categoria": "Chofer",
        "patenteVehiculo": "MO123OM",
        "marcaVehiculo": "Marca6",
        "modeloVehiculo": "Modelo6",
        "colorVehiculo": "Azul",
    },
    {
        "rut": "17111111-1",
        "correo": "pabl.maldonado@duocuc.cl",
        "contrasennia": "pablomaldonado",
        "nombre": "Pablo",
        "apellidoPaterno": "Maldonado",
        "apellidoMaterno": "Maldonado",
        "carrera": "Ingeniería en Informática",
        "sede": "Antonio Varas",
        "categoria": "Pasajero",
    }
]

usuarios.insert_many(usuarios_data)


# Crear viajes 
viajes = db["core_viaje"]
viajes_data = [
    {
        "sede": "Antonio Varas",
        "rut": "16111111-1",
        "horaSalida": "22:00:00",
        "capacidadPasajeros": 4,
        "precioPorPersona": 3000,
        "estadoViaje": "Programado",
        "patenteVehiculo": "AB123CD",
        "marcaVehiculo": "Marca1",
        "modeloVehiculo": "Modelo1",
        "colorVehiculo": "Rojo",
        "correoChofer": "juan.perez@duocuc.cl"
    },
    {
        "sede": "Antonio Varas",
        "rut": "17000000-0",
        "horaSalida": "21:00:00",
        "capacidadPasajeros": 2,
        "precioPorPersona": 4000,
        "estadoViaje": "Programado",
        "patenteVehiculo": "MO123OM",
        "marcaVehiculo": "Marca6",
        "modeloVehiculo": "Modelo6",
        "colorVehiculo": "Azul",
        "correoChofer": "mart.orellana@duocuc.cl"
    }

]

viajes.insert_many(viajes_data)



# Cerrar la conexión a MongoDB
client.close()
