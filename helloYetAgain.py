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

def factorial(first, second):
    number1 = 1
    number2 = 1
    target1 = 1
    target2 = 1
    for x in range(second):
        target1*number1
        number1+=1
    for x in range(first):
        target2*number2
        number2+=1
    print(target1/target2)

def conversion(value, to_base=None):
    if isinstance(value, str):
        decimal_value = int(value, 0)
    elif isinstance(value, int):
        # If it's already an integer, just use it directly
        decimal_value = value
    else:
        raise ValueError("Input must be a string or integer.")

    # Step 2: If a target base is provided, convert from decimal to the target base
    if to_base:
        if to_base == 2:
            return bin(decimal_value)[2:]  # Return binary string without "0b"
        elif to_base == 8:
            return oct(decimal_value)[2:]  # Return octal string without "0o"
        elif to_base == 16:
            return hex(decimal_value)[2:]  # Return hexadecimal string without "0x"
        else:
            # Convert to any base between 2 and 36
            if to_base < 2 or to_base > 36:
                raise ValueError("Base must be between 2 and 36.")
            return decimal_to_base(decimal_value, to_base)
    else:
        # If no target base is provided, just return the decimal value
        return decimal_value

# Helper function to convert decimal to any base between 2 and 36
def decimal_to_base(n, base):
    if n == 0:
        return "0"
   
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Digits for bases up to 36
    result = ""
   
    while n > 0:
        result = digits[n % base] + result
        n = n // base
       
    return result





#infinite loop
while (4>0):
    primary = input("First Number Please: \n")
    secondary = input("Second Number Please: \n")
    function = input("please input function: \n")

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

    elif (function == "factorial"):
        factorial(primary, secondary)
    
    elif (function == "to base ten"):
        base = input("what base would you like to convert to?\n")
        conversion(primary, secondary, base)
    
    elif (function == "convert")
        decimal_to_base(primary, secondary)
