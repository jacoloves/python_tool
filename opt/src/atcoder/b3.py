def main():
    str = input()
    YY = []
    MM = []
    YYMM_flg = False
    MMYY_flg = False
    AMB_flg = False
    NA_flg = False

    for i in range(2):
    	YY.append(str[i])

    for i in range(2, 4):
    	MM.append(str[i])

    yy = int(''.join(YY))
    mm = int(''.join(MM))

    if (yy >= 1 and yy <= 12) and (mm >= 1 and mm <= 12):
    	AMB_flg = True
    elif (mm >= 1 and mm <= 12) and (yy != 0 or mm != 0):
    	YYMM_flg = True
    elif (yy >= 1 and yy <= 12) and (yy != 0 or mm != 0):
    	MMYY_flg = True
    else:
    	NA_flg = True

    if AMB_flg:
    	print("AMBIGUOUS")
    elif YYMM_flg:
    	print("YYMM")
    elif MMYY_flg:
    	print("MMYY")
    elif NA_flg:
    	print("NA")


if __name__ == "__main__":
    main()
