from application.db.people import *
from application.salary import *

if __name__ == '__main__':
    salary1 = Salary('Oleg')
    employee1 = Employee('Oleg', 'manager')
    print(employee1.get_employees())
    print(salary1.calculate_salary())
