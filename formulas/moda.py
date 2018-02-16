#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
	Created: on Sunday September 13 11:07:22 2017
	Project developed by:
		@autor: DKL&Derek
		@Sub-Autor: Pedro Ortiz Luis Roberto
	This program calculates the fashion from a list of lista
	Copyright © 2017-2020 UV
	Version 1.0, Build 0001
"""
def moda(n,lista):
	repeticiones = 0
	for i in lista:
		apariciones = lista.count(i)
		if apariciones > repeticiones:
			repeticiones = apariciones
	modas = []
	for i in lista:
		apariciones = lista.count(i)
		if apariciones == repeticiones and i not in modas:
			modas.append(i)
	return modas