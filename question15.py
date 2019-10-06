import pylab as pl
import numpy as np

D = 2

M1 = np.array([0.0, 0.0])
M2 = np.array([1.0, 1.0])

C1 = np.array([[2.0, 0.4], [0.4, 1.0]])
C2 = np.array([[1.0, 0.6], [0.6, 2.0]])

X, Y = np.mgrid[-2:2:100j, -2:2:100j]
points = np.c_[X.ravel(), Y.ravel()]

invC = np.linalg.inv(C1)
v = points - M1
g1 = -0.5*np.sum(np.dot(v, invC) * v, axis=1) - D*0.5*np.log(2*np.pi) - 0.5*np.log(np.linalg.det(C1))
g1.shape = 100, 100

invC = np.linalg.inv(C2)
v = points - M2
g2 = -0.5*np.sum(np.dot(v, invC) * v, axis=1) - D*0.5*np.log(2*np.pi) - 0.5*np.log(np.linalg.det(C2))
g2.shape = 100, 100

fig, axes = pl.subplots(1, 3, figsize=(15, 5))
ax1, ax2, ax3 = axes.ravel()
for ax in axes.ravel():
    ax.set_aspect("equal")

ax1.pcolormesh(X, Y, g1)
ax2.pcolormesh(X, Y, g2)
ax3.pcolormesh(X, Y, g1 > g2)