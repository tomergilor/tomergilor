# loop = True
# counter = 0
#
# list = []
#
# while (loop == True):
#     var = raw_input("Please enter something: ")
#
#     if var != "-1":
#        list.append(int(var))
#     elif(var == "-1"):
#         loop = False
#
# print list
# =====================================================
#
# passwordFile = open('SecretPasswordFile.txt')
# secretPassword = passwordFile.read()
# print('Enter your password.')
# typedPassword = input()
# if typedPassword == secretPassword:
#     print('Access granted')
# if typedPassword == '12345':
#     print('That password is one that an idiot puts on their luggage.')
# else:
#      print('Access denied')
# _________________________________________________________________________
# # create new file named tttt
# # it's necessary to add permission
# # r=read , w=write, a=append, r+ = read+write
#
# my_file = open("tttt.file","w")
# #my_file.close()
#
# #to write to the file
#
# my_file.write(" this is test")
# my_file.close()
# _________________________________________________________________________________
# #to add(not  replace) to the text
# my_file = open("tttt.file","a")
# my_file.write(" this is test2")
# my_file.close()
# _________________________________________________________________________________
# #to read from file
# my_file = open("tttt.file","r")
# print my_file.read()
# my_file.close()
# _________________________________________________________________________________
# # to read from the file
# my_file = open("tttt.file","r")
# print my_file.read()
# my_file.close()
# _________________________________________________________________________________
# # to find word in the file and how much times
# count =0
# my_file = open("tttt.file","r")
# for line in my_file:
#     if("this" in line):
#         count = count + 1
#
# print "the word found " + str(count) + " times "
#
# _________________________________________________________________________________
# # to find any word(this) and print the line it shown
# my_file = open("tttt.file","r")
# for line in my_file:
#     if("this" in line):
#        print "found",line
#
# _________________________________________________________________________________
# # run loop from 1-50 and if find the number 20 stop the loop and write "found it"
# for number in range(1,50):
#     print number
#     if number == 20:
#         print "found it"
#         break
# _________________________________________________________________________________
# #enter numbers 1-100 to continue and 100-200 to stop the loop
# print ("press 1-100 to continue\n"
#       "press 100-200 to exit")
#
# while True:
#     number = int(raw_input("inset number: "))
#     if number >= 1 and number <= 100:
#         print "another loop"
#     elif number >100 and number < 200:
#         print "stop loop"
#         break
#     else:
#         print "wrong number"
# _________________________________________________________________________________
# # While loop counting 1 to 50
# number=1
# while number<51:
#     print number
#     number=number+1  #it's possible to write this line also: number+=1
# _________________________________________________________________________________
#
# #insert number while the number is not 0
# number = 1
# while number !=0:
#     number = int(raw_input("inset number:(to stop click 0):"))
#     if number >= 1:
#         print "The number bigger than 0"
#     elif number < 0:
#         print "The number smaller than 0"
# print "the number is 0"
# _________________________________________________________________________
#
# # list and array
# List = [22,55,32,66,89,5]
# print List
#
# #add number to the List
# List.append(465)
# print List
#
# # replace the first number to 1
# List [0] = 1
# print List
#
# #sort the list
# List.sort()
# print List
#
# #show the index of specific number
# print List.index(66)
#
# List = [22,55,32,66,89,5]
# print List
#
# #remove number 66 fron the list
# List.remove(66)
#
# #to show the List Length (6)
# print len(List)
#
# #go over all the port of the list
# for port in List:
#     print port
#
# # set arr - this is another type of list(array) that exist in python. this is list that each number can appears ones
# #it means that its impossible add the same number twice
# #set
#
# setlist = {1,5,7,22,55}
# print setlist
#
# #remove from set list
# setlist.remove(7)
# print setlist
#
# setlist.add(27)
# print setlist
#
#
# # dictenary
# # another type of lisr(array) that can define list with values.
# # f.e - A=1, B=2, C=3

#
# dict = {'ssh':22,'telnet':23,'ftp':21}
# print dict
#
# #print the ssh value
# print dict['ssh']
#
# #add value
# #dict ['http'] =80
#
# #delete value from dict
# #del list['telnet']
#
# #print all keys from dic
# print dict.keys()
#
# #print all values from dict
# print dict.values()
#
############################################################################

#Function: example for add and min functions with user input

# def add(num1,num2):
#     add=num1+num2
#     return add
#
# def min(num1,num2):
#     min=num1-num2
#     return min
#
#
# #use the functions with input from the user
# act = int(raw_input(" Please choose sum or min (1-for add and 2-for min: "))
# if act == 1:
#     num1 = int(raw_input("Please enter the first number: "))
#     num2 = int(raw_input("Please enter the second number: "))
#     sum = add(num1,num2)
#     print "The sum is: %d "% (sum)
#
# elif act==2:
#     num1 = int(raw_input("Please enter the first number: "))
#     num2 = int(raw_input("Please enter the second number: "))
#     sum = min(num1,num2)
#     print "The sum is: %d"% (sum)
###################################################################################

# program that input from the user 10 numbers and calc and print the biggest number:
#
# str_num = []
# k = 1
# max = 0
#
# for i in range(0,10):
#     num = int(raw_input("Please enter a number: "))
#
#     str_num.append(int(num))
#
# for j in range(0,10):
#
#     if str_num[j] > str_num[k]:
#         max = str_num[j]
#         str_num[j] = str_num[k]
#         str_num[k] = max
#
# print "The biggest number is: %d" %(max)
#
###################################################################################
# # The program choose 7 numbers randomaly and sum all the numbers. if the sum devided by 7 print also BOOM!
#
# from random import randint
# num = 0
#
# list = []
#
# for i in range(0,7):
#     num = num + randint(0, 100)
#
# print num
# if num % 7 == 0:
#     print "BOOM !"
####################################################################################
# # Program that get rand number and return the sum of the numbers f.e = 34 return 7
# from random import randint
# sum=0
#
# num = randint(10, 100)
#
# num_str = str(num)
# print num_str
#
#
# for c in num_str:
#     sum = sum + int(c)
#
# print sum
########################################################################################
#
#
# Write a program that reads 10 numbers from
# the user and prints the largest one
#
#
# max_number = int(raw_input("Enter number:"))
#
# for X in range(9):
#     num = int(raw_input("Enter number:"))
#     if num > max_number:
#         max_number = num
#
# print "Max number = %d" % max_number
#
# ######################################################################################
#
# """
# Write a Python program that randomizes 7 numbers
# and prints their sum total.
# If the sum is divisable by 7, also print the word "Boom"
# """
#
# from random import randint
#
# total = 0
#
# for _ in range(7):
#     num = randint(1,100)
#     total += num
#
# print "Total sum is: %d" % total
# if total % 7 == 0: print "Boom!"
#########################################################################################
"""
Write a program that reads lines from the user until an empty line is inserted.
After the user typed in an empty line, print all previously inserted lines in reverse
order (from last to first)
"""
#
# text = ""
#
# while True:
#     line = raw_input("Enter text:")
#     text = line + "\n" + text
#     if len(line) == 0: break
#
# print text
#
#
#
# number = 0
# list = []
# loop = True
#
# while (loop == True):
#     number = raw_input("Please enter a number: ")
#
#     if number != "-1":
#        list.append(int(number))
#     elif number == "-1":
#        loop = False
#
# print list
###############################################################################
## Guess a random number from the computer
# from random import randint
#
# num = randint(1,100)
#
# while True:
#      guess = raw_input("Hi, please guess the number between 1-100:")
#      if int(guess) > num:
#          print " your number is too big"
#      elif int(guess) < num:
#          print " Your number is too small"
#      else:
#          print "BINGO !!!"
#          break
##################################################################################
#
# mil = {'a':1, 'b':2, 'c':3}
# print ['a' in mil]
# print mil['a']
# print ['d' in mil]
#
# print mil.get(1)
#
# mil =  {'d':4}
# print mil['b']

#################################################################################


