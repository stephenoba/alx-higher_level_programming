#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    argv = sys.argv
    argc = len(argv)
    ops = {"+": add, "-": sub, "*": mul, "/": div}
    result = "{} {} {} = {}"
    msg_1 = "Usage: ./100-my_calculator.py <a> <operator> <b>"
    msg_2 = "Unknown operator. Available operators: +, -, * and /"
    if argc != 4:
        print("{}".format(msg_1))
        sys.exit(1)
    if argv[2] not in ops.keys():
        print("{}".format(msg_2))
        sys.exit(1)
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    print(result.format(a, op, b, ops[op](a, b)))
    sys.exit(0)
