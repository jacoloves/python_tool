target_str = input()

change_str = ""
for i in range(len(target_str)):
    if target_str[i].islower():
        change_str += target_str[i].upper()
    elif target_str[i].isupper():
        change_str += target_str[i].lower()
    else:
        change_str += target_str[i]

print(change_str)
