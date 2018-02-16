from matplotlib import pyplot

lenguajes = ('python','C','Java','Go','JavaScript')
slices = (100,130,90,80,128)
colores = ('red','blue','green','#DD98AA','#18492D')
valores = (0.1, 0, 0, 0)

pyplot.rcParams['toolbar'] = 'None'

_, _, texto = pyplot.pie(slices,colors=colores, labels=lenguajes, autopct='%1.1f%%',startangle=90)#explode=valores, startangle=90)
for tex in texto:
	tex.set_color('white')
pyplot.axis('equal')
pyplot.title('Gráfica de lenguajes de programación')
#pyplot.legend(labels=lenguajes)

pyplot.show()
#pyplot.savefig(lenguajes.png)