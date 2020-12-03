n, m = map(int, input().split())

arr = []

for _ in range(n):
    arr2 = list(map(int, input().split()))
    arr.append(arr2)

arr3 = []
for _ in range(m):
    num = int(input())
    arr3.append(num)


for i in range(n):
    ans = 0
    for j in range(m):
        ans += arr[i][j] * arr3[j]
    print(ans)