#
#
# ##registration
# name = raw_input("Hi please enter your user name:")
# psw = raw_input("Please enter your password:")
# nick = raw_input("Please enter your nick name:")
# print """*************************************************************
#       Thank you, the registration process has completed !
# *************************************************************"""
# ## enter to the system
# user_check = raw_input("Please enter your user name:")
# psw_check = raw_input("Please enter your password:")
#
# if user_check == name and psw_check == psw:
#     print " you've passed the security check !!! "
# elif user_check != name:
#     print " your user name is incorrect !"
# elif psw_check != psw:
#     print " your password is incorrect !"
# ## nick name question
#     quest = raw_input("Do you want to answer the private question ? (yes/no) ")
#     if quest == "yes":
#         quest2 = raw_input("What is your nick name ? :")
#     if quest2 == nick:
#         print " Right !!!"
#     else:
#         print "Wrong !!!"
#     elif quest == "no":
#         print "Bye Bye !"
#
# data = {}
#
# data.items().append(name,psw)


# def add_name():
#     # global d1
#     print "Enter name"
#     name=raw_input()
#     print "Enter password"
#     psw=raw_input()
#     d1[name]=psw
#
# d1 = {}
# while 1:
#      print "Type name to search"
#      print "Type 'add' to add names or 'quit' to exit:"
#      x=raw_input()
#      if x=='quit':
#           break
#      if x in d1.keys():
#           print d1[x], x
#      if x=='add':
#           add_name()
#################################################################################
#
# str = [1,4,7,9]
#
# print str
# print max(str)      #print the higher number in the arr
# print min(str)      #PRINT THE LOWER NUMBER IN THE ARR.
#
################################################################################
# # counting how many times each letter appears in the arr
#
# from collections import Counter
#
# arr = ['a', 'a', 'a', 'b', 'c', 'b', 'a', 'c','d','c']
# dict = Counter(arr)
# print dict.items()

##################################################################################
# """
# Count how many letters in a word
# and print them sorted, using a Counter
# """
#
# from collections import Counter   #Counter it a fumction that count how many letters appers in a word or sentece
#
# print "Please type in a word"
# word = raw_input()
#
# freq = Counter(word)
#
# print freq
#
# for k in sorted(freq, key=freq.get, reverse=True):      #loop that runing and print how mant times each letter appers sorted ( like counter but different)
#     print "%s => %d" % (k, freq[k])
# ##################################################################################

# # function that reverse string:
#
# def rev(word):
#     return word[::-1]
#
# reverse = rev("1234")
# print reverse
#
# reverse = rev("tomer")
# print reverse
#
#_______________________________________________________________________________________

# # Define a function to return the type of triangle
# def typeOfTriangle(sideOne, sideTwo, sideThree):
#     # Check if both sideOne and sideTwo are equal or sideOne and sideThree are equal
#     if sideOne == sideTwo or sideOne == sideThree:
#         # Now that either sideOne is equal to sideTwo or sideOne = sideThree, we can make an equilateral triangle check by checking if sideTwo and sideThree are equal too
#         if sideTwo == sideThree:
#             # Since all the 3 sides are equal, the triangle is an equilateral triangle
#             return('Equilateral triangle')
#         else:
#             # Not all 3 sides are equal, but 2 sides are equal and hence the triangle is an Isosceles triangle
#             return('Isosceles triangle')
#     elif sideTwo == sideThree:
#             # This executes if sideOne is not equal to both sideTwo and sideThree. Here, if sideTwo and sideThree are equal, the triangle is an Isosceles triangle since two sides are equal
#         return('Isosceles triangle')
#     else:
#         # If no sides are equal, the triangle is a Scalene triangle
#         return('Scalene triangle')
#
# # Declare three sides of a triangle
# sideOne = 10
# sideTwo = 20
# sideThree = 20
# # Declare a variable to store the type of the triangle returned
# triangle = typeOfTriangle(sideOne, sideTwo, sideThree)
# print(triangle)
#
# # Output => Isosceles triangle
#
# _______________________________


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
#___________________________________________________________________________________

value = "abraka"
print(len(value))
#__________________________________________________________________________________
pi = 3.14
print str(pi)

#___________________________________________________________________________________

a=0
while a<10:
    a = a+1
    print a
#_____________________________________________________________________________________

words = ['pu', 'window', 'dog']
for word in words:
    print word, len(word)
##_____________________________________________________________________________________

word1 = raw_input ("Enter first word :")
word2 = raw_input ("Enter second word :")
word3 = raw_input ("Enter third word :")

print "all the words together:" + str(word1) + " " + str(word2) + " " + str(word3)
##_____________________________________________________________________________________


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

# ______________________________________________________________________________


print("Hello !!!")
num = input("please enter number:")
if num > 0:
    print "The number is greater than 0"
elif num ==0:
    print "The num is 0"
else:
    print "the numer is negative"

________________________________________________________________________________
num1 = input ("Enter number 1:")
num2 = input ("Enter number 2:")
num3 = input ("Enter number 3:")

print "your numbers are:" + str(num1) + " "  + str(num2) + " " +  str(num3)

______________________________________________________________________________

value = "abrakadabra"
print(len(value))
________________________________________________________________________________
a=0
while a<10:
    a = a+1
    print a
__________________________________________________________________________________
words = ['pu', 'window', 'dog']
for word in words:
    print word, len(word)
_____________________________________________________________________________________
word1 = raw_input ("Enter first word :")
word2 = raw_input ("Enter second word :")
word3 = raw_input ("Enter third word :")

print "all the words together:" + str(word1) + " " + str(word2) + " " + str(word3)
______________________________________________________________________________________


def sum(num1, num2):
    return num1+num2

x = input ("Enter first number:")
y = input ("Enter second number:")

result = sum(x,y)
print "The result is=" + str(result)
________________________________________________________________________________________

def sum(num1, num2):
    return num1+num2

def min(num1, num2):
    return num1-num2

def mult(num1, num2):
    return num1*num2

def div(num1, num2):
    return num1/num2

num1 = input ("Please enter the first number:")
num2 = input ("Please enter your second number:")
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
______________________________________________________________________________________

num = input ("Please enter number:")
for i in range (1,num):
    for j in range (num,0):
        print (" ")
            for h in range (1,i):
                  print ("X")
                      for g in range (i,h):
                             print ("X")
                             print '\n'
______________________________________________________________________________________

size = int(raw_input("Enter the size: "))
char = raw_input("Enter the character to draw: ")
for i in range(1, size+1):
    print char*i
______________________________________________________________________________________


size = input("Enter the size: ")
for i in range(1, size+1):
    print " " * (size+1) + "X" * i

size = int(raw_input("Enter the size: "))
temp = size-1
for i in range(1, size+1):
    print (" " * temp) + ("X" * (i*2 -1))
    temp = temp-1

______________________________________________________________________________________

size = int(raw_input("Enter the size: "))
temp = size-1
for i in range(1, size+1):
    print (" " * temp) + ("X" * (i*2 -1))
    temp = temp-1
______________________________________________________________________________________

size = int(raw_input("Enter the size: "))
temp = size-1
for i in range(1, size+1):
    print (" " * temp) + ("X" * (i*2 -1))
    temp = temp-1
        for i in range(size+1, 1):
             print (" " * temp) + ("X" * (j*2 -1))
             temp = temp-1
_______________________________________________________________________________________________________________
a = [5, 2, 3, 1, 4]
a.sort()
print a
________________________________________________________________________________________________________________

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
___________________________________________________________________________________________________________________

list = [5, 2, 3, 1, 4, 9, 6, 7, 10, 8]

for j in range(0, len(list)):
    min = 100000
    for i in range(j, len(list)):
        if list[i] < min:
            min = list[i]
            index = i

    temp = list[j]
    list[j] = list[index]
    list[index] = temp


    print min

loop = True
counter = 0

list = []

while (loop == True):
    var = raw_input("Please enter something: ")

    if var != "-1":
      print "you entered", var
      list.append(int(var))
    elif(var == "-1"):
        loop = False


