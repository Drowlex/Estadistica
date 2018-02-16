import random
def generar_datos(self):
	self.n = int(self.insertar_random.toPlainText())
	if self.n < 0:
		self.n *= -1
	for i in range(self.n):
		self.lista.append(random.randint(10,100))
	self.insertar_random.clear()
	self.n = len(self.lista)
	nString = str(self.n)
	#Ordeno la lista
	self.lista.sort()
	listaString = str(self.lista)
	self.n_datos.setText(nString)
	self.datos_text.setText(listaString)
