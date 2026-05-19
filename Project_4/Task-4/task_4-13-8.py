n = int(input("Введите размер массива: "))
a = []
for i in range(n):
    a.append(float(input(f"Введите элемент {i+1}: ")))

count = 0
i = 0

while i < n:
    if a[i] > 0:
        count = count + 1
    i = i + 1

print("Количество положительных чисел:", count)