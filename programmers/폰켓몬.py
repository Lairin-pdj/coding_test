def solution(nums):
    # 중복을 제거하는 집합을 이용하여 갯수 체크
    return min(len(set(nums)), len(nums) / 2)
