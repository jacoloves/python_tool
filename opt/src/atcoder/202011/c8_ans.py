n = int(input())

divs = []

for d in range(1, n+1):
    if d * d > n: break
    if n % d == 0:
        divs.append(d)
        if n // d != d:
            divs.append(n // d)

for div in sorted(divs):
    print(div)
