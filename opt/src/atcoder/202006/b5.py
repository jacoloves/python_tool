import math

def main():
    a, b = map(int, input().split())
    array = []
    for _ in range(b):
        c = int(input())
        d = list(map(int, input().split()))
        array = array + d

    print(a - len(set(array)))





if __name__ == "__main__":
    main()