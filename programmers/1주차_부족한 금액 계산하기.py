def solution(price, money, count):

    return max(0, ((((1 + count) * count) / 2) * price) - money)
