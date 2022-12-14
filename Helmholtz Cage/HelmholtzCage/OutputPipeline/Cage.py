import sys
from Sensors import Magnetometer2 as mag
from InputPipeline import currentGenerator as cg
import OutputPipeline.DutyCycle as dc
import OutputPipeline.PWM as PWM
import time
import OutputPipeline.Pinout as Pinout

sys.path.append('../')

class Cage:

    def __init__(self, Ix, Iy, Iz, Bx, By, Bz, test_length):
        self.z = None
        self.y = None
        self.x = None
        self.Ix = Ix
        self.Iy = Iy
        self.Iz = Iz
        self.Bx = Bx
        self.By = By
        self.Bz = Bz
        self.magnet = mag.Magnetometer()
        self.magnet.setup()
        self.cal_constx = None
        self.cal_consty = None
        self.cal_constz = None
        self.N = 30
        self.a = 1
        self.gamma = .5445
        self.PWM = PWM.PWM()
        self.PWM.connectI2C()
        self.PWM.set_frequency(1000)
        self.pins = Pinout.Pins()
        self.loop_time = range(test_length)
        self.test_length = test_length

    def calibrate(self):
        "Use to set calibration point"
        time.sleep(5)
        i = 0
        while i < 4:
            try:
                self.magnet.read()
                print('Initial Reading:')
                self.magnet.display('G')
                if i == 0:
                    bx_init = 0 - self.magnet.Mx
                    by_init = 0 - self.magnet.My
                    bz_init = 0 - self.magnet.Mz
                    print(bx_init)
                    print(by_init)
                    print(bz_init)
                else:
                    bx_init += -self.magnet.Mx
                    by_init += -self.magnet.My
                    bz_init += -self.magnet.Mz
                    print(bx_init)
                    print(by_init)
                    print(bz_init)
                
                cycles_cal = dc.DutyCycle(bx_init, by_init, bz_init)
                cycles_cal.single_calc()
                
                #if cycles_cal.dir_x == 0:
                    #cycles_cal.dir_x = 1
                #else:
                    #cycles_cal.dir_x = 0
                #if cycles_cal.dir_y == 0:
                    #cycles_cal.dir_y = 1
                #else:
                    #cycles_cal.dir_x = 0
                #if cycles_cal.dir_z == 0:
                    #cycles_cal.dir_z = 1
                #else:
                    #cycles_cal.dir_x = 0
                self.PWM.set_DutyCycles(cycles_cal.xDutyCycle, cycles_cal.yDutyCycle, cycles_cal.zDutyCycle)
                self.pins.set_directions(cycles_cal.dir_x, cycles_cal.dir_y, cycles_cal.dir_z)
            except:
                print("Failed Read")
            time.sleep(5)
            #self.magnet.status()
            i += 1
        self.Bx = [ele + bx_init for ele in self.Bx]
        self.By = [ele + by_init for ele in self.By]
        self.Bz = [ele + bz_init for ele in self.Bz]

    def control(self):
        "set main control of the Helmholtz Cage"
        i = 0
        for i in range(len(self.Bx)):
            
            bx = self.Bx[i]
            by = self.By[i]
            bz = self.Bz[i]
            

            cycles = dc.DutyCycle(bx, by, bz)
            cycles.single_calc()
            print(bx)
            print(cycles.xDutyCycle)
            print(by)
            print(cycles.yDutyCycle)
            print(bz)
            print(cycles.zDutyCycle)
            
            self.PWM.set_DutyCycles(cycles.xDutyCycle, cycles.yDutyCycle, cycles.zDutyCycle)
            self.pins.set_directions(cycles.dir_x, cycles.dir_y, cycles.dir_y)
            j = 0
            while j < self.test_length:
    
                try:
                    self.magnet.read()
                    
                    bx_change = bx - self.magnet.Mx  # Theoretical- read value
                    by_change = by - self.magnet.My
                    bz_change = bz - self.magnet.Mz
                    
                    
                    cycles_loop = dc.DutyCycle(bx, by, bz)
                    cycles_loop.single_calc()
                    
                    if cycles_loop.dir_x == 0:
                        cycles_loop.dir_x = -1
                    if cycles_loop.dir_y == 0:
                        cycles_loop.dir_y = -1
                    if cycles_loop.dir_z == 0:
                        cycles.loop.dir_z =-1
                    
                    duty_change_x = self.cycles_loop.xDutyCycle*cycles_loop.dir_x
                    duty_change_y = self.cycles_loop.yDutyCycle*cycles_loop.dir_y
                    duty_change_z = self.cycles_loop.zDutyCycle*cycles_loop.dir_z

                    cycles.xDutyCycle += cycles_loop.xDutyCycle
                    cycles.yDutyCycle += cycles_loop.yDutyCycle
                    cycles.yDutyCycle += cycles_loop.zDutyCycle
                    
                    self.PWM.set_DutyCycles(cycles.xDutyCycle, cycles.yDutyCycle, cycles.zDutyCycle)
                    self.pins.set_directions(cycles.dir_x, cycles.dir_y, cycles.dir_y)
                except:
                    print("Read Failed")
                    #self.magnet.status()
                minuto = len(self.Bx)
                minuto = minuto - 1
                print("Executing Orbit Minute {} of {}".format(i,minuto))
                time.sleep(10)
                j+=10
                
            i += 1
            
        self.PWM.set_DutyCycles(0, 0, 0)

    def off(self):
        print("Turning Off Cage")
        self.PWM.set_DutyCycles(0, 0, 0)

        

    

