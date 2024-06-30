from datetime import datetime

enter_date = input("Enter a date YYYY-MM-DD:")


def get_days_from_today(date):
    while True:
        try:
            date = datetime.strptime(date, '%Y-%m-%d').date()
            current_date = datetime.today().date()
            return current_date.toordinal() - date.toordinal()
        except ValueError:
            date = input("Please enter a valid date YYYY-MM-DD :")


result = get_days_from_today(enter_date)
print(result)
