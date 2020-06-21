
def main():
    a, b, c = map(int, input().split())
    sum = a+b+c

    if (sum <=  21):
        print("win")
    elif(sum >= 22):
        print("bust")

if __name__ == "__main__":
    main()