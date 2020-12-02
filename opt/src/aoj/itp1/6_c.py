man_list = [
        [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
        [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
        [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
        [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        ]

n = int(input())
arr = []

for _ in range(n):
    arr2 = list(map(int, input().split()))
    arr.append(arr2)

for i in range(len(arr)):
    man_list[arr[i][0]-1][arr[i][1]-1][arr[i][2]-1] += arr[i][3]

for i in range(len(man_list)):
    for j in range(len(man_list[i])):
        print(end=" ")
        for k in range(len(man_list[i][j])):
            if k != len(man_list[i][j])-1:
                print(man_list[i][j][k], end=" ")
            else:
                print(man_list[i][j][k])
    if i != len(man_list)-1:
        print("####################")
