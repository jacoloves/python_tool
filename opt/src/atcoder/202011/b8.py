import math

n = int(input())
x = list(map(int, input().split()))

m_ans = 0
eu_ans = 0
che_ans = 0

for i in range(len(x)):
    m_ans += abs(x[i])
    eu_ans = math.sqrt(abs(eu_ans)**2 + abs(x[i])**2)
    che_ans = max(abs(che_ans), abs(x[i]))

print(m_ans)
print(eu_ans)
print(che_ans)
