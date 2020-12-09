w = input()
t = []
while True:
    arr = list(map(str, input().split()))
    if arr[0] == "END_OF_TEXT":
        break
    for i in range(len(arr)):
        t.append(arr[i].lower())

match_cnt = 0
for i in range(len(t)):
    w_cnt = 0
    for j in range(len(t[i])):
        if w[w_cnt] == t[i][j]:
            w_cnt += 1
        else:
            w_cnt = 0
            break
        if len(w) != len(t[i]):
            break
        if w_cnt == len(w) and w_cnt == len(t[i]):
            match_cnt += 1
            break

print(match_cnt)

