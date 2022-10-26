import math
import numpy as np


class Coil:

    def __init__(self, name, B, N, a, gamma):

        self.Iout = []
        self.Bin = B
        self.N = N
        self.a = a
        self.gamma = gamma
        self.name = name

    def get_current(self):
        mu = 4*math.pi*(10**(-7))
        self.Bin = np.array(self.Bin)
        p = 0
        for i in self.Bin:
            B = self.Bin[p]
            num = B*math.pi*self.a*(1+(self.gamma**2))*((2+(self.gamma**2))**.5)
            den = mu*4*self.N
            I = num/den
            self.Iout.append(I)
            p +=1

    def display(self):
        print('Currents for {} ='.format(self.name))
        print(self.Iout)