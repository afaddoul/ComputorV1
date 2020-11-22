import sys
from tools import find_gcd

def is_equation(expressions):
    for expression in expressions:
        for c in expression:
            if (c.isalpha() or c.isdigit() 
                or c == '=' or c == '+' or c == '-' 
                    or c == '*' or c == '^' or c == '.'):
                continue
            else:
                return False
    return True

def scanner(expressions):
    return is_equation(expressions)

def split_polynomial(equation):
    expressions = equation.replace(" ", "").split(sep='=')
    if len(expressions) != 2 or  len(expressions[0]) == 0 or len(expressions[1]) == 0:
        return False
    return expressions


def get_input():
    if len(sys.argv) != 2:
        exit("bad input")
    return sys.argv[1]

def tokenizer(expressions):
    equation = []
    print('expr 1', expressions[1])
    for expression in expressions:
        tokens = []
        j = 0
        for i in range(0, len(expression)):
            if expression[i] == '+' or expression[i] == '-':
                if len(expression[j:i]):
                    tokens.append(expression[j:i])
                j = i
        tokens.append(expression[j:i+1])
        equation.append(tokens)
    return equation

def negative_exponent_handler(exprs):
    for expr in exprs:
        for i in range(0, len(expr)):
            print(expr[i])
            if expr[i][0] == '-' and expr[i][1:].isdigit():
                if i > 0:
                    expr[i - 1] += expr[i]
                    print('bef and current',expr[i -1], expr[i])
        expr = [elm for elm in expr if not (elm[0] == '-' and elm[1:].isdigit())]
        print('final', expr)
    return exprs

def coeff_expo_parser(expressions):
    exprs = tokenizer(expressions)
    exprs = negative_exponent_handler(exprs)
    print('expr', exprs)
    equation = [[],[]]
    i = 0
    for expr in exprs:
        #print('expr n',expr)
        for token in expr:
            #print('token',token)
            lst = token.split(sep='*')
            #print('<-lst->',lst)
            if len(lst) != 2:
                return False
            equation[i].append({
                'coeff': lst[0],
                'expo': lst[1]
            })
        i = i + 1
        #print(equation)
    return equation

def is_coeff(coeff):
    try:
        coeff = float(coeff)
    except:
        exit('coefficient not properly formated')
    return coeff

def is_exponent(expo):
    unk = ['X^']
    #print(expo[:2])
    if not expo[:2] in unk:
        #print(expo)
        exit('exponent not properly formated')
    expo = int(expo[2:])
    print(expo)
    return expo

def semantic_analyser(equation):
    for expression in equation:
        for elm in expression:
            elm['coeff'] = is_coeff(elm['coeff'])
            elm['expo'] = is_exponent(elm['expo'])



def parser():
    equation = get_input()
    expressions = split_polynomial(equation)
    if not expressions:
        exit("this expression isn't an equation")
    if not scanner(expressions):
        exit("1 this expression isn't an equation")
    equation = coeff_expo_parser(expressions)
    if not equation:
        exit("2 this expression isn't an equation")
    semantic_analyser(equation)
    return equation
