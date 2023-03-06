from classes.person import Person


class Employee(Person):

    def __init__(self, firstname, surname, age, salary, department, hours):
        super().__init__(firstname, surname, age)
        self.salary = salary
        self.department = department
        self.hours = hours











