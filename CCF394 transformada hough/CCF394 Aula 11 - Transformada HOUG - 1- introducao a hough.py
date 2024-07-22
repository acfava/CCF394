import matplotlib.pyplot as plt
angulo=[]
for i in range (0,180):
	angulo.append(i)
import math
import numpy as np
ro1=[]
ro2=[]
ro3=[]
angulo=[]
for x in range (0,180):
  angulo.append(x)
for i in range (0,180):
	x1=2*math.cos(angulo[i]*6.28/360)+5*math.sin(angulo[i]*6.28/360)
	x2=4*math.cos(angulo[i]*6.28/360)+7*math.sin(angulo[i]*6.28/360)
	x3=6*math.cos(angulo[i]*6.28/360)+9*math.sin(angulo[i]*6.28/360)
	ro1.append(x1)
	ro2.append(x2)
	ro3.append(x3)
y=[]
x=[]
for i in range (0,180):
	y.append(2*i+3)
	x.append(i)
fig, axs = plt.subplots(2)
fig.suptitle('Conversao retangular polar')
axs[0].set_title('y=2x+3')
axs[0].plot(x, y)
axs[1].plot(angulo,ro1)
axs[1].plot(angulo,ro2)
axs[1].plot(angulo,ro3)
plt.show()

