def main():
    a = int(input())
    ans = ''

    for i in range(1, 99):
        if a <= 26 ** i:
            a -= 1
            for j in range(i):
                ans += chr(ord('a') + a % 26)
                a //= 26
            break
        else:
            a -= 26 ** i
    print(ans[::-1])


if __name__ == "__main__":
    main()