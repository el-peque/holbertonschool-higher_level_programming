#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a, b, op = int(sys.argv[1]), int(sys.argv[3]), sys.argv[2]
    operators = ["+", "-", "*", "/"]
    if op not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if op == "+":
        res = (add(a, b))
    if op == "-":
        res = (sub(a, b))
    if op == "*":
        res = (mul(a, b))
    if op == "/":
        res = (div(a, b))

    print(f"{a} {op} {b} = {res}")
