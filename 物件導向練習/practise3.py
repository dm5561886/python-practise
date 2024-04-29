class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(f"{self.name} is sleeping")

    def eat(self, food):
        print(f"{self.name} is eating {food}....")


class Student(People):
    def __init__(self, name, age, student_id):
        # 也能寫成People.__init__(self,name,age)
        # self.name = name
        # self.age = age
        self.student_id = student_id
        super().__init__(name, age)


student1 = Student("leo", 24, "f111193105")
student1.sleep()
student1.eat("beef")
print(student1.name)
