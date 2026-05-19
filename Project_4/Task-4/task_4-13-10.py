n = int(input("Введите размер массива: "))
a = []
for i in range(n):
    a.append(int(input(f"Введите элемент {i+1}: ")))

sum = 0
i = 1

while i < n:
    sum = sum + a[i]
    i = i + 2

print("Сумма элементов с нечётными индексами:", sum)