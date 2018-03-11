import matplotlib.pyplot as plt
import numpy as np

inp_file = 'frac_1'

frac_data = np.loadtxt(inp_file)

plt.plot(frac_data[:, 0], frac_data[:, 1])
plt.xlabel('frac')
plt.ylabel('<I>')
plt.show()