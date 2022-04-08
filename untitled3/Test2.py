"""
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

"""
l = [1,2,3]
print l
l.reverse()
print l

_________________________________________________________________________

num = input ("Please enter number:")

for i in range (1,num):
    for j in range (num,0):
        print (" ")
            for h in range (1,i):
                 print ("X")
                      for g in range (i,h):
                         print ("X")
                         print '\n'
_____________________________________________________________________________

"""

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
"""










