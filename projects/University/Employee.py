from Person import Person

class Employee(Person):

    def __init__(self, id, name, age, role, salary):
        super().__init__(id, name, age)
        self.role = role
        self.salary = salary

    def employee_details(self):
        data = self.details()
        data["Role"] = self.role
        data["Salary"] = self.salary
        return data