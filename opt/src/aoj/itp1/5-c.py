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
    cnt = 0
    for _ in range(arr1[i][0]):
        min_cnt = 0 
        for _ in range(arr1[i][1]): 
            if cnt % 2 == 0:
                if min_cnt % 2 == 0:
                    print("#", end="")
                    min_cnt += 1
                else:
                    print(".", end="")
                    min_cnt += 1
            else:
                if min_cnt % 2 == 0:
                    print(".", end="")
                    min_cnt += 1
                else:
                    print("#", end="")
                    min_cnt += 1
        cnt += 1
        print("")
    print("")

