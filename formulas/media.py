#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
	Created: on Sunday September 13 11:07:22 2017
	Project developed by:
		@autor: DKL&Derek
		@Sub-Autor: Pedro Ortiz Luis Roberto
	This program calculates the average of a list of numbers
	Copyright © 2017-2020 UV ESTADISTICA DKL
	Version 1.0, Build 0001
"""
def media(n,lista):
	suma = 0
	for i in range(n):
		suma += lista[i]
	return suma/n
	