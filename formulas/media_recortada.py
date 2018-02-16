#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
	Created: on Sunday September 13 11:07:22 2017
	Project developed by:
		@autor: DKL&Derek
		@Sub-Autor: Pedro Ortiz Luis Roberto
	This program calculates the cropped average
	Copyright © 2017-2020 UV ESTADISTICA DKL
	Version 1.0, Build 0001
"""
def media_recortada(n,lista,porciento):
	valor = porciento / 100 * porciento
	aux = round(valor / 2)
	tope = n - aux
	sumatoria = 0
	for i in range(aux,tope):
		sumatoria += lista[i]
	tope = n - valor		
	return round((sumatoria/tope),2)
"""
lista = [0,0,0,0,0,0,1,1,1,1,1,2,2,2,3,4,4,5,6,12]
n = len(lista)
print (media_recortada(n,lista,15))
"""