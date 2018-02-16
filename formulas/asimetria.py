#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
	Created: on Saturday October 14 12:21:10 2017
	Project developed by:
		@autor: DKL&Derek
		@Sub-Autor: Pedro Ortiz Luis Roberto
	This program calculates the symmetry
	Copyright © 2017-2020 UV ESTADISTICA DKL
	Version 1.0, Build 0001
"""
import math
def asimetria(n,lista,media,desviacion):
	suma = 0
	for i in range(1,n):
		suma +=  math.pow((lista[i] - media),3)
	divide = n*math.pow(desviacion,3)
	Ca = round(((suma/divide)-3),2)
	return Ca