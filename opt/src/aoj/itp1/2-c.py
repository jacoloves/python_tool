a, b, c = map(int, input().split())

min_num = min(a, b, c)
max_num = max(a, b, c)
mid_num = 0

if a != min_num and a != max_num:
    mid_num = a
elif b != min_num and b != max_num:
    mid_num = b
else:
    mid_num = c

print(min_num, mid_num, max_num)
