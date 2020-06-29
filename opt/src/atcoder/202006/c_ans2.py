A, B, C = map(int, input().split())
D = list(map(int, input().split()))
E = list(map(int, input().split()))

a, b = [0], [0]
for i in range(A):
    a.append(a[i] + D[i])
for i in range(B):
    b.append(b[i] + E[i])

ans, j = 0, B
for i in range(A + 1):
    if a[i] > C:
        break

    while b[j] > C - a[i]:
        j -= 1
    ans = max(ans, i + j)
print(ans)