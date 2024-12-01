from hw.salary import *
from hw.db.people import *
from datetime import *

if __name__ == '__main__':
    print(f'Сегодняшняя дата: {datetime.today().strftime("%d-%m-%Y")}')
    get_employees()
    calculate_salary()