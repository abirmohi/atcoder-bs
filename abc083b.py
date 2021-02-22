# Atcode ABC083B

def sum_digit(num):
    '''
    num: integer
    return: sum of each digit
    '''
    total = 0
    while num > 0:
        total += num % 10
        num = num // 10
    return total


N,A,B = map(int,input().split())

g_total = 0
for num in range(1,N+1):
    if A <= sum_digit(num) and sum_digit(num) <= B:
        g_total += num
print(g_total)