print("==========Date===========")

current_date = "11.12.2017"
print(current_date)
lst = current_date.split(".")
mounth = lst[0]
day = lst[1]
year = lst[2]
european_format = day + "." + mounth + "." + year
print(european_format)

print("============Student==============")

student1 = "Oleksandr Kuchanskyi"
print(student1)
lst = student1.split(" ")
name = lst[0]
surname = lst[1]
student2 = surname + " " + name
print(student2)

print("==================================")

snake_style = 'defence_of_the_ancients'
lst = snake_style.split('_')
defence = lst[0]
of = lst[1]
the = lst[2]
ancients = lst[3]
result = defence.title() + of.title() + the.title() + ancients.title()
print(result)


print("==================================")

s = 'Sergey Yesenin*1895-10-03*1925-12-28'
lst = s.split('*')
print(lst)
writer = s.split("*")[0]
life = lst[1]
death = lst[2]
year1 = life.split('-')[0]
year2 = death.split('-')[0]
age = int(year2) - int(year1)
result ="%s, %d," % (writer, age)
print(result)



