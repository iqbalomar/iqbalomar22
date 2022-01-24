num1=int(input("The first number is: "))
num2=int(input("The second number is: "))
num3=int(input("The third number is: "))
if (num1>num2) and (num1>num3):
    print("Number :",num1, "is the largest number")
elif (num2>num1) and (num2>num3):
    print("Number :",num2,"is the largest number")
else:
    print("Number :",num3," is the largest number")