for j in range(0, len(list)):
    min = 100000
    for i in range(j, len(list)):
        if list[i] < min:
            min = list[i]
            index = i

    temp = list[j]
    list[j] = list[index]
    list[index] = temp


    print min



f = open("textfile.txt","w")

str = f.write("This is line for test")

f = open("textfile.txt","r")

contents = f.read()

print contents

print contents.replace("T","3")


str = raw_input("Please enter string: ")
for i in range((len(str)-1), -1, -1):
     print  (str[i]),
______________________________________________________________________________________
import random

should_guessed = random.randint(1,100)
guess = 0
# print should_guessed

while guess != should_guessed:
    guess = input("Please enter your guess: ")
    if guess > should_guessed:
        print "Number too large"
    elif guess < should_guessed:
        print "Number too small"
    else:
        print "Congratulation. You made it!"

----------------------------------------------------------------------
import random

for a in range(0,100):

    rand_num = random.randint(1,1000)
    print rand_num

    if rand_num % 2 == 0 and rand_num % 3 == 0 and rand_num % 10 == 0:
        print "Bingo !"
        break
------------------------------------------------------------------------------

import random

x = random.randint(0, 10)
y = random.randint(0, 10)

print "I have %d dollars and %d cents" % (x,y)


print "Hello World"
n = input("Pick a number, any number: ")
print "Did you know that " + str(n) + " squared is " + str(n * n) + "?"
print "Goodbye"

print("Hello !!!")
num = input("please enter number:")
if num > 0:
    print "The number is greater than 0"
elif num ==0:
    print "The num is 0"
else:
    print "the numer is negative"

________________________________________________________________________________
num1 = input ("Enter number 1:")
num2 = input ("Enter number 2:")
num3 = input ("Enter number 3:")

print "your numbers are:" + str(num1) + " "  + str(num2) + " " +  str(num3)

______________________________________________________________________________

value = "abrakadabra"
print(len(value))
________________________________________________________________________________
a=0
while a<10:
    a = a+1
    print a
__________________________________________________________________________________
words = ['pu', 'window', 'dog']
for word in words:
    print word, len(word)
_____________________________________________________________________________________
word1 = raw_input ("Enter first word :")
word2 = raw_input ("Enter second word :")
word3 = raw_input ("Enter third word :")

print "all the words together:" + str(word1) + " " + str(word2) + " " + str(word3)
______________________________________________________________________________________






def sum(num1, num2):
    return num1+num2

x = input ("Enter first number:")
y = input ("Enter second number:")

result = sum(x,y)
print "The result is=" + str(result)
________________________________________________________________________________________

def sum(num1, num2):
    return num1+num2

def min(num1, num2):
    return num1-num2

def mult(num1, num2):
    return num1*num2

def div(num1, num2):
    return num1/num2

num1 = input ("Please enter the first number:")
num2 = input ("Please enter your second number:")
act = raw_input ("please choose your action: sum, min, mult, div : ")

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
_________________________________________________________________________________________________________



num = input ("Please enter number:")
for i in range (1,num):
    for j in range (num,0):
        print (" ")
            for h in range (1,i):
                  print ("X")
                      for g in range (i,h):
                             print ("X")
                             print '\n'
_________________________________________________________________________________________________________
size = int(raw_input("Enter the size: "))
char = raw_input("Enter the character to draw: ")
for i in range(1, size+1):
    print char*i
_________________________________________________________________________________________________________

size = input("Enter the size: ")
for i in range(1, size+1):
    print " " * (size+1) + "X" * i

size = int(raw_input("Enter the size: "))
temp = size-1
for i in range(1, size+1):
    print (" " * temp) + ("X" * (i*2 -1))
    temp = temp-1

_________________________________________________________________________________________________________

size = int(raw_input("Enter the size: "))
temp = size-1
for i in range(1, size+1):
    print (" " * temp) + ("X" * (i*2 -1))
    temp = temp-1
_________________________________________________________________________________________________________

size = int(raw_input("Enter the size: "))
temp = size-1
for i in range(1, size+1):
    print (" " * temp) + ("X" * (i*2 -1))
    temp = temp-1
        for i in range(size+1, 1):
             print (" " * temp) + ("X" * (j*2 -1))
             temp = temp-1
_________________________________________________________________________________________________________
a = [5, 2, 3, 1, 4]
a.sort()
print a
_________________________________________________________________________________________________________
str = raw_input("Please enter string: ")
for i in range((len(str)-1), -1, -1):
     print  (str[i]),
_________________________________________________________________________________________________________
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
_________________________________________________________________________________________________________

list = [5, 2, 3, 1, 4, 9, 6, 7, 10, 8]

for j in range(0, len(list)):
    min = 100000
    for i in range(j, len(list)):
        if list[i] < min:
            min = list[i]
            index = i

    temp = list[j]
    list[j] = list[index]
    list[index] = temp


    print min
_________________________________________________________________________________________________________

arr = list(5)
print arr

def calc_min (num1, num2):
 if (num1 > num2):
     return num2
else:
     return num1

arr[0] = input("Insert number 1: ")
num2 = input("Insert number 2: ")
num3 = input("Insert number 2: ")
num4 = input("Insert number 2: ")
num5 = input("Insert number 2: ")


arr = []
n = int(raw_input('Enter how many elements you want: '))
for i in range(0, n):
    x = raw_input('Enter the numbers into the array: ')
    arr.append(x)
print(arr)

___
loop = True
counter = 0

list = []

while (loop == True):
    var = raw_input("Please enter number: ")

    if var != "-1":
      print "you entered", var
      list.append(int(var))
    elif(var == "-1"):
        loop = False


for j in range(0, len(list)):
    min = list[j]+1
    for i in range(j, len(list)):
        if list[i] < min:
            min = list[i]
            index = i

    temp = list[j]
    list[j] = list[index]
    list[index] = temp

   print min
________________________________________________________________________

def main():

 # f = open("Tomer.txt","w+")

  #for i in range(10):
  #  f.write("Tomer %d\r\n" % (i+1))

 # f.close()

  f = open("Tomer.txt","r")
  if f.mode == 'r':

    contents = f.read()
    print contents

    contents.find('2')

def check():
    datafile = file('tomer.txt')
    found = False

    for word in datafile:
        if '2' in word:
            found = True
            break
check()
if True:
    print "true"
else:
    print "false"

_________________________________________________________________________________________________________

o = open("tomer","w")
for line in open("tomer"):
   line = line.replace("tomer","oren")
   o.write(line + "\n")
o.close()

#__________________________________________________________________________________________________________
f = open("textfile.txt", "w")

str = f.write("This is line for test")

f = open("textfile.txt", "r")

contents = f.read()

print contents

print contents.replace("T", "3")

