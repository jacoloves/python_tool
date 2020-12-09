import re

s = input()
p = input()

cnt = len(p)

start_line = len(s) - cnt

match_flg = False

if s[0] == s[-1] and (p in s):
    match_flg = True
elif re.search(p, s):
    match_flg = True


if match_flg == False:
    while True:
        p_arr_cnt = 0
        for a in range(start_line, len(s)):
            if s[a] == p[p_arr_cnt]:
                p_arr_cnt += 1
            else:
                p_arr_cnt = 0
        if p_arr_cnt != 0:
            for b in range(len(s)):
                if s[b] == p[p_arr_cnt]:
                    p_arr_cnt += 1
                    if p_arr_cnt == len(p):
                        match_flg = True
                        break
                else:
                    break
        if start_line == len(s):
            break
        else:
            start_line += 1


if match_flg:
    print("Yes")
else:
    print("No")
