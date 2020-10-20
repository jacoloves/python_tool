# window clear

import os
import time

# os.system('clear')

# print()
# print()
# print('           _ _ _ _ _ _ _ _ ')
# print('          |               |')
# print('           - - -      - - -')
# print('               |     |    ')
# print('               |     |    ')
# print('               |     |    ')
# print('               |     |    ')
# print('               |     |    ')
# print('               - - - -    ')


arr = []
# for i in range(10):
#     if i != 0:
#         arr.append(" ")
#         for j in range(i):
#             print(arr[j], end="")

str_main = ""

for i in range(10):
    if i == 0:
        arr.append(i)
        print("\r" + str(arr[0]), end="")
    if i != 0:
        for j in range(i):
            arr.append(" ")
        arr.append(i)
        for j in range(i+1):
            str_main = str_main + str(arr[j])
        print("\r" + str_main, end="")

    str_main= ""
    arr.clear()
    time.sleep(0.3)


# for i in range(10):
#     if i != 0:
#         for j in range(i):
#             arr.append(" ")
#     print("\r" + str(i), end="")
#     time.sleep(1)