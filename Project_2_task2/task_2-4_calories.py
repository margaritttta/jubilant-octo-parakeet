proteins = int(input("Введите массу белков в продукте: "))
fats = int(input("Введите массу жиров в продукте: "))
carbohydrates = int(input("Введите массу углеводов в продукте: "))

calories = ( proteins * 4) + (fats * 9) + (carbohydrates * 4)

print(calories)