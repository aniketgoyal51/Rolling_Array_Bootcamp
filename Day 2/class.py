class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    pass    # it help to bypass any error

name=input("Enter your name: ")
age=input("Enter your age: ")

p1=Person(name,age)

print(p1.name , p1.age)

changeAge=input("Enter your New age: ")

del p1.age
p1.age=changeAge

print(p1.age)
