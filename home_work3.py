import math

#Задание №1

def degrees2radians(degrees):
    result = (degrees * math.pi) / 180
    return result

angle = 60
result = degrees2radians(angle)
print(math.cos(result))

angle = 45
result = degrees2radians(angle)
print(math.cos(result))

angle = 40
result = degrees2radians(angle)
print(math.cos(result))

#Задание №2


def three_digit_number(number):
    tdn = (number // 100) + (number % 100 // 10) + (number % 10)
    return tdn

result = three_digit_number(666)
print('Сумма цифр трехзначного числа:', result)


#Задание №3

def square_perimetr(catheter1, catheter2):
    square = (catheter1 * catheter2) / 2

    hypotenuse = math.sqrt((catheter1)**2 + (catheter2)**2)
    perimeter = hypotenuse + catheter1 + catheter2
    return square, perimeter

catheter1 = 4
catheter2 = 2
example = square_perimetr(catheter1, catheter2)
print(example)
