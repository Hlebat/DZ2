def average_grade(a, b, c): # Функция для расчета среднего балла
    result = (a + b + c) / 3
    return result
def grade_message(avg): # Функция для вывода сообщения в зависимости от балла
    if avg >= 4.5:
        return "Отлично"
    elif avg >= 3.5:
        return "Хорошо"
    else:
        return "Нужно повторить материал"
g1 = 5 # Первый набор оценок: 5, 4, 5
g2 = 4
g3 = 5
mid1 = average_grade(g1, g2, g3)
msg1 = grade_message(mid1)
print("Оценки:", g1, g2, g3)
print("Средний балл:", round(mid1, 2))
print("Сообщение:", msg1)
g1 = 3 # Второй набор оценок: 3, 4, 3
g2 = 4
g3 = 3
mid2 = average_grade(g1, g2, g3)
msg2 = grade_message(mid2)
print("Оценки:", g1, g2, g3)
print("Средний балл:", round(mid2, 2))
print("Сообщение:", msg2)