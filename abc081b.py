'''
s = input()
token = s.split()

num_list = [] # empty list
while token:
    num_list.append(int(token.pop(0))) #take 1st element and convert to int
'''
size = int(input())
num_list = list(map(int, input().split()))

num_div = 0
all_even = True
while all_even:
    for i in range(size):
        if num_list[i]%2 == 1: # if element is odd number?
            all_even = False
            break
        else:
            num_list[i] //= 2
    if all_even:
        num_div +=1
print(num_div)