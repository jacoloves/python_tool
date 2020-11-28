num_list = []

while True:
    x = int(input())
    if x == 0:
        break
    num_list.append(x)

cnt = 1

for i in range(len(num_list)):
    print("Case %d: %d" % (cnt, num_list[i]))
    cnt += 1


