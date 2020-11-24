n = int(input())

d = []
for _ in range(n):
    lis = list(map(int, input().split()))
    d.append(lis)

cnt = 0
flg = False
for i in range(n):
    if d[i][0] == d[i][1]:
        cnt += 1
    else:
        cnt = 0

    if cnt == 3:
        flg = True
        break

if flg:
    print("Yes")
else:
    print("No")

