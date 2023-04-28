x = input("Enter first value:")
y = input ("Enter second value:")
op =input ("Operator (+,-,*,/):")
try :
    x = int(x)
    y = int(y)
    output = True
    if op == "+" :
        result =x+y
    elif op == "-":
        result = x-y
    elif op == "*":
        result =x*y
    elif op == "/":
        result = x/y
    else :
        output = False
        print ("wrong operator")
    if output :
        print ("Result is",result)
except ValueError:
    print ("please enter only number only")

