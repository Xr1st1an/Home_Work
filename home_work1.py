#example 1 ==========

a = 12
b = 34
c = 56
equation = a + b * (c / 2)
result = ("При a = %d, b = %d, c = %d, равно %d") % (a, b, c, equation)
print(result)

#example 2 ========

a = 5
b = 6
equation = (a**2 + b**2) % 2
result = "При a = %d, b = %d, равно %d." % (a, b, equation)
print(result)

#example 3 ==========

a = 6
b = 12
c = 18
equation = (a + b) / 12 * c % 4 + b
result = "При a = %d, b = %d, c = %d, b = %d, равно %d" % (a, b, c, b, equation)
print(result)

#example 4

a = 12
b = 23
c = 34
equation = (a - b * c) / (a + b) % c
result = "При a = %d, b = %d, c = %d, a = %d, b = %d, c = %d, равно %d" % (a, b, c, a, b, c, equation)
print(result)

#example 5

a = 5
b = 6
c = 7
equation = math.fabs(a - b) / (a + b)**3 - math.cos(c)
print("При a = %d,  b = %d, c = %d равно %.2f" %
(a, b, c, equation))

#example 6

a = 3
b = 6
c = 9
equation = (math.log1p(1 + c) / - b)**4 + math.fabs(a)
print("При a = %d,  b = %d, c = %d равно %.2f" %
(a, b, c, equation))