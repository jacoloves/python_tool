def main():
    a, b, c, d = map(int, input().split())
    sum = 0

    while True:
        if (a < d):
            sum = a
            d -= a
        else:
            sum = d
            break

        if (b < d):
            d -= b
        else:
            break
        sum -= d
        break

    print(sum)


if __name__ == "__main__":
    main()
