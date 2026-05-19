N = int(input("Введите число N: "))

i = 1
sum = 0

while i <= N:
    sum = sum + i  
    i = i + 1     

print("Сумма первых", N, "натуральных чисел равна:", sum)