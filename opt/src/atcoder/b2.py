
def main():
    a, b, c = map(int, input().split())
    array = [input()]
    
    # 多重リスト
    multi_list = [[input()] for _ in range(a)]

    print(array)
    print(multi_list)



if __name__ == "__main__":
    main()