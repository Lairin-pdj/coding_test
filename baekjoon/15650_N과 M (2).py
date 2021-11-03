import sys
input = sys.stdin.readline
from itertools import combinations

n, count = map(int, input().split(" "))

array = [str(i) for i in range(1, n + 1)]

for i in combinations(array, count):
    print(" ".join(i))
