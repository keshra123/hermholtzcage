import OrbitPropagator
import MagneticFieldCalcuation
import CurrentGeneration

test = OrbitPropagator.Orbit('SPOC', 9000, 900)
test.generate()
test.display()
print(len(test.positions))
mag = MagneticFieldCalcuation.MagneticField(test.positions)
mag.calculate()
mag.display()

X = CurrentGeneration.Coil('X-axis', mag.Bx, 30, 1, .5445)
X.get_current()
X.display()

Y = CurrentGeneration.Coil('Y-axis', mag.By, 30, 1, .5445)
Y.get_current()
Y.display()

Z = CurrentGeneration.Coil('Z-axis', mag.Bz, 30, 1, .5445)
Z.get_current()
Z.display()