# encapsulation封裝:把資訊藏起來，設定為private
class Robot:
    def __init__(self, name):
        self.name = name
        # private property
        self.__age = 25  # "__"age 前面加雙底線就好

    def get_age(self):
        return self.__age

    def set_age(self):
        self.__age += 1

    def age_setter(self, new_age):
        if new_age > 0 and new_age < 100:
            self.__age = new_age
        else:
            print('new age setting is invalid')

    def age_getter(self):
        print(self.__age)

    # private method 一樣前面雙底線
    def __this_is_private_method(self):
        print('from private method')

    def greet(self):
        print('I am arobot')
        self.__this_is_private_method()


robot1 = Robot("LEO")
robot1.greet()  # 若執行__this_is_private_method會輸出erro
robot1.age_setter(-30)
robot1.age_getter()
