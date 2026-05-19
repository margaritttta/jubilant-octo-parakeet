n = int(input("Введите размер массива: "))
a = []
for i in range(n):
    a.append(float(input(f"Введите элемент {i+1}: ")))

i = 0
sum = 0

while i < n:
    sum = sum + a[i]
    i = i + 1

average = sum / n
print("Среднее арифметическое:", average)