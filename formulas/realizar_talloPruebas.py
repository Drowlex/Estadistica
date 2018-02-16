#def talloAndHoja(self):
#	print (self.lista)
import random
def talloAndHoja(lista,n):

	hoja = []
	tallo = []
	contador = 0
	for i in range(n):
		if lista[i] >= 10:
			decMillar = lista[i] / 10000
			tmp = lista[i] % 10000
			UniMillar = tmp / 1000
			tmp = lista[i] % 1000
			centenas = tmp / 100
			tmp = tmp % 100
			decenas = tmp / 10
			hoja.append(tmp % 10)
			print ("Principal: ",lista[i])
			aux = lista[i]
			aux -= hoja[contador]
			aux /= 10
			aux = round(aux)
			tallo.append(aux)
			print ("Tallo:",tallo[contador],"Hoja:",hoja[contador])
			contador += 1
	print ("\n\n")
	planta = {}
	#planta = 
	agrupar(tallo,hoja)
	#print (planta)
def agrupar(tallo,hoja):
	tallos = []
	hojas = []
	n = len(tallo)
	
	for i in range(n):
		print ("Tallo:",tallo[i],"Hoja:",hoja[i])
	
	for i in tallo:
	    if i not in tallos:
	        tallos.append(i)
	print ("\n")
	for i in tallos:
		print ("Tallos:",i)
	n = len(tallo)
	agrupamiento = {}
	for i in range(n):
		agrupamiento["N_Tallo"+str(i)] = tallo[i]
		agrupamiento["N_Hoja"+str(i)] = hoja[i]
	print("agrupamiento")
	for i in range(n):
		print (agrupamiento["N_Tallo"+str(i)],agrupamiento["N_Hoja"+str(i)])
	n2 = len(tallos)
	planta = {}
	print (tallo)
	print (tallos)
	print ()
	for j in range(n2):
		for i in range(n):
			if tallo[i] == tallos[j]:
				print (tallo[i]," == ",tallos[j],"hojas:",agrupamiento["N_Hoja"+str(i)])
				planta["ResultadosT"+str(j)] = agrupamiento["N_Tallo"+str(i)]
				hojas.append(hoja[i])	
				planta["ResultadosH"+str(j)] = hojas
			if tallo[i] != tallos[j]:
				print ("Diferentes: ",tallo[i],"!=",tallo[j])	
				hojas = []
				#print ("->",planta["ResultadosH"+str(j)])
	print ("Resultados")
	nuevo = {}
	nuevo2 = {}
	#planta["ResultadosH"+str(0)] = hojas
	
	for i in range(n2):
		nuevo['uno'+str(i)] = planta["ResultadosT"+str(i)]
		nuevo2['dos'+str(i)] = planta["ResultadosH"+str(i)]

		#print (planta["ResultadosH"+str(i)])
		#print (nuevo2)
		#nuevo['uno'+str(i)] = planta["ResultadosT"+str(i)],"      ",planta["ResultadosH"+str(i)]
		#print (planta["ResultadosT"+str(i)],"\t\t",planta["ResultadosH"+str(i)])
	l = list(nuevo.values())
	
	#print (l2,"\n")
	
	#print (l)
	
	l = sorted(l)
	#l2 = sorted(l2)
	x = ''
	n = len (l)
	for i in range(n):
		x += l[i].__str__() + '\t' + nuevo2['dos'+str(i)].__str__() + '\n'
	print (x)

	#print ("-->",l)
	#l = planta.items()
	#l.sorted()
	#print ("Item:",sorted(l),"\n")
	return planta

#lista = []	
#lista = [30,31,40,52,55,120,121,10, 11, 13, 13, 13, 14, 14, 15, 16, 16, 17, 18, 18, 19, 20, 20, 20, 20, 20, 20]
lista = [11,12,13,14,22,22,23,33,34]
"""
for i in range(10):
	lista.append(random.uniform(1,500))
	#lista.append(round(float(input("Dame el valor:"))))
for i in range(10):
	lista[i] = round(lista[i])
"""
n = len(lista)
lista.sort()
print (lista)
#tallo,hoja = 
talloAndHoja(lista,n)
#print ("Tallo: ",tallo)
#print ("Hoja: ",hoja)
#agrupar(tallo,hoja)