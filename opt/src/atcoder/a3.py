def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())

    sum1 = a-c
    sum2 = b-d

    ans = sum1*sum2

    print(ans)


if __name__ == "__main__":
    main()
