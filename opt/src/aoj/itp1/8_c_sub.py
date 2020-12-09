alpha = 'abcdefghijklmnopqrstuvwxyz'
text = ''

while True:
    try:
        text += input().lower()
    except EOFError:
        break

for a in alpha:
    print('{} : {}'.format(a, text.count(a)))
