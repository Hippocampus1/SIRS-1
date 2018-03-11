import time
from SIRS import *
import numpy as np

# ranges for probabilities
p1_range = np.arange(0, 1.1, 0.1)
p3_range = np.arange(0, 1.1, 0.1)

# making data for the averages file
timestr = time.strftime("%Y-%m-%d-%H-%M-%S")
print(timestr)
out_file = 'SIRS_' + timestr
#create_plot = True

def main():
    for p1 in p1_range:
        for p3 in p3_range:
            # create the simulation object
            sim = SIRS(p1=p1, p2=0.5, p3=p3, create_anim=False, x_dim=20, y_dim=20)
            sim.count_infected_sites = True
            print(p1, p3)
            inf_array = sim.simulate()
            avg = np.mean(inf_array)/float(sim.sweep)
            susc = np.var(inf_array)/float(sim.sweep)
            with open(out_file, 'a+') as f:
                f.write(' '.join((str(p1), str(p3), str(avg), str(susc), '\n')))


if __name__ == '__main__':
    main()



