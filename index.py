import random
import csv


class Student:
    def __init__(self, name, age, department):
        self.id = random.randint(1000, 9999)
        self.name = name
        self.age = age
        self.department = department

    def display(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
        print("-------------------")


class StudentManagement:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        for s in self.students:
            s.display()

    def search_student(self, id):
        for s in self.students:
            if str(s.id) == id:
                s.display()
                return
        print("Student not found")

    def save_student(self, filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(["ID", "Name", "Age", "Department"])

            for s in self.students:
                writer.writerow([s.id, s.name, s.age, s.department])


manager = StudentManagement()

while True:
    print("\n1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Save to CSV")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        dept = input("Enter Department: ")

        student = Student(name, age, dept)
        manager.add_student(student)

    elif choice == "2":
        manager.display_students()

    elif choice == "3":
        sid = input("Enter ID to search: ")
        manager.search_student(sid)

    elif choice == "4":
        manager.save_student("students.csv")
        print("Data saved to students.csv")

    elif choice == "5":
        break