import math
def circle_area(r):
    return round(math.pi*r**2, 2) if type(r) == int and r > 0 else False
