a = int(input())

arr = list(map(int, input().split()))
arr.sort()

cnt = 0
for i in range(a - 2):
    for j in range(i+1, a - 1):
        for k in range(j+1, a):
            if arr[i] != arr[j] != arr[k]:
                if arr[i] + arr[j] > arr[k]:
                    cnt += 1
print(cnt)
