import SensorVerification.magnetometer as mag
import OrbitPropagation.CurrentGeneration as cg
import Frequency_DutyCycle_Calculation as dc
import PWM.PWM as PWM
import time

class Cage():
    
    def __init__(self, Ix, Iy, Iz, Bx, By, Bz, test_length):
        self.Ix = Ix
        self.Iy = Iy
        self.Iz = Iz
        self.Bx = Bx
        self.By = By
        self.Bz = Bz
        self.mag = mag.Magnetometer()
        self.cal_constx = None
        self.cal_consty = None
        self.cal_consty = None
        self.N = 30
        self.a = 1
        self.gamma = .5445
        self.PWM = PWM()
        self.PWM.set_frequency(1000)
        self.loop_time = range(test_length)
        
    def calibrate(self):
        "Use to set calibration point"
        self.mag.read()
        
        self.x = cg.Coil('coilx', self.mag.Mx, self.N, self.a, self.gamma)
        self.y = cg.Coil('coily', self.mag.My, self.N, self.a, self.gamma)
        self.z = cg.Coil('coilz', self.mag.Mz, self.N, self.a, self.gamma)
        
        self.cal_constx = -(self.x.get_current())
        self.cal_consty = -(self.y.get_current())
        self.cal_constz = -(self.z.get_current())
        
        cycles = dc.DutyCycle(self.cal_constx, self.cal_consty, self.calconstz)
        cycles.calculate()
    
        self.PWM.set_DutyCycles(cycles.xDutyCycle, cycles.yDutyCycle, cycles.zDutyCycle)
        
        self.Ix = self.Ix + self.cal_constx
        self.Iy = self.Iy + self.cal_consty
        self.Iz = self.Iz + self.cal_constz
        
    def control(self):
        "set main control of the Helmholtz Cage"
        for i in self.loop_time:
            
            ix = self.Ix[i]
            iy = self.Iy[i]
            iz = self.Iz[i]
            bx = self.Bx[i]
            by = self.By[i]
            bz = self.Bz[i]
            
            cycles  = dc.DutyCycle(ix, iy, iz)
            cycles.calculate()
            
            self.PWM.set_DutyCycles(cycles.xDutyCycle, cycles.yDutyCycle, cycles.zDutyCycle)
            
            
            
            for j < 11:
            
            time.sleep(1)
            
            self.mag.read()
            bx_change = bx - self.mag.Mx #Theoretical- read value
            by_change = by - self.mag.My
            bz_change = bz - self.mag.Mz
            
            self.x = cg.Coil('coilx', bx_change, self.N, self.a, self.gamma)
            self.y = cg.Coil('coily', by_change, self.N, self.a, self.gamma)
            self.z = cg.Coil('coilz', bz_change, self.N, self.a, self.gamma)
            
            ix_change = x.get_current()
            iy_change = y.get_current()
            iz_change = z.get_current()
            
            ix += ix_change
            iy += iy_change
            iz += iz_change
            
            cycles  = dc.DutyCycle(ix, iy, iz)
            cycles.calculate()
            
            self.PWM.set_DutyCycles(cycles.xDutyCycle, cycles.yDutyCycle, cycles.zDutyCycle)
            
            time.sleep(4)
    
            
        