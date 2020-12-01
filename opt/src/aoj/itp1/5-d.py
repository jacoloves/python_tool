def include3(num2):
    print(num2)
    x = num2 
    if (x % 10 == 3):
        #print(" %d" % num2, end="")
        return
    x /= 10
    if x:
        include3(x)


def check_num(num):
    x = num 
    if (x % 3 == 0):
        #print(" %d" % num, end="")
        return
        
def main():
    n = int(input())
    i = 1
    while True:
        if i > n:
            break
        check_num(i)
        include3(i)
        i += 1
    print("")


if __name__ == "__main__":
    main()
