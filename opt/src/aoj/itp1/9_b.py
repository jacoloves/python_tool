ans_arr=[]
while True:
    s = input()
    if s == '-':
        break
    m = int(input())
    
    rep_text = s
    for _ in range(m):
        h = int(input())
        text1 = ''
        text2 = ''
        tmp_text = ''
        for i in range(h):
            text1 += rep_text[i]
        for j in range(h, len(rep_text)):
            text2 += rep_text[j]
        tmp_text += text2
        tmp_text += text1
        rep_text = tmp_text
    ans_arr.append(rep_text)

for i in range(len(ans_arr)):
    print(ans_arr[i])
    
