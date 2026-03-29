# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import math
import matplotlib.pyplot as plt

#définition des constantes
G=1 #6.67*(10**11)
mpl = 1 #6*10**24normalemnt mais 1 pour simplifier
dt=0.01

#terre
#position de base
px = 1#1.5*(10**8)normalement mais 1 pour simplifier
py = 0

#vitesse de base
vx = 0
vy = 1 

plt.ion()
fig, ax = plt.subplots()

for i in range(5000):
    
    #calcule de la distance solei(x=o; y=0)/centre de la terre 
    D = math.sqrt(px**2 + py**2)
   
    #accélération
    a = G*mpl/(D**2)
    
    ax = -a*px
    ay = -a*py
    
    vx = vx + ax *dt
    vy = vy +ay *dt
    
    px = px + vx * dt
    py = py + vy * dt
    
    
    plt.clf()
    
    plt.scatter(0,0, color="red")
    plt.scatter(px, py, color="blue")
    
    plt.xlim(-2, 2)
    plt.ylim(-2,2)
    
    plt.pause(0.001)
    
plt.ioff()
plt.show()
