'''
# :7:: 과 같은 케이스 처리 불가 
import sys
input = sys.stdin.readline

# 파싱
adds = input().split(":")
print(adds)
# 복원
answer = ""
for i in range(len(adds)):
    if adds[i] != "":
        answer += adds[i].zfill(4) + ":"
    # '::'이 있는 경우
    else:
        # 맨 앞이 비지 않은 경우만 체크 (빈 경우엔 스킵)
        if (i + 1 < len(adds) and adds[i + 1] != "") or i + 1 == len(adds):
            count = 0
            for j in adds:
                if j != "":
                    count += 1
            for _ in range(8 - count):
                answer += "0000:"

# 결과 출력
print(answer[:-1])
'''
