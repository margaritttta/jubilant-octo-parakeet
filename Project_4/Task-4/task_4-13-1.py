a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))
d = float(input("Введите число d: "))

if a < b:
    min = a
else:
    min = b

if c < min:
    min = c

if d < min:
    min = d

print("Минимальное число:", min)