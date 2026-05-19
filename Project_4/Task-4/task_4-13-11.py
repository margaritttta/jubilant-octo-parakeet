n = int(input("Введите размер массива: "))
a = []
for i in range(n):
    a.append(int(input(f"Введите элемент {i+1}: ")))

sum = 0
count = 0
i = 0

while i < n:
    if i % 2 == 0:
        sum = sum + a[i]
        count = count + 1
    i = i + 1

average = sum / count
print("Среднее арифметическое элементов с чётными индексами:", average)