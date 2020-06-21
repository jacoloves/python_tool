
def main():
    a, b, c = map(int, input().split())
    array = list(map(int, input().split()))
    
    # 多重リスト
    multi_list = [list(map(int, input().split())) for _ in range(a)]

    cnt = 0

    for i in range(a):
        sum = 0
        for j in range(b):
            sum += multi_list[i][j] * array[j]
        if sum + c > 0:
            cnt += 1


    print(cnt)


if __name__ == "__main__":
    main()