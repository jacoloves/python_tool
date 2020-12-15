import statistics

ans_list = []
while True:
    n = int(input())
    if n == 0:
        break
    arr = list(map(int, input().split()))
    std_dev = statistics.pstdev(arr)
    ans_list.append(std_dev)

for i in range(len(ans_list)):
    print(ans_list[i])
