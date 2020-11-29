a, b = map(int, input().split())

ans1 = a//b
ans2 = a%b
ans3 = float(format(a/b,'.5f'))

print(ans1, ans2, ans3)
