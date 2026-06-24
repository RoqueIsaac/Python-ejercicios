import art
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

ops = {"+": add,
       "-": subtract,
       "*": multiply,
       "/": divide
       }

while True:
    print(art.logo)
    n1 = float(input("What is the first number?: "))
    next_round = 'a'
    while next_round:
        for keys in ops:
            print(keys)
        operation = input("Pick an operation: ")
        n2 = float(input("What is the next number?: "))

        result = ops[operation](n1, n2)

        print(f"{n1} {operation} {n2} = {result}")

        next_round = input(f"Type 'y' to continue calculating with {result}, or 'n' to star a new calculation: ")
        if next_round == "y":
            n1 = result
            continue
        else:
            print("\n"*20)
            break


