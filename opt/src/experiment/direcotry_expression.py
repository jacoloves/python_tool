import os

path = os.getcwd()

test_lis = list(path.split('/'))

sum = ""

for i in range(len(test_lis)):
    str = ''.join(test_lis[i])
    sum += str
    sum += "/"
    print(f'%s' % sum)


print(sum)