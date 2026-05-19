N = int(input("Введите N: "))
i = 1
max = float(input("Введите max: "))

while i < N:
    x = float(input("Введите x: "))
    if x > max:
        max = x
    i = i + 1

print("Максимальное значение:", max)