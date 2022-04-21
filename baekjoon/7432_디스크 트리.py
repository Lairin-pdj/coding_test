from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(300000)

# 파싱
n = int(input())
dic = defaultdict(set)
for _ in range(n):
    line = input().rstrip().split("\\");
    
    # 시작 디렉토리 체크
    dic[("", -1)].add(line[0])
    
    # 디렉토리를 통채로 키로 사용
    temp = ""
    for i in range(len(line) - 1):
        if i != 0:
            temp += "\\"
        temp += line[i]
        dic[(temp, i)].add(line[i + 1])

# dfs
def dfs(name, target, depth):
    # 들여쓰기 조정
    if depth != -1:
        print((" " * depth) + target)

    if (name, depth) in dic:
        temp = list(dic[(name, depth)])
        temp.sort()
        
        if depth != -1:
            name += "\\"
            
        for i in temp:
            dfs(name + i, i, depth + 1)

# 결과 출력
dfs("", "", -1)
