
def main():
    N, A, B = map(int, input().split())
    ans = N // (A+B)*A
    rem = N % (A+B)
    ans += min(rem, A)
    print(ans)


if __name__ == "__main__":
    main()