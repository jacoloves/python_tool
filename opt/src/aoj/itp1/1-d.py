s = int(input())

h = s // 3600
h_s = s - h * 3600

m = h_s // 60
m_s = h_s - m * 60

print("%d:%d:%d" % (h, m, m_s))
