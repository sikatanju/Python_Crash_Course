class Student:
    def __init__(self, name, dept, cgpa):
        self.name = name
        self.dept = dept
        self.cgpa = cgpa
        self.age = 23

    def __init__(self):
        self = self

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

# std = Student('Sika', 'CSE', 3.8)
# * Utilizing default constructor
std = Student()

# * Modifying an attribute's value(s) direct
std.name, std.age = 'Sika', 23

# * Modifying an attribute's value through a method:
std.set_name('std')

print(f'Student\'s name : {std.name} & Student\'s age : {std.age}')