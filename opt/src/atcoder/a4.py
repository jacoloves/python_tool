def main():
    a, b = map(int, input().split())

    sum_eve = (a * (a-1))/2
    sum_odd = (b * (b-1))/2

    print(int(sum_eve + sum_odd))


if __name__ == "__main__":
    main()