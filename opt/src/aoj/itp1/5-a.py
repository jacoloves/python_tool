arr1 = []
while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break
    arr2 = []
    arr2.append(h)
    arr2.append(w)
    arr1.append(arr2)

for i in range(len(arr1)):
    for _ in range(arr1[i][0]):
        for _ in range(arr1[i][1]):
            print("#", end="")
        print("")
    print("")

