def main():
    str = input()
    num = int(len(str)/2)
    dflg = int(len(str)%2)
    array1=[]
    array2=[]
    
    if dflg == 0:
        for i in range(num):
        	array1.append(str[i])
        for i in range(num, len(str)):
            array2.append(str[i])
    else:
        for i in range(num):
            array1.append(str[i])
        for i in range(num+1, len(str)):
            array2.append(str[i])

    cnt = 0
    rev_array = array1[::-1]

    for i in range(num):
        if rev_array[i] != array2[i]:
            cnt = cnt+1
    
    print(cnt)

if __name__ == "__main__":
    main()
