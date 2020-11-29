entire_list = []

while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    num_list = [] 
    num_list.append(x)
    num_list.append(y)
    entire_list.append(num_list)

for i in range(len(entire_list)):
    ans_list = sorted(entire_list[i])
    print(ans_list[0], ans_list[1])

