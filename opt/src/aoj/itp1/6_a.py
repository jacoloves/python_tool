n = int(input())

arr = list(map(int, input().split()))

arr.reverse()
for i in range(len(arr)):
    if n-1 == i:
        print(arr[i])
    else:
        print(arr[i], end=" ")
