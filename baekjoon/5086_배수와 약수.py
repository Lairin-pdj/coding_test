import sys
input = sys.stdin.readline

while True:
    # νμ±
    n, m = map(int, input().split())
    
    # νμΆ
    if n == 0 and m == 0:
        break
    
    # case 1
    if m % n == 0:
        print("factor")
    # case 2
    elif n % m == 0:
        print("multiple")
    # case 3
    else:
        print("neither")
