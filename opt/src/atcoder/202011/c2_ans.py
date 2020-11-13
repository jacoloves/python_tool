a, b, c = map(int, input().split())

def sgn(a):
    if a > 0: return 1
    if a < 0: return -1
    return 0

if a > 0:
    a_greedy = a - b * c
else:
    a_greedy = a + b * c

if sgn(a) == sgn(a_greedy):
    print(abs(a_greedy))
    exit()
a_r = a % c
a_l = a_r - c

r_parity = (abs(a - a_r) // c) % 2

if b%2 == r_parity:
    print(abs(a_r))
else:
    print(abs(a_l))