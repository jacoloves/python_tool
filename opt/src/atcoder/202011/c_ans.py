a = int(input())

res = 7

for i in range(1, 10 ** 6 + 1):
    if res % a == 0:
        print(i)
        quit()
    else:
        res %= a
        res = res * 10 + 7

print(-1)