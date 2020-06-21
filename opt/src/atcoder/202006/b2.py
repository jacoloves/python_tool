
def main():
    cnt = int(input())
    str = input()

    sum_str = []
    sum_cnt = 0
    for i in range(len(str)):
        sum_cnt += 1
        if (sum_cnt > cnt):
            sum_str.append('...')
            break
        sum_str.append(str[i])

    str2 = ''.join(sum_str)

    print(str2)


if __name__ == "__main__":
    main()