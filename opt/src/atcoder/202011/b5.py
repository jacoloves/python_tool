s = input()
t = input()

ans = len(s)

for i in range(len(s)):
    if i + len(t) - 1 >= len(s): break
    dif = 0
    for j in range(len(t)):
        if s[i+j] != t[j]:
            dif += 1
    ans = min(ans, dif)

print(ans)
