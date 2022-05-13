import sys
input = sys.stdin.readline

# 파싱
n = int(input())
s = [input().rstrip() for _ in range(n)]

# 문자열 생성
t = ""
i, j = 0, n - 1;
while i <= j:
    
    # 같은 경우
    if s[i] == s[j]:
        # 안쪽 까지 확인 하여 체크
        ti, tj = i + 1, j - 1
        flag = True
        while ti <= tj:
            # 앞이 큰 경우
            if s[ti] > s[tj]:
                t += s[j]
                j -= 1
                flag = False
                break
            # 뒤가 큰 경우
            elif s[ti] < s[tj]:
                t += s[i]
                i += 1
                flag = False
                break
            else:
                ti += 1
                tj -= 1
        
        # 전부 같을 경우
        if flag:
            t += s[i]
            i += 1
            
    # 앞이 큰 경우
    elif s[i] > s[j]:
        t += s[j]
        j -= 1
    # 뒤가 큰 경우
    elif s[i] < s[j]:
        t += s[i]
        i += 1

# 결과 출력
for i in range((len(t) // 80) + 1):
    print(t[i * 80:(i + 1) * 80])
