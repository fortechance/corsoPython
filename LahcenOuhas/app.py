from Employee import Employee
Employee1 =Employee("lahcen", 25,"fastcloud", True, 5, 1500)
Employee2 =Employee("islam", 26, "facebook", False, 3.5, 500)

print(Employee1.name)
print(Employee2.name)
print(Employee1.age)
print(Employee2.age)
print(Employee1.rating)
print(Employee2.rating)



print(Employee1.salary)

Employee1.bonus()
print(Employee2.salary)
Employee2.bonus()