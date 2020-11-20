n = int(input())
arr = list(map(int, input().split()))

mod_num = 10**9+7

ans = 0
for i in range(len(arr)-1):
    for j in range(len(arr)-1):
        if len(arr) == j + i + 1:
            break
        else:
            print(arr[i], arr[j+i+1])
            ans += (arr[i] * arr[j+i+1]) % mod_num

print(ans)
        
