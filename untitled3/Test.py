"""
print("Hello !!!")
num = raw_input("please enter number:")
if num > 0:
    print "The number is greater than 0"
elif num ==0:
    print "The num is 0"
else:
    print "the numer is negative"

-----------------------------------------------------------------------------------
num1 = input ("Enter number 1:")
num2 = input ("Enter number 2:")
num3 = input ("Enter number 3:")

print "your numbers are:" + str(num1) + " "  + str(num2) + " " +  str(num3)
___________________________________________________________________________________

value = "abraka"
print(len(value))
__________________________________________________________________________________
pi = 3.14
print str(pi)

___________________________________________________________________________________

a=0
while a<10:
    a = a+1
    print a
_____________________________________________________________________________________

words = ['pu', 'window', 'dog']
for word in words:
    print word, len(word)
_____________________________________________________________________________________

word1 = raw_input ("Enter first word :")
word2 = raw_input ("Enter second word :")
word3 = raw_input ("Enter third word :")

print "all the words together:" + str(word1) + " " + str(word2) + " " + str(word3)
_____________________________________________________________________________________


def sum(num1, num2):        #function that sum 2 numbers
    return num1+num2

x = input ("Enter first number:")
y = input ("Enter second number:")

result = sum(x,y)
print "The result is = " + str(result)
_____________________________________________________________________________________


def sum(num1, num2):
    return num1+num2

def min(num1, num2):
    return num1-num2

def mult(num1, num2):
    return num1*num2

def div(num1, num2):
    return float(num1)/float(num2)

num1 = input ("Please enter the first number : ")
num2 = input ("Please enter your second number : ")
act = raw_input ("please choose your action:sum, min, mult, div : ")

if str(act) == 'sum':
    result = sum(num1,num2)
    print "The result is: " + str(result)
elif str(act) == 'min':
    result = min(num1,num2)
    print "The result is: " + str(result)
elif str(act) == 'mult':
    result = mult(num1,num2)
    print "The result is :" + str(result)
elif str(act) == 'div':
    result = div(num1,num2)
    print "The result is: " + str(result)
________________________________________________________________________________


size = int(raw_input("Enter the size: "))
char = raw_input("Enter the character to draw: ")
for i in range(1, size+1):
    print char*i

__________________________________________________________________________________


size = input("Enter the size: ")

for i in range(1, size+1):
    print " " * (size+1) + "X" * i

_____________________________________________________________________________________


size = input("Enter the size: ")
temp = size-1

for i in range(1, size+1):
    print (" " * temp) + ("X" * (i*2 -1))
    temp = temp-1
_____________________________________________________________________________________


size = input("Enter the size: ")

k=size
for i in range(1, size+1):
    print " " * (k) + "X" * i
    k = k-1
_____________________________________________________________________________________
#################### sort a list######################
a = [5, 2, 3, 1, 4]
a.sort()
print a

_______________________________________________________________________________________

############ implement sorting: #######################

list = [5, 2, 3, 1, 4, 9, 6]
small = list[0]
big = list[0]

for i in range(1,len(list)):

 if (list[i] > big):
    big = list[i]
 elif (list[i] < small):
    small = list[i]
print "The small number is: " + str(small)
print "The big number is: " + str(big)


_______________________________________________________________________________________________

user_input = raw_input("Please enter numbers separated by a single space only: ").strip()
list = [int(i) for i in user_input.split(' ')]
print list


small = list[0]
big = list[0]

for i in range(1,len(list)):

 if (list[i] > big):
    big = list[i]
 elif (list[i] < small):
    small = list[i]
print "The small number is: " + str(small)
print "The big number is: " + str(big)

___________________________________________________________________________________________

meal = 44.50
tax = 6.75 / 100
tip = 15.0 / 100

meal = meal + meal * tax
total = meal + (meal * tip)

print("%.2f" % total)
______________________________________________________________________________________________


# The string "PYTHON" has six characters,
# numbered 0 to 5, as shown below:
#
# +---+---+---+---+---+---+
# | P | Y | T | H | O | N |
# +---+---+---+---+---+---+
#   0   1   2   3   4   5
#
# So if you wanted "Y", you could just type
# "PYTHON"[1] (always start counting from 0!)

fifth_letter = "MONTY"[4]

print fifth_letter        #output=Y
_____________________________________________________________________


parrot = "norwegian Blue   Yes  "

print "The original string is : %s \n" % parrot
print "parrot.lower:" + parrot.lower()
print "parrot.upper:" + parrot.upper()
print "parrot.strip:" + parrot.strip()
print "parrot.split: %s" % parrot.split()
print "parrot.capitalize : " + parrot.capitalize()
print "parrot.isalnum: %s " % parrot.isalnum()
print "parrot.isdigit: %s " % parrot.isdigit()
print "parrot.isdigit: %s " % parrot.isalpha()
print "parrot.swapcase: %s " % parrot.swapcase()
print "parrot.replace %s " % parrot.replace('B','G')

__________________________________________________________________________

print "The value of pi is around " + str(3.14)

_____________________________________________________________________________________________________________________________________________________

string_1 = "Camelot"
string_2 = "place"

print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)         # The output is:  Let's not go to Camelot. 'Tis a silly place.

_______________________________________________________________________________________________________________________________________________________


name = raw_input("What is your name? ")
age = raw_input("What is your age? ")
color = raw_input("What is your favorite color? ")
print "Ah, so your name is %s, your age is %s ,and your favorite color is %s" % (name,age,color)
____________________________________________________________________________________________________________________________________________________

from datetime import datetime
now = datetime.now()

print '%s/%s/%s %s:%s:%s' % (now.month,now.day,now.year ,now.hour, now.minute, now.second)
_________________________________________________________________________________________________________

def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"

    answer = raw_input("Type left or right and hit 'Enter'.").lower()

    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
    else:
        print "You didn't pick left or right! Try again."
        clinic()

clinic()
__________________________________________________________________________________________________________

def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:
        return -1
    else:
        return 0


print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)

________________________________________________________________________________________________________________

# Pig Latin:

while True:
    wrd = raw_input("Give me a word: ")
    if len(wrd) > 1 and wrd.isalpha():
         pig = wrd[1:] + wrd[0] + "ay"
         print("The original string it's:", wrd, "in Pig Latin it's:", pig.lower())
         break
    else:
         print "Please insert at least 2 letters (only letters!)"
#____________________________________________________________________________________________________________________


pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
  print original
  word = original.lower()
  word2 =  word[0]
  print word2
else:
  print 'empty'
 __________________________________________________________________________________________


original = raw_input("Give me a word: ")

if len(original) > 1 and original.isalpha():
    pig = original[1:] + original[0] + "ay"
    print("The original string it's:", original, "in Pig Latin it's:", pig.lower())
    word = original.lower()
    first = word[0]
    print first
    new_word = original + first + pig
    print new_word
else:
    print "Please insert at least 2 letters (only letters!)"
_________________________________________________________________________________________


def tax(bill):
    #Adds 8% tax to a restaurant bill.
    bill *= 1.08
    print "With tax: %f" % bill
    return bill

def tip(bill):
    #Adds 15% tip to a restaurant bill.
    bill *= 1.15
    print "With tip: %f" % bill
    return bill

meal_cost = input("Please enter the meal cost:")

meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_cost)

___________________________________________________________________________________________

def square(n):
    #####Returns the square of a number.#####

    squared = n ** 2
    print "%d squared is %d." % (n, squared)
    return squared


# Call the square function on line 10! Make sure to
# include the number 10 between the parentheses.
square(10)
______________________________________________________________________________________________

def power(base, exponent):  # Add your parameters here!
  result = base ** exponent
  print "%d to the power of %d is %d." % (base, exponent, result)

power(37, 4)  # Add your arguments here!

________________________________________________________________________________________________

#Let's look at the two functions in the editor: one_good_turn (which adds 1 to the number it takes in as an argument) and deserves_another (which adds 2).

#Change the body of deserves_another so that it always adds 2 to the output of one_good_turn.

def one_good_turn(n):
    return n + 1

def deserves_another(n):
    return one_good_turn(n) + 2
_________________________________________________________________________________________________________________________

def shout(phrase):
  if phrase == phrase.upper():
    print "YOU'RE SHOUTING!"
  else:
    print "Can you speak up?"

shout("I'M INTERESTED IN SHOUTING")
________________________________________________________________________________________________________________________

def cube(number):
    return number**3


def by_three(number):
    if number % 3 == 0 :
         return cube(number)
    else :
         return False
________________________________________________________________________________________________________________________


def biggest_number(*args):
    print max(args)
    return max(args)


def smallest_number(*args):
    print min(args)
    return min(args)


def distance_from_zero(arg):
    print abs(arg)
    return abs(arg)


biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)
________________________________________________________________________________________________________________________

# Set maximum to the max value of any set of numbers on line 3!

maximum = max(2,4,6,8)
minimum = min(2,4,6,8)
absolute = abs(5)

print "The max number is:" ,maximum
print "The min number is:" ,minimum
print "The absiloute is:" ,absolute

________________________________________________________________________________________________________________________
#types:

print type(42)
print type(4.2)
print type(10000000000)
print type('spam')
________________________________________________________________________________________________________________________

def shut_down(s):
  if s == "yes":
    return "Shutting down"
  elif s == "no":
    return "Shutdown aborted"
  else:
    return "Sorry"
________________________________________________________________________________________________________________________
# find shoresh (sqrt)

from math import sqrt

print sqrt(9)
________________________________________________________________________________________________________________________


def distance_from_zero(num):

    if type(num) == int or type(num) == float:
       print abs(num)
    else:
       print "Nope"

distance_from_zero('a')
________________________________________________________________________________________________________________________


def hotel_cost(city, nights):
    return (city * nights)


def plane_ride_cost(city,nights):
    if city == "Charlotte":
      return hotel_cost(183,nights)
    elif city == "Tampa":
        return hotel_cost(220, nights)
    elif city == "Pittsburgh":
        return hotel_cost(222, nights)
    elif city == "Los Angeles":
        return hotel_cost(475, nights)
    else:
        print "we don't have this city"


city_input = raw_input("please enter the name of the city (Charlotte/Tampa/Pittsburgh/Los Angeles) - ")
num_input = input("Please enter the number of nights:")

ans = plane_ride_cost(city_input, num_input)
print ans
________________________________________________________________________________________________________________

# def plane_ride_cost(city):
#     if city == "Charlotte":
#       return 183
#     elif city == "Tampa":
#        return 220
#     elif city == "Pittsburgh":
#        return 222
#     elif city == "Los Angeles":
#        return 475
#     else:
#        print "we don't have this city"
__________________________________________________________________________________________________________________

def rental_car_cost(days):

  if days >= 3 and days < 7:
      calc = (40 * days) - 20
  elif days >= 7:
      calc = (40 * days) - 50
  else:
      calc = 40 * days

  return calc

days = input("Please enter number of days for renting a car:")
print rental_car_cost(days)
_________________________________________________________________________________________________________________
######### LISTS #######################

zoo_animals = ["pangolin", "cassowary", "sloth", "Lion" ];
# One animal is missing!

if len(zoo_animals) > 3:
  print "The first animal at the zoo is the " + zoo_animals[0]
  print "The second animal at the zoo is the " + zoo_animals[1]
  print "The third animal at the zoo is the " + zoo_animals[2]
  print "The fourth animal at the zoo is the " + zoo_animals[3]

________________________________________________________________________________________________________________


suitcase = []
suitcase.append("sunglasses")

# Your code here!
suitcase.append("book")
suitcase.append("disc")
suitcase.append("phone")

list_length = len(suitcase)     # Set this to the length of suitcase

print "There are %d items in the suitcase." % (list_length)
print suitcase

# Output:
# There are 4 items in the suitcase.
# ['sunglasses', 'book', 'disc', 'phone']
_______________________________________________________________________________________________________________


letters = ['a', 'b', 'c', 'd', 'e']
slice = letters[1:3]
print slice
print letters
________________________________________________________________________________________________________________

suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

# The first and second items (index zero and one)
first = suitcase[0:2]

# Third and fourth items (index two and three)
middle =  suitcase[2:4]

# The last two items (index four and five)
last =  suitcase[4:]
___________________________________________________________________________________________________________________

animals = ["ant", "bat", "cat"]
print animals.index("cat")
animals.insert(1, "dog")
print animals
print animals.index("dog")

# Output:
# 2
# ['ant', 'dog', 'bat', 'cat']
# 1
______________________________________________________________________________________________________________________

animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]

#find the index of "duck"
duck_index = animals.index("duck")

# Your code here!
animals.insert(duck_index, "cobra")

print animals # Observe what prints after the insert operation
_____________________________________________________________________________________________________________________


my_list = [1,9,3,8,5,7]

for number in my_list:
  # Your code here
    print (2*number)
_______________________________________________________________________________________________________________________

start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for mult in start_list:
    square_list.append(mult**2)

square_list.sort()
print square_list
________________________________________________________________________________________________________________________


d = {'key1' : 1, 'key2' : 2, 'key3' : 3}
print d['key3'],d['key2'],d['key1']

________________________________________________________________________________________________________________________

# Assigning a dictionary with three key-value pairs to residents:

residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Sloth'],residents['Burmese Python']        # Prints Puffin's room number

_____________________________________________________________________________________________________________________


menu = {}                               # Empty dictionary
menu['Chicken Alfredo'] = 14.50         # Adding new key-value pair
print menu['Chicken Alfredo']

# Your code here: Add some dish-price pairs to menu!
menu['flan'] = 10.50
menu['mous'] = 8.0

print "There are " + str(len(menu)) + " items on the menu."
print menu

_______________________________________________________________________________________________________________________


# key - animal_name : value - location
zoo_animals = {
  'Unicorn' : 'Cotton Candy House',
  'Sloth' : 'Rainforest Exhibit',
  'Bengal Tiger' : 'Jungle House',
  'Atlantic Puffin' : 'Arctic Exhibit',
  'Rockhopper Penguin' : 'Arctic Exhibit'
}
# A dictionary (or list) declaration may break across multiple lines
print "the dictionart before the edit: ",zoo_animals
# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

# Your code here!
del zoo_animals['Bengal Tiger']
del zoo_animals['Sloth']

zoo_animals['Rockhopper Penguin'] = 'Lol'

print "the dictionary after edit: ", zoo_animals

________________________________________________________________________________________________________________________

beatles = ["john","paul","george","ringo","stuart"]
beatles.remove("stuart")
print beatles
_______________________________________________________________________________________________________________________
# dictionary can holds many types of values and not just 1

my_dict = {
  "fish": ["c", "a", "r", "p"],
  "cash": -4483,
  "luck": "good"
}
print my_dict["fish"][0]
_____________________________________________________________________________________________________________________


inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],                   # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['gold'] = 550

# Sorting the list found under the key 'pouch'
inventory['backpack'].sort()

# Your code here
inventory['backpack'].remove('dagger')
______________________________________________________________________________________________________________________
# for loop on a list #

names = ["Adam","Alex","Mariah","Martine","Columbus"]
for a in names:
		print a
______________________________________________________________________________________________________________________
# for loop on a dictionary to loop through its keys #

webster = {
  "Aardvark" : "A star of a popular children's cartoon show.",
  "Baa" : "The sound a goat makes.",
  "Carpet": "Goes on the floor.",
  "Dab": "A small amount."
}

for key in webster:
  print webster[key]
________________________________________________________________________________________________________________________

numbers = [1, 3, 4, 7]
for number in numbers:
  if number > 6:
    print number
________________________________________________________________________________________________________________________
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for number in a:
	if number % 2 == 0:         # (check if number is even)
  	 print number


#### output: 0,2,4,6,8,10,12  ####

________________________________________________________________________________________________________________________


##### Functions can also take lists as inputs and perform various operations on those lists. ###

def count_small(numbers):
  total = 0
  for n in numbers:
    if n < 10:
      total = total + 1
  return total

lotto = [4, 8, 1, 16, 23, 42]
small = count_small(lotto)
print small
_______________________________________________________________________________________________________________________

def fizz_count(str_list):
    count = 0

    for item in str_list:
        if item == string_search:
            count += 1
    return count

string_search = "fizz"
appear_count = fizz_count(["fizz","cat","fizz"])
print appear_count

_______________________________________________________________________________________________________________________


for letter in "Codecademy":       # if you write: for letter in "Codecademy",:  - it print the letters in the same line
    print letter

# Empty lines to make the output pretty
print
print

word = "Programming is fun!"

for letter in word:
    # Only print out the letter i
    if letter == "i":
        print letter
_______________________________________________________________________________________________________________________

lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]


print lloyd.keys()
print lloyd.values()
print lloyd["name"]
print lloyd["tests"]

_______________________________________________________________________________________________________________________

prices = {
    "banana": 8,
    "apple": 2.5,
    "orange": 12,
    "pear": 5
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

for key in prices.keys():

  print "Fruit: %s"  % key
  print "Prices: %s" % prices[key]
  print "Stock: %s" % stock[key]

total = 0

for key in prices:
    calc = prices[key]*stock[key]
    total = total + calc


print total
_______________________________________________________________________________________________________________________

def sum(numbers):
  total = 0
  for number in numbers:
    total += number
  return total

n = [1, 2, 5, 10, 13]
print sum(n)

________________________________________________________________________________________________________________________


food_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# def compute_bill(food_list):
#     total = 0
#     for i in food_list:
#         total += prices[i]
#     return total

def compute_bill(food_list):
    total = 0
    for i in food_list:
        if i in prices.keys() and i in stock.keys():
            total += prices[i] * stock[i]

    print total

compute_bill(food_list)
________________________________________________________________________________________________________________________


# lloyd = {
#   "name": "Lloyd",
#   "homework": [90.0, 97.0, 75.0, 92.0],
#   "quizzes": [88.0, 40.0, 94.0],
#   "tests": [75.0, 90.0]
# }
# alice = {
#   "name": "Alice",
#   "homework": [100.0, 92.0, 98.0, 100.0],
#   "quizzes": [82.0, 83.0, 91.0],
#   "tests": [89.0, 97.0]
# }
# tyler = {
#   "name": "Tyler",
#   "homework": [0.0, 87.0, 75.0, 22.0],
#   "quizzes": [0.0, 75.0, 78.0],
#   "tests": [100.0, 100.0]
# }
#
# students = [lloyd, alice, tyler]
#
# for name in students:
#
#     print name["name"]
#     print name["homework"]
#     print name["quizzes"]
#     print name["tests"]

______________________________________________________________________________________________________________________

def average(numbers):
    total = sum(numbers)

    res = float(total)/len(numbers)
    print res

numbers = [3,1]

average(numbers)
________________________________________________________________________________________________________________________

________________________________________________________________________________________________________________________
#####  Dictionary / List actions ##########

# print lloyd.keys()
# print lloyd.values()
# print lloyd["name"]
# print lloyd["tests"]
#

# list = [1,3,5,7,9]
# print len(list)
#______________________________________________________________________________________________________________________


lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

students = [lloyd,alice,tyler]

def get_average(student):
    hw = (tyler["homework"] + alice["homework"] + lloyd["homework"])
    number_hw = len(hw)
    homework = sum(hw) / number_hw
    print homework

get_average(students)
________________________________________________________________________________________________________________________
Now let's write a get_letter_grade function that takes a number score as input and returns a string with the letter grade that that student should receive:

lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

# Add your function below!
def average(numbers):
  total = sum(numbers)
  total = float(total)
  return total/len(numbers)

def get_average(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  return 0.1 * homework + 0.3 * quizzes + 0.6 * tests

def get_letter_grade(score):
  if score >= 90:
    return "A"
  elif score >=80:
    return "B"
  elif score >=70:
    return "C"
  elif score >=60:
    return "D"
  else:
    return "F"

print get_average(lloyd)

________________________________________________________________________________________________________________________

def get_letter_grade(score):

        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"

score = True

while True:

    score = input("Please insert a numbers (for stop insert '0'): ")
    if score != 0:
         get = get_letter_grade(score)
         print get
    else:
         break

________________________________________________________________________________________________________________________
###########   LISTS    #############

n = [1, 3, 5]

mult = n[1]*5
n[1] = mult

print n
___________________________________________________________________________

n = [1, 3, 5]
# Append the number 4 here

n.append(4)
print n
_________________________________________________________________________


#############################   Removing elements from lists  ################################

##### n.pop(index) will remove the item at index from the list and return it to you: ####

n = [1, 3, 5]

n.pop(1)
# Returns 3 (the item at index 1)
print n
# prints [1, 5]


#####  n.remove(item) will remove the actual item if it finds it:  ####

n.remove(1)
# Removes 1 from the list,
# NOT the item at index 1
print n
# prints [3, 5]


##### del(n[1]) is like .pop in that it will remove the item at the given index, but it won't return it:  #####

del(n[1])
# Doesn't return anything
print n
# prints [1, 5]

____________________________________________________________________________________________________________________

m = 5
n = 13

def add_function(m, n):
    return m + n

print add_function(m, n)
___________________________________________________________________________________________________________________


n = "Hello"

def string_function(n):
    str = "%s world !" % n
    return str

print string_function(n)
____________________________________________________________________________________________________________________

# def list_function(x):
#     return x
#
# n = [3, 5, 7]
#
# print list_function(n)
#

###### Output: [3, 5, 7]

_____________________________________________________________________________________________________________________


n = [3, 5, 7]

def list_function(n):
    n[1] = n[1] + 3
    return n

print list_function(n)
______________________________________________________________________________________________________________________

lst = [3, 5, 7]

def list_extender(lst):
    lst.append(4)
    return lst

print list_extender(lst)


############ output: [3, 5, 7, 4]  ############
______________________________________________________________________________________________________________________


n = [3, 5, 7]

def print_list(n):
    for i in range(0, len(n)):
        print n[i]

print_list(n)

________________________________________________________________________________________________________________________


x = [3, 5, 7]

def double_list(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print double_list(x)
_______________________________________________________________________________________________________________________
#############      Range    ##################

print range(6)              # => [0, 1, 2, 3, 4, 5]            # range(stop)

print range(1, 6)           # => [1, 2, 3, 4, 5]               # range(start, stop)

print range(1, 6, 3)        # => [1, 4]                        # range(start, stop, step)

_______________________________________________________________________________________________________________________


def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print my_function(range(3))
______________________________________________________________________________________________________________________

list = [3, 5, 7]

### There are two ways of iterating through a list.
for item in list:
  print item,
----------------------------
for i in range(len(list)):
  print list[i],
______________________________________________________________________________________________________________________

########################    Reverse funcion   ###############

def rev(word):
     return word[::-1]

reverse = rev("1234")
print reverse

reverse = rev("tomer")
print reverse
"""
# ______________________________________________________________________________

