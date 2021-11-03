import sys
input = sys.stdin.readline

# 파싱
n, k = map(int, input().split(" "))
choco = list(map(int, input().split(" ")))

low = min(choco[:k])

count = 0
total = 0
for i in choco:
    if i > low:
        count += 1
        total += i - low
        
print(total, count)
