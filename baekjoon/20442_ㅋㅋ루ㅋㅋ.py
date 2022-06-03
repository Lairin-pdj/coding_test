import sys
input = sys.stdin.readline

# 파싱
string = input().rstrip()

# 갯수 체크
r = 0
for char in string:
    if char == "R":
        r += 1

# 투포인터
answer = r
k = 0
i, j = 0, len(string) - 1

while i < j:
    # 양 옆에서 k를 찾을 때까지 이동
    while string[i] != "K":
        i += 1
        r -= 1
    while string[j] != "K":
        j -= 1
        r -= 1
        
    # 탈출 
    if r == 0:
        break
    
    # k를 선택하고 안의 r 갯수로 값 갱신 
    if i < j:
        k += 2
        answer = max(answer, k + r)
        i += 1
        j -= 1

# 최대 결과 출력
print(answer)
