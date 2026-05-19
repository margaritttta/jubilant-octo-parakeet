N = int(input("Введите число N: "))
i = 1
F = 1

while i < N:
    F = F * i
    i = i + 1

print("Факториал:", F)