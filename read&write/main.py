##To Read from the file

# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# file.close()

# To write into the file

with open("my_file.txt", mode="a") as file:
    file.write("\nNigga 2 + 3")