#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
	Created: on Sunday September 13 11:07:22 2017
	Project developed by:
		@autor: DKL&Derek
		@Sub-Autor: Pedro Ortiz Luis Roberto
		This program organizes the data to be 
		displayed in the frequency table
	Copyright © 2017-2020 UV
	Version 1.0, Build 0001
"""
def organizalo(lista,lista2):
	x = ''
	n = len (lista)
	for i in range(n):
		x += lista[i].__str__() + '\t' + lista2['llave'+str(i)].__str__() + '\n'
	return x
