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

def perimetr(amount1, amount2):
    square = (amount1 * amount2) / 2

    hypotenuse = math.sqrt((amount1)**2 + (amount2)**2)
    perimeter = hypotenuse + amount1 + amount2
    return square, perimeter

amount1 = 4
amount2 = 2
example = perimetr(amount1, amount2)
print(example)
