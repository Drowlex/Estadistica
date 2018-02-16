#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
	Created: on Sunday September 13 11:07:22 2017
	Project developed by:
		@autor: DKL&Derek
		@Sub-Autor: Pedro Ortiz Luis Roberto
	This program calculates the deviation of a list of numbers
	Copyright © 2017-2020 UV ESTADISTICA DKL
	Version 1.0, Build 0001
"""
import math
def varianza(n,lista,media):
	valor = 0
	for i in range(n):
		valor += pow((lista[i]-media),2)
	valor = valor/n
	return valor 
def desviacion(n,lista,media):
	temporal = varianza(n,lista,media)
	return math.sqrt(temporal)