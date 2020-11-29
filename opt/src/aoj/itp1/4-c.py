arr = []
while True:
    a, op, b = map(str,input().split())

    if op == '?':
        break
    elif op == '+':
        arr.append(int(a) + int(b))
    elif op == '-':
        arr.append(int(a) - int(b))
    elif op == '*':
        arr.append(int(a) * int(b))
    elif op == '/':
        arr.append(int(a) // int(b))

for i in range(len(arr)):
    print(arr[i])


