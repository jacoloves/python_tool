import math
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN


n = int(input())
x_list=list(map(int,input().split()))
y_list=list(map(int,input().split()))

p=0.0
p2=0.0
p3=0.0
p4=0.0

# p=1
for i in range(n):
    p += abs(x_list[i]-y_list[i])

# p=2
sum = 0
for i in range(n):
    sum += (abs(x_list[i]-y_list[i]))**2
p2 = math.sqrt(sum)

# p=3
sum = 0
for i in range(n):
    sum += (abs(x_list[i]-y_list[i]))**3
p3 = sum**(1/3)

# p=infinity
for i in range(n):
    if i == 0:
        p4 = abs(x_list[i]-y_list[i])
    else:
        if p4 < abs(x_list[i]-y_list[i]):
            p4 = abs(x_list[i]-y_list[i])

print(Decimal(str(p)).quantize(Decimal('0.000001'), rounding=ROUND_HALF_UP))
print(Decimal(str(p2)).quantize(Decimal('0.000001'), rounding=ROUND_HALF_UP))
print(Decimal(str(p3)).quantize(Decimal('0.000001'), rounding=ROUND_HALF_UP))
print(Decimal(str(p4)).quantize(Decimal('0.000001'), rounding=ROUND_HALF_UP))
