def demonstrate_exec():
    code = """def greet(name):
    return f"Hello, {name}!\""""

    # Execute the code string
    local_scope = {}
    exec(code, {}, local_scope)
    print(local_scope['greet']("Alice"))

def demonstrate_eval():
    # Evaluate the expression
    expression = input("Enter an expression: ")
    result = eval(expression)
    print(f"The result of the expression is: {result}")


def demonstrate_safe_eval():
    expression = input("Enter an expression that uses a, b and c: ")

    #define variabkes for expression
    variables = {"a": 10, "b": 20, "c": 30}

    # evaluate the expression in the context of the provided variables
    result = eval(expression, {}, variables)

    print(f"The result of the expression is: {result}\n")

demonstrate_safe_eval()