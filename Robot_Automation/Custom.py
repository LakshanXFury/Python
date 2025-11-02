"""The class name should be in Title case or it won't work"""


class Custom:
    def add(self, a, b):
        return int(a) + int(b)

    def used_name(self, name):
        """Prints the name (Robot keyword will be 'Used Name')"""
        print(f"Working on the name {name}")

    def full_name(self, first_name, last_name):
        """Concatenate first and last name (Robot keyword 'Full Name')"""
        return f"{first_name} {last_name}"
