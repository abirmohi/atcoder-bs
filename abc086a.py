s = input()
token = s.split()
a = int(token[0])
b = int(token[1])

if (a*b)%2== 0:
    print('Even')
else:
    print('Odd')