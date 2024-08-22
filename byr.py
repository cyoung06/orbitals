from orbits import *
import math

import matplotlib
import numpy as np
import matplotlib.pyplot as plt


def draw(n,l,m, bohr):
    print(f"Drawing... {n} {l} {m}")
    precision = 100000
    Rs = np.linspace(0,bohr * a0,precision)
    Ts = np.linspace(0,math.pi,100)
    Ps = np.linspace(0, math.pi * 2, 100)

    radial = psi_r(Rs,n,l) ** 2  * Rs ** 2
    byphi = np.sum(psi_phi(Ps, m) ** 2) / 100
    bytheta = np.sum( psi_theta(Ts, l, m) ** 2 * np.sin(Ts) ) / 100

    realparts = radial * byphi * bytheta
    print(realparts)

    interval = bohr * a0 / precision



    matplotlib.pyplot.xticks(np.linspace(0, bohr * a0, bohr))
    matplotlib.pyplot.axis([0.0, bohr * a0, 0, np.max(realparts) * 1.2])
    matplotlib.pyplot.plot(Rs, realparts)
    matplotlib.pyplot.title(f'n={n} l={l} m={m}, theta=90deg phi=0, tick mark={bohr}')
    matplotlib.pyplot.show()

draw(1,0,0, 10) # 1s
draw(2,0,0, 15) # 2s
draw(2,1,-1, 15) # 2p_x
draw(2,1,0, 15) # 2p_y
draw(2,1,1, 15) # 2p_z
draw(3,0,0, 30) # 3p