def solution(n, build_frame):
    ans = []
    
    for x, y, build_type, con in build_frame:
        # 설치
        if con == 1:
            # 가능한지 확인
            if build_type == 0:
                # 아래 기둥이 있거나, 오른쪽에 보가 있거나, 왼쪽에 보가 있는 경우가 아닌 경우 설치 불가
                if not ([x, y - 1, 0] in ans or [x, y, 1] in ans or [x - 1, y, 1] in ans):
                    # 바닥이라면 상관없이 설치
                    if y != 0:
                        continue
            else: 
                # 왼쪽 기둥이 있거나, 오른쪽 기둥이 있거나, 양 옆 보가 있는 경우가 아닌 경우 설치 불가
                if not ([x, y - 1, 0] in ans or [x + 1, y - 1, 0] in ans or ([x - 1, y, 1] in ans and [x + 1, y, 1] in ans)):
                    continue
            
            # 결과에 추가
            ans.append([x, y, build_type])
            
        # 철거
        else:
            # 가능한지 확인
            if build_type == 0:
                # 바로 위 기둥 체크
                if [x, y + 1, 0] in ans:
                    # 왼쪽 보, 오른쪽 보가 둘 다 없으면 불가
                    if not([x, y + 1, 1] in ans or [x - 1, y + 1, 1] in ans):
                        continue
                
                # 왼쪽 보 체크
                if [x - 1, y + 1, 1] in ans:
                    # 왼쪽 보를 지지해줄 왼쪽 기둥이나 양 옆 보가 없으면 불가
                    if not([x - 1, y, 0] in ans or ([x - 2, y + 1, 1] in ans and [x, y + 1, 1] in ans)):
                        continue
                
                # 오른쪽 보 체크
                if [x, y + 1, 1] in ans:
                    # 오른쪽 보를 지지해줄 오른쪽 기둥이나 양 옆 보가 없으면 불가 
                    if not([x + 1, y, 0] in ans or ([x - 1, y + 1, 1] in ans and [x + 1, y + 1, 1] in ans)):
                        continue
                    
            else:
                # 왼쪽 기둥 체크 
                if [x, y, 0] in ans:
                    # 아래 기둥이나 왼쪽 보가 둘 다 없는 경우 불가
                    if not([x, y - 1, 0] in ans or [x - 1, y, 1] in ans):
                        continue
                            
                # 오른쪽 기둥 체크
                if [x + 1, y, 0] in ans:
                    # 아래 기둥이나 오른쪽 보가 둘 다 없는 경우 불가
                    if not([x + 1, y - 1, 0] in ans or [x + 1, y, 1] in ans):
                        continue
                
                # 왼쪽 보 체크
                if [x - 1, y, 1] in ans:
                    # 밑에 기둥이 없으면 불가
                    if not([x - 1, y - 1, 0] in ans or [x, y - 1, 0] in ans):
                        continue
                
                # 오른쪽 보 체크
                if [x + 1, y, 1] in ans:
                    # 밑에 기둥이 없으면 불가
                    if not([x + 1, y - 1, 0] in ans or [x + 2, y - 1, 0] in ans):
                        continue
            
            # 결과에서 제거
            ans.pop(ans.index([x, y, build_type]))
            
    # 결과물 정렬
    ans.sort(key = lambda x : (x[0], x[1], x[2]))
        
    return ans
