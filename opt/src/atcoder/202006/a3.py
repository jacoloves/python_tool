
def main():
    str = input()
    str2 = input()

    err_flg = 0

    for i in range(len(str)):
        if (str[i] != str2[i]):
            err_flg = 1
            break

    if err_flg == 1:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()