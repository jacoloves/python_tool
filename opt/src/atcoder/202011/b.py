import math

a, b = map(int, input().split())
cnt = 0



for i in range(a):
    num, num2 = map(int, input().split())
    ans_root = math.sqrt((num ** 2) + (num2 ** 2))
    if ans_root <= b:
        cnt = cnt + 1

print(cnt)
