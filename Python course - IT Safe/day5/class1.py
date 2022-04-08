
class Employee(object):
    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position

    def get_salary(self):
        print ("Your salary is {0}".format(self.salary))

    def update_salary(self, salary):
        self.salary = salary

    def get_employee(self):
        return ("{0} his salary is {1} and position is {2}".format(self.name, self.salary, self.position))

emp1 = Employee("roman", 1000, "cyber")
my_emp = emp1.get_employee()
print (my_emp)

emp1.get_salary()
emp1.update_salary(2000)
emp1.get_salary()

emp2 = Employee("david", 5000, "cyber")
my_emp2 = emp2.get_employee()
print (my_emp2)

emp2.get_salary()
emp2.update_salary(10000)
emp2.get_salary()
