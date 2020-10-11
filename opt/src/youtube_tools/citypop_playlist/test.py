f = open('apikey.txt', 'r', encoding='UTF-8')

data = ""

while True:
    data = f.readline()
    break

print(data)