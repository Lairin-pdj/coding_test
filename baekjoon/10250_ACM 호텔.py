n = int(input())

for _ in range(n):
    h, w, n = map(int, input().split(" "))
    
    floor = (n - 1) % h
    unit = (n - 1) // h
    
    print(str(floor + 1) + str(unit + 1).zfill(2))
