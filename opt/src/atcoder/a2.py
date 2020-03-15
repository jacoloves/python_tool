
def main():
    a, b = map(int, input().split())
    str = input()

    array = []

    for i in range(len(str)):
        if (i+1 == b):
            array.append(str[i].lower())
        else:
            array.append(str[i])

    str2 = ''.join(array)
    print(str2)

if __name__ == "__main__":
    main()