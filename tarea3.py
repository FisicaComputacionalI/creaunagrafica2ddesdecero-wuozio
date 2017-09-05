import pylab as pl
import matplotlib.pylot as plt
x = [1,2,3,4,5,6,7,8]
y = [9,8,8.25,8,7.5,8,8,8.75]
pl.plot(x,y, 'D')
plt.title("Grafica de promedios semestral")
plt.xlabel("Semestres cursados")
plt.ylabel("Promedio")
pl.savefig('promedios.png')
plt.show()
