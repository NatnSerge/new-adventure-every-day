def whatisx():
    x = int(raw_input("x=:"))
    if (x < 10) or (x > 20):
        print "x is bad"

    elif (10 < x < 20):
        print "x is good!"

    else:
        print "x is werid"

def xsq():
    x = int(raw_input("x=:"))

    print "x * x = ", x * x

def xlist():
    x = 0
    while x <= 10:
        print x
        x += 1

def xsqrt():
    x = int(raw_input("x=:"))

    import math;
    print math.sqrt(x)

def triangle():
    a = int(raw_input("a=:"))
    b = int(raw_input("b=:"))

    import math;
    x = math.sqrt(a * a + b * b)

    print "x = ", x

def Quad_eq():
    a = int(raw_input("a=:"))
    b = int(raw_input("b=:"))
    c = int(raw_input("c=:"))

    import math;

    D = b * b - 4 * a * c

    print "D = ", D

    if (D < 0):
        print "no x"

    elif (0 < D):
        x1 = (-b + math.sqrt(D)) / 2 / a
        x2 = (-b - math.sqrt(D)) / 2 / a
        print "x are ", x1, x2

    else:
        x = (-b + math.sqrt(D)) / 2 / a
        print "x is ", x

def Mult_table():
    M = int(raw_input("M = "))
    a = int(raw_input("from a "))
    b = int(raw_input("to b "))

    for x in range(a, b + 1):
        print "%s * %s = %s" % (M, x, M * x)

def Salary():
    A = map(int, raw_input("input salaries ").split(' '))
    print A

    x = max(A)
    print "max salary is", x
    print A.count(x), "persons get it"