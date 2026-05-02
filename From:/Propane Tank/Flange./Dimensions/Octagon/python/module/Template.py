import math
from module.octagon import *

width = 8 + (9/16)

tan = math.tan(math.radians(half_angle))

print("Half angle:", half_angle)

print("Tangent", tan)

opposite = tan * width

print("Width", width)

print("Opposite", opposite)
