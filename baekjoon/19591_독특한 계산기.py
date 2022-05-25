import sys, re
input = sys.stdin.readline

# 파싱
line = input().rstrip()
nums = re.split("[+*-/]", line) 
ops = re.split("[0-9][0-9]*", line)

# 맨앞에 -가 붙는 경우
if nums[0] == '':
    nums.pop(0)
    nums[0] = '-' + nums[0]
    ops[0] = ''

# 숫자 int화
nums = list(map(int, nums))

# 숫자가 1개인 경우
if len(nums) == 1:
    print(nums[0])
else:
    # 연산 우선순위
    order = {'*' : 1, '/' : 1, '+' : 2, '-' : 2}
    
    # 연산 함수
    def calc(a, b, op):
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return int(a / b)
    
        return -1
    
    # 연산 진행
    i, j = 1, len(ops) - 2
    while i < j:
        # 우선순위가 i가 빠른 경우
        if order[ops[i]] < order[ops[j]]:
            nums[i] = calc(nums[i - 1], nums[i], ops[i])
            i += 1
        # 우선순위가 j가 빠른 경우
        elif order[ops[i]] > order[ops[j]]:
            nums[j - 1] = calc(nums[j - 1], nums[j], ops[j])
            j -= 1
        # 우선순위가 같은 경우
        else:
            left = calc(nums[i - 1], nums[i], ops[i])
            right = calc(nums[j - 1], nums[j], ops[j])
            
            # 결과가 i가 큰 경우
            if left > right:
                nums[i] = left
                i += 1
            # 결과가 j가 큰 경우
            elif left < right:
                nums[j - 1] = right
                j -= 1
            # 결과가 같은 경우
            else:
                nums[i] = left
                i += 1

    # 마지막 연산 후 결과 출력
    print(calc(nums[i - 1], nums[i], ops[i]))
