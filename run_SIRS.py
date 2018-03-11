import simplejson as json
from collections import OrderedDict
from SIRS import *
import ast

def main():
    print('reading in the input data...')
    with open('SIRS_input.dat', 'r') as f:
        config = json.load(f, object_pairs_hook=OrderedDict)
    x_dim = config["x dimension"]
    y_dim = config["y dimension"]
    p1 = config["p1"]
    p2 = config["p2"]
    p3 = config["p3"]
    anim = ast.literal_eval(config["create animation"])
    frac = config["fraction of immune agents"]
    print('setting up the simulation...')
    sim = SIRS(x_dim=x_dim, y_dim=y_dim, p1=p1, p2=p2, p3=p3, create_anim=anim, immune_frac=frac)
    print("running the simulation...")
    sim.simulate()











if __name__ == '__main__':
    main()