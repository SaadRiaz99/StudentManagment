class Student:
    def __init__(self , id ,  name , age , department):
        self.id = id
        self.name = name
        self.age = age
        self.department = department

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
        print("-------------------")
class StudentManagment:
    def __init__(self):
        self.students = []
    
    def add_Sudent(self, student):
        self.students.append(student)

    def display_students(self):
        for s in self.students:
            s.dispaly()

    def search_student(self ,id):
        for s in students:
            if s.id == id:
                return s 
manager = StudentManager()

while True:
    print("\n1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        sid = input("Enter ID: ")
        name = input("Enter Name: ")
        dept = input("Enter Department: ")

        student = Student(sid, name, dept)
        manager.add_student(student)

    elif choice == "2":
        manager.show_students()

    elif choice == "3":
        sid = input("Enter ID to search: ")
        manager.search_student(sid)

    elif choice == "4":
        break