n, x, t = map(int, input().split())

cnt=0
while n > 0:
    n -= x
    cnt += t

print(cnt)
