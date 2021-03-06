from tools import find_gcd


def equation_simplifier(equation):
    i = 0
    for elm in equation[1]:
        elm['coeff'] = elm['coeff'] * -1
        equation[0].append(elm)
        i += 1
    equation[0] = sorted(equation[0], key=lambda k: k['expo'], reverse=True)
    equation[0] = [elm for elm in equation[0] if elm['coeff']]
    for i in equation[0]:
        for j in equation[0]:
            if j['expo'] == i['expo'] and equation[0].index(
                    i) != equation[0].index(j):
                i['coeff'] += j['coeff']
                if len(equation[0]) > 0:
                    equation[0].pop(equation[0].index(j))
    coeff_lst = [elm['coeff'] for elm in equation[0]]
    if len(coeff_lst) == 0:
        print("can't manage this format")
        exit()
    gcd = find_gcd(coeff_lst)
    if (gcd > 1):
        for elm in equation[0]:
            elm['coeff'] = elm['coeff'] / gcd
    equation[0] = [elm for elm in equation[0] if elm['coeff']]
    if len(equation) == 2:
        equation.pop(1)
        equation = equation[0]
    if len(equation):
        for elm in equation:
            elm['coeff'] = round(elm['coeff'], 6)
    return equation
