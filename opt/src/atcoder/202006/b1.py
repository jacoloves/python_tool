
def main():
    a = input()
    array = list(map(int, input().split()))

    sum = 1

    new_array = sorted(array)
    for i in range(len(new_array)):
        sum *= new_array[i]
        if (sum > 10**18 or sum == 0):
            break

    if (sum > 10**18):
        sum = -1

    print(sum)

if __name__ == "__main__":
    main()