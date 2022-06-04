import sys
input = sys.stdin.readline

# 파싱
n, k = map(int, input().split())
line = input().rstrip()

# 그리디
stack = []
count = 0
for i in line:
    temp = int(i)
    
    # 스택 안에 현재 수 보다 작은 수 팝하기
    while stack and count < k:
        if stack[-1] < temp:
            stack.pop()
            count += 1
        else:
            break
    
    stack.append(temp)

# count를 k개로 맞추기
while count != k:
    stack.pop()
    count += 1

# 결과 출력
print("".join(map(str, stack)))
