def check(num):
    if(num%2==0):
        return "Even"
    else:
        return "Odd"

num=int(input("Enter a number :"))

print(check(num))