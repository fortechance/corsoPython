class Employee:
    def __init__(self, name, age, department, manager, rating, salary):
        self.name = name
        self.age = age
        self. department = department
        self. manager = manager
        self.rating = rating  #rating is from 1-5
        self. salart= salary 

def is_excellent(self):
    if self.rating >=4.5:
        return True
    
    else:
        return False
    
    
def bonus(self):
    if self.age == 26:
        self.salary += 500
        print("salary increased to "+str(self.salary))
    else:
        print("no bonus added, salary is still " +str(self.salary))