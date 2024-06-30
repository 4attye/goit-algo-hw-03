from datetime import datetime
enter_date = input("Enter date YYYY-MM-DD:")


def get_days_from_today(date):
    date = datetime.strptime(date, '%Y-%m-%d')
    current_date = datetime.today()
    return current_date.toordinal() - date.toordinal()

print(get_days_from_today(enter_date))