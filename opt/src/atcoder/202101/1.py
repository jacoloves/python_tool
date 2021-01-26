a = int(input())

b = list(map(int, input().split()))

c = list(set(b))

for i in range(len(c)):
    if b.count(c[i]) == 4:
        print("YES")
        exit()

print("NO")