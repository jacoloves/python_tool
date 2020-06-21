import math

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def Base_10_10_n(X, n):
    array = []
    X_dumy = X
    out = 0
    while X_dumy > 0:
        out = int(math.floor(X_dumy)%n)
        X_dumy = int(math.floor(X_dumy)/n)
        array.append(ALPHABET[out-1])
    out_array = list(reversed(array))
    str = ''.join(out_array)
    return str

def main():
    num = int(input())

    x26 = Base_10_10_n(num, 26)
    print(x26)


if __name__ == "__main__":
    main()
