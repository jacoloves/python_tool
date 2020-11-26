import math

n = int(input())

dest = int(math.sqrt(n))

flg = False
for i in range(2,dest):
    print(i)
    if n % i == 0:
        flg = True
print(flg)
print(1)
if flg:
    for i in range(1,n//2):
        if n % (i+1) == 0:
            print(i+1)
print(n)
