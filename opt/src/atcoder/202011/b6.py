a, b, c, d = map(int, input().split())

arr = []

arr.append(a*c)
arr.append(a*d)
arr.append(b*c)
arr.append(b*d)

print(max(arr))
