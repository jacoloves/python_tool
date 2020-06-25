import math

def main():
    a, b = map(str, input().split())
    arr = []
    num = int(a)

    arr.append(b[0])
    arr.append(b[2])
    arr.append(b[3])

    dec = int(''.join(arr))

    print((num*dec)//100)





if __name__ == "__main__":
    main()