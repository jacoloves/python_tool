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
    print(entire_list[i])
