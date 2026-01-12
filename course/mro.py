"""
Method Resolution Order (MRO) in Python's multiple inheritance!
"""

class A:

    def test1(self):
        print(" method named test1 of A called ")

class B(A):

    def test1(self):
        print(" method named test1 of B called ")

class C(A):

    def test1(self):
        print(" method named test1 of C called ")

class D(B,C):

    def test2(self):
        print(" method named test2 of D called ")

object1=D()
object1.test1()

"""
Method Resolution Order (MRO):
Python searches for methods in a specific order:

D (the object's own class) - no test1() here
B (first parent in class D(B,C)) - FOUND! ✓
C (would be next, but we already found it)
A (would be last, but we already found it)
"""