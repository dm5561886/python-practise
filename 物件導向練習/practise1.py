# Class name 第一個字要大寫'C'ar
class Car:
    energy_used = "oil"
    """練習用的"""
    # __init__()初始化

    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year

    def run(self):
        print(f"{self.brand} 跑得很快")

    def fix(self, time):
        print(f"{self.brand} 要開去維修，需要維修{time}小時")


car1 = Car("benz", "black", 2024)
car1.fix(12)
print(car1.energy_used)
