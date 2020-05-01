#Write a program that uses an ADT Stack to evaluate arithmetic expressions in RPN format. The
#contents of the stack should be displayed on the screen during evaluation.
#The allowed arithmetic operators are +, -, x, and /

import operator

ops = { '+': operator.add,
        '-': operator.sub,
        'x': operator.mul,
        '/': operator.truediv
}

#Operators will apply on 2 operands

def evaluate(expression):
    stack = []

    for char in expression:
        if char.isdigit():
            stack.append(char)
            print("pushing", char)
        if not char:
            break

    print("The contents of the stack is: ", stack)
    stack.pop()
    print("The contents of the stack is: ", stack)

rpnexp = ["2", "1", "+", "3", "*"]
evaluate(rpnexp)

"""Psuedocode:
    Read through expression in a list character by character
    If char is number, push onto the stack
    if we meet an operand, we
        pop last two numbers from stack
        work out that operation
        push result into stack
"""