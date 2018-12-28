import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import random

N = 1000
a = 0
b = 5
b1 = 2

x = random.uniform(a,b,N)

k = [0, 0, 0, 0, 0]
for i in range(N):
    if x[i] < 1:
        k[0] = k[0] + 1
    elif x[i] < 2:
        k[1] = k[1] + 1
    elif x[i] < 3:
        k[2] = k[2] + 1
    elif x[i] < 4:
        k[3] = k[3] + 1
    else:
        k[4] = k[4] + 1
print(k)

from math import cos

y = random.uniform(a,b1,N)

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Funkcija un taas integraalis (laukums starp funkciju un x ass)')
plt.plot(x,y,'ko')
N1 = 0


for i in range(N):
    if y[i] < cos(x[i]/2)*cos(x[i]/2):
        plt.plot(x[i],y[i],'go')
        N1 = N1 + 1
    else:
        plt.plot(x[i],y[i],'ro')

##Izveidoju savas intereses peec
##for i in range(N):
##    if y[i] > 0:
##        if y[i] < cos(x[i]/2):
##            plt.plot(x[i],y[i],'go')
##            N1 = N1 + 1
##        elif y[i] > cos(x[i]/2):
##            plt.plot(x[i],y[i],'ro')
##    if y[i] < 0:
##        if y[i] > cos(x[i]/2):
##            plt.plot(x[i],y[i],'go')
##            N1 = N1 + 1
##        elif y[i] < cos(x[i]/2):
##            plt.plot(x[i],y[i],'ro')

S_zinaamais = (b-a) * (b1-a)
S_nezinaamais = 1. * S_zinaamais * N1 / N
print(S_nezinaamais)

plt.show()
