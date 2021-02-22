# Atcoder ABC088B card game for tow

N = int(input())
cards = list(map(int,input().split()))
cards.sort(reverse=True)

alice = 0
bob = 0

for i in range(N):
    if i % 2==0:
        alice += cards[i]
    else:
        bob += cards[i]

print(alice-bob)