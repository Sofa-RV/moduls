from hw.db.people import get_employees as get_employees
from hw.salary import calculate_salary as calculate_salary
from datetime import datetime

if __name__ == '__main__':
    print(f'Сегодняшняя дата: {datetime.today().strftime("%d-%m-%Y")}')
    get_employees()
    calculate_salary()