import sys
input = sys.stdin.readline

# 파싱
dance = []
for _ in range(5):
    dance.append(input().rstrip())

final = []
for i in list(map(list, zip(*dance))):
    if i == ['.', 'o', 'm', 'l', 'n']:
        final.append(['o', 'w', 'l', 'n', '.'])
    elif i == ['o', 'w', 'l', 'n', '.']:
        final.append(['.', 'o', 'm', 'l', 'n'])
    else:
        final.append(['.', '.', 'o', 'L', 'n'])
        

for i in list(map(lambda x : "".join(x), zip(*final))):
    print(i)
