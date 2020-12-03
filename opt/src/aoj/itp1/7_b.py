arr = []
while True:
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        break
    arr.append([n, x])


for i in range(len(arr)):
    n = arr[i][0]
    x = arr[i][1]
    num = 0
    for j in range(1, n-1):
        x2 = x-j 
        for k in range(j+1, n):
            x3 = x2-k
            for l in range(k+1, n+1):
                x4 = x3-l
                if x4 == 0:
                    num += 1
    print(num)


