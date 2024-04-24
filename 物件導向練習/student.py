from person import Person


class Student(Person):
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school

    def print_school(self):
        print(self.school)


student1 = Student("澤軒", 25, "高科大")
student1.print_school()
student1.print_name()
student1.print_age()
