n, m, x = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
p = float("inf")

for i in range(1, 2 ** n):
    s = [0] * m
    count = 0
    ps = 0
    for j in range(n):
        if (i >> j) & 1:
            ps += a[j][0]
            for k in range(m):
                s[k] += a[j][k + 1]

    for k in range(m):
        if s[k] >= x:
            count += 1

    if count == m:
        p = min(ps, p)

if p == float('inf'):
    print(-1)
else:
    print(p)