

class Employee(object):
    count = 0

    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position
        Employee.count +=1

    def get_salary(self):
        print ("Your salary is {0}".format(self.salary))

    def update_salary(self, salary):
        self.salary = salary

    def get_employee(self):
        return ("{0} his salary is {1} and position is {2}".format(self.name, self.salary, self.position))

    def employee_number(self):
        return Employee.count


emp1 = Employee("roman", 1000, "cyber")
emp2 = Employee("david", 5000, "cyber")
emp3 = Employee("noa", 10000, "cyber")

print (emp1.employee_number())
print (emp1.name)

print (emp2.employee_number())
print (emp2.name)

print (emp3.employee_number())
print (emp3.name)