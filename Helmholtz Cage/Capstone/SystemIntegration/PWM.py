import board
import busio
import adafruit_pca9685

class PWM:
    def __init__(self):
        self.pi = pigpio.pi()
        self.currentX = currentX
        self.currentY = currentY
        self.currentZ = currentZ
    def connectI2C(self):
        i2c = busio.I2C(board.scl, board.sda)
        self.hat = adafruit_pca9685(i2C)
        self.X = self.hat.channels[0]
        self.Y = self.hat.channels[1]
        self.Z = self.hat.channels[2]
    def set_frequency(self, freq)
        self.hat.frequency(freq)
    def set_DutyCycles(self, x, y, z):
        self.X.duty_cycle(x)
        self.Y.duty_cycle(y)
        self.Z.duty_cycle(z)
    
    