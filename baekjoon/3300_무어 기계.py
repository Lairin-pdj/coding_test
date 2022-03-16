import sys, re
input = sys.stdin.readline

# 파싱
t = int(input())
for _ in range(t):
    a = input().rstrip()
    b = input().rstrip()
    
    # 없어도 체크가 되는 경우
    if re.match(a + "$", b):
        print("_")
    else:
        # _에 알파벳 넣으며 체크
        flag = True
        
        for i in range(65, 91):
            target = chr(i)
            trans = re.sub("_", target, a)
            temp = re.match(trans + "$", b)
            
            # 가능하면 체크
            if temp:
                flag = False
                print(target)
                break
    
        # 모두 실패
        if flag:
            print("!")
