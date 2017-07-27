A = map(int, raw_input("input salaries ").split(' '))
print A

x = max(A)
print "max salary is", x
print A.count(x), "persons get it"