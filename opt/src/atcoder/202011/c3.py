n=int(input())
lis = []
a=list(map(int, input().split()))
lis = lis + a

anslis = []
max = 0
for i in range(n):
    if i == 0:
        max = lis[i]
        anslis.append(0)
    else:
        if max < lis[i]:
            anslis.append(0)
            max = lis[i]
        else:
            anslis.append(max-lis[i])

ans = 0
for i in range(len(anslis)):
    ans += anslis[i]

print(ans)
        
