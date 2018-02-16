def agregar_datos(self):
	self.lista.append(float(self.insertar_text.toPlainText()))
	#Ordeno la lista
	self.lista.sort()
	self.n = len(self.lista)
	for i in range(self.n):
		if self.lista[i] < 0:
			self.lista[i] *= -1
	listaString = str(self.lista)
	#Impresiones en pantalla
	nString = str(self.n)
	self.n_datos.setText(nString)
	self.datos_text.setText(listaString)
	#Función clear exitosa!
	self.insertar_text.clear()            