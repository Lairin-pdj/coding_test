import sys
input = sys.stdin.readline

# 파싱
n, l = map(int, input().split())

# 계산
low = ((l - 1) * l) / 2
while True:
    
    # 이미 초과한 경우 
    if low > n or l > 100:
        print(-1)
        break
    else:
        low += l
    
    # 홀수
    if l % 2 != 0:
        # 가능한 경우
        if n % l == 0:
            # 음의 정수가 없다면 출력 후 탈출
            temp = (n // l) - (l // 2)
            if temp >= 0:
                for i in range(l):
                    print(temp + i, end = " ")
                break

    # 짝수
    else:
        # 가능한 경우
        if n % l != 0 and (2 * n) % l == 0:
            # 음의 정수가 없다면 출력 후 탈출
            temp = (n // l) - (l // 2) + 1
            if temp >= 0:
                for i in range(l):
                    print(temp + i, end = " ")
                break
    
    # 불가능한 경우
    l += 1
