from University import University

u1 = University()

# Available Courses
print("Available Courses:")
print(u1.available_courses())

# Add Students
print("\n")
print(u1.add_student("Charan", 21, "CSE"))
print(u1.add_student("Rahul", 22, "AI"))

# Add Employees
print("\n")
print(u1.add_employee("Kumar", 45, "Professor", 50000))
print(u1.add_employee("Ramesh", 40, "Lab Assistant", 30000))

# Show All Students
print("\nAll Students")
print(u1.show_all_students())

# Show All Employees
print("\nAll Employees")
print(u1.show_all_employees())

# Student By ID
print("\nStudent By ID")
print(u1.student_by_id(1))

# Employee By ID
print("\nEmployee By ID")
print(u1.employee_by_id(2))

# Delete Student
print("\n")
print(u1.delete_student(1))

# Delete Employee
print(u1.delete_employee(2))

# After Delete
print("\nStudents After Delete")
print(u1.show_all_students())

print("\nEmployees After Delete")
print(u1.show_all_employees())