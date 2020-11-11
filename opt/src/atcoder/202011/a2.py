a = input()
cnt = 0

for i in range(len(a)):
    if a[i] == 'R':
        cnt += 1
    else:
        if cnt == 0:
            pass
        else:
            break

print(cnt)
