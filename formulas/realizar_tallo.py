#def talloAndHoja(self):
#	print (self.lista)
import random
from formulas import organizar_tallo
def talloAndHoja(self,lista,n):
	templante = self.lista
	for i in range(n):
		if self.lista[i] < 10 and isinstance(self.lista[i],float) == True:
			self.lista[i] = int(self.lista[i] * 10)
		else:
			self.lista[i] = round(templante[i])
	hoja = []
	tallo = []
	contador = 0
	for i in range(n):
		if self.lista[i] >= 10:
			decMillar = self.lista[i] / 10000
			tmp = lista[i] % 10000
			UniMillar = tmp / 1000
			tmp = lista[i] % 1000
			centenas = tmp / 100
			tmp = tmp % 100
			decenas = tmp / 10
			hoja.append(tmp % 10)
			#print ("Principal: ",self.lista[i])
			aux = self.lista[i]
			aux -= hoja[contador]
			aux /= 10
			aux = round(aux)
			tallo.append(aux)
			#print ("Tallo:",tallo[contador],"Hoja:",hoja[contador])
			contador += 1
	planta = {}
	planta,n2 = agrupar(tallo,hoja)
	return planta,n2
def agrupar(tallo,hoja):
	tallos = []
	hojas = []
	n = len(tallo)
	#for i in range(n):
	#	print ("Tallo:",tallo[i],"Hoja:",hoja[i])
	
	for i in tallo:
	    if i not in tallos:
	        tallos.append(i)
	#print ("\n")
	#for i in tallos:
	#	print ("Tallos:",i)
	n = len(tallo)
	agrupamiento = {}
	for i in range(n):
		agrupamiento["N_Tallo"+str(i)] = tallo[i]
		agrupamiento["N_Hoja"+str(i)] = hoja[i]
	#print("agrupamiento")
	#for i in range(n):
	#	print (agrupamiento["N_Tallo"+str(i)],agrupamiento["N_Hoja"+str(i)])
	n2 = len(tallos)
	planta = {}
	#print (tallo)
	#print (tallos)
	#print ()
	for j in range(n2):
		for i in range(n):
			if tallo[i] == tallos[j]:
				#print (tallo[i]," == ",tallos[j],"hojas:",agrupamiento["N_Hoja"+str(i)])
				planta[str(j)+".ResultadosT"] = agrupamiento["N_Tallo"+str(i)]
				hojas.append(hoja[i])	
				planta[str(j)+".ResultadosH"] = hojas
			if tallo[i] != tallos[j]:
				#print ("Diferentes: ",tallo[i],"!=",tallo[j])	
				hojas = []
				#print ("->",planta["ResultadosH"+str(j)])}
	nuevo = {}
	nuevo2 = {}
	#print ("Resultados")
	for i in range(n2):
		nuevo['llave'+str(i)] = planta[str(i)+".ResultadosT"]
		nuevo2['llave'+str(i)] = planta[str(i)+".ResultadosH"]
	#	print (planta[str(i)+".ResultadosT"],planta[str(i)+".ResultadosH"])
	nuevo = list(nuevo.values())
	#print ("valores",nuevo)
	nuevo = sorted(nuevo)
	nuevo = organizar_tallo.organizalo(nuevo,nuevo2)	
	return nuevo,n2