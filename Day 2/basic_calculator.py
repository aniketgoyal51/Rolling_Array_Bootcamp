def calculate(num1,num2,operator):
    if(operator=="+"):
        return num1+num2
    elif(operator=="-"):
        return num1-num2
    elif(operator=="*"):
        return num1*num2
    elif(operator=="/"):
        return abs(num1/num2)
    else:
        return "enter correct operator"


num1=int(input("Enter number 1 :"))
num2=int(input("Enter number 2 :"))
operator=input("Enter operator symbol :")

print(calculate(num1,num2,operator))