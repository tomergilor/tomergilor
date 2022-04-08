"""
______________________________________________________________________________

class Complex:
    def __init__(self,real,im):
        self.r = real
        self.i = im

    def show(self):
        print str(self.r) + "+" + str(self.i) + "I"

    def add(self,tomer):
        total_r = self.r + tomer.r
        total_i = self.i + tomer.i
        return Complex(total_i,total_r)


x = Complex(3,5)
x.show()
y = Complex(9,1)
z = x.add(y)
z.show()
_____________________________________________________________________________


class Point2D():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line2D(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def get_distance(self):
        x1 = self.p1.x
        y1 = self.p1.y
        x2 = self.p2.x
        y2 = self.p2.y
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def my_test():
    p1 = Point2D(10, 20)
    p2 = Point2D(30, 40)
    l1 = Line2D(p1, p2)
    print l1.get_distance()

class Point3d(Point2D):
    z=0

    def setZ(self, z):
        self.z= z


my_test()

_____________________________________________________________________________________________________


class Fruit(object):

  def __init__(self, name, color, flavor, poisonous):
    self.name = name
    self.color = color
    self.flavor = flavor
    self.poisonous = poisonous


  def description(self):
    print "I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor)

  def is_edible(self):
    if not self.poisonous:
      print "Yep! I'm edible."
    else:
      print "Don't eat me! I am super poisonous."


lemon = Fruit("lemon", "yellow", "sour", False)
melon = Fruit("melon", "Green", "sweet", False)
Kikyon = Fruit("Kikyon","gray","sour", True)


lemon.description()
lemon.is_edible()
melon.description()
melon.is_edible()
Kikyon.description()
Kikyon.is_edible()

___________________________________________________________________________________

class Animal(object):
    def __init__(self,name):
        self.name = name


zebra = Animal("Jeffrey")
print zebra.name

___________________________________________________________________________________

# Class definition
class Animal(object):
    ###Makes cute animals.

    # For initializing our instance objects
    def __init__(self, name, age, is_hungry):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry


# Note that self is only used in the __init__()
# function definition; we don't need to pass it
# to our instance objects.

zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

print zebra.name, zebra.age, zebra.is_hungry
print giraffe.name, giraffe.age, giraffe.is_hungry
print panda.name, panda.age, panda.is_hungry

_____________________________________________________________________________________


class Animal(object):

  is_alive = True
  def __init__(self, name, age):
    self.name = name
    self.age = age

zebra = Animal("Jeffrey", 2)
giraffe = Animal("Bruce", 1)
panda = Animal("Chad", 7)

print zebra.name, zebra.age, zebra.is_alive
print giraffe.name, giraffe.age, giraffe.is_alive
print panda.name, panda.age, panda.is_alive

_________________________________________________________________________________________


class Animal(object):

    is_alive = True
    health = "good"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        print self.name
        print self.age


hippo = Animal('Anderson', 36)
hourse = Animal('Dale', 15)
bird = Animal('Fuzzy', 7)

print hippo.health
print hourse.health
print bird.health
print hippo.is_alive
hippo.is_alive = False
print hippo.is_alive

print bird.name
print bird.age

___________________________________________________________________________________


class ShoppingCart(object):

  items_in_cart = {}

  def __init__(self, customer_name):
    self.customer_name = customer_name

  def add_item(self, product, price):
    ###   Add product to the cart.

    if not product in self.items_in_cart:
      self.items_in_cart[product] = price
      print product + " added."
    else:
      print product + " is already in the cart."

  def remove_item(self, product):
    ###   Remove product from the cart.

    if product in self.items_in_cart:
      del self.items_in_cart[product]
      print product + " removed."
    else:
      print product + " is not in the cart."



my_cart = ShoppingCart('Tomer')

my_cart.add_item("Banana",10)
___________________________________________________________________________________


class Customer(object):
  ###Produces objects that represent customers.
  def __init__(self, customer_id):
    self.customer_id = customer_id

  def display_cart(self):
    print "I'm a string that stands in for the contents of your shopping cart!"


class ReturningCustomer(Customer):
  ###For customers of the repeat variety.

  def display_order_history(self):
    print "I'm a string that stands in for your order history!"

monty_python = ReturningCustomer("ID: 12345")

monty_python.display_cart()
monty_python.display_order_history()

__________________________________________________________________________________


class Shape(object):
  ###   Makes shapes!
  def __init__(self, number_of_sides):
    self.number_of_sides = number_of_sides


class Triangle(Shape):
  def __init__(self, side1, side2, side3):
   self.side1 = side1
   self.side2 = side2
   self.side3 = side3


___________________________________________________________________________________



class Employee(object):
  def __init__(self, name):
    self.name = name
  def greet(self, other):
    print "Hello, %s" % other.name

class CEO(Employee):
  def greet(self, other):
    print "Get back to work, %s!" % other.name

ceo = CEO("Emily")
emp = Employee("Steve")


emp.greet(ceo)          # Hello, Emily
ceo.greet(emp)          # Get back to work, Steve!
___________________________________________________________________________________________________________________________
# Create a new class, PartTimeEmployee, that inherits from Employee.
# Give your derived class a calculate_wage method that overrides Employee's. It should take self and hours as arguments.
# Because PartTimeEmployee.calculate_wage overrides Employee.calculate_wage, it still needs to set self.hours = hours.
# It should return the part-time employee's number of hours worked multiplied by 12.00 (that is, they get $12.00
# per hour instead of $20.00).
# Hint:
# In the example code above, we created an overriding CEO.greet method. It had the same arguments as Employee.greet.
# You'll want to add a calculate_wage() method to your PartTimeEmployee class, and it should also take self and hours as'
# arguments. Instead of returning hours * 20.00, though, it should return hours * 12.00.
#----------------------------

class Employee(object):

    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

class PartTimeEmployee(Employee):

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 12.00

emp = Employee('Tom')
part_emp = PartTimeEmployee('Dan')

print emp.employee_name
print emp.calculate_wage(200)
print part_emp.employee_name
print part_emp.calculate_wage(200)

_______________________________________________________________________________________________________

class Employee(object):

    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00

    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours)

milton = PartTimeEmployee('Milton')
print milton.full_time_wage(10)


# emp = Employee('Tom')
# part_emp = PartTimeEmployee('Dan')
#
# print emp.employee_name
# print emp.calculate_wage(200)
# print part_emp.employee_name
# print part_emp.calculate_wage(200)

____________________________________________________________________________________

# Inside the Triangle class:
# Create a variable named number_of_sides and set it equal to 3.
# Create a method named check_angles. The sum of a triangle's three angles should return True if
# the sum of self.angle1, self.angle2, and self.angle3 is equal 180, and False otherwise.


class Triangle(object):
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    number_of_sides = 3

    def check_angles(self):
        if (self.angle1 + self.angle2 + self.angle3 == 180):
            return True
        else:
            return False

tri = Triangle(60,60,60)

print tri.check_angles()

__________________________________________________________________________________________________________

# Create a variable named my_triangle and set it equal to a new instance of your Triangle class.
# Pass it three angles that sum to 180 (e.g. 90, 30, 60).
# # Print out my_triangle.number_of_sides
# # Print out my_triangle.check_angles()

class Triangle(object):
    number_of_sides = 3

    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self):
        if (self.angle1 + self.angle2 + self.angle3) == 180:
            return True
        else:
            return False

my_triangle = Triangle(30, 60, 90)

print my_triangle.number_of_sides
print my_triangle.check_angles()

class Equilateral(Triangle):
    angle = 60

    def __init__(self):
       self.angle1 = self.angle
       self.angle2 = self.angle
       self.angle3 = self.angle

________________________________________________________________________________________

# Class basics:
# Classes can be very useful for storing complicated objects with their own methods and variables.
# Defining a class is much like defining a function, but we use the class keyword instead.
# We also use the word object in parentheses because we want our classes to inherit the object class.
# This means that our class has all the properties of an object, which is the simplest, most basic class.
# Later we'll see that classes can inherit other, more complicated classes. An empty class would look like this:

# Below your Car class, create a new object named my_car that is an instance of Car.

class Car(object):
    condition = "new"

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

    def display_car(self):
        print "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))

    def drive_car(self):
        self.condition = "used"

class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        self.model = model
        self.color = color
        self.mpg   = mpg
        self.battery_type = battery_type

    def drive_car(self):
        self.condition = 'like new'

my_car = ElectricCar("DeLorean", "silver", 88, "molten salt")

#my_car = Car("DeLorean", "silver", 88)

print my_car.condition
my_car.drive_car()
print my_car.condition
#print my_car.battery_type
#my_car.display_car()

______________________________________________________________________________________________________

class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "%d,%d,%d" % (self.x, self.y, self.z)


my_point = Point3D(1,2,3)

print my_point

_______________________________________________________________________________________________________

class MyClass(object):

    def set_val(self, val):
        self.value = val

    def get_val(self):
        return self.value

a = MyClass
b = MyClass

a.set_val(10)
b.set_val(100)
a.value = 'hello'

print (a.get_val())
print (b.get_val())
_____________________________________________________________________________________________________


class Joe(object):
    def callme(self):
        print ('calling "callme" method with instance:')
        print (self)

thisjoe = Joe()

thisjoe.callme()
______________________________________________________________________________________________________


class MyClass(object):
    def dothis(selfself):
        print ('doing this')

myinst = MyClass()
myinst.dothis()
______________________________________________________________________________________________________

import random

class MyClass(object):
    def dothis(self):
        self.rand_val = random.randint(1,10)

myinst = MyClass()
myinst.dothis()

print (myinst.rand_val)

________________________________________________________________________________________________________


class InstanceCounter(object):
    count = 0

    def __init__(self, val):
        self.val = val
        InstanceCounter.count += 1

    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        return self.val

    def get_count(self):
        return InstanceCounter.count

a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)
d = InstanceCounter(20)

for obj in (a,b,c,d):
    print "val of obj: %s" %(obj.get_val())         #Initialized value (5,13,etc...)
    print "count: %s" % (obj.get_count())           # Always 4

# Output:
#--------
# val of obj: 5
# count: 4
# val of obj: 13
# count: 4
# val of obj: 17
# count: 4
# val of obj: 20
# count: 4
#

___________________________________________________________________________________________________________________
class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

# print(emp_1 + emp_2)

print(len(emp_1))
_______________________________________________________________________________________________


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith')

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

_____________________________________________________________________________________________________________________


class Date(object):             # inherits from the 'object' class (will discuss shortly)
    def get_date(self):
        return '2014-10-13'

class Time(Date):               #inherits from the 'Date' class
    def get_time(self):
        return '08:13:07'

dt = Date()

print (dt.get_date())

tm = Time()

print (tm.get_time())

print (tm.get_date())         #found this methos in the 'Date' class

_________________________________________________________________________________________________________________


class Animal(object):
    def __init__(self,name):
        self.name = name

    def eat(self, food):
        print '%s goes after the %s!' % (self.name, food)

class Dog(Animal):
    def fetch(self, thing):
        print '%s goes after the %s!' % (self.name, thing)

class Cat(Animal):
    def swatstring(self):
        print '%s shreds the string!' % (self.name)

d = Dog('Tulip')
c = Cat('Mitzi')

d.fetch('paper')        #Tulip goes after the paper!
c.swatstring()          #Mitzi shreds the string!
d.eat('dog food')       #Tulip is eating dog
c.eat('cat food')       #Mitzi is eating cat food.
#d.swatstring()      # AttributeError: 'Dog' object has no attribute 'swatstring'


_____________________________________________________________________________________________________________

class Point2D(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_abc(self):
        print '2D'

    def get_def(self):
        print '2D'


class Point3D(Point2D):
    def __init__(self, x, y, z):
        self.z = z
        super(Point3D, self).__init__(x, y)

    def get_def(self):
        print '3D'

    def get_tyu(self):
        print '3D'


p3 = Point3D(1, 2, 3)
p3.get_abc()
# p2 = Point2D(1, 2)
_____________________________________________________________________________________________________

# Super Class Car

class Car(object):

    def __init__(self, car_type, color):

        self.car_type = car_type
        self.color = color

    def drive(self):
        print "Driving my %s %s" % (self.color, self.car_type)

    def park(self):
        print "Parked the car"

# Sub Class of Car called Honda

class Honda(Car):
    def __init__(self, color):

        super(Honda, self).__init__("Honda", color)

mycar = Car("Toyota", "yellow")
myHonda = Honda("Green")

mycar.drive()
myHonda.drive()
print myHonda.color0

__________________________________________________________________________________________________


class Employee(object):
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        return int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super(Developer, self).__init__(first, last, pay)
        self.prog_lang = prog_lang

emp_1 = Employee('Tom','Cohen', 20000)
emp_2 = Employee('Dan', 'Levi', 10000)
dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

print (dev_1.first, dev_1.last, dev_1.pay,dev_1.prog_lang, dev_1.email, dev_1.apply_raise())
print (dev_2.first, dev_2.last, dev_2.pay,dev_2.prog_lang, dev_2.email, dev_2.apply_raise())

print (emp_1.first)
print (emp_1.last)
print (emp_1.email)
print (emp_1.pay)
print emp_1.apply_raise()


_____________________________________________________________________________________________


class Employee(object):

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):

    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super(Developer, self).__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
        super(Manager, self).__init__(first, last, pay)

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
        else: print "The employee is exist already"

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
        else: print "There is no employss with this name"

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev_1 = Developer('Dan', 'Cohen', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')
dev_3 = Developer('Avi', 'Levy', 70000, 'C#')
mgr_1 = Manager('Sue', 'Smith', 90000, [])

print "----------Before remove Dev1 (Dan)---------- "
mgr_1.print_emps()

mgr_1.add_emp(dev_1)
mgr_1.add_emp(dev_2)
mgr_1.add_emp(dev_3)
mgr_1.print_emps()
print "--------- After remove Dev1 ----------------"
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

______________________________________________________________________________________

"""





















