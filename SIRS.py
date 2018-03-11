import numpy as np
import matplotlib.pyplot as plt
import simplejson as json
from collections import OrderedDict


class SIRS(object):
    def __init__(self, x_dim=50, y_dim=50, p1=0.5, p2=0.5, p3=0.5, create_anim=True, immune_frac=0.0):
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.system = self.create_random_system()
        self.p1 = p1 # probability S -> I
        self.p2 = p2 # probability I -> R
        self.p3 = p3 # probability R -> S
        self.sweep = self.x_dim * self.y_dim
        self.count_infected_sites = False
        # list of the numbers of average infected sites recorded on each sweep during one simulation
        self.I_array = []
        self.create_animation = create_anim
        # fraction of agents that are immune to the disease
        self.immune_frac = immune_frac
        # list of the locations of agents/sites that are immune (list of tuples)
        self.immune_agents = self.generate_immune_agents()

    def create_random_system(self):
        system = np.random.randint(0, 3, size=(self.y_dim, self.x_dim))
        return system

    def generate_immune_agents(self):
        # list to hold the locations of immune agents
        agent_arr = []
        # how many agents are immune
        agent_nr = int(self.immune_frac*self.sweep)
        print(agent_nr)
        for i in range(agent_nr):
            agent = (np.random.randint(0, self.x_dim), np.random.randint(0, self.y_dim))
            self.system[agent[1], agent[0]] = 2
            agent_arr.append(agent)
            # make sure no sites were randomly generated more than once
            check = True
            while check:
                agent = (np.random.randint(0, self.x_dim), np.random.randint(0, self.y_dim))
                for n in agent_arr:
                    if n == agent:
                        break
                    else:
                        check = False
            self.system[agent[1], agent[0]] = 2
            agent_arr.append(agent)
        #print(agent_arr)
        return agent_arr

    def change_to_infected(self, x, y):
        rand = np.random.uniform()
        if rand < self.p1:
            self.system[y, x] = 1

    # determines if a state is next to an infected state
    def find_infected_neighbour(self, x, y):
        x_len = self.x_dim
        y_len = self.y_dim
        # n_up
        if self.system[(y - 1 + y_len) % y_len, x] == 1:
            self.change_to_infected(x, y)
        # n_down
        elif self.system[(y + 1) % y_len, x] == 1:
            self.change_to_infected(x, y)
        # n_left
        elif self.system[y, (x - 1 + x_len) % x_len] ==1:
            self.change_to_infected(x, y)
        # n_right
        elif self.system[y, (x + 1) % x_len] == 1:
            self.change_to_infected(x, y)
        else:
            return

    # method for updating (or not updating) the state of an agent
    def update_state(self, x, y):
        n_state = self.system[y, x]
        if n_state == 0:
            self.find_infected_neighbour(x, y)
        elif n_state == 1:
            rand = np.random.uniform()
            if rand < self.p2:
                self.system[y, x] = 2
        elif n_state == 2:
            rand = np.random.uniform()
            if rand < self.p3:
                self.system[y, x] = 0

    # method for counting the number of infected agents/sites in a system
    def count_I(self):
        n = 0
        for x in range(self.x_dim):
            for y in range(self.y_dim):
                if self.system[y, x] == 1:
                    n += 1
        return n

    def animate_SIRS(self):
        im = plt.imshow(self.system) #cmap=cm.RdBu)
        plt.ion()
        plt.show()
        plt.pause(0.00001)
        plt.cla()

    def simulate(self):
        for i in range(self.sweep * 100):
            rand_x = np.random.randint(0, self.x_dim)
            rand_y = np.random.randint(0, self.y_dim)
            # check if this agent is supposed to be permanently immune
            check = False
            for n in self.immune_agents:
                if n == (rand_x, rand_y):
                    check = True
            if check:
                continue
            self.update_state(rand_x, rand_y)
            if self.create_animation and i % (1*self.sweep) == 0:
                self.animate_SIRS()
            if self.count_infected_sites and i >= 10*self.sweep:
                self.I_array.append(self.count_I())
        if self.count_infected_sites:
            return self.I_array

