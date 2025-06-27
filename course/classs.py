"""
Class is specification or design to create object.
S1 is reference variable
Object : A physical existence of a class.
Functions defined inside a class is called as Methods.
"""


class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def talk(self):
        print("Hello my name is :", self.name)
        print("My Roll No is :", self.roll_no)
        print("My marks is :", self.marks)


s1 = Student("Lakshan", "CS07", 90)
s2 = Student("Night Fury", "CS077", 70)

s1.talk()