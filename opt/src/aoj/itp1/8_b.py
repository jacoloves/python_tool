arr = []

while True:
    num = int(input())
    if num == 0:
        break
    arr.append(num)

for i in range(len(arr)):
    ans = 0 
    arr_num = arr[i]
    while True:
        ans += arr_num%10
        if arr_num//10 == 0:
            break
        else:
            arr_num = arr_num//10
    print(ans)


