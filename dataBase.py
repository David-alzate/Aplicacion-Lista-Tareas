import psycopg2

# Clase de la base de datos para realizar su conexión
class Basedatos:
    def __init__(self,url,user,password,):
        self.url = url
        self.user = user
        self.password = password
        
# Método para conectar a la base de datos
    def conectar(self):
        try:        
             credenciales  ={
                  "dbname": "lsTareas",
                  "user": self.user,
                  "password": self.password,
                  "host": self.url,
                  "port": 5432
                  }
             conexion = psycopg2.connect(**credenciales)
             if conexion:
                  return conexion
        except psycopg2.error as e:
            print("Ocurrio un error al conectar", e )

    

