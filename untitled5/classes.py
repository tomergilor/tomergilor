"""
class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total employees %d" % Employee.empCount

    def displayEmployee(self):
        print "Name: " , self.name, ",Salary:" , self.salary

emp1 = Employee("Bob", 10000)
emp2 = Employee("Dan", 20000)

emp1.displayEmployee()
emp2.displayEmployee()

emp1.displayCount()
emp2.displayCount()

__________________________________________________________________


class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def setWidthHeight(self, w, h):
        self.width = w
        self.height = h

    def displayMe(self):
        print "My height: ",self.height, ", My width:" , self.width


r1 = Rectangle(10,20)
r2 = Rectangle(40,60)

r1.setWidthHeight(2,4)
r1.displayMe()

r1.displayMe()
r2.displayMe()
___________________________________________________________________________________
"""

