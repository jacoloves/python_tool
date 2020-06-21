
def main():
    array = list(map(int, input().split()))


    for i in range(len(array)):
        if array[i] == 0:
            cnt = i + 1

    print(cnt)



if __name__ == "__main__":
    main()