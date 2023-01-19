class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_employees(self):
        return f'{self.name} is a {self.position}'
