def main():
    str = input()
    num = len(str)/2
    dflg = len(str)%2
    array1=[]
    array2=[]
    
    if dflg == 0:
        for i in range(num):
        	array1.append(str[i])

    print(array1)


if __name__ == "__main__":
    main()
