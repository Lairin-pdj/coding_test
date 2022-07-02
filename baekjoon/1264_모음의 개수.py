import sys
input = sys.stdin.readline

# 파싱
while True:
    line = input().rstrip().lower()
    
    # 탈출
    if line == "#":
        break
    
    # 계산
    count = 0
    for i in line:
        if i in ('a', 'e', 'i', 'o', 'u'):
            count += 1
    
    # 출력
    print(count)
