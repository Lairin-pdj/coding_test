from collections import defaultdict
import sys, re
input = sys.stdin.readline

# 파싱
n = int(input())
for t in range(n):
    l = int(input())
    line = ""
    for _ in range(l):
        line += input().rstrip()
    
    # 문자열 처리
    line = re.sub(" ", "", line)
    record, stack, names = [], [], []
    link = defaultdict(list)
    i = 0
    while i < len(line):
        if line[i] == "(":
            stack.append(i)
        elif line[i] == ")":
            temp = stack.pop()
            
            # 파싱
            part = line[temp + 1:i]
            num = re.sub("[a-z]+", "", part)
            name = re.sub("[0-9\.]+", "", part)
            
            if name != "":
                record.append(name)
                
                # 순서 체킹
                for _ in range(2):
                    link[name].append(names.pop()[0])
                names.append((name, len(stack)))
                
            # 빈 공간을 알리는 blank 처리
            else:
                record.append("blank")
                names.append(("blank", len(stack)))
                
            record.append(num)

            # 문자열 정리
            line = line[:temp] + line[i + 1:]
            i = temp - 1
        
        i += 1
    
    # 값 연결
    case = defaultdict(list)
    stack = []
    for i in record:
        # 문자
        if i.isalpha():
            if i != "blank":
                for _ in range(2):
                    case[i].append(stack.pop())
 
        # 숫자
        else:
            stack.append(float(i))
    
    # 쿼리 진행
    a = int(input())
    print("Case #" + str(t + 1) + ":")
    for _ in range(a):
        query = input().rstrip().split()
        answer = stack[0]
        temp = names[0][0]
        while True:
            # 탈출
            if temp == "blank":
                break
            
            else:
                if temp in query[2:]:
                    answer *= case[temp][1]
                    temp = link[temp][1]
                else:
                    answer *= case[temp][0]
                    temp = link[temp][0]
        
        # 결과 출력
        print(format(answer, ".7f"))
