class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")


class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)  # Call Person's __init__() from Parent Class
        self.student_id = student_id

    def show_id(self):
        print(f"My student ID is {self.student_id}")


# Create a Student
s1 = Student("Anjali", "ST123")
s1.greet()  # Output: Hello, my name is Anjali
s1.show_id()  # Output: My student ID is ST123