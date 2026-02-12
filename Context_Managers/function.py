"""
Using Functions for Context Managers

A context manager handles setup and cleanup automatically
"""

from contextlib import contextmanager

@contextmanager
def open_file(file_name, mode):
    f = open(file_name, mode)
    yield f
    f.close()

with open_file('test.txt', 'w') as file:
    file.write('Testing Hello World from Function')

print(file.closed)


"""
Calls open_file('test.txt', 'w')
Runs setup: f = open('test.txt', 'w')
Hits yield f - gives file to the variable file
Executes the with block: writes to the file
After with block finishes, runs cleanup: f.close()

# Execution order:

1. with open_file('test.txt', 'w') as file:
   ↓
2. f = open('test.txt', 'w')  # SETUP
   ↓
3. yield f  # Give 'f' to 'file' variable
   ↓
4. file.write('Testing Hello World from Function')  # Your code
   ↓
5. f.close()  # CLEANUP (runs automatically after 'with')
   ↓
6. print(file.closed)  # True
"""