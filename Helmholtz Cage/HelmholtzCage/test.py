from InputPipeline import orbitPropagator as op
from InputPipeline import currentGenerator as cg
from InputPipeline import ppigrf
from InputPipeline import fieldGenerator as fg
from OutputPipeline import DutyCycle
from OutputPipeline import PWM
from OutputPipeline import Cage
import time

day = 28
month = 4
year = 2022
test_length = 5
segments = 5

test = op.Orbit('SPOC', test_length, segments)
test.generate()
test.display()
print(len(test.positions))

mag = fg.MagneticField(test.positions, day, month, year, test_length, segments)
mag.calculate()
mag.fix_datatype()
mag.display()
mag.plot_fields()

X = cg.Coil('X-axis', mag.Bx, 30, 1, .5445)
X.get_current()
X.display()

Y = cg.Coil('Y-axis', mag.By, 30, 1, .5445)
Y.get_current()
Y.display()

Z = cg.Coil('Z-axis', mag.Bz, 30, 1, .5445)
Z.get_current()
Z.display()

cage = Cage.Cage(X.Iout, Y.Iout, Z.Iout,mag.Bx,mag.By, mag.Bz, 10)

print("Calibrate 1")
cage.calibrate()
#print("Calibrate 2")
#print("Starting Simulation for: {}".format('SPOC'))
cage.control()
#cage.control()
cage.off()
