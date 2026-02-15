dna = input("Введите последовательность ДНК: ")
dna_upper = dna.upper()

count_A = dna_upper.count("A")
count_T = dna_upper.count("T")
count_G = dna_upper.count("G")
count_C = dna_upper.count("C")

total_length = len(dna_upper)

percent_A = (count_A / total_length) * 100
percent_T = (count_T / total_length) * 100
percent_G = (count_G / total_length) * 100
percent_C = (count_C / total_length) * 100

print("===Анализ последовательности ДНК===")
print(f"\nВведите последовательность ДНК: {dna}")
print(f"\nПоследовательность в верхнем регистре: {dna_upper}")
print("\nПодсчёт нуклеотидов:")
print(f"A: {count_A}; {percent_A:.0f}%")
print(f"T: {count_T}; {percent_T:.0f}%")
print(f"G: {count_G}; {percent_G:.0f}%")
print(f"C: {count_C}; {percent_C:.0f}%")