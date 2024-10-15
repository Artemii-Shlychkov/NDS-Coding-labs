import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
import sys
sys.path.append('/Users/a1/Desktop/NDS Coding labs/poisson-gpfa')
sys.path.append('/Users/a1/Desktop/NDS Coding labs/poisson-gpfa/funs')

import funs.util as util
import funs.engine as engine

n_neurons = 30
n_trials = 100
time = 1000  # ms
bin_size = 50  # ms
# Initialize random number generator
seed = np.random.seed(0)
maxEMiter = 50

d = 0.5
# Display the help for the function
#print(util.dataset.__doc__)
print(engine.PPGPFAfit.__doc__)


