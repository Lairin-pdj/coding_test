n = int(input())

for _ in range(n):
    line = input()
    score = 0
    count = 1
    for i in line:
        if i == "O":
            score += count
            count += 1
        else:
            count = 1
        
    print(score)
