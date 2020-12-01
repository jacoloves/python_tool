pattern = [['S','H','C','D'],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]]

n = int(input())
arr1 = []
for _ in range(n):
    arr2 = []
    a, b = map(str, input().split())
    arr2.append(a)
    arr2.append(int(b))
    arr1.append(arr2)

arr3 = []
for i in range(len(pattern[0])):
    for j in range(len(pattern[1])):
        flg = False
        for k in range(len(arr1)):
            if flg:
                break
            if  arr1[k][0] == pattern[0][i] and arr1[k][1] == pattern[1][j]:
                flg = True
        if flg == False:
            arr3.append([pattern[0][i], pattern[1][j]])


for i in range(len(arr3)):
    print(arr3[i][0], arr3[i][1])

