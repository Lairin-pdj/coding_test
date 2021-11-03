import sys
input = sys.stdin.readline

def track(n, count, route):
    if count == 0:
        print(" ".join(map(str, route)))
    else:
        for i in range(1, n + 1):
            track(n, count - 1, route + [i])

n, count = map(int, input().split(" "))

track(n, count, [])
