check = set()

for _ in range(10):
    n = int(input())
    
    check.add(n % 42)

print(len(check))
