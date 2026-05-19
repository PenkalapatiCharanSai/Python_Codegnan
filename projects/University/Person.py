class Person:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
    def details(self):
        return {
            "ID": self.id,
            "Name": self.name,
            "Age": self.age
        }