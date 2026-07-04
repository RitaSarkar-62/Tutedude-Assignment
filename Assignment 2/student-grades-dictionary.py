
students={}

# Add a student
name = input("Enter student name: ")
grade = input("Enter grade: ")
students[name] = grade

# Update a student's grade
update = input("Do you want to update the grade? (yes/no): ")

if update == "yes":
    name = input("Enter student name: ")
    if name in students:
        new_grade = input("Enter new grade: ")
        students[name] = new_grade
        print("Grade updated successfully.")
    else:
        print("Student not found.")

# Display all students
print("\nStudent Grades:")
for name, grade in students.items():
    print(name, ":", grade)

