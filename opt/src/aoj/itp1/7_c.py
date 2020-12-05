r, c = map(int, input().split())

arr = []
for i in range(r):
    arr2 = list(map(int, input().split()))
    arr.append(arr2)

for i in range(r):
    sum = 0
    for j in range(c):
        sum += arr[i][j]
    arr[i].append(sum)

arr3 =[] 
for i in range(c+1):
    sum = 0
    for j in range(r):
        sum += arr[j][i]
    arr3.append(sum)

arr.append(arr3)

for i in range(r+1):
    for j in range(c+1):
        if j == c:
            print(arr[i][j])
        else:
            print(arr[i][j], end=" ")

