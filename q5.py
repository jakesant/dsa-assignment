#Write a program that uses an ADT Stack to evaluate arithmetic expressions in RPN format. The
#contents of the stack should be displayed on the screen during evaluation.
#The allowed arithmetic operators are +, -, x, and /

import operator as op

ops = { '+': op.add,
        '-': op.sub,
        'x': op.mul,
        '*': op.mul,
        '/': op.truediv
}

#Operators will apply on 2 operands

def evaluate(expression):
    stack = []

    for char in expression:
        if not char:
            break
        elif char in ops:
            num1 = stack.pop()
            num2 = stack.pop()
            operator = ops[char]
            result = operator(num1,num2)
            stack.append(result)
        else:
            stack.append(char)

    print("The result of the expression is", stack)

rpnexp = [2, 1, "+", 3, "*"]
evaluate(rpnexp)

"""Psuedocode:
    Read through expression in a list character by character
    If char is number, push onto the stack
    if char is an operand,
        pop last two numbers from stack
        work out that operation
        push result into stack
"""