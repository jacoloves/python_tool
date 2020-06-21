
def main():
    a = int(input())


    if a > 100:
        a = a % 100

    if a > 10:
        a = a % 10

    if a in [2, 4, 5, 7, 9]:
        print('hon')
    elif a in [0, 1, 6, 8]:
        print('pon')
    else:
        print('bon')



if __name__ == "__main__":
    main()