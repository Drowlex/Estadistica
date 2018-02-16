#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
	Created: on Sunday September 13 11:07:22 2017
	Project developed by:
		@autor: DKL&Derek
		@Sub-Autor: Pedro Ortiz Luis Roberto
	This program calculates the median of a list of numbers
	Copyright © 2017-2020 UV
	Version 1.0, Build 0001
"""
def mediana_impar(n,lista):
	n = int((n-2) / 2)
	valor = lista[n]
	return valor
def mediana_par(n,lista):
	n = int(n/2)
	suma = lista[n-1] + lista[n]
	#print ("La mediana en valores: [",lista[n-1],"][",lista[n],"]")
	return suma/2