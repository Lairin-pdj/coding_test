import sys
input = sys.stdin.readline

# 파싱
n = input().rstrip()
m = input().rstrip()

high = min(len(n), len(m))

# 가능한 경우의 수 set에 저장
check = set()
for j in range(1, high + 1):
    a = [0 for _ in range(26)]
    for i in range(j):
        a[ord(n[i]) - 97] += 1
    check.add(tuple(a))
    
    for i in range(len(n) - j):
        a[ord(n[i]) - 97] -= 1
        a[ord(n[i + j]) - 97] += 1
        check.add(tuple(a))

# 가능한지 체크
answer = 0
flag = False
for j in range(high, -1, -1):
    b = [0 for _ in range(26)]
    for i in range(j):
        b[ord(m[i]) - 97] += 1
    if tuple(b) in check:
        answer = j
        flag = True
    
    if not flag:
        for i in range(len(m) - j):
            b[ord(m[i]) - 97] -= 1
            b[ord(m[i + j]) - 97] += 1
            if tuple(b) in check:
                answer = j
                flag = True
                break
    
    # 탈출
    if flag:
        break

# 결과 출력
print(answer)
