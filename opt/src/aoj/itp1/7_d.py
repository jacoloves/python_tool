n, m, l = map(int, input().split())

nm_arr = []
for _ in range(n):
    input_arr = []
    input_arr = list(map(int, input().split()))
    nm_arr.append(input_arr)

ml_arr = []
for _ in range(m):
    input_arr = []
    input_arr = list(map(int, input().split()))
    ml_arr.append(input_arr)

nl_arr = []
for i in range(n):
    tmp_nl_arr = []
    for j in range(l):
        ans = 0
        for k in range(m):
            ans += nm_arr[i][k]*ml_arr[k][j]
        tmp_nl_arr.append(ans)
    nl_arr.append(tmp_nl_arr)

for i in range(len(nl_arr)):
    for j in range(len(nl_arr[i])):
        if j == len(nl_arr[i])-1:
            print(nl_arr[i][j])
        else:
            print(nl_arr[i][j], end=" ")

