import sys
input = sys.stdin.readline

# 파싱
line = input().rstrip()
q = int(input())

# 누적합
lis = [0] * 26 
check = []
for i in range(len(line)):
    lis[ord(line[i]) - 97] += 1
    check.append(lis[:])

# 쿼리 처리
for _ in range(q):
    a, l, r = input().split()
    l, r = int(l), int(r)
    target = ord(a) - 97
    
    if l == 0:
        print(check[r][target])
    else:
        print(check[r][target] - check[l - 1][target])
