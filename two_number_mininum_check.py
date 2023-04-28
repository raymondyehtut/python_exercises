num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
try:
    if num1 < num2:
        print(num1, "is less than", num2)
    else:
        print(num1, "is not less than", num2)
except ValueError:
    print("please enter number only")
