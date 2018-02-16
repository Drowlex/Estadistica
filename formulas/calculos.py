#Librerias utilizadas para realizar las operaciones
from formulas import media, mediana, moda, rango_medio, varianza, desviacion, frecuencia
from formulas import organizar, curtosis, asimetria, media_recortada, error_byZero
import math
def realizar_calculos(self):
	self.n = len(self.lista)
	nString = str(self.n)
	#Ordeno la lista
	self.lista.sort()
	listaString = str(self.lista)
	#media
	med = round(media.media(self.n,self.lista),2)
	mediaString = str(med)
	#mediana
	if self.n%2 == 0:
	    medianaString = str(mediana.mediana_par(self.n,self.lista))
	else:
	    medianaString = str(mediana.mediana_impar(self.n,self.lista))
	#moda
	if len(moda.moda(self.n,self.lista)) == 1:
	    modas = moda.moda(self.n,self.lista)
	    modaString = str(modas)
	else:
	    if len(moda.moda(self.n,self.lista)) == self.n:
	        modaString = "NO existe ninguna moda"
	    else:
	        modas = moda.moda(self.n,self.lista)
	        modaString = "Las modas son:"+str(modas)
	#Rango medio
	RangoMedioString = str(rango_medio.rango_medio(self.n,self.lista))
	#varianza
	temporal = media.media(self.n,self.lista)
	VarianaString = str(round(varianza.varianza(self.n,self.lista,temporal),2))
	#Desviacion estandar
	desv = round(desviacion.desviacion(self.n,self.lista,temporal),2)
	DesviacionString = str(desv)
	#Calculos Necesarios
	#Intervalos TF
	self.intervalos = int(1+3.3*math.log10(self.n))
	IntervalosString = str(self.intervalos)
	#Rango TF
	self.rango = int(self.lista[self.n-1] - self.lista[0])
	RangoString = str(self.rango)
	#Amplitud TF
	self.amplitud = int(self.rango/self.intervalos)
	amplitudString = str(self.amplitud)
	#Frecuencias y Graficas
	if self.amplitud != 0:
	    self.tabla,self.maximo,self.absoluta = frecuencia.calcula_frecuencia(self.n,self.lista,self.intervalos,self.rango,self.amplitud)
	    intervalo1String = str(organizar.organizar(self.tabla['1.Datos']))
	    intervalo2String = str(organizar.organizar(self.tabla['2.intervalo']))
	    faString = str(organizar.organizar(self.tabla['3.frecuencia absoluta']))
	    faaString = str(organizar.organizar(self.tabla['4.frecuencia absoluta acomulada']))
	    frString = str(organizar.organizar(self.tabla['5.frecuencia relativa']))
	    fraString = str(organizar.organizar(self.tabla['6.frecuencia relativa acomulada']))
	    maString = str(organizar.organizar(self.tabla['7.Marca de Clase']))
	elif self.amplitud == 0:
	    intervalo1String,intervalo2String,faString,faaString,frString,fraString,maString = error_byZero.error_byZero()
	    self.maximo = 0
	#Calculo de curtosis       
	g2 = curtosis.curtosis(self.n,self.lista,med,desv)
	if g2 < 0:
	    curtosisString = 'Es platicúrtica: '+str(g2)
	elif g2 == 0:
	    curtosisString = 'Es mesocúrtica: '+str(g2)
	elif g2 > 0:
	    curtosisString = 'Es lepcúrtica: '+str(g2)
	#Calculo de simetria
	Ca = asimetria.asimetria(self.n,self.lista,med,desv)
	if Ca < 0:
	    simetriaString = str(Ca)
	elif Ca == 0:
	    simetriaString = 'Simetrica: '+str(Ca)
	elif Ca > 0:
	    simetriaString = str(Ca)
	#Media Recortada
	if self.porciento == 0:
	    mediaRString = "Falta porcentaje"
	elif self.porciento != 0:
	    mediaRString = str(media_recortada.media_recortada(self.n,self.lista,self.porciento))
	porcentajeString = str(self.porciento)+" %"
	#Calculo del tallo de hoja xD!
	#Impresiones en pantalla        
	self.n_datos.setText(nString)
	self.media_text.setText(mediaString)
	self.mediana_text.setText(medianaString)
	self.moda_text.setText(modaString)
	self.rangoM_text.setText(RangoMedioString)
	self.varianza_text.setText(VarianaString)
	self.desviacion_text.setText(DesviacionString)
	self.intervalos_text.setText(IntervalosString)
	self.rango_text.setText(RangoString)
	self.amplitud_text.setText(amplitudString)
	self.intervalo1_text.setText(intervalo1String)
	self.intervalo2_text.setText(intervalo2String)
	self.fa_text.setText(faString)
	self.faa_text.setText(faaString)
	self.fr_text.setText(frString)
	self.fra_text.setText(fraString)
	self.ma_text.setText(maString)
	self.curtosis_text.setText(curtosisString)
	self.simetria_text.setText(simetriaString)
	self.mediaR_text.setText(mediaRString)
	self.porcentaje_text.setText(porcentajeString)
