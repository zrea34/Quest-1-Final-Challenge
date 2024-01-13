def calc_driver():
    print("welcome to the calculator")
    print("1. add")
    print("2. sub")
    print("3. mult")
    print("4. div")
    print("5. Fibonancci sequence calculator")
    sel = input("Enter an option: ")

    if sel == str(1):
        num1 = float(input("Enter 1st number to be added: "))
        num2 = float(input("Enter 2nd number to be added: "))
        print(add(num1, num2))
    elif sel == str(2):
        num1 = float(input("Enter 1st number to be subtracted: "))
        num2 = float(input("Enter 2nd number to be subtracted: "))
        print(sub(num1, num2))
    elif sel == str(3):
        num1 = float(input("Enter 1st number to be multiplied: "))
        num2 = float(input("Enter 2nd number to be multiplied: "))
        print(mult(num1, num2))
    elif sel == str(4):
        num1 = float(input("Enter 1st number to be divided: "))
        num2 = float(input("Enter 2nd number to be divided: "))
        print(div(num1, num2))
    elif sel == str(5):
        num = int(input("Enter the sequence upper bound: "))
        print(fib(num))
    else:
        print("Please enter an integer!")


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mult(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1/num2


def fib(n):
    result = []
    a = 0
    b = 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result
