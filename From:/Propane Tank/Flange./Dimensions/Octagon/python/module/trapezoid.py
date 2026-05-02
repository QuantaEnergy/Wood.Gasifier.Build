import math
from module.octagon import *
from module.var import *

# One side of the Octagon, a trapezoid, Inner or Shorter side.

print("Radius", radius)

half_inner = math.sin(math.radians(half_angle))

inner = half_inner * radius * 2

print("Inner side", inner)
