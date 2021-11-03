import sys
input = sys.stdin.readline

n = int(input())

mans = []
for i in range(n):
    a, b = input().rstrip().split(" ")
    mans.append([int(a), b, i])

mans.sort(key = lambda x : (x[0], x[2]))

for a, b, c in mans:
    print(a, b)
