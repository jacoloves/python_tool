n = int(input())

cnt = 0
for a in range(n):
    for b in range(n):
        for c in range(n):
            if a*b == n-c:
                cnt += 1
print(cnt)
