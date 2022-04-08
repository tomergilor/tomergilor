"""
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
_____________________________________________________________________________________________________









