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

print("======================")
