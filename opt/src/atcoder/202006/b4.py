def main():
    a, b = map(int, input().split())
    array = list(map(int, input().split()))

    new_array = sorted(array)
    sum  = 0
    for i in range(b):
        sum += new_array[i]

    print(sum)


if __name__ == "__main__":
    main()