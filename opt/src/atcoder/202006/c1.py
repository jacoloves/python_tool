import math


def main():
    a, b = map(int, input().split())
    array = list(map(int, input().split()))

    cnt = 1
    ans = 0
    array2 = []
    zero_flg = 0

    if len(array) != 0:
        for i in range(len(array)):
            if a == array[i]:
                zero_flg = 1

    if zero_flg == 0:
        ans = a
    else:
        if ans == 0:
            while True:
                for i in range(len(array)):
                    if (a + cnt == array[i]) or (a - cnt == array[i]):
                        array2.append(array[i])
                if len(array2) != 2:
                    break
                cnt += 1
                array2.clear()

        if len(array2) == 0:
            if a + cnt < a - cnt:
                ans = a + cnt
            else:
                ans = a - cnt
        elif len(array2) == 1:
            if array2[0] == a + cnt:
                ans = a - cnt
            else:
                ans = a + cnt

    print(ans)


if __name__ == "__main__":
    main()
