import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as sp

data = np.loadtxt('SIRS_2018-03-07-14-37-06')
p1_arr = data[:, 0]
p2_arr = data[:, 1]
avg = data[:, 2]
_var = data[:, 3]

P1, P3 = np.linspace(p1_arr.min(), p1_arr.max(), 100), np.linspace(p2_arr.min(), p2_arr.max(), 100)
P1, P3 = np.meshgrid(P1, P3)

rbf = sp.Rbf(p1_arr, p2_arr, avg, function='linear')
zi = rbf(P1, P3)

plt.imshow(zi, vmin=avg.min(), vmax=avg.max(), origin='lower',
           extent=[p1_arr.min(), p1_arr.max(), p2_arr.min(), p2_arr.max()])
plt.colorbar()
plt.show()


# VARIANCE

rbf = sp.Rbf(p1_arr, p2_arr, _var, function='linear')
zi = rbf(P1, P3)

plt.imshow(zi, vmin=_var.min(), vmax=_var.max(), origin='lower',
           extent=[p1_arr.min(), p1_arr.max(), p2_arr.min(), p2_arr.max()])
plt.colorbar()
plt.show()