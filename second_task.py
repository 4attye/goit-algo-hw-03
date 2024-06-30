import random


def get_numbers_ticket(min_num, max_num, quantity):
    # Перевірка валідності вхідних параметрів
    if not (1 <= min_num <= max_num <= 1000) or quantity >= max_num or quantity <= 0:
        return []
    # Генеруємо унікальні випадкові числа
    random_numbers = set()
    while len(random_numbers) < quantity:
        random_numbers.add(random.randint(min_num, max_num))
    # Повертаємо відсортований список
    return sorted(random_numbers)



lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
