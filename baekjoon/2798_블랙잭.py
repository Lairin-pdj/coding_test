from itertools import combinations

n, m = map(int, input().split(" "))
cards = list(map(int, input().split(" ")))

high = 0
for card in combinations(cards, 3):
    temp = sum(card)
    if temp <= m:
        high = max(high, temp)

print(high)
