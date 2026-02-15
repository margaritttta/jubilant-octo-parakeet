weight= float(input("Введите ваш вес (кг): ")) 
height = float(input("Введите ваш рост (м): ")) 

bmi = weight / (height ** 2) 

print("---Отчет о состоянии здоровья---") 
print(f"Рост:\t{height} м") 
print(f"Вес:\t{weight} кг") 
print(f"Индекс массы тела:\t{bmi:.2f}") 