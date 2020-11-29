import math

r = float(input())

area = float(format(math.pi * (r*r), '.6f'))
radius = float(format(2 * math.pi * r, '.6f'))

print(area, radius)
