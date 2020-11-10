a = int(input())
tmp_num = a
cnt = 0
str = ""
if (a % 2) == 0:
    print(-1)
else:
    while True:
        if int(a) == 0:
            break
        a = a / 10
        cnt = cnt + 1
    for i in range(cnt):
        str = str + "7"
    while True:
        str_num = int(str)
        ans_num = str_num / tmp_num
        if ans_num.is_integer():
            break
        else:
            str = str + "7"
            cnt = cnt + 1
    print(cnt)