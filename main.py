import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QPushButton 
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import QtCore, QtWidgets
import os


from dataBase import *
from tablas import *


conexion = Basedatos("localhost","postgres","000")
script_dir = os.path.dirname(os.path.realpath(__file__))

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(script_dir, 'interfaz.ui'), self)

        # Cargar datos en tablas
        self.cargarDatosEnTabla()
       


        #Control de barra de titulos
        self.btnNormalizar.hide()
        self.btnCerrar.clicked.connect(lambda: self.close())
        self.btnMaximizar.clicked.connect(self.crontrolBtMaximizar)
        self.btnNormalizar.clicked.connect(self.crontrolBtNormalizar)
        self.btnMinimizar.clicked.connect(self.crontrolBtMinimizar)


        # Eliminar Barra de titulo y opacidad
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        #Redimensionar ventana
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)
        # Mover Ventana 
        self.frameSuperior.mouseMoveEvent = self.moverVentana


        # coneccion botones
        self.btnTareas.clicked.connect(lambda: self.paginaTareas())
        self.btnNuevaTarea.clicked.connect(lambda: self.paginaNuevaTarea())
        self.btnActualizarTarea.clicked.connect(lambda: self.paginaActualizar())
        self.btnEliminarTarea.clicked.connect(lambda: self.paginaEliminarTarea())
        self.btnTareasCompletadas.clicked.connect(lambda: self.paginaTareasCompletadas())
        self.btnAjustes.clicked.connect(lambda: self.paginaAjustes())
        self.btnMenu.clicked.connect(self.moverMenu)
        self.btnActualizar.clicked.connect(self.cargarDatosEnTabla)
        self.agregar.clicked.connect(self.agregarTarea)
        self.btnBuscarActualizar.clicked.connect(self.buscarTareaPorTitulo)
        self.btnActualizarEliminar.clicked.connect(self.cargarDatosEnTablaEliminar)
        self.btnActualizarTarea_2.clicked.connect(self.actualizarTarea)
        self.btnEliminarTarea_2.clicked.connect(self.eliminarTareaPorTitulo)
        self.btnEliminarTareaId.clicked.connect(self.eliminarTareaPorId)
        self.eliminarRegistroTareas.clicked.connect(self.eliminarTareas)
        self.eliminarRegistroTareasCompleetadas.clicked.connect(self.eliminarTareasRealizadas)
      

        # Ancho Tablas
        self.tablaTareas.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        # Redimensionar la columna ID para ajustarse al tamaño del número
        self.tablaTareas.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        # Redimensionar la columna de título para llenar el espacio restante
        self.tablaTareas.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.tablaTareas.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        # Ancho Tablas Eliminar
        self.tablaEliminar.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        # Redimensionar la columna ID para ajustarse al tamaño del número
        self.tablaEliminar.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        # Redimensionar la columna de título para llenar el espacio restante
        self.tablaEliminar.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.tablaEliminar.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        #anchos tablas tareas completadas
        self.tablaTareasCompletadas.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        # Redimensionar la columna ID para ajustarse al tamaño del número
        self.tablaTareasCompletadas.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        # Redimensionar la columna de título para llenar el espacio restante
        self.tablaTareasCompletadas.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.tablaTareasCompletadas.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

   
   # Funciones para cambiar de paginas 
    def paginaTareas(self):
        self.stackedWidget.setCurrentWidget(self.pageTareas)
        self.cargarDatosEnTabla()
    
    def paginaNuevaTarea(self):
        self.stackedWidget.setCurrentWidget(self.pageNuevaTarea)
        self.mostrarMensajeAgregar.setText("")

    def paginaActualizar(self):
        self.stackedWidget.setCurrentWidget(self.pageActualizar)
        self.labelConfirmacionActualizar.setText("")
        self.txtBuscarTareaActualizar.setText("")
        self.txtIdActualizar.setText("")
        self.txtTituloActualizar.setText("")
        self.txtDescripcionActualizar.setText("")
      
    def paginaEliminarTarea(self):
        self.stackedWidget.setCurrentWidget(self.pageEliminar)
        self.labelConfirmacionEliminar.setText("")
        self.txtBuscarTareaEliminar.setText("")
        self.txtIdTareaEliminar.setText("")
        self.cargarDatosEnTablaEliminar()

    def paginaTareasCompletadas(self):
         self.stackedWidget.setCurrentWidget(self.pageTareasCompletadas)
         self.cargarDatosEntablaTareasCompletadas()

    def paginaAjustes(self):
         self.stackedWidget.setCurrentWidget(self.pageAjustes)
         self.labelInfoAjustes.setText("")


    def moverMenu(self):
        if True:
            width = self.frameBarra.width()
            normal = 0
            if width == 0:
                extender = 200
            else:
                extender = normal
            self.animacion = QPropertyAnimation(self.frameBarra, b"minimumWidth")
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()

    def cargarDatosEnTabla(self):
         # Obtener los datos de la base de datos
         conexion_db = conexion.conectar()
         tareas = Tablas.consultarTareas(conexion_db)
         conexion_db.close()

         # Ocultar la cabecera vertical que muestra los números de fila
         self.tablaTareas.verticalHeader().setVisible(False)

         # Limpiar la tabla
         self.tablaTareas.setRowCount(0)

         # Verificar si hay tareas antes de recorrerlas
         if tareas:
            # Recorrer los datos de la consulta
            for tarea in tareas:
                  # Insertar una fila en la tabla
                  rowPosition = self.tablaTareas.rowCount()
                  self.tablaTareas.insertRow(rowPosition)

                  # Crear un botón
                  confirm_button = QPushButton()
                  # Establecer el fondo en blanco
                  confirm_button.setStyleSheet("background-color: white;")
                  
                  # Agregar un icono al botón
                  icon = QIcon("C:/Users/alzat/Documents/Lista De Tareas/iconos/confirmacion.png")  # Reemplaza con la ruta de tu icono
                  confirm_button.setIcon(icon)
                  self.tablaTareas.setCellWidget(rowPosition, 3, confirm_button)

                  # Conectar el evento "clicked" del botón a la función confirmarTarea
                  confirm_button.clicked.connect(lambda checked, tarea_id=tarea[0]: self.confirmarTarea(tarea_id))

                  # poner los títulos de las columnas (esto debería estar fuera del bucle)
                  self.tablaTareas.setHorizontalHeaderLabels(["ID", "Título", "Descripción", "Confirmar"])

                  # Insertar los datos en las celdas  
                  self.tablaTareas.setItem(rowPosition, 0, QTableWidgetItem(str(tarea[0])))
                  self.tablaTareas.setItem(rowPosition, 1, QTableWidgetItem(tarea[1]))
                  self.tablaTareas.setItem(rowPosition, 2, QTableWidgetItem(tarea[2]))
         else:
            # Si no hay tareas, puedes mostrar un mensaje o tomar la acción adecuada
            self.labelInfoTareas.setText("No hay tareas disponibles en la base de datos")

    def confirmarTarea(self, tarea_id):
       # Realiza la actualización en la base de datos, por ejemplo:
       conexion_db = conexion.conectar()
       Tablas.actualizarEstadoTarea(conexion_db, tarea_id, True)
       
       # Elimina la fila correspondiente en la tabla
       Tablas.eliminarTarea(conexion_db, tarea_id)
       self.cargarDatosEnTabla()
       conexion_db.close()

         
    def cargarDatosEnTablaEliminar(self):
      # Obtener los datos de la base de datos
      conexion_db = conexion.conectar()
      tareas = Tablas.consultarTareas(conexion_db)
      conexion_db.close()

      # Ocultar la cabecera vertical que muestra los números de fila
      self.tablaEliminar.verticalHeader().setVisible(False)

      # Limpiar la tabla
      self.tablaEliminar.setRowCount(0)

      # Verificar si hay tareas antes de recorrerlas
      if tareas:
         # Recorrer los datos de la consulta
         for tarea in tareas:
               # Insertar una fila en la tabla
               rowPosition = self.tablaEliminar.rowCount()
               self.tablaEliminar.insertRow(rowPosition)

               # poner los títulos de las columnas (esto debería estar fuera del bucle)
               self.tablaEliminar.setHorizontalHeaderLabels(["ID", "Título", "Descripción"])

               # Insertar los datos en la fila
               self.tablaEliminar.setItem(rowPosition, 0, QTableWidgetItem(str(tarea[0])))
               self.tablaEliminar.setItem(rowPosition, 1, QTableWidgetItem(tarea[1]))
               self.tablaEliminar.setItem(rowPosition, 2, QTableWidgetItem(tarea[2]))
      else:
         # Si no hay tareas, puedes mostrar un mensaje o tomar la acción adecuada
          self.labelConfirmacionEliminar.setText("No hay tareas disponibles en la base de datos")
         
    def cargarDatosEntablaTareasCompletadas(self):
        # Obtener los datos de la base de datos
      conexion_db = conexion.conectar()
      tareas = Tablas.consultarTareasRealizadas(conexion_db)
      conexion_db.close()

      # Ocultar la cabecera vertical que muestra los números de fila
      self.tablaTareasCompletadas.verticalHeader().setVisible(False)

      # Limpiar la tabla
      self.tablaTareasCompletadas.setRowCount(0)

      # Verificar si hay tareas antes de recorrerlas
      if tareas:
         # Recorrer los datos de la consulta
         for tarea in tareas:
               # Insertar una fila en la tabla
               rowPosition = self.tablaTareasCompletadas.rowCount()
               self.tablaTareasCompletadas.insertRow(rowPosition)

               # poner los títulos de las columnas (esto debería estar fuera del bucle)
               self.tablaTareasCompletadas.setHorizontalHeaderLabels(["ID", "Título", "Descripción"])

               # Insertar los datos en la fila
               self.tablaTareasCompletadas.setItem(rowPosition, 0, QTableWidgetItem(str(tarea[0])))
               self.tablaTareasCompletadas.setItem(rowPosition, 1, QTableWidgetItem(tarea[1]))
               self.tablaTareasCompletadas.setItem(rowPosition, 2, QTableWidgetItem(tarea[2]))
      else:
         # Si no hay tareas, puedes mostrar un mensaje o tomar la acción adecuada
          self.txtInfoTareasCompletadas.setText("No hay tareas completadas en la base de datos")
        

    def agregarTarea(self):
            # Obtener los datos de los LineEdit
            titulo = self.txtTitulo.text()
            descripcion = self.txtDescripcion.text()

            # Crear la tarea
            conexion_db = conexion.conectar()
            Tablas.crearTarea(conexion_db, titulo, descripcion)
            conexion_db.close()

            # Limpiar los LineEdit
            self.txtTitulo.setText("")
            self.txtDescripcion.setText("")

            # Mostrar mensaje de éxito
            self.mostrarMensajeAgregar.setText("Tarea creada exitosamente")

    def buscarTareaPorTitulo(self):
     # Obtener el título de la tarea
     titulo = self.txtBuscarTareaActualizar.text()

     # Buscar la tarea
     conexion_db = conexion.conectar()
     tarea = Tablas.consultarTareaPorTitulo(conexion_db, titulo)
     conexion_db.close()
     print(tarea)
     if tarea:
         self.labelConfirmacionActualizar.setText("Tarea encontrada")
         self.txtTituloActualizar.setText(tarea[1])
         self.txtDescripcionActualizar.setText(tarea[2])
         self.txtIdActualizar.setText(str(tarea[0]))
     else:
         self.labelConfirmacionActualizar.setText("Tarea no encontrada")

    def actualizarTarea(self):
       # Obtener los datos de los LineEdit
       id = self.txtIdActualizar.text()
       titulo = self.txtTituloActualizar.text()
       descripcion = self.txtDescripcionActualizar.text()
   
       # Actualizar la tarea
       conexion_db = conexion.conectar()
       Tablas.modificarTarea(conexion_db, id, titulo, descripcion)
       conexion_db.close()
   
       # Limpiar los LineEdit
       self.txtIdActualizar.setText("")
       self.txtTituloActualizar.setText("")
       self.txtDescripcionActualizar.setText("")
   
       # Mostrar mensaje de éxito
       self.labelConfirmacionActualizar.setText("Tarea actualizada exitosamente")
      
    def eliminarTareaPorTitulo(self):
       # Obtener el título de la tarea
       titulo = self.txtBuscarTareaEliminar.text()
   
       # Buscar la tarea
       conexion_db = conexion.conectar()
       tarea = Tablas.eliminarPorTitulo(conexion_db, titulo)
       conexion_db.close()
       if tarea:
          self.labelConfirmacionEliminar.setText("Tarea eliminada exitosamente")
          self.cargarDatosEnTablaEliminar()
       else:
          self.labelConfirmacionEliminar.setText("Tarea no encontrada")
         
    def eliminarTareaPorId(self):
        # Obtener el título de la tarea
       id = self.txtIdTareaEliminar.text()
   
       # Buscar la tarea
       conexion_db = conexion.conectar()
       tarea = Tablas.eliminarTarea(conexion_db, id)
       conexion_db.close()
       if tarea:
          self.labelConfirmacionEliminar.setText("Tarea eliminada exitosamente")
          self.cargarDatosEnTablaEliminar()
       else:
          self.labelConfirmacionEliminar.setText("Tarea no encontrada")
       
    def eliminarTareas(self):
         # Buscar la tarea
         conexion_db = conexion.conectar()
         tarea = Tablas.eliminarTareas(conexion_db)
         conexion_db.close()
         if tarea:
            self.labelInfoAjustes.setText("Tareas eliminadas exitosamente")
         else:
            self.labelInfoAjustes.setText("No hay tareas para eliminar")

    def eliminarTareasRealizadas(self):
         # Buscar la tarea
         conexion_db = conexion.conectar()
         tarea = Tablas.eliminarTareasRealizadas(conexion_db)
         conexion_db.close()
         if tarea:
            self.labelInfoAjustes.setText("Tareas Completadas eliminadas exitosamente")
         else:
            self.labelInfoAjustes.setText("No hay tareas para eliminar")
        
      
    # Control de barra de titulo
    def crontrolBtMinimizar(self):
       self.showMinimized()

    def crontrolBtNormalizar(self):
       self.showNormal()
       self.btnNormalizar.hide()
       self.btnMaximizar.show()
      
    def crontrolBtMaximizar(self):
       self.showMaximized()
       self.btnMaximizar.hide()  
       self.btnNormalizar.show()
    
    # Redimensionar ventana 
    def resizeEvent(self, event):
       rect = self.rect()
       self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    # Mover ventana 
    def mousePressEvent(self, event):
       self.clickPosition = event.globalPos()

    def moverVentana(self, event):
       if self.isMaximized() == False:
          if event.buttons() == QtCore.Qt.LeftButton:
             self.move(self.pos() + event.globalPos() - self.clickPosition)
             self.clickPosition = event.globalPos()
             event.accept()
       if event.globalPos().y() <= 10:
          self.showMaximized()
          self.btnMaximizar.hide()
          self.btnNormalizar.show()
       else:
          self.showNormal()
          self.btnNormalizar.hide()
          self.btnMaximizar.show()

if __name__ == '__main__':
            app = QApplication(sys.argv)
            gui = GUI()
            gui.show()
            sys.exit(app.exec_())