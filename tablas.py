import psycopg2
from dataBase import Basedatos

class Tablas():
    def __init__(self,id, titulo, descripcion,estado):
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado


    def crearTarea(conexion, titulo, descripcion):
        try:
            with conexion.cursor() as cursor:
                consulta = "INSERT INTO tareas(titulo, descripcion, estado) VALUES (%s, %s, false);"
                cursor.execute(consulta, (titulo, descripcion))
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Ocurrió un error al crear la tarea:", e)
            return False
        
    def modificarTarea(conexion, id, titulo, descripcion):
        try:
            with conexion.cursor() as cursor:
                consulta = "UPDATE tareas SET titulo = %s, descripcion = %s WHERE id = %s;"
                cursor.execute(consulta, (titulo, descripcion, id))
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Ocurrió un error al modificar la tarea:", e)
            return False
        
    def consultarTarea(conexion, id):
        # Hacemos la consulta SQL para extraer la información de la base de datos del id ingresado
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM tareas WHERE id="+str(id))
                tarea = cursor.fetchone()
                if tarea:
                    print(tarea)
                else:
                    print("La tarea no existe")
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)

    def consultarTareaPorTitulo(conexion, titulo):
        # Hacemos la consulta SQL para extraer la información de la base de datos del titulo ingresado
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM tareas WHERE titulo='"+titulo+"'")
                tarea = cursor.fetchone()
                if tarea:
                    return tarea
                else:
                    print("La tarea no existe")
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)


    def consultarTareas(conexion):
        # Hacemos la consulta SQL para extraer la información de la base de datos
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM tareas")
                tareas = cursor.fetchall()
                if tareas:
                    return tareas
                else:
                    print("No hay tareas")
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)

    def consultarTareasRealizadas(conexion):
        # Hacemos la consulta SQL para extraer la información de la base de datos
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM tareasrealizadas")
                tareas = cursor.fetchall()
                if tareas:
                    return tareas
                else:
                    print("No hay tareas")
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)
            

    def eliminarTarea(conexion, id):
        # Hacemos la consulta SQL para eliminar el usuario 
        try:
            with conexion.cursor() as cursor:
                consulta = "DELETE FROM tareas WHERE id =" + str(id)
                cursor.execute(consulta)
                print("Tarea eliminada")
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Error eliminando: ", e)

    def eliminarPorTitulo(conexion, titulo):
        # Hacemos la consulta SQL para eliminar el usuario 
        try:
            with conexion.cursor() as cursor:
                consulta = "DELETE FROM tareas WHERE titulo ='" + titulo+"'"
                cursor.execute(consulta)
                print("Tarea eliminada")
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Error eliminando: ", e)

    def eliminarTareasRealizadas(conexion):
        # Hacemos la consulta SQL para eliminar el usuario 
        try:
            with conexion.cursor() as cursor:
                consulta = "DELETE FROM tareasRealizadas"
                cursor.execute(consulta)
                print("Tareas eliminadas")
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Error eliminando: ", e)

    def eliminarTareas(conexion):
        # Hacemos la consulta SQL para eliminar el usuario 
        try:
            with conexion.cursor() as cursor:
                consulta = "DELETE FROM tareas"
                cursor.execute(consulta)
                print("Tareas eliminadas")
            conexion.commit()
            return True
        except psycopg2.Error as e:
            print("Error eliminando: ", e)



    def actualizarEstadoTarea(conexion, id, estado):
            # Actualiza el estado de la tarea en la tabla de tareas
            try:
                with conexion.cursor() as cursor:
                    consulta = "UPDATE tareas SET estado = %s WHERE id = %s"
                    cursor.execute(consulta, (estado, id))
                    conexion.commit()
                    print("Tarea actualizada")
            except psycopg2.Error as e:
                    print("Error actualizando: ", e)
                    return False

            # Verifica si la tarea se actualizó con éxito
            if cursor.rowcount > 0:
                # Mueve la tarea de la tabla de tareas a la tabla de tareas realizadas
                try:
                    with conexion.cursor() as cursor:
                        consulta = "INSERT INTO tareasRealizadas SELECT * FROM tareas WHERE id = %s"
                        cursor.execute(consulta, (id,))
                        conexion.commit()
                        print("Tarea movida a tareasRealizadas")
                        # Elimina la tarea de la tabla original
                        consulta = "DELETE FROM tareas WHERE id = %s"
                        cursor.execute(consulta, (id,))
                        conexion.commit()
                        print("Tarea eliminada de tareas")
                except psycopg2.Error as e:
                    print("Error al mover la tarea: ", e)       
                    return False

            return True

        