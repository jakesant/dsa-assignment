#Write a program that uses an ADT Stack to evaluate arithmetic expressions in RPN format. The
#contents of the stack should be displayed on the screen during evaluation.
#The allowed arithmetic operators are +, -, x, and /

import operator

ops = { '+': operator.add,
        '-': operator.sub,
        'x': operator.mul,
        '/': operator.div
}

def stack():
    