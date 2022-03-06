import sys
input = sys.stdin.readline

# 파싱
n, m = map(int, input().split())
mind = [0] * m
birds = []
for _ in range(n):
    d, sound = input().rstrip().split()
    
    if d == "L":
        temp = -1
    else:
        temp = 1
        
    birds.append((temp, sound))
    
    for i in range(m):
        if sound[i] == "1":
            mind[i] += temp

# 새를 한마리씩 제외해가며 체크
answer = 0
con = 1000000000
for i in range(n):
    high = 0
    temp = 0
    for j in range(m):
        temp += mind[j] - (birds[i][0] * int(birds[i][1][j]))
        high = max(high, abs(temp))

    if high < con:
        con = high
        answer = i + 1

# 결과 출력
print(answer)
print(con)
