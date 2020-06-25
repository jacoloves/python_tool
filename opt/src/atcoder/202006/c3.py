import math

def main():
    a, b, c, d = map(int, input().split())

    rad = 2 * math.pi * (((c / 12) + (12 * (d / 60))) - (d / 60))

    if math.cos(rad) == 1:
        print(abs(a-b))
    elif math.cos(rad) == -1:
        print(a + b)
    else:
        print(math.sqrt(a**2 + b**2 - 2*a*b*math.cos(rad)))


if __name__ == "__main__":
    main()