def analyze_scores(*scores): # Функция для анализа баллов команды
    if len(scores) == 0:
        return 0, 0, 0
    sum_s = 0
    for s in scores:
        sum_s = sum_s + s
    count_s = len(scores)
    avg = sum_s / count_s
    return sum_s, count_s, avg
def print_report(team_name, **info): # Функция для вывода отчёта о команде
    print("Команда:", team_name)
    for key in info:
        print(key + ":", info[key])
s1, n1, a1 = analyze_scores(8, 10, 7, 9) # Проверяем для набора (8, 10, 7, 9)
print("Набор (8, 10, 7, 9):")
print("Сумма:", s1)
print("Количество:", n1)
print("Средний балл:", a1)
s2, n2, a2 = analyze_scores(5, 5) # Проверяем для набора (5, 5)
print("Набор (5, 5):")
print("Сумма:", s2)
print("Количество:", n2)
print("Средний балл:", a2)
s3, n3, a3 = analyze_scores() # Проверяем без аргументов
print("Без аргументов:")
print("Сумма:", s3)
print("Количество:", n3)
print("Средний балл:", a3)
print_report("Комета", coach="Крутой", derevna="Сморгонь") # Выводим отчёт для команды "Комета"