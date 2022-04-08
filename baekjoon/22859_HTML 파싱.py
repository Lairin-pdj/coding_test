import sys, re
input = sys.stdin.readline
    
# 파싱
html = input().rstrip()

# div 분리
for div in re.split("</div>", html[6:-7]):
    if div != "":

        # 제목 추출
        front = div.find("\"")
        back = div.find("\"", front + 1)
        print("title :", div[front + 1:back])
        
        div = div[div.find(">") + 1:]
    
        # p 분리
        for p in re.split("</p>", div):
            if p != "":
                
                # 태그 제거
                p = re.sub("<[^>]+>", "", p)
                
                # 공백처리
                p = re.sub("(  )( )*", " ", p.strip())
                
                # 문장 출력
                print(p)
