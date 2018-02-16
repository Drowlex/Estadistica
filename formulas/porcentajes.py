def tanto_porciento(self):
	self.porciento = int(self.insertar_porcentaje.toPlainText())
	self.insertar_porcentaje.clear()
	porcentajeString = str(self.porciento)+" %"
	self.porcentaje_text.setText(porcentajeString)
