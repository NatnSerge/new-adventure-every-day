a = int(raw_input("a=:"))
b = int(raw_input("b=:"))
c = int(raw_input("c=:"))

import math;

D = b * b - 4 * a * c

print "D = ", D

if (D < 0):
    print "no x"

elif (0 < D):
    x1= (-b + math.sqrt(D)) / 2 / a
    x2 = (-b - math.sqrt(D)) / 2 / a
    print "x are ", x1, x2

else:
    x = (-b + math.sqrt(D)) / 2 / a
    print "x is ", x