import sys
input = sys.stdin.readline

n = int(input())

strings = set()
for _ in range(n):
    strings.add(input().rstrip())

strings = list(strings)
strings.sort(key = lambda x : (len(x), x))

for a in strings:
    print(a)
