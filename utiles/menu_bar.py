from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction
def menuB(self):
    menu = self.menuBar()
    #Menús Padres
    menu_archivo = menu.addMenu("&Archivo")
    menu_ayuda = menu.addMenu("&Ayuda")

    #Agregar un elemento acción al menu_archivo
    menu_archivo_nuevo = QAction(QIcon(),"&Nuevo", self)
    #Atajo del teclado
    menu_archivo_nuevo.setShortcut("Ctrl+n")
    menu_archivo_nuevo.triggered.connect(self.menuArchivoNuevo) #Lanzador
    menu_archivo.addAction(menu_archivo_nuevo)
    #Agregar un elemento acción al menu_archivo
    menu_archivo_guardar = QAction(QIcon(),"&Guardar", self)
    """
    #Atajo del teclado
    menu_archivo_guardar.setShortcut("Ctrl+s")
    menu_archivo_guardar.triggered.connect(self.menuArchivoGuardar) #Lanzador
    menu_archivo.addAction(menu_archivo_guardar)
    """
    #Agregar un elemento acción al menu_archivo
    menu_archivo_cerrar = QAction(QIcon(),"&Cerrar", self)
    #Atajo del teclado
    menu_archivo_cerrar.setShortcut("Ctrl+w")
    menu_archivo_cerrar.triggered.connect(self.menuArchivoCerrar) #Lanzador
    menu_archivo.addAction(menu_archivo_cerrar)
    #Agregar un elemento acción al menu_ayuda
    menu_ayuda_facebook = QAction(QIcon(),"&Facebook", self)
    #Atajo del teclado
    menu_ayuda_facebook.setShortcut("Ctrl+f")
    menu_ayuda_facebook.triggered.connect(self.menuAyudaFacebook) #Lanzador
    menu_ayuda.addAction(menu_ayuda_facebook)
    menu_ayuda.addSeparator() 
    #Agregar un elemento acción al menu_ayuda
    menu_ayuda_acerca_de = QAction(QIcon(),"&Acerca de EstadisticaDKL", self)
    #Atajo del teclado
    menu_ayuda_acerca_de.setShortcut("Ctrl+p")
    menu_ayuda_acerca_de.triggered.connect(self.menuAyudaAcercade) #Lanzador
    menu_ayuda.addAction(menu_ayuda_acerca_de) 
