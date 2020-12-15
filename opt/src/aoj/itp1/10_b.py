import math
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

a, b, c = map(float, input().split())


d = math.sqrt(a**2+b**2-2*a*b*math.cos(math.radians(c)))
l = a+b+d

cosb = (a**2+d**2-b**2)/(2*a*d)
degreeB = math.degrees(math.acos(cosb))
h = d*math.sin(math.radians(degreeB))

s=(h*a)/2

print(Decimal(str(s)).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP))
print(Decimal(str(l)).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP))
print(Decimal(str(h)).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP))
