n, m, x = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

flg = True
n_cnt = 0
m_cnt = 0
doku_cnt = 0

while flg:
    if n_cnt != n and m_cnt != m:
        if x >= a[n_cnt] or x >= b[m_cnt]:
            if a[n_cnt] <= b[m_cnt] or n_cnt >= n:
                x = x - a[n_cnt]
                n_cnt += 1
                doku_cnt += 1
            else:
                x = x - b[m_cnt]
                m_cnt += 1
                doku_cnt += 1
        else:
            flg = False
    else:
        if m == m_cnt and n == n_cnt:
            flg = False
        elif n == n_cnt:
            x = x - b[m_cnt]
            m_cnt += 1
            doku_cnt += 1
        elif m == m_cnt:
            x = x - a[n_cnt]
            n_cnt += 1
            doku_cnt += 1

print(doku_cnt)
