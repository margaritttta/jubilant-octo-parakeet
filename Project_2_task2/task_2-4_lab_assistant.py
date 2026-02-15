volume_of_solution = float(input("Укажите объем раствора (мл): ")) 
volume_of_water = volume_of_solution

salt_mass = volume_of_solution * 0.009
salt_mass_round = round(salt_mass, 2)

with open("recipe.txt", "w", encoding="utf-8") as file:    
    file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
    file.write("-" * 23 + "\n")
    file.write(f"Общий объем: {volume} мл\n")
    file.write(f"Масса соли:  {salt_mass_rounded} г\n")
    file.write(f"Объем воды:  {water_volume} мл\n")

    print("Отчет сохранен в файле recipe.txt")