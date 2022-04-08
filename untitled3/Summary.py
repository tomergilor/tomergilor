"""
#########   Dictionary    ############


######  To set new Dictionary  ########

priceOfCameras = {'sony': 500, 'nikon': 600, 'Canon': 700}

###### To show the dictionary   ######

print priceOfCameras

##### To show the value of Sony key

print priceOfCameras["sony"]

#####  To change the value of Sony

priceOfCameras["sony"] = 800

##### Show the new dictionary  #######

print priceOfCameras

###### To show the Dictionary keys  #######

print priceOfCameras.keys()

###### To show the Dictionary values  #######

print priceOfCameras.values()

##### To copy the dictionary to another dictionary: #####

copyOFPriceOFCameras = priceOfCameras.copy()

##### To show the new Dictionary  ########

print copyOFPriceOFCameras

##### To delete the Sony key/Value from the Dictionary  ########

del priceOfCameras["sony"]

print priceOfCameras

###### To Clear a Dictionary  #######

priceOfCameras.clear()

print priceOfCameras


_______________________________________________________________
#######################		LIST	######################


####    How to define a list
####    Syntax to define a list is as follows:
####    listName = [object1, object2, object3]

bestFriends = ['Mark', 'Mary', 'Maria', 'John']

print bestFriends

####  How to access the values in a list ?

print bestFriends[0]  # Mark

print bestFriends[0:2]  # ['Mark', 'Mary']

#### Add new element to the list:

bestFriends.append('Febin')

print bestFriends  # ['Mark', 'Mary', 'Maria', 'John', 'Febin']

####    Insert operation is used to add a new element at a specified index and shift the other elements to the right.


bestFriends.insert(1, 'Ben')

print bestFriends  # ['Mark', 'Ben', 'Mary', 'Maria', 'John', 'Febin']

####    Remove element from list

bestFriends.remove('Mary')

print bestFriends  # ['Mark', 'Ben', 'Maria', 'John', 'Febin']

####    Sort list

bestFriends.sort()

print bestFriends  # ['Ben', 'Febin', 'John', 'Maria', 'Mark']

####    Reverse List

bestFriends.reverse()

print bestFriends  # ['Mark', 'Maria', 'John', 'Febin', 'Ben']

####    Pop - Pop operation is used to return an element at the specified index and remove it from the list.

bestFriends.pop(2)

print bestFriends


________________________________________________________________

################		Tuples		########

'''
 What is a tuple ?

A tuple is a container that holds many objects under a
single name. A tuple is immutable which means, a tuple once
defined cannot be modified.
'''

dateOfBirth = ('01-01-1900', '31-12-2016')

print dateOfBirth
print dateOfBirth[1]

#### Delete tuple
del (dateOfBirth)

____________________________________________________________

# Create a tuple of 4 elements

leapYear = (2016, 2020, 2024, 2028)
print leapYear

# To convert the tuple into a list, perform a typecasting

leapYearList = list(leapYear)
print leapYear

# Delete first element of list

del leapYearList[0]

# To convert the list to tuple, perform a typecasting

convertedLeapYearTuple = tuple(leapYearList)
print(convertedLeapYearTuple)  # Output => (2020, 2024, 2028)

__________________________________________________________________


################	Functions	#################


# def helloWorld():
#     print "Hello, World!"
#
# helloWorld()
#
#
__________________________________________________________________
#
# def findMaximum (numberOne, numberTwo):
#     if numberOne > numberTwo:
#         return numberOne
#     else:
#         return numberTwo
#
# numberOne = 10
# numberTwo = 20
#
# greaterNumber = findMaximum(numberOne, numberTwo)
#
# print greaterNumber
#
#
__________________________________________________________________
#
#
# # Define a function that adds two numbers and returns the result
# def returnSum(numberOne, numberTwo):
#     return(numberOne + numberTwo)
#
# # Declare two numbers
# numberOne = 10
# numberTwo = 20
# # Declare a variable that would store the result of the returned function
# additionResult = returnSum(numberOne, numberTwo)
# print(additionResult)
#
#
________________________________________________________________
#
#
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
# __________________________________________________________________

# def add(x,y):
#     return x+y
#
# sum = add(5,3)
# print sum

# ________________________________________________________________

#####	function that reverse string:
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
# _________________________________________________________________

# Read the names and marks of at least 3 students
# Rank the top three students with highest marks
# Give cash rewards. $500 for first rank, $300 for second rank, $100 for third rank. Value cannot be modified
# Appreciate students who secured 950 marks and above

import operator


def readStudentDetails():
    print()
    # { 'John': 600, 'Ben': 800, 'David': 950, 'Mark': 980}
    print "Enter the number of students: "
    numberOfStudents = int(input())
    studentRecord = {}
    for student in range(0, numberOfStudents):
        print "Enter the name of the student: "
        name = raw_input()
        print "Enter the marks of students: "
        marks = input()
        studentRecord[name] = marks
    print()
    return studentRecord


def rankStudents(studentRecord):
    try:
        print""
        # [('Mark', 980), ('David', 950), ('Ben', 800), ('John', 600)]
        sortedStudentRecord = sorted(studentRecord.items(), key=operator.itemgetter(1), reverse=True)
        print(sortedStudentRecord)
        print(
        "{} has secured first rank, scoring {} marks".format(sortedStudentRecord[0][0], sortedStudentRecord[0][1]))
        print(
        "{} has secured second rank, scoring {} marks".format(sortedStudentRecord[1][0], sortedStudentRecord[1][1]))
        print(
        "{} has secured third rank, scoring {} marks".format(sortedStudentRecord[2][0], sortedStudentRecord[2][1]))
        print()
        return sortedStudentRecord
    except IndexError:
        print "Enter a minimum of 3 students"
        quit()


def rewardStudents(sortedStudentRecord, reward):
    print""
    print("{} has received a cash reward of ${}".format(sortedStudentRecord[0][0], reward[0]))
    print("{} has received a cash reward of ${}".format(sortedStudentRecord[1][0], reward[1]))
    print("{} has received a cash reward of ${}".format(sortedStudentRecord[2][0], reward[2]))
    print""


def appreciateStudents(sortedStudentRecord):
    print""
    for record in sortedStudentRecord:
        if record[1] >= 950:
            print ("Congratulations on scoring {} marks, {}".format(record[1], record[0]))
        else:
            break
    print""


studentRecord = readStudentDetails()
sortedStudentRecord = rankStudents(studentRecord)
reward = (500, 300, 100)
rewardStudents(sortedStudentRecord, reward)
appreciateStudents(sortedStudentRecord)

_______________________________________________________________

#####################   IF   ###################

distance = 100

if distance == 100:
    print('Distance is 100')

#################  IF-Else  #############

distance = 200

if distance <= 100:
    print('Distance is less than or equal to 100')
else:
    print('Distance is greater than 100')

######################  If-Elif-Else   ##########################

distance = 400

if distance <= 100:
    print('Distance is less than or equal to 100')
elif distance <= 200:
    print('Distance is less than or equal to 200')
elif distance <= 300:
    print('Distance is 300')
else:
    print('Distance is greater than 300')

########    Nested If   ########################################

distance = 50

if distance < 100:
    if distance == 50:
        print 'Distance is 50'

# Write a program to check if a given number is odd or even
#   Even numbers are numbers that are divisible by 2. If the number is not divisible by 2, that's an odd number

number = 11

if number % 2 is 0:  # if number % 2 = 0 so the number is even
    print('Even number')
else:
    print('Odd number')

# Output => Odd number


__________________________________________________________________
'''
Write a program to check if a number is divisible by both 10 as well as 50. If it is
divisible by 30 as well, print 'This number is divisible by 10, 50 and 30'. If not, print
This number divisible by 10 and 50 but not 30
'''

number = 150
if number % 10 is 0 and number % 50 is 0:
    if number % 30 is 0:
        print('This number is divisible by 10, 50 and 30')
    else:
        print('This number is divisible by 10 and 50 but not 30')

_______________________________________________________________
#####################		LOOPS		################



numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print (str(number) + "  "),

________________________________________________________________

##############       While Loop        ############

length = 1

while length <= 3:
    print "Value of length = ", length
    length = length + 1

_______________________________________________________________

outerLoopValue = 1
innerLoopValue = 1

while outerLoopValue <= 2:  ### This inner loop runs three times for every iteration of the outer loop

    while innerLoopValue <= 3:
        print ("Outer loop value = ", outerLoopValue)
        print ("Inner loop value = ", innerLoopValue)

        innerLoopValue = innerLoopValue + 1
        outerLoopValue = outerLoopValue + 1

________________________________________________________________
#######       break:   A break statement is used to stop a loop from further execution."


length = 1

while length > 0:
    if length == 3:
        break
    print ("Length = ", length)
    length = length + 1

________________________________________________________________
print "       Continue:  Continue statement is used to skip a particular iteration of the loop."
print ""

length = 1
while length <= 4:
    if length == 2:
        length = length + 1
        continue
    print ("Length = ", length)
    length = length + 1

_______________________________________________________________

################          ELSE  in loops             ##########



length = 1
while length <= 3:
    if length == 5:
        break
    print ("Length = ", length)
    length = length + 1
else:
    print "Break statement was not executed"

________________________________________________________________

# Numbers that are divisible by just 1 and itself are called prime numbers
# Declare a variable to store an integer number


isPrimeNumber = 3
for number in range(2, isPrimeNumber):
    # Check if 'isPrimeNumber' is divisible by any other number in the range 2 to isPrimeNumber - 1
    if isPrimeNumber % number is 0:
        print('Number is not a prime number.')
        break
# If 'isPrimeNumber' was divisible by no other number, the else corresponding to the for loop gets executed
else:
    print (isPrimeNumber, 'is a prime number')

_________________________________________________________________


###################		CLASS		################


class pound:
    value = 1.00
    color = "gold"
    num_edges = 1
    diameter = 22.5  # mm
    thickness = 3.15  # mm
    heads = True


coin1 = pound()

print coin1.value
print coin1.color

coin1.color = "Green"

coin2 = pound()

print coin2.color
print coin1.color

coin1.value = 2.5

print coin1.value
print coin2.value

__________________________________________________________________

########## 	Strings  	 ################

#
# string = "Python programming is easy"
#
# ##### show string

# print string
#

# #### string.upper()

# print string.upper()
#

# ##### string.lower()

# print string.lower()
#

# ##### String.replace("easy", "powerful")

# print string.replace("easy", "powerful")
#

# ##### Slice

# print string[0:6]
# print string[2:6]
# print string[:5]
# print string[4:]
#

# #####  lenght

# print len(string)

_____________________________________________________________
#####       count       ####

text = "happy birthday"

print text.count("a")

print text.islower()
print text.isupper()

text = "tomer"
print text.isalpha()

text = "13579"
print text.isdigit()

text = "happy birthday to you"
print text.find("t")

text = "tomer  "
print text.strip()  ### remove space

word = "happybirthdaytoyou"

print word.index("bir")
print word[word.index("bir"):]
print word[word.index("hap"):word.index("bir")]

____________________________________________________________

# get user eamil address
email = raw_input("what is you email? ").strip()

# slice out user name
username = email[:email.index("@")]

# slice domain name
domain = email[email.index("@") + 1:]

# format message
output = "Your username is {} and your domain name is {}".format(username, domain)

print output

_________________________________________________________________

wrd = raw_input("Give me a word: ")

pig = wrd[1:] + wrd[0] + "ay"

print(wrd, "in Pig Latin it is:", pig.lower())

________________________________________________________________

###############		Test Chrome with Selenium+Python  #######

from selenium import webdriver

driver = webdriver.Ie()

driver.get("http://www.google.com")

_________________________________________________________________

###############	    Test FF  with Selenium+Python  #######


from selenium import webdriver

driver = webdriver.Firefox()

driver.get("http://www.google.com")

driver.implicitly_wait(10)

driver.close()

__________________________________________
OR:


from selenium import webdriver

driver = webdriver.Firefox()

# save the url to navigate to in a variable

url = 'http://www.w3schools.com/default.asp'

# Navigate to the url

driver.get(url)

_________________________________________________________________












