def evaluate_postfix(expression):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        elif char in operators:
            if len(stack) < 2:
                raise ValueError("Invalid expression")
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                stack.append(a / b)
            elif char == '^':
                stack.append(a ** b)
    if len(stack) != 1:
        raise ValueError("Invalid expression")
    return stack[0]
if __name__ == "__main__":
    expression = input("Enter a postfix expression: ")
    result = evaluate_postfix(expression)
    print(f"The result of the postfix expression is: {result}")
