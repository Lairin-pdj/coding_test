import sys
input = sys.stdin.readline

# 파싱
for _ in range(3):
    a = int(input())
    total = 0
    for _ in range(a):
        total += int(input())
    
    # 결과 출력
    if total > 0:
        print("+")
    elif total < 0:
        print("-")
    else:
        print(0)
