# -*- coding: utf-8 -*-
from numpy import sin, cos, linspace, pi
from matplotlib import pyplot as plt

def f1(x):
    return (-1)**0*x**0/(1)

def f2(x):
    return f1(x) + x**2/2*(1*2)

def f3(x):
    return f2(x) + x**4/2*(1*2*3*4)

def f4(x):
    return f3(x) + x**6/2*(1*2*3*4*5*6)

x = linspace(-0.5,0.5,41)
y = cos(x/2)*cos(x/2)
y1 = f1(x)
y2 = f2(x)
y3 = f3(x)
y4 = f4(x)

legend = []

plt.grid()
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.title("$cos^2(x/2)$ funkcija un tās izvirzījumi rindā")
plt.plot(x,y,color = "#000000")
legend.append("$cos^2(x/2)$")
plt.plot(x,y1,color = "#FF0000")
legend.append("$1$")
plt.plot(x,y2,color = "#00FF00")
legend.append("$1 + x^2/2*(2*1)!$")
plt.plot(x,y3,color = "#0000FF")
legend.append("$1 + x^2/2*(2*1)! + x^4/2*(2*2)!$")
plt.plot(x,y4,color = "#FFFF00")
legend.append("$1 + x^2/2*(2*1)! + x^4/2*(2*2)! + x^6/2*(2*3)!$")
plt.legend(legend, loc = 2)
plt.show()

def manssin(x):
    k = 0
    a = (-1)**0*x**1/(1)
    S = a

    while True:
        k = k + 1
        R = (-1)*x*x/((2*k)*(2*k+1))
        a = a * R
        S = S + a
        if abs(sin(x)-S) < 0.01:
            k = k - 1
            return k

cx = pi
cy = manssin(cx)
p = u"\u03C0"
print("Cietaa rieksta atrisinaajums:")
print("Pie argumenta vertibas %s kluda starp teoretisko un praktisko ar summesanu ieguto tuvinajumu bus verojama pie locekla nr.%i"%(p,cy))