create
new
file )named
tttt(
# it's necessary to add permission
# r=read , w=write, a=append, r+ = read+write

my_file = open("tttt.file", "w")
my_file.close()

# To replace the text inside :
my_file = open("tttt.file", "w")

my_file.write("this is test2")
my_file.close()

# To add text to the text inside:

my_file = open("tttt.file", "a")

my_file.write("this is test2")
my_file.close()

# to read from file

# to read from the file
my_file = open("tttt.file", "r")
print my_file.read()
my_file.close()

# to find word(this)in the file and how much times

count =0
my_file = open("tttt.file","r")
for line in my_file:
    if("this" in line):
        count = count + 1

print "the word found " + str(count) + " times "



##############################################################

# run loop from 1-50

For number in range(1,50)
Print number

# run loop from 1-50 with steps of 10

For number in range(1,50,10)
Print number


# run loop from 1-50 and if find the number 20 stop the loop and write "found it"
for number in range(1,50):
    print number
    if number == 20:
        print "found it"
        break
_____________________________________________________________________________________
#enter numbers 1-100 to continue and 100-200 to stop the loop
print ("press 1-100 to continue\n"
      "press 100-200 to exit")

while True:
    number = int(raw_input("inset number: "))
    if number >= 1 and number <= 100:
        print "another loop"
    elif number >100 and number < 200:
        print "stop loop"
        break
    else:
        print "wrong number"
_________________________________________________________________________________
# While loop counting 1 to 50
number=1
while number<51:
    print number
    number=number+1  #it's possible to write this line also: number+=1

__________________________________________________________________________________
# insert number while the number is not 0
number = 1
while number != 0:
    number = int(raw_input("inset number:(to stop click 0):"))
    if number >= 1:
        print "The number bigger than 0"
    elif number < 0:
        print "The number smaller than 0"
print "the number is 0"
________________________________________________________________________________

# list and array
0
1
2
3
4
5
List = [22, 55, 32, 66, 89, 5]
print List

# add number to the List
List.append(465)
print List

# replace the first number to 1
List[0] = 1
print List

# sort the list
List.sort()
print List

# show the index of specific number(f.e 66)
print List.index(66)

# Outup will be: 3 , cause 66 is in the 3 position in the list

# to remove 66 from the List
List.remove(66)

# to show the List Length (6)
# print len(List)

# go over all the port of the list and print it
for port in List:
    print port

    # set arr - this is another type of list(array) that exist in python. this is list that each number can appears ones
    # it means that its impossible add the same number twice –

# set
setlist = {1, 5, 7, 22, 55}
print setlist

# remove from set list
setlist.remove(7)
print setlist

setlist.add(27)
print setlist

# dictionary – another type of lisr(array) that can define list with values.
# A=1, B=2, C=3


dict = {'ssh': 22, 'telnet': 23, 'ftp': 21}
print dict

# print the ssh value
print dict['ssh']

# add value
# dict ['http'] =80


# delete value from dict
# del list['telnet']

# print all keys from dic
print dict.keys()

# print all values from dict
print dict.values()

milon = {'a': 1, 'b': 2, 'c': 3}
print milon
print ['a' in milon]
print milon['a']
print [‘d’ in milon]
print mil.get('a')

output:
{'a': 1, 'b': 2, 'c': 3}
[True]
1
[False]
1

str = [1, 4, 7, 9]

print str
print max(str)  # print the higher number in the arr
print min(str)  # PRINT THE LOWER NUMBER IN THE ARR.

################################################################################
# # counting how many times each letter appears in the arr

from collections import Counter

arr = ['a', 'a', 'a', 'b', 'c', 'b', 'a', 'c', 'd', 'c']
dict = Counter(arr)
print dict.items()

##################################################################################
Count
how
many
letters in a
word
and print them
sorted, using
a
Counter


from collections import Counter   #Counter is a build in function that count how many letters or anything
				    appears in a word or sentence or Arr and list

print "Please type in a word:"
word = raw_input()
freq = Counter(word)
print freq

for k in sorted(freq, key=freq.get, reverse=True):      #loop that running and print
						        how many times each letter
						        appear sorted ( like counter but without the
                                                                                word counter and the {} etc.)
    print "%s => %d" % (k, freq[k])
##################################################################################
Output:
Please type in a word: tttommer
Counter({'t': 3, 'm': 2, 'e': 1, 'r': 1, 'o': 1})

t => 3
m => 2
e => 1
r => 1
o => 1




Write
a
program
that
reads
10
numbers
from

the
user and prints
the
largest
one


max_number = int(raw_input())

for _ in range(9):
    num = int(raw_input())
    if num > max_number:
        max_number = num

print "Max number = %d" % max_number


Sorting Arr

list = [8,2,3,5,7]
print list

index = 0
index2 = 1
val = 0

while index < len(list)-1:
while index < len(list)-1:
    if list[index] > list[index2]:
         val = list[index]
         list[index] = list[index2]
         list[index2] = val

         index += 1
         index2 += 1

print list





______________________________________________________________________________________

###### Enter number, if 2 following numbers equal to the entered number, print true.

# list = [8,2,3,5,7]
# print "Your list is: " + str(list)
#
# num = int(raw_input("Please enter a number: "))
# print num
#
# index = 0
# while index < len(list)-1:
#     if list[index] + list[index+1] == num:
#         print "True"
#         break
#     index += 1

######################################################################################
# sum how much characters in the string
###  ###  a|a|a|b|b|b|c

# str_arr = raw_input("Please enter string: ")
#
# num = 1
# index = 0
#
# while index < len(str_arr)-1:
#     if index+1 == len(str_arr)-1: ## if last character
#           if str_arr[index] == str_arr[index + 1]:
#              num+=1
#              print str_arr[index] + str(num)
#           else:
#              print str_arr[index] + str(num)
#              print str_arr[index+1] + str(1)
#     elif str_arr[index] == str_arr[index+1]:
#         num+= 1
#     else:
#           print str_arr[index] + str(num)
#           num = 1
#     index+= 1
#
# Output:
# Please enter string: rrrffd
# r3
# f2
# d1

######################################################################
# ## enter port number and find if it appears in the file (text.file.txt) with all the ports and if existing print it
# text_file = open ("test.txt","r")
# print text_file.read()
# port = raw_input("For find specific port, Please enter the port number:")
#
# for i in text_file:
#     if port in str(i):
#         print i
#     else:
#         print "Can't find the specific port "
#         break
# text_file.close()
#######################################################################




# # Program to check if a string is palindrome or not
#
# my_str = []
# my_str = raw_input("Enter a string: ")
#
# rev_str = reversed(my_str)
#
# if list(my_str) == list(rev_str):
#    print("It is palindrome")
# else:
#    print("It is not palindrome")
########################################################################
#rr=[]
arr = raw_input("please enter some words:")

for i in range(len(arr)):
print i, arr[i]
########################################################################

1. כתוב סקריפט בפייתון, המבקש מהמשתמש להכניס 3 אורכי צלעות משולש במספרים שלמים (כולל בדיקת הערך הנקלט) ומחזיר כפלט האם מדובר במשולש שווה שוקיים או

# get user input as string
def int_input(prompt):
num = raw_input(prompt)

# check if the input is integer
try:
    num = int(num)
except ValueError as e:
    print "Error: Illegal input: {}"
    exit()

# check if the input is positive or 0 number
if num <= 0:
    print "Error: Negative number or 0:"
    exit()
elif num > 32500:
    print "you can't insert long number"
return num

rib1 = int_input("Enter first rib: ")
rib2 = int_input("Enter second rib: ")
rib3 = int_input("Enter third rib: ")


# find  Equilateral triangle
if ((rib1==rib2) and (rib1+rib2>rib3)) or ((rib2==rib3) and (rib2+rib3>rib1)) or ((rib1==rib3) and (rib1+rib3>rib2)):
print "This is a 'Triangle Equilateral triangle'"

# find  Right triangle (a^ + b^ = c^)
elif ((rib1**2) == (rib2**2) + (rib3**2)) or ((rib2**2) == (rib1**2) + (rib3**2)) or ((rib3**2) == (rib1**2) + (rib2**2)):
print "This is a 'Right triangle'"
else:
print "incorrect data !”
######################################################################################

mul.py
### Luach hakefel   ###

for i in range(1,11):
    for j in range(1,11):
        result = i * j
        print "%4d" % (result),
    print

# ###################################################################
#
####### Bingo choose game     ######
#
# import random
# while True:
#     num = (random.randint(0,10))
#     guess = int(raw_input("Please enter your guess code: "))
#     if guess == num:
#          print " Bingo !!!"
#          break
#     else:
#         continue

#####################################################################


l = [1,2,3]
print l
l.reverse()
print l

#_________________________________________________________________________

num = input ("Please enter number:")

for i in range (1,num):
    for j in range (num,0):
        print (" ")
            for h in range (1,i):
                 print ("X")
                      for g in range (i,h):
                         print ("X")
                         print '\n'
#_____________________________________________________________________________



for i in range(1,10):
    for j in range(1,10):
        result = i * j
        print "%4d" % (result),
    print

print "Hello World"
n = input("Pick a number, any number: ")
print "Did you know that " + str(n) + " squared is " + str(n * n) + "?"
print "Goodbye"


print("Hello !!!")
num = input("please enter number:")
if num > 0:
    print "The number is greater than 0"
elif num ==0:
    print "The num is 0"
else:
    print "the numer is negative"

________________________________________________________________________________
num1 = input ("Enter number 1:")
num2 = input ("Enter number 2:")
num3 = input ("Enter number 3:")

print "your numbers are:" + str(num1) + " "  + str(num2) + " " +  str(num3)

______________________________________________________________________________

value = "abrakadabra"
print(len(value))
________________________________________________________________________________
a=0
while a<10:
    a = a+1
    print a
__________________________________________________________________________________
words = ['pu', 'window', 'dog']
for word in words:
    print word, len(word)
_____________________________________________________________________________________
word1 = raw_input ("Enter first word :")
word2 = raw_input ("Enter second word :")
word3 = raw_input ("Enter third word :")

print "all the words together:" + str(word1) + " " + str(word2) + " " + str(word3)
______________________________________________________________________________________


def sum(num1, num2):
    return num1+num2

x = input ("Enter first number:")
y = input ("Enter second number:")

result = sum(x,y)
print "The result is=" + str(result)
________________________________________________________________________________________

def sum(num1, num2):
    return num1+num2

def min(num1, num2):
    return num1-num2

def mult(num1, num2):
    return num1*num2

def div(num1, num2):
    return num1/num2

num1 = input ("Please enter the first number:")
num2 = input ("Please enter your second number:")
act = raw_input ("please choose your action: sum, min, mult, div : ")

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
_________________________________________________________________________________________________________



num = input ("Please enter number:")
for i in range (1,num):
    for j in range (num,0):
        print (" ")
            for h in range (1,i):
                  print ("X")
                      for g in range (i,h):
                             print ("X")
                             print '\n'
_________________________________________________________________________________________________________
size = int(raw_input("Enter the size: "))
char = raw_input("Enter the character to draw: ")
for i in range(1, size+1):
    print char*i
_________________________________________________________________________________________________________

size = input("Enter the size: ")
for i in range(1, size+1):
    print " " * (size+1) + "X" * i

size = int(raw_input("Enter the size: "))
temp = size-1
for i in range(1, size+1):
    print (" " * temp) + ("X" * (i*2 -1))
    temp = temp-1

_________________________________________________________________________________________________________

size = int(raw_input("Enter the size: "))
temp = size-1
for i in range(1, size+1):
    print (" " * temp) + ("X" * (i*2 -1))
    temp = temp-1
_________________________________________________________________________________________________________

size = int(raw_input("Enter the size: "))
temp = size-1
for i in range(1, size+1):
    print (" " * temp) + ("X" * (i*2 -1))
    temp = temp-1
        for i in range(size+1, 1):
             print (" " * temp) + ("X" * (j*2 -1))
             temp = temp-1
_________________________________________________________________________________________________________
a = [5, 2, 3, 1, 4]
a.sort()
print a
_________________________________________________________________________________________________________
str = raw_input("Please enter string: ")
for i in range((len(str)-1), -1, -1):
     print  (str[i]),
_________________________________________________________________________________________________________
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
_________________________________________________________________________________________________________

list = [5, 2, 3, 1, 4, 9, 6, 7, 10, 8]

for j in range(0, len(list)):
    min = 100000
    for i in range(j, len(list)):
        if list[i] < min:
            min = list[i]
            index = i

    temp = list[j]
    list[j] = list[index]
    list[index] = temp


    print min
_________________________________________________________________________________________________________

arr = list(5)
print arr

def calc_min (num1, num2):
 if (num1 > num2):
     return num2
else:
     return num1

arr[0] = input("Insert number 1: ")
num2 = input("Insert number 2: ")
num3 = input("Insert number 2: ")
num4 = input("Insert number 2: ")
num5 = input("Insert number 2: ")


arr = []
n = int(raw_input('Enter how many elements you want: '))
for i in range(0, n):
    x = raw_input('Enter the numbers into the array: ')
    arr.append(x)
print(arr)

___
loop = True
counter = 0

list = []

while (loop == True):
    var = raw_input("Please enter number: ")

    if var != "-1":
      print "you entered", var
      list.append(int(var))
    elif(var == "-1"):
        loop = False


for j in range(0, len(list)):
    min = list[j]+1
    for i in range(j, len(list)):
        if list[i] < min:
            min = list[i]
            index = i

    temp = list[j]
    list[j] = list[index]
    list[index] = temp

   print min
________________________________________________________________________

def main():

 # f = open("Tomer.txt","w+")

  #for i in range(10):
  #  f.write("Tomer %d\r\n" % (i+1))

 # f.close()

  f = open("Tomer.txt","r")
  if f.mode == 'r':

    contents = f.read()
    print contents

    contents.find('2')

def check():
    datafile = file('tomer.txt')
    found = False

    for word in datafile:
        if '2' in word:
            found = True
            break
check()
if True:
    print "true"
else:
    print "false"

_________________________________________________________________________________________________________

o = open("tomer","w")
for line in open("tomer"):
   line = line.replace("tomer","oren")
   o.write(line + "\n")
o.close()


f = open("textfile.txt", "w")

str = f.write("This is line for test")

f = open("textfile.txt", "r")

contents = f.read()

print contents

print contents.replace("T", "3")

create
new
file )named
tttt(
# it's necessary to add permission
# r=read , w=write, a=append, r+ = read+write

my_file = open("tttt.file", "w")
my_file.close()

# To replace the text inside :
my_file = open("tttt.file", "w")

my_file.write("this is test2")
my_file.close()

# To add text to the text inside:

my_file = open("tttt.file", "a")

my_file.write("this is test2")
my_file.close()

# to read from file

# to read from the file
my_file = open("tttt.file", "r")
print my_file.read()
my_file.close()

# to find word(this)in the file and how much times

count =0
my_file = open("tttt.file","r")
for line in my_file:
    if("this" in line):
        count = count + 1

print "the word found " + str(count) + " times "



##############################################################

# run loop from 1-50

For number in range(1,50)
Print number

# run loop from 1-50 with steps of 10

For number in range(1,50,10)
Print number


# run loop from 1-50 and if find the number 20 stop the loop and write "found it"
for number in range(1,50):
    print number
    if number == 20:
        print "found it"
        break
_____________________________________________________________________________________
#enter numbers 1-100 to continue and 100-200 to stop the loop
print ("press 1-100 to continue\n"
      "press 100-200 to exit")

while True:
    number = int(raw_input("inset number: "))
    if number >= 1 and number <= 100:
        print "another loop"
    elif number >100 and number < 200:
        print "stop loop"
        break
    else:
        print "wrong number"
_________________________________________________________________________________
# While loop counting 1 to 50
number=1
while number<51:
    print number
    number=number+1  #it's possible to write this line also: number+=1

__________________________________________________________________________________
# insert number while the number is not 0
number = 1
while number != 0:
    number = int(raw_input("inset number:(to stop click 0):"))
    if number >= 1:
        print "The number bigger than 0"
    elif number < 0:
        print "The number smaller than 0"
print "the number is 0"
________________________________________________________________________________

# list and array
0
1
2
3
4
5
List = [22, 55, 32, 66, 89, 5]
print List

# add number to the List
List.append(465)
print List

# replace the first number to 1
List[0] = 1
print List

# sort the list
List.sort()
print List

# show the index of specific number(f.e 66)
print List.index(66)

# Outup will be: 3 , cause 66 is in the 3 position in the list

# to remove 66 from the List
List.remove(66)

# to show the List Length (6)
# print len(List)

# go over all the port of the list and print it
for port in List:
    print port

    # set arr - this is another type of list(array) that exist in python. this is list that each number can appears ones
    # it means that its impossible add the same number twice
# set
setlist = {1, 5, 7, 22, 55}
print setlist

# remove from set list
setlist.remove(7)
print setlist

setlist.add(27)
print setlist

# dictionary – another type of lisr(array) that can define list with values.
# A=1, B=2, C=3


dict = {'ssh': 22, 'telnet': 23, 'ftp': 21}
print dict

# print the ssh value
print dict['ssh']

# add value
# dict ['http'] =80


# delete value from dict
# del list['telnet']

# print all keys from dic
print dict.keys()

# print all values from dict
print dict.values()

milon = {'a': 1, 'b': 2, 'c': 3}
print milon
print ['a' in milon]
print milon['a']
print [‘d’ in milon]
print mil.get('a')

output:
{'a': 1, 'b': 2, 'c': 3}
[True]
1
[False]
1

str = [1, 4, 7, 9]

print str
print max(str)  # print the higher number in the arr
print min(str)  # PRINT THE LOWER NUMBER IN THE ARR.

################################################################################
# # counting how many times each letter appears in the arr

from collections import Counter

arr = ['a', 'a', 'a', 'b', 'c', 'b', 'a', 'c', 'd', 'c']
dict = Counter(arr)
print dict.items()

##################################################################################
Count
how
many
letters in a
word
and print them
sorted, using
a
Counter


from collections import Counter   #Counter is a build in function that count how many letters or anything
				    appears in a word or sentence or Arr and list

print "Please type in a word:"
word = raw_input()
freq = Counter(word)
print freq

for k in sorted(freq, key=freq.get, reverse=True):      #loop that running and print
						        how many times each letter
						        appear sorted ( like counter but without the
                                                                                word counter and the {} etc.)
    print "%s => %d" % (k, freq[k])
##################################################################################
Output:
Please type in a word: tttommer
Counter({'t': 3, 'm': 2, 'e': 1, 'r': 1, 'o': 1})

t => 3
m => 2
e => 1
r => 1
o => 1




Write
a
program
that
reads
10
numbers
from

the
user and prints
the
largest
one


max_number = int(raw_input())

for _ in range(9):
    num = int(raw_input())
    if num > max_number:
        max_number = num

print "Max number = %d" % max_number


###Sorting Arr

list = [8,2,3,5,7]
print list

index = 0
index2 = 1
val = 0

while index < len(list)-1:
while index < len(list)-1:
    if list[index] > list[index2]:
         val = list[index]
         list[index] = list[index2]
         list[index2] = val

         index += 1
         index2 += 1

print list



______________________________________________________________________________________

###### Enter number, if 2 following numbers equal to the entered number, print true.

# list = [8,2,3,5,7]
# print "Your list is: " + str(list)
#
# num = int(raw_input("Please enter a number: "))
# print num
#
# index = 0
# while index < len(list)-1:
#     if list[index] + list[index+1] == num:
#         print "True"
#         break
#     index += 1

######################################################################################
# sum how much characters in the string
###  ###  a|a|a|b|b|b|c

# str_arr = raw_input("Please enter string: ")
#
# num = 1
# index = 0
#
# while index < len(str_arr)-1:
#     if index+1 == len(str_arr)-1: ## if last character
#           if str_arr[index] == str_arr[index + 1]:
#              num+=1
#              print str_arr[index] + str(num)
#           else:
#              print str_arr[index] + str(num)
#              print str_arr[index+1] + str(1)
#     elif str_arr[index] == str_arr[index+1]:
#         num+= 1
#     else:
#           print str_arr[index] + str(num)
#           num = 1
#     index+= 1
#
# Output:
# Please enter string: rrrffd
# r3
# f2
# d1

######################################################################
# ## enter port number and find if it appears in the file (text.file.txt) with all the ports and if existing print it
# text_file = open ("test.txt","r")
# print text_file.read()
# port = raw_input("For find specific port, Please enter the port number:")
#
# for i in text_file:
#     if port in str(i):
#         print i
#     else:
#         print "Can't find the specific port "
#         break
# text_file.close()
#######################################################################




# # Program to check if a string is palindrome or not
#
# my_str = []
# my_str = raw_input("Enter a string: ")
#
# rev_str = reversed(my_str)
#
# if list(my_str) == list(rev_str):
#    print("It is palindrome")
# else:
#    print("It is not palindrome")
########################################################################
arr=[]
arr = raw_input("please enter some words:")

for i in range(len(arr)):
print i, arr[i]
########################################################################


# get user input as string
def int_input(prompt):
num = raw_input(prompt)

# check if the input is integer
try:
    num = int(num)
except ValueError as e:
    print "Error: Illegal input: {}"
    exit()

# check if the input is positive or 0 number
if num <= 0:
    print "Error: Negative number or 0:"
    exit()
elif num > 32500:
    print "you can't insert long number"
return num

rib1 = int_input("Enter first rib: ")
rib2 = int_input("Enter second rib: ")
rib3 = int_input("Enter third rib: ")


# find  Equilateral triangle
if ((rib1==rib2) and (rib1+rib2>rib3)) or ((rib2==rib3) and (rib2+rib3>rib1)) or ((rib1==rib3) and (rib1+rib3>rib2)):
print "This is a 'Triangle Equilateral triangle'"

# find  Right triangle (a^ + b^ = c^)
elif ((rib1**2) == (rib2**2) + (rib3**2)) or ((rib2**2) == (rib1**2) + (rib3**2)) or ((rib3**2) == (rib1**2) + (rib2**2)):
print "This is a 'Right triangle'"
else:
print "incorrect data !”
######################################################################################

mul.py

for i in range(1,11):
    for j in range(1,11):
        result = i * j
        print "%4d" % (result),
    print

# ###################################################################
#
####### Bingo choose game     ######
#
# import random
# while True:
#     num = (random.randint(0,10))
#     guess = int(raw_input("Please enter your guess code: "))
#     if guess == num:
#          print " Bingo !!!"
#          break
#     else:
#         continue

#####################################################################


import random
while True:
    num = (random.randint(0,10))

    guess = int(raw_input("Please enter your guess code(1-10): "))
    if guess < 1 or guess > 10:
        print "Your number is illegal"
    elif guess == num:
          print " Bingo !!!"
          break
    else:
          continue

--------------------------------------------
# mult table
for i in range(1,11):
    for j in range(1,11):
        result = i * j
        print "%4d" % (result),
    print
____________________________________________________

Program to check if a string is palindrome or not

my_str = []
my_str = raw_input("Enter a string: ")

rev_str = reversed(my_str)

if list(my_str) == list(rev_str):
    print("It is palindrome")
else:
    print("It is not palindrome")
_________________________________________________________________

# Bingo choose game

import random
trial = 1

while True:
     num = (random.randint(0,10))
     guess = int(raw_input("Please enter your guess code: "))

     if guess == num:
          print " Bingo !!!"
          #print (" you tried:" + trial)
          break
     elif guess > num:
         print "choose smaller number"
     elif guess < num:
         print "Choose bigger number"
     else:
         continue
#trial = trial + 1
_________________________________________________________________________

# num = input ("Please enter number:")
# for i in range (1,num):
#     for j in range (num,0):
#         print (" x ")
#            for h in range (1,i):
#                print ("X")
#                   for g in range (i,h):
#                      print ("X")
#                      print '\n'
#
#______________________________________________________________

# word = raw_input("please insert a word:")
#
# def rev(word):
#     rv = word[::-1]
#     return rv
#
# print rev(word)

#_______________________________________________________________

# num = input ("Please enter number:")
# for i in range (1,num):
#     for j in range (num,0):
#         print (" x ")
#            for h in range (1,i):
#                print ("X")
#                   for g in range (i,h):
#                      print ("X")
#                      print '\n'
#
#______________________________________________________________

# word = raw_input("please insert a word:")
#
# def rev(word):
#     rv = word[::-1]
#     return rv
#
# print rev(word)
#_______________________________________________________________



n = ["Michael", "Lieberman"]

def join_strings(words):
    result = ""
    for a in words:
        result = result + a

    return result

print join_strings(n)

______________________________________________________

m = [1, 2, 3]
n = [4, 5, 6]

# Add your code here!
def join_lists(m,n):
    return m+n

print join_lists(m, n)
_______________________________________________________

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
    results=[]

print flatten(n)
____________________________________________________________

list_of_lists = [[1, 2, 3], [4, 5, 6]]

for lst in list_of_lists:
  for item in lst:
    print item

___________________________________________________________________


list = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

def flatten(list):
    results = []

    for numbers in list:
        for item in numbers:
            results.append(item)
    print results

flatten(list)
___________________________________________________________________
# print Board of  "O" 5*5

board = []

def print_board(board):
    for x in range(5):
        board= (["O"] * 5)
        print board
    return board

print_board(board)

______________________________________________________________________



board = []

for i in range(5):
  board.append(['O'] * 5)

print board

___________________________________________________________________________

# print Board of  "O" 5*5

board = []

for i in range(5):
    board.append(['O'] * 5)

#print the board

def print_board(board_in):
    for row in board:
        print row

print_board(board)

____________________________________________________________________________

######  BATTLESHIP Game

from random import randint

board = []
for i in range(5):
    board.append(['O'] * 5)

#print the board

def print_board(board_in):
    for row in board:
        print " ".join(row)           # The .join method uses the string to combine the items in the list.

print_board(board)

def random_row(board_in):
    row = randint(0, len(board_in) - 1)
    return row

def random_col(board_in):
    col = randint(0, len(board_in) - 1)
    return col

for turn in range(4):
    print "Turn", turn + 1

    ship_row = random_row(board)
    ship_col = random_col(board)
    print ship_row
    print ship_col

    # Everything from here on should be in your for loop
    # don't forget to properly indent!
    for turn in range(4):
        if turn == 3:
           print "Game Over !", exit()

        print "Turn", turn + 1
        guess_row = int(raw_input("Guess Row: "))
        guess_col = int(raw_input("Guess Col: "))

        if guess_row == ship_row and guess_col == ship_col:
            print "Congratulations! You sank my battleship!"
        else:
            if guess_row not in range(5) or \
                            guess_col not in range(5):
                print "Oops, that's not even in the ocean."
            elif board[guess_row][guess_col] == "X":
                print("You guessed that one already.")
            else:
                print "You missed my battleship!"
                board[guess_row][guess_col] = "X"
            print_board(board)

__________________________________________________________________________________

######  BATTLESHIP Game (option 2)


from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

# Everything from here on should be in your for loop
# don't forget to properly indent!

for turn in range(4):
  print "Turn", turn + 1
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"
    break
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print "Oops, that's not even in the ocean."
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"
    if (turn == 3):
      print "Game Over"
    print_board(board)

___________________________________________________________________________

count = 0

if count < 5:
  print "Hello, I am an if statement and count is", count

while count < 10:
  print "Hello, I am a while and count is", count
  count += 1
___________________________________________________________________________

num = 1

while num < 11:
    res = num ** 2
    print res
    num += 1
________________________________________________________________________________

choice = raw_input('Enjoying the course? (y/n)')

while choice != "y" and choice != "n":
  choice = raw_input("Sorry, I didn't catch that. Enter again: ")
_________________________________________________________________________________


import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
  num = random.randint(1, 6)
  print num
  if num == 5:
    print "Sorry, you lose!"
    break
  count += 1
else:
  print "You win!"

__________________________________________________________________________________

from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)
print random_number

