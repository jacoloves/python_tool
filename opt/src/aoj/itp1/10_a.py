import math

x1, y1, x2, y2 = map(float, input().split())

xlength = x2 - x1
ylength = y2 - y1

print(math.sqrt(xlength**2+ylength**2))
