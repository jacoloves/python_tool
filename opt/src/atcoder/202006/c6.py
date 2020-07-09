a, b = map(int, input().split())
arr = list(map(int, input().split()))

ans_arr = []
dif_arr = []
for i in range(a):
    ans_arr.append(0)
    dif_arr.append(i+1)


input_arr = []
for _ in range(b):
    add_arr = list(map(int, input().split()))
    input_arr.append(add_arr)


input_arr2 = []
for i in range(b):
    input_arr2.append(input_arr[i][0])
    input_arr2.append(input_arr[i][1])
    if arr[input_arr[i][0]-1] < arr[input_arr[i][1]-1]:
        ans_arr[input_arr[i][0] - 1] = 0
        ans_arr[input_arr[i][1] - 1] = 1
    elif arr[input_arr[i][0]-1] > arr[input_arr[i][1]-1]:
        ans_arr[input_arr[i][0] - 1] = 1
        ans_arr[input_arr[i][1] - 1] = 0

A = set(input_arr2)
B = set(dif_arr)

C = list(B.difference(A))

for i in range(len(C)):
    ans_arr[C[0]-1] = 1

print(sum(ans_arr))