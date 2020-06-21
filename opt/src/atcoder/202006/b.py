
def main():
    X, Y = map(int, input().split())
    ans = 'No'

    for a in range(X+1):
        b = X - a
        if 2 * a + 4 * b == Y:
            ans = 'Yes'

    print(ans)


if __name__ == "__main__":
    main()