guesses_left = 3

###Start your game!

while guesses_left > 0:
    guess = int(raw_input("Your guess: "))
    guesses_left -= 1
    if guess == random_number:
        print "You win!"
        break
    else:
        print "You lose !"
____________________________________________________________________________________


hobbies = []

for i in range(3):
    hobby = raw_input("Please enter your hobby:")
    hobbies.append(hobby)
print hobbies

______________________________________________________________________________________



phrase = "A bird in the hand..."

for char in phrase:
    if char == "A" or char == "a":
        print "X",
    else:
        print char,'
________________________________________________________________________________________

numbers  = [7, 9, 12, 54, 99]

print "This list contains: "

for num in numbers:
  print num

# Add your loop below!

for n in numbers:
    print n**2
_______________________________________________________________________________

######  Loops on dictionary     #######

d = {'x': 9, 'y': 10, 'z': 20}
for key in d:
  if d[key] == '10':
    print "This dictionary has the value 10!"
________________________________________________________________________________

d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
  # Your code here!
  print key + " " + d[key]
_______________________________________________________________________________

##########      enumerate

choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
  print index+1, item


list_a = [3, 9, 17, 15, 19]
list_b = [2, 11, 8, 18, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):          # zip will create pairs of elements when passed two lists, and will stop at the end of the shorter list. zip can handle three or more lists as well!
    if a > b:
        print a
    else:
        print b
