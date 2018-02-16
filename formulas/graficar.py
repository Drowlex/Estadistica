#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
	Created: on Sunday September 13 11:02:12 2017
	Project developed by:
		@autor: DKL&Derek
		@Sub-Autor: Pedro Ortiz Luis Roberto
	This program produces the histogram of the frequency table
	Copyright © 2017-2020 UV
	Version 1.0, Build 0001
"""
import numpy as np
import matplotlib.pyplot as plt


def graficar(n,numbers,absoluta):
	x = np.zeros(n)
	y = np.zeros(n)
	for i in range(n):
		y[i] = absoluta[i]
		x[i] = numbers[i]
	plt.title('Gráfica de Tabla de Frecuencias')
	plt.bar(x, y, facecolor='cyan', edgecolor='white')
	plt.ylabel("Frecuencia Absoluta")
	plt.xlabel("DATOS")
	plt.grid(axis='both')
	plt.scatter(x,y,color='red')
	plt.plot(x,y,color='maroon')
	#plt.show(block=False)
	plt.show()