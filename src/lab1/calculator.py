from collections import deque  

def is_num(ch):
    return ord('0') <= ord(ch) <= ord('9') or ch == '.' or ch == ',' or ch == '-'
def if_normal(ch):
    return is_num(ch) or ch in "+/*()"

def calculate(st):
    q = deque()
    i = 0
    while(i < len(st)):
        if(st[i] == '('):
            q.append(i)
        elif (st[i] == ')'):
            if(len(q) > 0):
                li = q.pop()
                old_len = len(st)
                t = str(plus_minus(st[li + 1:i])) 
                if(st[li - 1] == '-' and t[0] == '-'):
                    st = st[:li - 1] + t[1:] + st[i + 1:]
                else:
                    st = st[:li] + t + st[i + 1:]
                i -= old_len - len(st)
            else:
                raise ArithmeticError('Неверная скобочная последовательность!')
        i += 1
    if(len(q) > 0):
        raise ArithmeticError('Неверная скобочная последовательность!')
    return plus_minus(st)


def plus_minus(st):
    li = 0
    while(li < len(st) and st[li] != '+'):
        li += 1
    a = mult_div(st[:li])
    i = li + 1
    while(li < len(st)):
        while(i < len(st) and st[i] != '+'):
            i += 1
        b = mult_div(st[li + 1:i])
        a += b
        li = i
        i += 1
    return int(a) if int(a) == a else a

def mult_div(st):
    li = 0
    while(li < len(st) and is_num(st[li])):
        li += 1
    if(li == 0):
        raise ArithmeticError('\'+\' должен стоять между оперантами!')
    a = float(st[:li])
    i = li + 1
    while(li < len(st)):
        while(i < len(st) and is_num(st[i])):
            i += 1
        if(i - li + 1 == 0):
            raise ArithmeticError('\'+\' должен стоять между оперантами!')
        b = float(st[li + 1:i])
        if(st[li] == '*'):
            a *= b
        elif(st[li] == '/'):
            if(b == 0):
                raise ArithmeticError('Деление на ноль!')
            a /= b
        else:
            raise ArithmeticError('Посторонний символ \'' + st[li] + '\'!')
        li = i
        i += 1
    return a

def change_format(st):
    s = ''.join(filter(lambda ch: ch not in ' \t', st))
    s = s.replace("--", '+')
    
    tmp0 = [s[0]]
    i = 1
    while(i < len(s) - 1):
        if(s[i] == '-' and (is_num(s[i - 1]) or s[i - 1] == ')')):
            tmp0.append('+')
            tmp0.append('-')
        else:
            tmp0.append(s[i])
        i += 1
    tmp0.append(s[-1])

    tmp1 = []
    for i in range(len(tmp0) - 1):
        tmp1.append(tmp0[i])
        if(tmp0[i + 1] == '(' and is_num(tmp0[i]) and tmp1[i] != '-'):
            tmp1.append('*')
    tmp1.append(tmp0[-1])

    tmp2 = [tmp1[0]]
    for i in range(1, len(tmp1)):
        if(tmp1[i - 1] == ')' and is_num(tmp1[i])):
            tmp2.append('*')
        tmp2.append(tmp1[i])
    
    tmp3 = []
    for i in range(len(tmp1) - 1):
        if(tmp2[i] != '+' or tmp1[i + 1] != '+'):
            tmp3.append(tmp2[i])
    tmp3.append(tmp2[-1])

    return ''.join(tmp3)

#or _ in range(1):
while True:
    print("\nВведите алгебраическое выражение:")
    inp = input()
    fin = change_format(inp)
    try:
        for el in fin:
            if(not if_normal(el)):
                raise ArithmeticError('Посторонний символ \'' + el + '\'!')
        print(fin, '=', calculate(fin))
    except Exception as error:
        print(fin, "Произошла ошибка во время рассчёта:", error)