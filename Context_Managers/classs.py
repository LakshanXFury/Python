"""
Using Class
"""


class Open_File():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()


with Open_File("test.txt", "w") as file:
    file.write("Testing Hello World")

print(file.closed)