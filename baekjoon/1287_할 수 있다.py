import sys, re
input = sys.stdin.readline

# 파싱
line = input().rstrip()
flag = False

# 괄호가 이상하거나 부호 갯수가 이상한 경우
num = len(re.findall("[0-9]+", line))
op = len(re.findall("[*/+-]", line))
if num - 1 == op and line.count("(") == line.count(")"):
    flag = True

if flag:
    # / 를 // 로 변경
    line = re.sub("/", "//", line)
    try:
        print(int(eval(line)))
    except:
        print("ROCK")
else:
    print("ROCK")
