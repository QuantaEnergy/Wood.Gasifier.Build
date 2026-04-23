import math
from module.var import *
from module.octagon import *


opposite = math.sin(math.radians(half_angle)) * radius
half_octagon_side = opposite

octagon_side = 2 * half_octagon_side

def test():
    cosine = math.cos(math.radians(half_angle))

    print("Cosine", cosine)

    adjacent = math.cos(math.radians(half_angle)) * radius

    print("Adjacent", adjacent)

    print("Half side", half_octagon_side)

    print("Radius", radius)

    hypotenuse = math.sqrt(adjacent**2 + opposite**2)

    print("Check work", hypotenuse) 

#test()
