from datetime import datetime
from time import sleep

from tqdm import tqdm

from application.db.people import Employee
from application.salary import Salary

if __name__ == '__main__':
    salary1 = Salary('Oleg')
    employee1 = Employee('Oleg', 'manager')
    print(f'Текущие дата и время: {datetime.now()}')
    print(employee1.get_employees())
    for i in tqdm(range(30)):
        sleep(.1)
    print(salary1.calculate_salary())
