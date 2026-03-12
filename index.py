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