import time as tm
import numpy as np
from SIRS import *

# ranges for probabilities
frac_range = np.arange(0, 1.1, 0.1)

# making data for the averages file
# timestr = t.strftime("%Y-%m-%d-%H-%M-%S"))
sim_num = 1
out_file = 'frac_' + str(sim_num)

def main():
    for frac in frac_range:
        print(frac)
        # create the simulation object
        sim = SIRS(p1=0.5, p2=0.5, p3=0.5, create_anim=False, immune_frac=frac, x_dim=20, y_dim=20)
        sim.count_infected_sites = True
        inf_array = sim.simulate()
        #inf_array_sq = [val*val for val in inf_array]
        avg = np.mean(inf_array)/float(sim.sweep)
        susc = np.std(inf_array)/float(sim.sweep)
        with open(out_file, 'a+') as f:
            f.write(' '.join((str(frac), str(avg), '\n')))


if __name__ == '__main__':
    main()