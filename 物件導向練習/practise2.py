class Circle:
    """this class is circle"""
    pi = 3.14159
    all_circles = []

    def __init__(self, radius):
        self.radius = radius
        self.__class__.all_circles.append(self)

    def area(self):
        return self.__class__.pi*(self.radius ** 2)

    @classmethod
    def total_area(cls):
        total = 0
        for circle in cls.all_circles:
            total += circle.area()
        return total


c1 = Circle(5)
print(c1.__class__.total_area())
