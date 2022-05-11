n = input()
print(int(n) == sum([int(i) ** len(n) for i in n]))