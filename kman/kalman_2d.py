import numpy as np

class KF2D:
    def __init__(self, initial_a, initial_o, initial_av, initial_ov):
        # mean of state GRV
        self.a = np.array([initial_a, initial_av])
        self.o = np.array([initial_o, initial_ov])


        self.P = np.eye(2)
