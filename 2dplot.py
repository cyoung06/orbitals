import itertools
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.colors as mcolors

from orbits import *
import math

import matplotlib
import numpy as np
import matplotlib.pyplot as plt


# matplotlib.use('macosx')


def set_axes_equal(ax):
    """
    Make axes of 3D plot have equal scale so that spheres appear as spheres,
    cubes as cubes, etc.

    Input
      ax: a matplotlib axis, e.g., as output from plt.gca().
    """

    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = np.mean(z_limits)

    # The plot bounding box is a sphere in the sense of the infinity
    # norm, hence I call half the max range the plot radius.
    plot_radius = 0.5*max([x_range, y_range, z_range])

    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])


def draw(n,l,m, bohr, Ts, Ps):
    print(f"Drawing... {n} {l} {m}")
    Rs = np.linspace(0,bohr * a0 * math.sqrt(2), 100)
    # Ts = np.linspace(0, math.pi ,50)
    # Ps = np.linspace(0, math.pi * 2, 50)

    radial = psi_r(Rs,n,l)
    byphi = psi_phi(Ps, m)
    bytheta = psi_theta(Ts, l, m)

    coordinates = np.array(list(itertools.product(Rs, Ts, Ps)))
    values = np.abs(np.outer(np.outer(radial * Rs, bytheta * np.sin(bytheta)), byphi)).flatten() ** 2

    RR = coordinates.T[0]
    TT = coordinates.T[1]
    PP = coordinates.T[2]

    coords = np.array([
        RR * np.sin(TT) * np.cos(PP),
        RR * np.sin(TT) * np.sin(PP),
        RR * np.cos(TT)
    ]).T

    # coordinates =

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    colormap = cm.jet
    normalize = mcolors.Normalize(vmin=np.min(values), vmax=np.max(values))
    s_map = cm.ScalarMappable(norm=normalize, cmap=colormap)
    print(np.min(values))
    print(np.max(values))

    cond = values > np.max(values) * 0.02
    # cond = ~np.isnan(values)


    ax.scatter(coords[:,0][cond], coords[:,1][cond], coords[:,2][cond], color= s_map.to_rgba(values[cond]))
    set_axes_equal(ax)
    plt.show()



# draw(4,3, -2, 30,  np.linspace(0, math.pi ,50), np.array([0, math.pi])) # px
# draw(5,4, 0, 40,  np.linspace(0, math.pi ,50), np.array([0, math.pi])) # px
# draw(5,4, 1, 40,  np.linspace(0, math.pi ,50), np.array([0, math.pi])) # px
# draw(5,4, 2, 40,  np.linspace(0, math.pi ,50), np.array([0, math.pi])) # px
# draw(5,4, 3, 40,  np.linspace(0, math.pi ,50), np.array([0, math.pi])) # px
# draw(5,4, 4, 40,  np.linspace(0, math.pi ,50), np.array([0, math.pi])) # px
# draw(3,1,0, 30,  np.linspace(0, math.pi ,50), np.array([0, math.pi])) # py
# draw(3,1, 1, 20,  np.linspace(0, math.pi ,50), np.array([math.pi / 2, math.pi * 3 / 2])) # pz
# draw(2,1, -1, 10,  np.linspace(0, math.pi ,50), np.linspace(0, math.pi * 2, 50)) # px
# draw(2,1, 0, 10,  np.linspace(0, math.pi ,50), np.linspace(0, math.pi * 2, 50)) # py
# draw(2,1, 1, 10,  np.linspace(0, math.pi ,50), np.linspace(0, math.pi * 2, 50)) # pz

# draw(4,2,  -2, 20,  np.linspace(0, math.pi ,50), np.linspace(0, math.pi * 2, 50)) # px
# draw(5,4,  0, 40,  np.linspace(0, math.pi ,50), np.linspace(0, math.pi * 2, 50)) # px
# draw(5,4, 1, 40,  np.linspace(0, math.pi ,50), np.linspace(0, math.pi * 2, 50)) # py
# draw(5,4, 2, 40,  np.linspace(0, math.pi ,50), np.linspace(0, math.pi * 2, 50)) # pz
# draw(5,4, 3, 40,  np.linspace(0, math.pi ,50), np.linspace(0, math.pi * 2, 50)) # pz
draw(5,4, 4, 40,  np.linspace(0, math.pi ,50), np.linspace(0, math.pi * 2, 6)) # pz
