#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
	Created: on Thursday September 12 20:10:22 2017
	Project developed by:
		@autor: DKL&Derek
		@Sub-Autor: Pedro Ortiz Luis Roberto
	This program elaborates the table of frequencies of the given list
	Copyright © 2017-2020 UV
	Version 1.0, Build 0001
"""
import math
#import pandas as pd
def calcula_frecuencia(n,lista,intervalos,rango,amplitud):
	templante = lista
	for i in range(n):
		lista[i] = round(templante[i])
	da = []
	da1 = []
	fa = []
	faa = []
	fr = []
	fra = []
	ma = []
	#**************************Diccionario de frecuencias***********************************
	frecuencia = {	'1.Datos':da,
					'2.intervalo':da1,
					'3.frecuencia absoluta':fa,				
					'4.frecuencia absoluta acomulada': faa,
					'5.frecuencia relativa':fr,
					'6.frecuencia relativa acomulada':fra,
					'7.Marca de Clase':ma}
	try:
		#*************************Calculo de intervalos de Datoses*******************************
		for i in range(lista[0],lista[n-1]+amplitud,amplitud):
			da.append(i)
		maximo = len(da)
		temporal = da
		for i in range(maximo-1):
			da1.append(0)
		for i in range(maximo-1):
			da1[i] = da[i+1]
		da.pop()
		maximo = len(da)
		#************************Calculo de las frecuencias absoluta*****************************
		for i in range(maximo):
			fa.append(0)
		for i in range(n):
			if lista[i] == frecuencia['2.intervalo'][maximo-1]:
				fa[maximo-1] += 1
			for j in range(maximo):
				#print (frecuencia['1.Datos'][j],"<=",lista[i],"and",lista[i],"<",frecuencia['2.intervalo'][j])	
				if frecuencia['1.Datos'][j] <= lista[i] and lista[i] < frecuencia['2.intervalo'][j]:
					fa[j] += 1	
		absoluta = fa
		#*****************Calculo de las frecuencias absoluta acomulada*****************************
		contador = 0
		for i in range(maximo):
			faa.append(0)
		
		for i in range(n):
			if lista[i] == frecuencia['2.intervalo'][maximo-1]:
				contador += 1
				faa[maximo-1] = contador
			for j in range(maximo-1):
				if lista[i] >= frecuencia['1.Datos'][j] and lista[i] < frecuencia['2.intervalo'][j]:	
					contador += 1
					faa[j] = contador
		
		#************************Calculo de las frecuencias relativa********************************
		
		for i in range(maximo):
			fr.append(0)
		for i in range(maximo):
			fr[i] = round((fa[i]/n),2)
		
		#*******************Calculo de las frecuencias relativa acomulada****************************
		for i in range(maximo):
			fra.append(0)
		for i in range(maximo):
			if i == 0:
				fra[i] = round(fr[i],2)
			else:
				fra[i] = round((fra[i-1] + fr[i]),2)
		#****************************Calculo de la Marca de Clase************************************
		for i in range(maximo):
			ma.append(0)
		for i in range(maximo):
			ma[i] = (frecuencia['1.Datos'][i] + frecuencia['2.intervalo'][i])/2
		#*******************************IMPRESIÓN DE TABLA*******************************************
		"""
		f = frecuencia absoluta
		F = frecuencia absoluta acomulada
		h = frecuencia relativa
		H = frecuencia relativa acomulada
		Xi = Marca de Clase
		"""
		#print ("\n\n\t\tTABLA DE FRECUENCIA\n\n")
		#for i in range(maximo):
		#	print(frecuencia['1.Datos'][i],"-",frecuencia['2.intervalo'][i],"\t",frecuencia['3.frecuencia absoluta'][i],
		#		"",frecuencia['4.frecuencia absoluta acomulada'][i],"\t %.1f"%frecuencia['5.frecuencia relativa'][i],
		#			"\t%.1f"%frecuencia['6.frecuencia relativa acomulada'][i],"\t",frecuencia['7.Marca de Clase'][i])
		return frecuencia,maximo,absoluta
		#df  = pd.DataFrame(frecuencia)
		#print (df)
		#return df
		#Sentencia de error encontrada
		#Solucción burlando error
		#cuando se hace pop en da se borra igual de temporal -.-"
		
		#temporal.append(da1[maximo-1])
		#GR.graficar(maximo,temporal,absoluta)
	except Exception as e:
		print ("Error:",e)
#numbers = [8,9,10,10,11,12,12,13,13,14,14,15,17,17,20,20,23,25,28,33,38,48,59,61]
#n = len(numbers)
#calcula_frecuencia(n,numbers)