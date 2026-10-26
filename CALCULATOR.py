from math import *


# this is where I learn random shit and DO random shit

# this is a tokenizer which turns long equations into teeny tiny chunks.

def tokenizer(equation=None):
    if equation is None:
        equation = input("enter equation: ")
    bucket = ""
    tokens = []
    for i in equation:
        if i in ["+", "-", "*", "/", "^", " "] and bucket != "":
            tokens.append(bucket)
            if i != " ":
                tokens.append(i)
            bucket = ""
        else:
            bucket += i
    if bucket == "":
        return tokens
    else:
        tokens.append(bucket)
        return tokens


# this is ver1 strict left to right 1 operator calculator

def calculator_ver1(equation=None):
    if equation is None:
        equation = input("enter equation: ")
    tokens = tokenizer(equation=equation)
    operators = {"+": lambda a, b: a + b,
                 "-": lambda a, b: a - b,
                 "*": lambda a, b: a * b,
                 "/": lambda a, b: a / b,
                 "^": lambda a, b: a ** b, }
    num1 = 0
    operator = ""
    num2 = 0
    loop_count = 0
    for i in tokens:
        loop_count += 1
        if i not in operators and i.replace(".", "", 1).strip("-").isdigit() and loop_count == 1:
            num1 = float(i)
        elif i.replace(".", "", 1).strip("-").isdigit() and i not in operators and loop_count == 3:
            num2 = float(i)
        else:
            operator += i
    answer = operators[operator](num1, num2)
    return answer


# this is a flexible multiple operator calculator

def calculator_ver2(equation=None):
    if equation is None:
        equation = input("enter equation: ")
    tokens = tokenizer(equation=equation)
    operators = {"+": lambda a, b: a + b,
                 "-": lambda a, b: a - b,
                 "*": lambda a, b: a * b,
                 "/": lambda a, b: a / b,
                 "^": lambda a, b: a ** b}

    while "^" in tokens:
        for j in tokens:
            if j == "^":
                idx = tokens.index(j)
                num1 = float(tokens[idx - 1])
                num2 = float(tokens[idx + 1])
                result = operators[j](num1, num2)
                tokens[idx - 1: idx + 2] = [str(result)]
                break

    while "*" in tokens or "/" in tokens:
        for j in tokens:
            if j == "*" or j == "/":
                idx = tokens.index(j)
                num1 = float(tokens[idx - 1])
                num2 = float(tokens[idx + 1])
                result = operators[j](num1, num2)
                tokens[idx - 1: idx + 2] = [str(result)]
                break

    while "+" in tokens or "-" in tokens:
        for j in tokens:
            if j == "+" or j == "-":
                idx = tokens.index(j)
                num1 = float(tokens[idx - 1])
                num2 = float(tokens[idx + 1])
                result = operators[j](num1, num2)
                tokens[idx - 1: idx + 2] = [str(result)]
                break

    return float(tokens[0])


# ver3 hell yeaaaahhh baby.

def calculator_ver3(equation=None):
    if equation is None:
        equation = input("enter equation: ")
    while "(" in equation and ")" in equation:
        idx2 = equation.index(")")
        idx1 = equation.rfind("(",0, idx2)
        calc1 = calculator_ver2(equation=equation[idx1 + 1:idx2])
        equation = equation.replace(equation[idx1 :idx2 + 1], str(calc1),1)
    answer = calculator_ver2(equation=equation)
    return answer


if __name__ == "__main__":
    func = int(input())
    funcs = {1: calculator_ver1,
             2: calculator_ver2,
             3: calculator_ver3}
    if func in funcs:
        print(funcs[func]())
