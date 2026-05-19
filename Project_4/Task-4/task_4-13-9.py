n = int(input("Введите размер массива: "))
a = []
for i in range(n):
    a.append(int(input(f"Введите элемент {i+1}: ")))

sum = 0
i = 0

while i < n:
    if a[i] % 2 != 0:
        sum = sum + a[i]
    i = i + 1

print("Сумма нечётных элементов:", sum)