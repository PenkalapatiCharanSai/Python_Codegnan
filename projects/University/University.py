from Student import Student
from Employee import Employee


class University:

    def __init__(self):
        self.students = {}
        self.employees = {}
        self.courses = [
            "CSE",
            "ECE",
            "EEE",
            "MECH",
            "CIVIL",
            "AI",
            "DS"
        ]

    # Available Courses
    def available_courses(self):
        return self.courses

    # Add Student
    def add_student(self, name, age, dept):
        if dept not in self.courses:
            return "Course Not Available"
        student_id = len(self.students) + 1
        s = Student(student_id, name, age, dept)
        self.students[student_id] = s
        return f"Student Added Successfully with ID {student_id}"

    # Add Employee
    def add_employee(self, name, age, role, salary):
        employee_id = len(self.employees) + 1
        e = Employee(employee_id, name, age, role, salary)
        self.employees[employee_id] = e
        return f"Employee Added Successfully with ID {employee_id}"

    # Delete Student
    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            return "Student Deleted Successfully"
        return "Student ID Not Found"

    # Delete Employee
    def delete_employee(self, employee_id):
        if employee_id in self.employees:
            del self.employees[employee_id]
            return "Employee Deleted Successfully"
        return "Employee ID Not Found"

    # Show All Students
    def show_all_students(self):
        data = {}
        for id, student in self.students.items():
            data[id] = student.student_details()
        return data

    # Show All Employees
    def show_all_employees(self):
        data = {}
        for id, employee in self.employees.items():
            data[id] = employee.employee_details()
        return data

    # Student By ID
    def student_by_id(self, student_id):
        if student_id in self.students:
            return self.students[student_id].student_details()
        return "Student Not Found"

    # Employee By ID
    def employee_by_id(self, employee_id):
        if employee_id in self.employees:
            return self.employees[employee_id].employee_details()
        return "Employee Not Found"