import numpy as np
import scipy

a0 = 0.529e-10
def psi_r(r, n, l):
    thing = np.sqrt( (2/(n*a0))**3 * scipy.special.factorial(n-l-1) / (2*n * (scipy.special.factorial(n+l))**3)) * np.exp(-r / (n * a0) ) * ((2 * r / (n * a0)) ** l)
    thing *= scipy.special.assoc_laguerre((2 * r / (n * a0)), n-l-1, 2*l+1)
    # print(thing)
    return thing
def psi_theta(theta, l, m):
    m = np.abs(m)
    thing = np.sqrt( (2*l+1) * scipy.special.factorial(l-m) / (4 * np.pi * scipy.special.factorial(l+m)))
    thing = scipy.special.lpmn(m, l, np.cos(theta))[0][m][l] * thing
    thing *= (m % 2 == 0) * 2 - 1
    # print(thing)
    return thing
def psi_phi(phi, m):
    return np.exp(1j * phi * m)


