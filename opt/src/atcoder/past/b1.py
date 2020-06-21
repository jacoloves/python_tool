
def main():
    num = int(input())
    str = input()

    array = []

    for i in range(len(str)):
        change_str = ord(str[i])
        over_num = change_str +  num
        if (over_num > 90):
            over_num = over_num - 90 + 64
        
        array.append(chr(over_num))
    
    str2 = ''.join(array)
    print(str2)

if __name__ == "__main__":
    main()