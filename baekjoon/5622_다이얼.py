from collections import defaultdict
# 단어 해싱
dic = defaultdict(int)
dic["A"], dic["B"], dic["C"] = 3, 3, 3
dic["D"], dic["E"], dic["F"] = 4, 4, 4
dic["G"], dic["H"], dic["I"] = 5, 5, 5
dic["J"], dic["K"], dic["L"] = 6, 6, 6
dic["M"], dic["N"], dic["O"] = 7, 7, 7
dic["P"], dic["Q"], dic["R"], dic["S"] = 8, 8, 8, 8
dic["T"], dic["U"], dic["V"] = 9, 9, 9
dic["W"], dic["X"], dic["Y"], dic["Z"] = 10, 10, 10, 10

line = input()
count = 0
for i in line:
    count += dic[i]
    
print(count)
