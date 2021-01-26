a = list(map(str, input().split()))

R = False
L = False
winner = ""

for i in range(len(a)):
    if a[i] == "RU" and R == False:
        R = True
    elif a[i] == "RU" and R == True:
        winner = "Alice"
        break
    elif a[i] == "RD" and R == False:
        winner = "Alice"
        break
    elif a[i] == "RD" and R == True:
        R = False

    if a[i] == "WU" and L == False:
        L = True
    elif a[i] == "WU" and L == True:
        winner = "Alice"
        break
    elif a[i] == "WD" and L == False:
        winner = "Alice"
        break
    elif a[i] == "WD" and L == True:
        L = False

if winner == "Alice":
    print(winner)
else:
    print("Simon")
    if R == True and L == True:
        print("UU")
    elif R == True and L == False:
        print("UD")
    elif R == False and L == True:
        print("DU")
    elif R == False and L == False:
        print("DD")
