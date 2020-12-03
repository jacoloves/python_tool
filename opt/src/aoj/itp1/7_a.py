arr = []

while True:
    m, f, r = map(int, input().split())
    if m == -1 and f == -1 and r == -1:
        break
    arr2 = []
    arr2.append(m)
    arr2.append(f)
    arr2.append(r)
    arr.append(arr2)

for i in range(len(arr)):
    if arr[i][0] == -1 or arr[i][1] == -1:
        print("F")
    else:
        test_sum = arr[i][0]+arr[i][1]
        tuishi_num = arr[i][2]
        if 80 <= test_sum:
            print("A")
        elif 65 <= test_sum and test_sum < 80:
            print("B")
        elif 50 <= test_sum and test_sum < 65:
            print("C")
        elif 30 <= test_sum and test_sum < 50:
            if 50 <= tuishi_num:
                print("C")
            else:
                print("D")
        elif test_sum < 30:
            print("F")

