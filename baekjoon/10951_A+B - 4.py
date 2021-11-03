import sys

cases = sys.stdin.readlines()

for case in cases:
    a, b = map(int, case.split(" "))
    print(a + b)
