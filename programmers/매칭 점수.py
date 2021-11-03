import re

def solution(word, pages):
    answer = 0
    dic = {}
    urllist = []
    word = word.lower()
    for i in pages:                                                 # 페이지 마다 분석
        url = ""
        score = 0
        link = []
        
        headstart = i.find("<head>")                                # 헤드 부분에서 url 추출
        headend = i.find("</head>")
        head = i[headstart + 7:headend]
        line = head.split("\n")
        for j in line:
            urlpos = j.find("<meta property=\"og:url\" content=")
            if urlpos != -1:
                url = j[43:-3]
        urllist.append(url)
                
        bodystart = i.find("<body>")                                # 바디에서 문구 추출
        bodyend = i.find("</body>")
        body = i[bodystart + 7:bodyend]
        
        body = body.lower()                                         # 스코어 계산
        line = re.split("[^a-z]", body)
        for j in line:
            if j == word:
                score += 1
        
        line = body.split("<a href=\"")                             # 링크 체크
        for j in line:
            if not j.find("https"):
                k = j.split("\"")
                link.append(k[0][8:])
        
        if not url in dic:                                          # 사전을 통한 점수 관리
            dic[url] = score
        else:
            dic[url] = dic[url] + score
        for j in link:
            if not j in dic:
                dic[j] = score / len(link)
            else:
                dic[j] = dic[j] + (score / len(link))
    
    temp = 0
    for i, x in enumerate(urllist):
        if temp < dic[x]:
            temp = dic[x]
            answer = i

    return answer