_____________________________________________________________________________________


fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
  if f == 'tomato':
    print 'A tomato is not a fruit!' # (It actually is.)
    break
  print 'A' , f
else:
  print 'A fine selection of fruits!'
________________________________________________________________________________________


arr =[1,2,3,4,5]
for i in arr:
    if i == 2:
        print "Two"
        continue
    print i

else:
    print "END"
____________________________________________________________________________________________


def is_even(x):
    if x % 2 == 0:          # find if the number is even
        return True
    else:
        return False

num = input("Please enter a number:")
is_even(num)

_______________________________________________________________________________________________

x=1

def is_int(x):
    if type(x) == "<type 'int'>":
        return True
    else:
        return False

print is_int(x)



____________________________________________________________________________________________________

### Define a function called is_prime that takes a number x as input and return true if it's primary and false if not

def is_prime(x):
    if x ==1 or x==2:
        return False
    elif x % 2 == 0:
        return False
    else:
        return True

num=1

while (num != 0):
    num = input("please enter a number (1-100):")
    res = is_prime(num)
    print res

print "Thank you very much !!!"
_______________________________________________________________________________________

###  Define a function called reverse that takes a string textand returns that string in reverse. For example: reverse("abcd") should return "dcba".
###  You may not use reversed or [::-1] to help you with this.

