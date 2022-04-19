import sys
input = sys.stdin.readline
    
# 파싱
n = int(input())
mans = list(map(int, input().split()))
womans = list(map(int, input().split()))

# 분류
lmans, hmans = [], []
for i in mans:
    if i < 0:
        lmans.append(i)
    else:
        hmans.append(i)

lwomans, hwomans = [], []
for i in womans:
    if i < 0:
        lwomans.append(i)
    else:
        hwomans.append(i)

# 정렬
lmans.sort()
hmans.sort(reverse = True)
lwomans.sort()
hwomans.sort(reverse = True)

# 그리디
answer = 0

# 남자가 작은 사람을 찾는 경우
i, j = 0, 0
while i < len(lmans) and j < len(hwomans):
    
    if hwomans[j] < abs(lmans[i]):
        answer += 1
        i += 1
        j += 1
    else:
        j += 1

# 남자가 큰 사람을 찾는 경우
i, j = 0, 0
while i < len(hmans) and j < len(lwomans):
    
    if abs(lwomans[j]) > hmans[i]:
        answer += 1
        i += 1
        j += 1
    else:
        i += 1

# 결과 출력
print(answer)
