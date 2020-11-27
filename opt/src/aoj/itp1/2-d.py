w, h, x, y, r = map(int, input().split())

if x < 0 or y < 0:
    print("No")
elif x + r > w or x - r < 0:
    print("No")
elif y + r > h or y - r < 0:
    print("No")
else:
    print("Yes")

