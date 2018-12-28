
import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')


from numpy import cos, linspace

def f(x):
    return x**2

g = linspace(-10,10,41)
N = len(g)
deltax = g[1] - g[0]

def derivative(x):
    derivarray = []
    for i in range(N):
        temp = (f(x[i] + deltax) - f(x[i])) / deltax
        derivarray.append(temp)
    return derivarray


y=f(g)

from matplotlib import pyplot as plt
legend = []

plt.axis([-10,10,-1,16])
plt.grid()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Funkcija $cos^2(x/2)$ un taas atvasinaajumi")
plt.plot(g,y,"k")
legend.append("$cos^2(x/2)$ - default - viss ir savienots ar taisnaam liinijaam")
plt.plot(g,y,"ro")
legend.append("$cos^2(x/2)$ - tikai dazhi punkti")


fderivative = derivative(g)


##N = len(x)
##deltax = x[1] - x[0]
##dv = []
##for i in range(N):
##   temp = (f(x[i] + deltax) - f(x[i])) / deltax
##   dv.append(temp)

plt.plot(g, fderivative, "y")
legend.append("$cos^2(x/2)$ atvasinaajums - viss ir savienots ar taisnaam linijaam")
plt.plot(g, fderivative, "go")
legend.append("$cos^2(x/2)$ atvasinaajums - dazhi punkti")

##dvtwo = []
##M = len(dv)
##deltadx = dv[1] - dv[0]
##for i in range(N):
##   temptwo = (f(x[i] + deltax) - f(x[i])) / deltax*deltax
##   dvtwo.append(temptwo)

sderivative = derivative(fderivative)

plt.plot(g, sderivative, "k")
legend.append("$cos^2(x/2)$ 2.kaartas atvasinaajums - viss ir savienots ar taisnaam linijaam")
plt.plot(g, sderivative, "bo")
legend.append("$cos^2(x/2)$ 2.kaartas atvasinaajums - dazhi punkti")



##print(plt.legend.__doc__)
##plt.legend(legend, loc = "upper left")
##plt.legend(legend, loc=3, fancybox=True, framealpha=0.5, facecolor="green")
plt.show()

