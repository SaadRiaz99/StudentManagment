import random
import csv
import os


class Student:
    def __init__(self, name, age, department, student_id=None):
        if student_id:
            self.id = student_id
        else:
            self.id = random.randint(1000, 9999)

        self.name = name
        self.age = age
        self.department = department

    def display(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
        print("-------------------------")


class StudentManagement:
    def __init__(self):
        self.students = []

    def generate_unique_id(self):
        while True:
            new_id = random.randint(1000, 9999)
            if not any(s.id == new_id for s in self.students):
                return new_id

    def add_student(self, name, age, department):
        student_id = self.generate_unique_id()
        student = Student(name, age, department, student_id)
        self.students.append(student)
        print("Student added successfully!")

    def display_students(self):
        if not self.students:
            print("No students available.")
        else:
            for s in self.students:
                s.display()

    def search_student(self, student_id):
        for s in self.students:
            if str(s.id) == student_id:
                print("\nStudent Found:")
                s.display()
                return
        print("Student not found.")

    def delete_student(self, student_id):
        for s in self.students:
            if str(s.id) == student_id:
                self.students.remove(s)
                print("Student deleted successfully.")
                return
        print("Student not found.")

    def save_students(self, filename="students.csv"):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Age", "Department"])

            for s in self.students:
                writer.writerow([s.id, s.name, s.age, s.department])

        print("Data saved to CSV successfully.")

    def load_students(self, filename="students.csv"):
        if not os.path.exists(filename):
            return

        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                student_id, name, age, department = row
                student = Student(name, age, department, int(student_id))
                self.students.append(student)


manager = StudentManagement()
manager.load_students()

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Save to CSV")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        dept = input("Enter Department: ")

        manager.add_student(name, age, dept)

    elif choice == "2":
        manager.display_students()

    elif choice == "3":
        sid = input("Enter Student ID: ")
        manager.search_student(sid)

    elif choice == "4":
        sid = input("Enter Student ID to delete: ")
        manager.delete_student(sid)

    elif choice == "5":
        manager.save_students()

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")