def reverse(text):
    result = ""
    index = len(text) - 1
    for i in range(0,len(text)):
        result = result + text[index]
        index = index - 1
    return result

word= raw_input("Please enter any word:")
rev = reverse(word)
print rev
__________________________________________________________________________________________


def anti_vowel(word):
    vow = [ ]
    for i in word:
        if i not in("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
            vow.append(i)
    print"".join(vow)

anti_vowel("Hey look Words!")
___________________________________________________________________________________________

###     The method join() returns a string in which the string elements of sequence have been joined by str separator.

s = " - "
seq = ("a", "b", "c", "1", "2", "3")
print s.join( seq )


###     Output:  a - b - c - 1 - 2 - 3

_____________________________________________________________________________


score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

def scrabble_score(word):
    word = word.lower()
    tot = 0
    for lt in word:
        print score[lt]
        tot += score[lt]
    return tot


print scrabble_score("Helix")
_____________________________________________________________________________________


#   Write a function called censor that takes two strings, text and word, as input. It should return the text with the
#   word you chose replaced with asterisks. For example:  censor("this hack is wack hack", "hack")
#   should return:  "this **** is wack ****"


#def censor(text, word):

alphabet = "a b c d e f g"
data = alphabet.split()         #split string into a list
print data

for temp in data:
    print temp,

print ""
print data[0]
____________________________________________________________________________________________

def censor(text, words):
    textsplited=text.split()
    print text
    lst=[]
    for ch in textsplited:
        if ch==words:
            ch="*"*len(words)
        print ch
        lst.append(ch)
    print lst
    return " ".join(lst)

print censor("this hack is wack hack", "hack")
____________________________________________________________________________________________

def purify(lst):
    res = []
    for ele in lst:
        if ele % 2 == 0:
            res.append(ele)
    return res


s = purify([1,2,3,4,5])
print s
____________________________________________________________________________________________


n=raw_input('How many items do you want to enter in the list :')

while n.isdigit()==False :

    n=raw_input('How many items you want to enter in the list :')

n=int(n)

li=[int(raw_input('Enter your numbers in the list: ')) for i in range(n)]

def product(li):
    pro=li[0]
    for i in range(1,len(li)):
        pro*=li[i]
    return pro

print product(li)
____________________________________________________________________________________________


###  Define a function called product that takes a list of integers as input and returns the product of all of
###  the elements in the list. For example: product([4, 5, 5]) should return 100 (because 4 * 5 * 5 is 100).

def product(list):
  total = 1
  for num in list:
    total = total * num
  return total
____________________________________________________________________________________________________________________


class Point2D():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line2D(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

# Dist -  d**2=(x1-x2)**2+(y1-y2)**2
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


my_test()

__________________________________________________________________________________________


def remove_duplicates(inputlist):
    if inputlist == []:
        return []

    # Sort the input list from low to high
    inputlist = sorted(inputlist)
    # Initialize the output list, and give it the first value of the now-sorted input list
    outputlist = [inputlist[0]]

    # Go through the values of the sorted list and append to the output list
    # ...any values that are greater than the last value of the output list
    for i in inputlist:
        if i > outputlist[-1]:
            outputlist.append(i)

    return outputlist
___________________________________________________________________________________________


grades = [100, 90, 40, 80, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
    for gr in grades:
        print gr

print_grades(grades)

___________________________________________________________________________________________

grades = [100, 90, 40, 80, 85, 70, 90, 65, 90, 85]

def grades_sum(grades):
    sum = 0

    for gr in grades:
        sum = sum + gr
    print sum

grades_sum(grades)
_________________________________________________________________________________________


# find sum and avg of grades

grades = [100, 90, 40, 80, 85, 70, 90, 100, 90, 50.5]

def grades_sum(grades):
  total = 0
  for score in grades:
    total += score
  return total

def grades_average(scores):
    avg = 0
    avg = (grades_sum(grades)/len(grades))
    return avg


print grades_sum(grades)
print grades_average(grades)
____________________________________________________________________________________________


# find sum and avg of grades (option 2)

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


def print_grades(grades_input):
    for grade in grades_input:
        print grade


def grades_sum(scores):
    total = 0
    for score in scores:
        total += score
    return total


def grades_average(grades_input):
    sum_of_grades = grades_sum(grades_input)
    average = sum_of_grades / float(len(grades_input))
    return average

_____________________________________________________________________________________________

# Print out the following:
#
# all of the grades
# sum of grades
# average grade
# variance
# standard deviation

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


def print_grades(grades_input):
    for grade in grades_input:
        print grade


def grades_sum(scores):
    total = 0
    for score in scores:
        total += score
    return total


def grades_average(grades_input):
    sum_of_grades = grades_sum(grades_input)
    average = sum_of_grades / float(len(grades_input))
    return average


def grades_variance(grades):
    variance = 0
    for number in grades:
        variance += (grades_average(grades) - number) ** 2
    return variance / len(grades)


def grades_std_deviation(variance):
    return variance ** 0.5


variance = grades_variance(grades)

for grade in grades:
    print grade
print grades_sum(grades)
print grades_average(grades)
print grades_variance(grades)
print grades_std_deviation(variance)
_________________________________________________________________________________


d = {
  "Name": "Guido",
  "Age": 56,
  "BDFL": True
}
print d.items()             # => [('BDFL', True), ('Age', 56), ('Name', 'Guido')]
print d.keys()
print d.values()

my_dict = {
    "Name": "Tomer",
    "Age": 44,
    "Addr.": "Rehovot"
}

print my_dict.items()
print my_dict.keys()
print my_dict.values()
________________________________________________________________________________________


for number in range(5):
  print number


d = {
  "name": "Eric",
  "age": 26
}

for key in d:
  print key, d[key]

for letter in "Eric":
  print letter

________________________________________________________________________________________

# evens_to_50 = [i for i in range(51) if i % 2 == 0]
# print evens_to_50

# new_list = [x for x in range(1, 6)]
# print new_list
# => [1, 2, 3, 4, 5]

# doubles = [x * 2 for x in range(1, 6)]
# print doubles
# # => [2, 4, 6, 8, 10]
#
doubles_by_3 = [x * 2 for x in range(1, 4) if (x * 2) % 3 == 0]
print doubles_by_3
# # => [6]
_________________________________________________________________________________________

cubes_by_four = [x ** 3 for x in range(1, 11) if ((x ** 3) % 4) == 0]
print cubes_by_four
_________________________________________________________________________________________

to_five = ['A', 'B', 'C', 'D', 'E']

print to_five[3:]         # prints ['D', 'E']

print to_five[:2]        # prints ['A', 'B']

print to_five[::2]       # print ['A', 'C', 'E']

_______________________________________________________________________________________


my_list = range(1, 11)           # List of numbers 1 - 10. Use list slicing to print out every odd element of my_list from start to finish.
print my_list[::2]
______________________________________________________________________________________


# print in reverse order

letters = ['A', 'B', 'C', 'D', 'E']
print letters[::-1]

_______________________________________________________________________________________

my_list = range(1, 11)
print my_list
backwards = my_list[::-1]
print backwards
___________________________________________________________________________________________


to_one_hundred = range(101)                  # reverse from 101-0 in step of 10
backwards_by_tens = to_one_hundred[::-10]
print backwards_by_tens
_____________________________________________________________________________________________


# Create a list, to_21, that's just the numbers from 1 to 21, inclusive.
# Create a second list, odds, that contains only the odd numbers in the to_21 list (1, 3, 5, and so on). Use list slicing for this one instead of a list comprehension.
# Finally, create a third list, middle_third, that's equal to the middle third of to_21, from 8 to 14, inclusive.


to_21 = range(1,22)
odds = to_21[::2]
middle_third = to_21[8:14]

print to_21
print odds
print middle_third
____________________________________________________________________________________________________

######## Lambda:

# my_list = range(16)
# print filter(lambda x: x % 3 == 0, my_list)
#

# # Output:  [0, 3, 6, 9, 12, 15]

______________________________________________________________________________________________________


languages = ["HTML", "JavaScript", "Python", "Ruby"]

# Add arguments to the filter()
print filter(lambda x: x == "Python", languages)

___________________________________________________________________________________________________

movies = {
  "Monty Python and the Holy Grail": "Great",
  "Monty Python's Life of Brian": "Good",
  "Monty Python's Meaning of Life": "Okay"
}

print movies.items()
___________________________________________________________________________________________________


# Use a list comprehension to create a list, threes_and_fives, that consists only of the numbers
# between 1 and 15 (inclusive) that are evenly divisible by 3 or 5.

threes_and_fives = [x for x in range(1, 16) if x % 3 == 0 or x % 5 == 0]
__________________________________________________________________________________________________

# garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
# message = garbled[::-2]
# print message

###     Output:  I am the secret message!

____________________________________________________________________________________________________
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"

message = filter(lambda x: x != "X", garbled)
print message

# Output:  I am another secret message!

_______________________________________________________________________________________________________


##################    paint shapes
import time
import turtle
from easygui import msgbox



def squ():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")  # set the window background color

    move = turtle.Turtle()
    move.color("blue")  # make tess blue
    move.pensize(3)  # set the width of her pen

    for l in range (4):
        move.forward(50)
        move.left(90)

def tri():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")  # set the window background color

    move = turtle.Turtle()
    move.color("blue")  # make tess blue
    move.pensize(3)  # set the width of her pen

    for l in range (3):
        move.forward(200)
        move.left(120)
def cir():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")  # set the window background color

    move = turtle.Turtle()
    move.color("blue")  # make tess blue
    move.pensize(3)  # set the width of her pen

    for l in range (36):
        move.forward(10)
        move.left(10)

def rect():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")  # set the window background color

    move = turtle.Turtle()
    move.color("blue")  # make tess blue
    move.pensize(3)  # set the width of her pen

    for l in range (2):
        move.forward(200)
        move.left(90)
        move.forward(70)
        move.left(90)

choose = int(raw_input("Please choose a shape: 1-rectangle, 2-triangle 3-circle 4-square: "))


if choose == 1:
    rect()
    time.sleep(3)
elif choose == 2:
    tri()
    time.sleep(3)
elif choose == 3:
    cir()
    time.sleep(3)
elif choose == 4:
    squ()
    time.sleep(3)
else:
    print" Poor choice !!!"
##_____________________________________________________________________________________________________


