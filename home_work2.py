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

snake_style = 'Defence_Of_The_Ancients'
lst = snake_style.split('_')
camelized_style = '%s%s%s%s' % (lst[0], lst[1], lst[2], lst[3])
print(camelized_style)

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



