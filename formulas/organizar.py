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
def organizar(lista):
	x = ''
	for i in lista:
		x += i.__str__() + '\n' 
	return x