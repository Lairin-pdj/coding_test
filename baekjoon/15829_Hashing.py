import sys
input = sys.stdin.readline

# 파싱
l = int(input())
string = input().rstrip()

total = 0
ri = 1
r = 31
m = 1234567891
for i in string:
    temp = ord(i) - 96
    
    total += temp * ri
    total = total % m
    
    ri *= r
    ri = ri % m

print(total)
