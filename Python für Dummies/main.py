import math

def circle_area(radius):
    area = math.pi * (radius ** 2)
    return math.ceil(area)
radius = 3
area = circle_area(radius)
print(f"Area(r={radius}): {area}")