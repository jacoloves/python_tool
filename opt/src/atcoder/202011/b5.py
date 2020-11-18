s = input()
t = input()

maxcnt = 0
cnt = 0
for i in range(len(s)):
    if s[i] == t[cnt]:
        cnt += 1
    else:
        if maxcnt < cnt:
            maxcnt = cnt
        cnt = 0

if maxcnt == 0:
    if s[len(t)-1] == t[len(t)-1]:
        maxcnt += 1

print(len(t) - maxcnt)
