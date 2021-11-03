line = input()

alphabet = [chr(i) for i in range(97, 123)]

for i in alphabet:
    print(line.find(i), end = " ")
