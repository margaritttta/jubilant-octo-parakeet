number_of_capsules = int(input("Введите общее кол-во произведенных капсул: "))
cepacity = int(input("Укажите  вместимость одной упаковки (шт): "))

full_packages = number_of_capsules // cepacity

remaining_capsules = number_of_capsules % cepacity

print("---Отчет фасовочного цеха---")
print(f"Полных упаковок:\t{full_packages}")
print(f"Остаток капсул:\t\t{remaining_capsules}")