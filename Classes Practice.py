#**************************************************************************************************************
#Mozzam Hasnan
#FA24-BBD-103
#QUESTION_9
# Create a class Bank with attributes name, account_number, and balance. Implement methods to deposit and withdraw money.
print("\nClass Book")
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
circle = Circle(5)
print("Circle Area:", circle.area())

rectangle = Rectangle(4, 6)
print("Rectangle Area:", rectangle.area())

triangle = Triangle(3, 8)
print("Triangle Area:", triangle.area())
#***************************************************************************************************************
#QUESTION_10
#Create a class Animal with attributes name and sound. Create subclasses Dog, Cat, and Cow that inherit from Animal and implement their specific sounds.
print("\nClass Animal")
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        return f"{self.name} says {self.sound}"

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Woof")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow")

class Cow(Animal):
    def __init__(self, name):
        super().__init__(name, "Moo")
dog = Dog("Buddy")
print(dog.make_sound())

cat = Cat("Kitty")
print(cat.make_sound())

cow = Cow("Daisy")
print(cow.make_sound())
#***********************************************************************************************************************