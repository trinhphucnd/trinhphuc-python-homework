def calc(x,y,op):
    # x = 3
    # op = choice(["+", "-", "*","/"])
    # y = 7
    if op == "+":  
        result = x + y
    elif op == "-":
        result = x - y
    elif op == "*":
        result = x * y 
    elif op == "/":
        result = x / y
    return result