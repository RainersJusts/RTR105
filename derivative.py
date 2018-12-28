import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import cos, linspace
from matplotlib import pyplot as plt

def f(x):
    return cos(x/2)*cos(x/2)

x = linspace(0,6,21)
y = f(x)


dv = []
deltax = x[1] - x[0]
N = len(x)

for i in range(N):
    temp = (f(x[i] + deltax) - f(x[i])) / deltax
    dv.append(temp)


seconddv = []

for i in range(N-1):
    temp = (dv[i+1] - dv[i]) / deltax
    seconddv.append(temp)
    
legend = []
plt.axis([0,5,-1,1])
plt.grid()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Funkcija $cos^2(x/2)$ un taas atvasinaajumi")
plt.plot(x,y,"k")
legend.append("$cos^2(x/2)$ - default - viss ir savienots ar taisnaam liinijaam")
plt.plot(x,y,"ro")
legend.append("$cos^2(x/2)$ - tikai dazhi punkti")
plt.plot(x,dv,"y")
legend.append("$cos^2(x/2)$ atvasinaajums - viss ir savienots ar taisnaam linijaam")
plt.plot(x,dv,"go")
legend.append("$cos^2(x/2)$ atvasinaajums - dazhi punkti")
plt.plot(x[0:len(x)-1],seconddv,"m")
legend.append("$cos^2(x/2)$ 2.kaartas atvasinaajums - viss ir savienots ar taisnaam linijaam")
plt.plot(x[0:len(x)-1],seconddv,"bo")
legend.append("$cos^2(x/2)$ 2.kaartas atvasinaajums - dazhi punkti")
plt.legend(legend, loc = "upper left")
plt.legend(legend, loc=3, fancybox=True, framealpha=0.5, facecolor="green")
plt.show()
