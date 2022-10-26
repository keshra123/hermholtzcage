
class DutyCycle:

    def __init__(self, Ix, Iy, Iz):
        self.xDutyCycles = []
        self.yDutyCycles = []
        self.zDutyCycles = []
        self.dir_x = []
        self.dir_y = []
        self.dir_z = []
        self.Ix = Ix
        self.Iy = Iy
        self.Iz = Iz

    def calculate(self):
        # current = inputvoltage * PWMdutycycle / coilresistance
        # dummy variables need to pull from current in orbit propagation to get specific values
        for i in Ix:
            if Ix[i] < 0:
                self.dir_x.append(0)
            else
                self.dir_x.append(1)
        
        Ix_abs = abs(self.Ix)
        self.xDutyCycle = int(Ix_abs*.000144) #7.5A/65535 = .000144 mA
        
        for j in Iy:
            if Iy[j] < 0:
                self.dir_y.append(0)
            else
                self.dir_y.append(1)
        
        Iy_abs = abs(self.Iy)
        self.yDutyCycle = int(Iy_abs*.000144) #7.5A/65535 = .000144 mA
         
         for k in Iz:
            if Iz[k] < 0:
                self.dir_z.append(0)
            else
                self.dir_z.append(1)
        
        Iz_abs = abs(self.Iz)
        self.zDutyCycle = int(Iz_abs*.000144) #7.5A/65535 = .000144 mA
        
        
        
