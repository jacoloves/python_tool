n = int(input())

a_score = 0
b_score = 0
for _ in range(n):
    a_str, b_str = map(str, input().split())

    # A B virsus
    if a_str > b_str:
        a_score += 3
    elif a_str < b_str:
        b_score += 3
    else:
        a_score += 1
        b_score += 1


print(a_score, b_score)
