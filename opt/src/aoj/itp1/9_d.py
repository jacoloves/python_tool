s = list(input())
q = int(input())

for _ in range(q):
    tmp_list=list(map(str, input().split()))
    input_list=[]

    for i in range(len(tmp_list)):
        if i == 1 or i == 2:
            input_list.append(int(tmp_list[i]))
        else:
            input_list.append(tmp_list[i])

    if input_list[0] == 'replace':
        s[input_list[1]:input_list[2]+1] = input_list[3]
    elif input_list[0] == 'reverse':
        tmp_list2=[]
        for i in range(input_list[1], input_list[2]+1):
            tmp_list2.append(s[i])
        rev_list = list(reversed(tmp_list2))
        rev_cnt = 0
        for i in range(input_list[1], input_list[2]+1):
            s[i] = rev_list[rev_cnt]
            rev_cnt += 1
    elif input_list[0] == 'print':
        for i in range(input_list[1], input_list[2]+1):
            print(s[i],end="")
        print("")

