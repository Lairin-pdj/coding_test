def solution(a, b):
    # 배열을 이용하여 출력 체크
    text = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # 1월 1일 부터 주어진 날까지 일수 계산
    date = b - 1
    for i in range(a - 1):
        date += month[i]
    
    # 요일로 변환하여 반환
    return text[date % 7]
