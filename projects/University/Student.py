from Person import Person

class Student(Person):

    def __init__(self,id, name, age, dept):
        super().__init__(id, name, age)
        self.dept = dept
    
    def student_details(self):
        data = self.details()
        data["dept"] = self.dept

        return data
