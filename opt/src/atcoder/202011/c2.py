a, b, c = map(int, input().split())

odd_flg = 1
if b % 2 == 0:
    odd_flg = 0

a = abs(a)

com = 0
for i in range(b):
    if i == 0:
        tmp_a = abs(a - c)
        tmp_b = abs(a + c)
        if tmp_a <= tmp_b:
            com = tmp_a
        elif tmp_b <= tmp_a:
            com = tmp_b
    else:
        tmp_a = abs(com - c)
        tmp_b = abs(com + c)
        if tmp_a <= com:
            com = tmp_a
        elif tmp_b <= com:
            com = tmp_b
        else:
            com = b
            
        if odd_flg == 0 and i % 2 == 1:
            break
        elif odd_flg == 1 and i%2 == 0:
            break

print(com)