'''
# case 1
import sys
input = sys.stdin.readline

# 파싱
adds = input().rstrip().split(":")
count = 0
for i in range(1, len(adds) - 1):
    if adds[i] != "":
        count += 1

# 복원
answer = ""

# 앞 처리
if adds[0] == "":
    answer += "0000:"
else:
    answer += adds[0].zfill(4) + ":"

# 중간 처리
for i in range(1, len(adds) - 1):
    if adds[i] != "":
        answer += adds[i].zfill(4) + ":"
    else:
        for _ in range(6 - count):
            answer += "0000:"

# 끝 처리
if adds[-1] == "":
    answer += "0000"
else:
    answer += adds[-1].zfill(4)

# 결과 출력
print(answer)
'''

'''
# case 2
import sys
input = sys.stdin.readline

# 파싱
adds = input().rstrip().split(":")

# 복원
answer = ""
for i in range(len(adds)):
    if adds[i] != "":
        answer += adds[i].zfill(4) + ":"
    # '::'이 있는 경우
    else:
        # 연속 빈칸인 경우 스킵, 마지막일 경우 체크
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
