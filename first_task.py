from datetime import datetime

# Введення дати
entered_date = input("Enter a date YYYY-MM-DD:")


def get_days_from_today(given_date):
    while True:
        try:
            # Перетворення рядка дати у форматі 'YYYY-MM-DD'
            given_date = datetime.strptime(given_date, '%Y-%m-%d').date()
            # Отримання поточної дати
            current_date = datetime.today().date()
            # Розрахунок і повернення різниці між поточною датою та заданою датою
            return current_date.toordinal() - given_date.toordinal()
        except ValueError:
            # В разі помилки виводить "Please enter a valid date YYYY-MM-DD:" та очікує введення коректних данних
            given_date = input("Please enter a valid date YYYY-MM-DD:")


result = get_days_from_today(entered_date)
print(result)
