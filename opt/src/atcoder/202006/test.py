array = []
a = int(input())
array_ans = [a]
for _ in range(a):
    array.append(list(map(int, input().split())))

for i in range(a):
    for j in range(len(array[a])):