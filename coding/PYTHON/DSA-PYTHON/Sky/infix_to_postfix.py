def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    associativity = {'+': 'left', '-': 'left', '*': 'left', '/': 'left'}
    stack = []
    output = []
    for char in expression:
        if char.isalpha():
            output.append(char)
        elif char in precedence:
            while (stack and stack[-1]!='('and
                (precedence[stack[-1]]>precedence[char]or
                (precedence[stack[-1]]==precedence[char] and associativity[char]=='left'))):
                output.append(stack.pop())
            stack.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
    while stack:
        output.append(stack.pop())
    return ''.join(output)
infix_expr=input("Enter an infix expression: ")
postfix_expr=infix_to_postfix(infix_expr)
print("Infix Expression:",infix_expr)
print("Postfix Expression:",postfix_expr)