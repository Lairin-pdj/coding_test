import re

n, m = map(int, input().split(" "))

# 체스판 입력
lines = []
for _ in range(n):
    line = input()
    line = re.sub("W", "0", line)
    line = re.sub("B", "1", line)
    lines.append(line)

# 가능한 체스판 2종류
chess = [["01010101", "10101010"] * 4, ["10101010", "01010101"] * 4]
# 최저값 체크용
low = 64

# 각 체스판 별로
for k in range(2):
    # i, j에서 시작하는 체스판으로 체크
    for i in range(n - 8 + 1):
        for j in range(m - 8 + 1):
            # 비트 마스킹을 통해 차이나는 갯수 확인
            count = 0
            for l in range(8):
                count += sum(list(map(int, str(bin(int(chess[k][l], 2) ^ int(lines[i + l][j:j + 8], 2)))[2:])))
            # 최저값 저장
            low = min(low, count)

# 결과값 출력
print(low)
