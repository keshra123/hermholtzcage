import datetime
import ppigrf


class MagneticField:

    def __init__(self, positions):
        self.position = positions
        self.Bx = []
        self.By = []
        self.Bz = []
    def calculate(self):
        value = 0
        for i in self.position:
            p = self.position[value]
            phi = p[0]
            theta = p[1]
            r = p[2]
            date = datetime.datetime(2022, 3, 15)
            Br, Btheta, Bphi = ppigrf.igrf_gc(r, theta, phi, date)
            Bx = -Btheta *.000000001
            By = Bphi*.000000001
            Bz = -Br*.000000001
            self.Bx.append(Bx)
            self.By.append(By)
            self.Bz.append(Bz)
            value += 1




    def display(self):
        print("Magnetic Field Values")
        print('Bx = ')
        print(self.Bx)
        print('By = ')
        print(self.By)
        print('Bz = ')
        print(self.Bz)