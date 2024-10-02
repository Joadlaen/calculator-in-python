print("Hello again World")

#functions are used to decrease the RAM usage


def addition(first, second):
    print(first + second)

def subtraction(first, second):
    print(first - second)

def multiplication(first, second):
    print(first*second)

def division(first, second):
    print(first/second)

def exponent(first, second):
    print(first**second)

def modulo(first, second):
    print(first%second)

def series(first, second):
    start = first - 1
    ender = 0
    for x in range(second-first):
        start = start + 1
        ender = ender + start
    ender = ender + second
    print(ender)

def tetration(first, second):
    tetrate1 = first
    for x in range(second):
        tetrate1 = tetrate1**first
    print(first**tetrate1)




#infinite loop
while (4>0):
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
    
    elif (function == "index"):
        exponent(primary, secondary)

    elif (function == "mod"):
        modulo(primary, secondary)
    
    elif (function == "sum"):
        series(primary, secondary)

    elif (function == "tetra"):
        tetration(primary, secondary)