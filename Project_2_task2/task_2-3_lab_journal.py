researcher_name = input("Введите ФИО исследователя: ")
date = input("Введите дату: ")
experiment_name = input("Введите название эксперимента: ")
conclusion = input("Введите вывод эксперимента: ")

with open('journal.txt', 'w', encoding='utf-8') as file:
    file.write(f"|ФИО исследователя: \t|{researcher_name}/\t\n")
    file.write(f"|Дата: \t|{date}/\t\n")
    file.write(f"|Название эксперимента: \t|{experiment_name}/\t\n")
    file.write(f"|Вывод: \t|{conclusion}/\t\n")

print("Данные успешно записаны в файл journal.txt!")