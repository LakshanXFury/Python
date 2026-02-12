import os
from contextlib import contextmanager

# cwd = os.getcwd()
# os.chdir("Sample-Dir-One")
# print(os.listdir())
# os.chdir(cwd)

@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)

with change_dir("Sample-Dir-One"): # Go inside the directory
    print(os.listdir()) # List what is inside the directory

# Can be re-used over and over again
with change_dir("Sample-Dir-Two"): # Go inside the directory
    print(os.listdir()) # List what is inside the directory

