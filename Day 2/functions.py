def greeting(*name):
    print("My name is "+ name[1])

greeting("rohan","aniket","aman")


def age_display(age):
    print("your age is",age)   # or (+ str(age))

age=int(input("Enter your age :"))

age_display(age)