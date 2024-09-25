print("Hello again World")

#functions are used to decrease the RAM usage

def addition(first, second):
    sum = first + second
    print(sum)

def subtraction(first, second):
    diff = first - second
    print(diff)

def multiplication(first, second):
    product = first*second
    print(product)

def division(first, second):
    quotient = first/second
    print(quotient)
#infinite loop
while (1>0):
    primary = int(input("First Number Please: \n"))
    secondary = int(input("Second Number Please: \n"))
    function = input("please input function: \n")
    print(primary%secondary)
#
    if (function == "add"):
        addition(primary, secondary)

    elif (function == "subtract"):
        subtraction(primary, secondary)

    elif (function == "multiply"):
        multiplication(primary, secondary)

    elif (function == "divide"):
        division(primary, secondary)