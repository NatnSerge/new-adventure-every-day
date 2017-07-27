M = int(raw_input("M = "))
a = int(raw_input("from a "))
b = int(raw_input("to b "))

for x in range(a, b + 1):
    print "%s * %s = %s" % (M, x, M * x)