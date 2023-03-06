class Company:

    def __init__(self, location, employees):
        self.location = location
        self.employees = employees

    def __str__(self):
        return f"Location: {self.location}, Employees: {self.employees}"

    def __repr__(self):
        return f"Company({self.location}, {self.employees})"

    def __eq__(self, other):
        return self.location == other.location and self.employees == other.employees

    def __ne__(self, other):
        return not self.__eq__(other)
