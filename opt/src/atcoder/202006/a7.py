a = int(input())
b, c = map(int, input().split())

ans = int(c/a) * a

if b<=ans<=c:
    print('OK')
else:
    print('NG')