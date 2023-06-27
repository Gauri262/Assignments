print("Selec the operation you want to perform")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

opt = int(input("Enter which option you want to choose: "))

if opt==1:
    num1=int(input("enter num1: "))
    num2=int(input("enter num2: "))
    print("Sum of the the numbers is:",num1+num2) 
elif opt==2:
    num1=int(input("Enter num1: "))
    num2=int(input("Enter num2: "))
    print("Subtraction of the numbers is:",num1-num2)
elif opt==3:
    num1=int(input("Enter num1: "))
    num2=int(input("Enter num2: "))
    print("Multiplication of the numbers is:",num1*num2)
elif opt==4:
    num1=int(input("Enter num1: "))
    num2=int(input("Enter num2: "))
    if num2!=0:
        print("Division of the numbers is:",num1//num2)
    else:
        print("Number can't be divided by zero")
else:
    print("Invalid choice!!!!")