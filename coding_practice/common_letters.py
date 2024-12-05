def common_names():
    first_name = set(input("Enter the first name: "))
    second_name = set(input("Enter the second name: "))
    match = first_name & second_name
    print(match)


common_names()
