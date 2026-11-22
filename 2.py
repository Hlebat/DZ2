def ticket_total(count, price=12): # считаем общую стоимость билетов без скидки
    return count * price
def final_price(count, is_school_group=False): # считаем стоимость со скидкой для школьной группы
    total = ticket_total(count)
    if is_school_group == True:
        total = total * 0.75
    return total
result1 = final_price(3) # Случай, когда 3 обычных билета
print("3 обычных билета:", result1, "руб.")
result2 = final_price(4, is_school_group=True) # Случай, когда 4 билета для школьной группы
print("4 билета для школьной группы:", result2, "руб.")
result3 = ticket_total(2, price=15) # Случай, когда 2 билета по 15 рублей
print("2 билета по 15 рублей:", result3, "руб.")