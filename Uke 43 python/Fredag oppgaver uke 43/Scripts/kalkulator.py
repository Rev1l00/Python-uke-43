num01 = int(input("What is your first number? "))
num02 = int(input("What is your second number? "))

method = input("Do you want to Add, Subtract, Multiply or Divide? ")

def add(x, y):
    result = x + y
    return result

def sub(x, y):
    result = x - y
    return result

def multi(x, y):
    result = x * y
    return result

def division(x, y):
    result =  x / y
    if result.is_integer() == True:
        result = int(result)
        return result
    else:
        return result

while True:
    result = 0
    if method == "Add":
        result = add(num01, num02)
        break
    elif method == "Subtract":
        result = sub(num01, num02)
        break
    elif method == "Multiply":
        result = multi(num01, num02)
        break
    elif method == "Divide":
        result = division(num01, num02)
        break
    else:
        method = input("That is not an option. Try again: ")
print(result)
