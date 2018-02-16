from dialogos import dialogo2
from formulas import graficar
def grafica(self):
	if self.maximo != 0:
		temporal = []
		for i in range(self.maximo):
			temporal.append(self.tabla['2.intervalo'][i])
		graficar.graficar(self.maximo,temporal,self.absoluta)
	elif self.maximo == 0:
		dialogo2.errorGraficos(self)
