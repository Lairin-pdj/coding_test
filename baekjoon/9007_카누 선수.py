import sys
input = sys.stdin.readline

# 파싱
t = int(input())
for _ in range(t):
    k, n = map(int, input().split())
    student = [list(map(int, input().split())) for _ in range(4)]
    
    # 절반으로 쪼개기
    # left = 1, 2반
    # right = 3, 4반
    left, right = set(), set()
    
    for i in range(n):
        for j in range(n):
            left.add(student[0][i] + student[1][j])
            right.add(student[2][i] + student[3][j])
    
    # 정렬
    left = sorted(list(left))
    right = sorted(list(right))
    
    # 투 포인터
    answer = 1000000000
    i, j = 0, len(right) - 1
    while i < len(left) and j >= 0:
        temp = left[i] + right[j]
        
        # answer에 반영
        if abs(k - answer) > abs(k - temp):
            answer = temp
        elif abs(k - answer) == abs(k - temp):
            answer = min(answer, temp)
        
        # 값에 따른 이동
        if temp > k:
            j -= 1
        elif temp < k:
            i += 1
        else:
            break
    
    # 결과 출력
    print(answer)
