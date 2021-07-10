#Instance methods
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def say_hello(self):
        print(f'{self.first_name} says hello')

class Student(Person):
    def __init__(self, first_name, last_name, year):
        super().__init__(first_name, last_name)
        self.year = year

    def say_hello(self):
        super().say_hello()
        print('and is a student')


dani = Student('dani','barker',2021)
dani.say_hello()
print(dani.year)

john = Person('John','Smith')
john.say_hello()

#Class methods
class Person:
    age = 25
    @classmethod
    def get_age(cls):
        return cls.age



#Static methods
class Math:
    PI = 3.1415
    @staticmethod
    def floor(number):
        return int(number)
    @classmethod
    def area_of_circle(cls, radius):
        return cls.PI * radius * radius