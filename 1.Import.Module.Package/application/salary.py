class Salary:
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_salary(self):
        return f'It`s your salary, {self.employee_name}!'
