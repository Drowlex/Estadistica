def botonera(self):
    #Botones registrados en el diseño de QtDesinger
    self.boton_agregar.clicked.connect(self.agregar)
    self.boton_generarE.clicked.connect(self.generarE)
    self.boton_generarF.clicked.connect(self.generarF)
    self.boton_calcular.clicked.connect(self.calcular)
    self.boton_graficar.clicked.connect(self.graficar_tabla)
    self.boton_resetear.clicked.connect(self.menuArchivoNuevo)
    self.boton_salir.clicked.connect(self.menuArchivoCerrar)
    self.boton_tallo.clicked.connect(self.talloDeHoja)
    self.boton_porcentaje.clicked.connect(self.addporcentaje)