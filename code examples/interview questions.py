# """
# #########################################################################################################################
#
# # # Write a program that prints the numbers from 1 to 100. But for multiples of three, print "Fizz" instead of the number
# # #  and for the multiples of five, print "Buzz".
# # #  For numbers which are multiples of both three and five print "FizzBuzz".
# #
# # def modCald(a, z):
# #     while a < z:
# #         if a % 3 == 0 and a % 5 == 0:
# #             print "FizzBuzz"
# #         elif a % 3 == 0:
# #             print "Fizz"
# #         elif a % 5 == 0:
# #             print "Buzz"
# #         else:
# #             print a
# #         a += 1
# #
# # modCald(1,100)
# # _______________________________________________________________________________________________________________________
#
# # Enter A atring. if the string is palindrome so return True, and if not return False
#
#
# # def reverse_string(word):
# #     #return ''.join(reversed(word))
# #     return word[::-1]
#
# #
# # print reverse_string(word)
# # print reverse_string(word2)
#
#
# # def isPolindrom(word):
# #     reverse = word[::-1]
# #
# #     if word == reverse:
# #         return True
# #     else:
# #         return False
# #
# #
# # word = "abba"
# # word2 = "beauty"
# #
# #
# # if isPolindrom(word2):
# #     print "The word", word , "Is polindrom"
# # else:
# #     print "The word", word, "Is not polindrom"
#
# # _________________________________________________________________________________________________________________
#
# # Enter A number. if the number is palindrome so return True, and if not return False
#
# #
# # def isPolindrom(number):
# #     reverse = str(number[::-1])
# #
# #     if number == reverse:
# #         return True
# #     else:
# #         return False
# #
# #
# # number1 = 12321
# # number2 = 2468
# #
# # if isPolindrom(str(number1)):
# #     print "The number", number1 , "Is polindrom"
# # else:
# #     print "The number", number1 , "Is not polindrom"
#
# #______________________________________________________________________________________________________________
# # # This little program count letters in a string
# #
# # from collections import Counter
# #
# # def getMaxOccuringChar(str):
# #     print Counter(str)
# #
# # getMaxOccuringChar("argentina")
#
# # ___________________________________________________________________________________________________________________
#
# # Consider an array of non negative integers.
# # A second array is formed by shuffling the elements of the first array and deleting
# # random element. Given these two arrays, find which element is missing in the second array.
# # for example: arr1[1,2,3,4,5]
# #              arr2[1,3,4,5]
# # The missing value was 2
# # Try to solve this problem in multiple ways
# ###########
# # option1:
#
#
# # def finder(arr1, arr2):
# #
# #     arr1.sort()
# #     arr2.sort()
# #
# #     for num1,num2 in zip(arr1, arr2):
# #         if num1 != num2:
# #             return num1
# #
# #     return arr1[-1]
# #
# #
# # arr1 = [1,2,3,4,5]
# # arr2 = [1,4,2,5]
# #
# # print finder(arr1,arr2)
# #
# # ##################################
# # # option2: (sum of the 2 arrays):
# #
# #
# # def finder2(arr1, arr2):
# #     return sum(arr1) - sum(arr2)
# #
# # print finder2(arr1,arr2)
#
# #################################################################################################
#
# # # Given a string in the form 'AAAABBBBCCCDDE' compress it to become a 'A4B4C3D2E1'
# # # For this problem you can falsely 'compress' string of single or double letters
# #
# # def compress(s):
# #     run = ""
# #     length = len(s)
# #
# #     if length == 0:
# #         return ""
# #     if length == 1:
# #         return s + "1"
# #
# #     cnt = 1
# #     i = 1
# #
# #     while i < length:
# #         if s[i] == s[i - 1]:
# #             cnt += 1
# #         else:
# #             run = run + s[i - 1] + str(cnt)
# #             cnt = 1
# #
# #         i += 1
# #
# #     run = run + s[i - 1] + str(cnt)
# #     return run
# #
# #
# # print compress('AAAABBC')
# #
# # # Answer : A4B2C1
# # ____________________________________________________________________________________
#
#  # Python program to find number -largest, smallest, second largest and second smallest in a list with complexity O(n)
# #
# # def Range(list1):
# #     largest = list1[0]
# #     largest2 = list1[0]
# #     lowest = list1[0]
# #     lowest2 = list1[0]
# #     for item in list1:
# #         if item > largest:
# #             largest = item
# #         elif largest2 != largest and largest2 < item:
# #             largest2 = item
# #         elif item < lowest:
# #             lowest = item
# #         elif lowest2 != lowest and lowest2 > item:
# #             lowest2 = item
# #
# #     print("Largest element is:", largest)
# #     print("Smallest element is:", lowest)
# #     print("Second Largest element is:", largest2)
# #     print("Second Smallest element is:", lowest2)
# #
# #
# # # Driver Code
# # list1 = [12, 45, 2, 41, 31, 10, 8, 6, 4]
# # Range(list1)
#
# #--------------------------------------------------------
# # # Find the missing number from array of number 1-10
# # i = 1
# # sum10 = 0
# #
# # while i < 11:
# #     sum10 += i
# #     i += 1
# #
# # print sum10
# #
# #
# # list2 = [1,2,3,4,5,6,7,9,10]
# # sum_list =0
# #
# # for num in list2:
# #     sum_list += num
# #
# # print sum_list
# #
# # missNumber = sum10-sum_list # will return the missing number
# #
# # print "The missing number is:", missNumber
# ###################################################################
#
# ###############################################
# # Converting string to int, and int to string:
# ###############################################
#
# # num = 10
# # print "num =" , num
# # print "The type of num is:" , type(num)   ## type int
# # num_str = str(num)              ## convert int to string
# # print "num_str = str(num)       ## convert int to string "
# # print "The type of num_str now, is:", type(num_str)    ## type string
# # num_int = int(num_str)          ## convert string to int
# # print "num_int = int(num_str)   ## convert string to int"
# # print "The type of num_int now, is:", type(num_int)   ## type int
# #
# # ## How to Reverse string:
# #
# # word = "tomer"
# # print word
# # reverse_word = word[::-1]
# # print reverse_word
# #
# # ## Reverse a number
# # num = 12345
# # print num
# # reverse_num = int(str(num)[::-1])  # convert num to string -  (str(num), and then convert again to int  - int(str(num)
# # print reverse_num
#
# ##########################################################################################################################
#
# # ## How to find palindrome number:
# # def isPolindrome(number):
# #     if number  == int(str(number)[::-1]):
# #         print "The number is polidrom"
# #     else:
# #         print "The number is not polidrom"
# #
# #
# # isPolindrome(1234)
# # isPolindrome(2552)
#
# # ##################################################################
# #
# # s = 'Tom Jhons'
# # print "s[:] = ", s[:]
# # print "s[4] = ", s[4]
# # print "s[:4] = ", s[:4]
# # print "s[4:] = ", s[4:]
# # print "s[-1] = ", s[-1]
# # print "s[-7:-3] = ", s[-7:-3]
# # print "s[4:8] = ", s[4:8]
# # print "s[4:8:1] = ", s[4:8:1]
# # print "s[4:8:2] = ", s[4:8:2]
# # print "s.split() = ", s.split()
# #
# # ##################################
# #
# # time = '16:30:10'
# # print "time = " , time
# # hrs, mins, secs = time.split(':')
# # print "hrs = " , hrs
# # print "mins = ", mins
# # print "secs = " , secs
# #
# # ###################################
# #
# # # Reverse array:
# #
# # arr = ["apple", "banana", "candy"]
# # print arr
# # print arr[::-1]     # reverse
# #
# # ###################################################
# # aList = ['c', 'z', 'a', 'b', 'y']
# # aList.sort()
# # print "List : ", aList
#
#
# ###################################################################
# # # Sort array with sort function:
# #
# # arr_num = [2,5,8,4,9]
# # arr_num.sort()
# # print arr_num
# #
#
# #################################################
#
# # # sort without sort func.
# #
# # data_list = [-5, -23, 5, 0, 23, 70, 15, 90]
# # new_list = []
# #
# # while data_list:
# #     minimum = data_list[0]  # arbitrary number in list
# #     for x in data_list:
# #         if x < minimum:
# #             minimum = x
# #     new_list.append(minimum)
# #     data_list.remove(minimum)
# #
# # print new_list
# ###########################################################
# # # sorting with 2 loops:
# #
# # lst = [64, 25, 12, 22, 11, 1,2,44,3,122, 23, 34]
# #
# # for i in range(len(lst)):
# #     for j in range(i + 1, len(lst)):
# #         if lst[i] > lst[j]:
# #             lst[i], lst[j] = lst[j], lst[i]
# #
# # print lst
#
# #######################################################
# # # Sum list total:
# #
# # total = 0
# # for n in [5.99, 12.99, 20.99, 129.99]:
# #         total += n
# #         print 'Total is now', total
# #
# # print total
#
# #########################################################
# # An isogram is a word that has no repeating letters, consecutive or non-consecutive.
# # Implement a function that determines whether a string that contains only letters is an isogram.
# # Assume the empty string is an isogram. Ignore letter case.
# # is_isogram("Dermatoglyphics" ) == true
# # is_isogram("aba" ) == false
# # is_isogram("moOse" ) == false # -- ignore letter case
#
# #
# #string = "asdfgh"
# #
# # def is_isogram(string):
# #     for i in range(len(string)):
# #         for j in range(i + 1, len(string)):
# #             if string[i] == string[j]:
# #                 print "The string is not isogram !"
# #                 exit()
# #
# #     print "The string is isogram !"
# #
# #
# # is_isogram(string)
# #########################################################
#
# # ## Another option si to ise the command 'set'
# #
# # def is_isogram(string):
# #     return len(string) == len(set(string.lower()))
# #
# # print  is_isogram(string)
#
# #######################################################
#
# # # Write func that  count the number of capital letters in a word.
# # # Ans:  Let us first write a multiple line solution and then convert it to one liner code.
# #
# #
# # count = 0
# # text = 'aAdsSsaGsBa'
# #
# # for character in text:
# #
# #     if character.isupper():
# #         count += 1
# #
# # print count
# ########################################################################################
# ###### Sorting Arr
#
# # list = [8,2,3,5,7]
# # print list
# #
# # index = 0
# # index2 = 1
# # val = 0
# #
# # while index < len(list)-1:
# #     while index < len(list)-1:
# #         if list[index] > list[index2]:
# #             val = list[index]
# #             list[index] = list[index2]
# #             list[index2] = val
# #
# #             index += 1
# #             index2 += 1
# #
# # print list
#
# #________________________________________________________________________________________________________________________
#
# ###### Enter number, if 2 folowing numbers equal to the number, print true
#
# # list = [8,2,3,5,7]
# # print "Your list is: " + str(list)
# #
# # num = int(raw_input("Please enter a number: "))
# # print num
# #
# # index = 0
# # while index < len(list)-1:
# #     if list[index] + list[index+1] == num:
# #         print "True"
# #         break
# #     index += 1
#
# ########################################################################################################################
#
# # sum how much charakters in the string
# ###  a|a|a|b|b|c|c
# ###  a|a|a|b|b|b|c
#
# # str_arr = raw_input("Please enter string: ")
# #
# # num = 1
# # index = 0
# #
# # while index < len(str_arr)-1:
# #     if index+1 == len(str_arr)-1: ## if last character
# #           if str_arr[index] == str_arr[index + 1]:
# #              num+=1
# #              print str_arr[index] + str(num)
# #           else:
# #              print str_arr[index] + str(num)
# #              print str_arr[index+1] + str(1)
# #     elif str_arr[index] == str_arr[index+1]:
# #         num+= 1
# #     else:
# #           print str_arr[index] + str(num)
# #           num = 1
# #     index+= 1
# #
# # Output:
# # Please enter string: rrrffd
# # r3
# # f2
# # d1
#
# ######################################################################
# # ## enter port number and find if it appears in the file (text.file.txt) with all the ports and if existing print it
# # text_file = open ("test.txt","r")
# # print text_file.read()
# # port = raw_input("For find specific port, Please enter the port number:")
# #
# # for i in text_file:
# #     if port in str(i):
# #         print i
# #     else:
# #         print "Can't find the specific port "
# #         break
# # text_file.close()
# #######################################################################
# # # Program to check if a string is palindrome or not
# #
# # my_str = []
# #
# # my_str = raw_input("Enter a string: ")
# #
# # rev_str = reversed(my_str)
# #
# # if list(my_str) == list(rev_str):
# #    print("It is palindrome")
# # else:
# #    print("It is not palindrome")
# ########################################################################
# # arr=[]
# # arr = raw_input("please enter some words:")
# #
# # for i in range(len(arr)):
# #     print i, arr[i]
# ######################################################################
# # ## Open browser with url
# #
# # import webbrowser
# #
# # url = 'http://www.python.org/'
# #
# # webbrowser.open_new(url)
# #####################################################################
#
# # def someFunction(a, b):
# #    return (a+b)
# #
# # num1 = int(raw_input("Please enter number 1: "))
# # num2 = int(raw_input("Please enter number 2: "))
# #
# # print "The sum of number 1 + number 2 is:" + str(someFunction(num1,num2))
# #
# #
# ############################################################################
# # while True :
# #     z=0
# #     x = float (raw_input("Please enter your first number: "))
# #     y = float (raw_input("Please enter your first number: "))
# #
# #     try:
# #       z = x/y
# #     except ZeroDivisionError:
# #          print "you can't divide by zero"
# #          exit()
# #
# #     print z
# #
# ################################################################################
# # Test for insert int and not a string:
#
# # string = raw_input("Please enter an int: ")
# # try:
# #     i = int(string)
# #     print i
# # except ValueError:
# #     #Handle the exception
# #     print 'Please enter an integer'
# ################################################################################
#
# # """
# # loop = True
# # counter = 0
# #
# # list = []
# #
# # while (loop == True):
# #     var = raw_input("Please enter something: ")
# #
# #     if var != "-1":
# #        list.append(int(var))
# #     elif(var == "-1"):
# #         loop = False
# #
# # print list
# # =====================================================
# #
# # passwordFile = open('SecretPasswordFile.txt')
# # secretPassword = passwordFile.read()
# # print('Enter your password.')
# # typedPassword = input()
# # if typedPassword == secretPassword:
# #     print('Access granted')
# # if typedPassword == '12345':
# #     print('That password is one that an idiot puts on their luggage.')
# # else:
# #      print('Access denied')
# # _________________________________________________________________________
# # # create new file named tttt
# # # it's necessary to add permission
# # # r=read , w=write, a=append, r+ = read+write
# #
# # my_file = open("tttt.file","w")
# # #my_file.close()
# #
# # #to write to the file
# #
# # my_file.write(" this is test")
# # my_file.close()
# # _________________________________________________________________________________
# # #to add(not  replace) to the text
# # my_file = open("tttt.file","a")
# # my_file.write(" this is test2")
# # my_file.close()
# # _________________________________________________________________________________
# # #to read from file
# # my_file = open("tttt.file","r")
# # print my_file.read()
# # my_file.close()
# # _________________________________________________________________________________
# # # to read from the file
# # my_file = open("tttt.file","r")
# # print my_file.read()
# # my_file.close()
# # _________________________________________________________________________________
# # # to find word in the file and how much times
# # count =0
# # my_file = open("tttt.file","r")
# # for line in my_file:
# #     if("this" in line):
# #         count = count + 1
# #
# # print "the word found " + str(count) + " times "
# #
# # _________________________________________________________________________________
# # # to find any word(this) and print the line it shown
# # my_file = open("tttt.file","r")
# # for line in my_file:
# #     if("this" in line):
# #        print "found",line
# #
# # _________________________________________________________________________________
# # # run loop from 1-50 and if find the number 20 stop the loop and write "found it"
# # for number in range(1,50):
# #     print number
# #     if number == 20:
# #         print "found it"
# #         break
# # _________________________________________________________________________________
# # #enter numbers 1-100 to continue and 100-200 to stop the loop
# # print ("press 1-100 to continue\n"
# #       "press 100-200 to exit")
# #
# # while True:
# #     number = int(raw_input("inset number: "))
# #     if number >= 1 and number <= 100:
# #         print "another loop"
# #     elif number >100 and number < 200:
# #         print "stop loop"
# #         break
# #     else:
# #         print "wrong number"
# # _________________________________________________________________________________
# # # While loop counting 1 to 50
# # number=1
# # while number<51:
# #     print number
# #     number=number+1  #it's possible to write this line also: number+=1
# # _________________________________________________________________________________
# #
# # #insert number while the number is not 0
# # number = 1
# # while number !=0:
# #     number = int(raw_input("inset number:(to stop click 0):"))
# #     if number >= 1:
# #         print "The number bigger than 0"
# #     elif number < 0:
# #         print "The number smaller than 0"
# # print "the number is 0"
# # _________________________________________________________________________
# #
# # # list and array
# # List = [22,55,32,66,89,5]
# # print List
# #
# # #add number to the List
# # List.append(465)
# # print List
# #
# # # replace the first number to 1
# # List [0] = 1
# # print List
# #
# # #sort the list
# # List.sort()
# # print List
# #
# # #show the index of specific number
# # print List.index(66)
# #
# # List = [22,55,32,66,89,5]
# # print List
# #
# # #remove number 66 fron the list
# # List.remove(66)
# #
# # #to show the List Length (6)
# # print len(List)
# #
# # #go over all the port of the list
# # for port in List:
# #     print port
# #
# # # set arr - this is another type of list(array) that exist in python. this is list that each number can appears ones
# # #it means that its impossible add the same number twice
# # #set
# #
# # setlist = {1,5,7,22,55}
# # print setlist
# #
# # #remove from set list
# # setlist.remove(7)
# # print setlist
# #
# # setlist.add(27)
# # print setlist
# #
# #
# # # dictenary
# # # another type of lisr(array) that can define list with values.
# # # f.e - A=1, B=2, C=3
#
# #
# # dict = {'ssh':22,'telnet':23,'ftp':21}
# # print dict
# #
# # #print the ssh value
# # print dict['ssh']
# #
# # #add value
# # #dict ['http'] =80
# #
# # #delete value from dict
# # #del list['telnet']
# #
# # #print all keys from dic
# # print dict.keys()
# #
# # #print all values from dict
# # print dict.values()
# #
# ############################################################################
#
# #Function: example for add and min functions with user input
#
# # def add(num1,num2):
# #     add=num1+num2
# #     return add
# #
# # def min(num1,num2):
# #     min=num1-num2
# #     return min
# #
# #
# # #use the functions with input from the user
# # act = int(raw_input(" Please choose sum or min (1-for add and 2-for min: "))
# # if act == 1:
# #     num1 = int(raw_input("Please enter the first number: "))
# #     num2 = int(raw_input("Please enter the second number: "))
# #     sum = add(num1,num2)
# #     print "The sum is: %d "% (sum)
# #
# # elif act==2:
# #     num1 = int(raw_input("Please enter the first number: "))
# #     num2 = int(raw_input("Please enter the second number: "))
# #     sum = min(num1,num2)
# #     print "The sum is: %d"% (sum)
# ###################################################################################
#
# # program that input from the user 10 numbers and calc and print the biggest number:
# #
# # str_num = []
# # k = 1
# # max = 0
# #
# # for i in range(0,10):
# #     num = int(raw_input("Please enter a number: "))
# #
# #     str_num.append(int(num))
# #
# # for j in range(0,10):
# #
# #     if str_num[j] > str_num[k]:
# #         max = str_num[j]
# #         str_num[j] = str_num[k]
# #         str_num[k] = max
# #
# # print "The biggest number is: %d" %(max)
# #
# ###################################################################################
# # # The program choose 7 numbers randomaly and sum all the numbers. if the sum devided by 7 print also BOOM!
# #
# # from random import randint
# # num = 0
# #
# # list = []
# #
# # for i in range(0,7):
# #     num = num + randint(0, 100)
# #
# # print num
# # if num % 7 == 0:
# #     print "BOOM !"
# ####################################################################################
# # # Program that get rand number and return the sum of the numbers f.e = 34 return 7
# # from random import randint
# # sum=0
# #
# # num = randint(10, 100)
# #
# # num_str = str(num)
# # print num_str
# #
# #
# # for c in num_str:
# #     sum = sum + int(c)
# #
# # print sum
# ########################################################################################
# #
# #
# # Write a program that reads 10 numbers from
# # the user and prints the largest one
# #
# #
# # max_number = int(raw_input("Enter number:"))
# #
# # for X in range(9):
# #     num = int(raw_input("Enter number:"))
# #     if num > max_number:
# #         max_number = num
# #
# # print "Max number = %d" % max_number
# #
# # ######################################################################################
# #
# # """
# # Write a Python program that randomizes 7 numbers
# # and prints their sum total.
# # If the sum is divisable by 7, also print the word "Boom"
# # """
# #
# # from random import randint
# #
# # total = 0
# #
# # for _ in range(7):
# #     num = randint(1,100)
# #     total += num
# #
# # print "Total sum is: %d" % total
# # if total % 7 == 0: print "Boom!"
# #########################################################################################
# """
# Write a program that reads lines from the user until an empty line is inserted.
# After the user typed in an empty line, print all previously inserted lines in reverse
# order (from last to first)
# """
# #
# # text = ""
# #
# # while True:
# #     line = raw_input("Enter text:")
# #     text = line + "\n" + text
# #     if len(line) == 0: break
# #
# # print text
# #
# #
# #
# # number = 0
# # list = []
# # loop = True
# #
# # while (loop == True):
# #     number = raw_input("Please enter a number: ")
# #
# #     if number != "-1":
# #        list.append(int(number))
# #     elif number == "-1":
# #        loop = False
# #
# # print list
# ###############################################################################
# ## Guess a random number from the computer
# # from random import randint
# #
# # num = randint(1,100)
# #
# # while True:
# #      guess = raw_input("Hi, please guess the number between 1-100:")
# #      if int(guess) > num:
# #          print " your number is too big"
# #      elif int(guess) < num:
# #          print " Your number is too small"
# #      else:
# #          print "BINGO !!!"
# #          break
# ##################################################################################
# #
# # mil = {'a':1, 'b':2, 'c':3}
# # print ['a' in mil]
# # print mil['a']
# # print ['d' in mil]
# #
# # print mil.get(1)
# #
# # mil =  {'d':4}
# # print mil['b']
#
# #################################################################################
#
#
# #
# #
# # ##registration
# # name = raw_input("Hi please enter your user name:")
# # psw = raw_input("Please enter your password:")
# # nick = raw_input("Please enter your nick name:")
# # print """*************************************************************
# #       Thank you, the registration process has completed !
# # *************************************************************"""
# # ## enter to the system
# # user_check = raw_input("Please enter your user name:")
# # psw_check = raw_input("Please enter your password:")
# #
# # if user_check == name and psw_check == psw:
# #     print " you've passed the security check !!! "
# # elif user_check != name:
# #     print " your user name is incorrect !"
# # elif psw_check != psw:
# #     print " your password is incorrect !"
# # ## nick name question
# #     quest = raw_input("Do you want to answer the private question ? (yes/no) ")
# #     if quest == "yes":
# #         quest2 = raw_input("What is your nick name ? :")
# #     if quest2 == nick:
# #         print " Right !!!"
# #     else:
# #         print "Wrong !!!"
# #     elif quest == "no":
# #         print "Bye Bye !"
# #
# # data = {}
# #
# # data.items().append(name,psw)
#
#
# # def add_name():
# #     # global d1
# #     print "Enter name"
# #     name=raw_input()
# #     print "Enter password"
# #     psw=raw_input()
# #     d1[name]=psw
# #
# # d1 = {}
# # while 1:
# #      print "Type name to search"
# #      print "Type 'add' to add names or 'quit' to exit:"
# #      x=raw_input()
# #      if x=='quit':
# #           break
# #      if x in d1.keys():
# #           print d1[x], x
# #      if x=='add':
# #           add_name()
# #################################################################################
# #
# # str = [1,4,7,9]
# #
# # print str
# # print max(str)      #print the higher number in the arr
# # print min(str)      #PRINT THE LOWER NUMBER IN THE ARR.
# #
# ################################################################################
# # # counting how many times each letter appears in the arr
# #
# # from collections import Counter
# #
# # arr = ['a', 'a', 'a', 'b', 'c', 'b', 'a', 'c','d','c']
# # dict = Counter(arr)
# # print dict.items()
#
# ##################################################################################
# # """
# # Count how many letters in a word
# # and print them sorted, using a Counter
# # """
# #
# # from collections import Counter   #Counter it a fumction that count how many letters appers in a word or sentece
# #
# # print "Please type in a word"
# # word = raw_input()
# #
# # freq = Counter(word)
# #
# # print freq
# #
# # for k in sorted(freq, key=freq.get, reverse=True):      #loop that runing and print how mant times each letter appers sorted ( like counter but different)
# #     print "%s => %d" % (k, freq[k])
# # ##################################################################################
# #
# # # Build dynamic array. to finish enter -1
# #
# # loop = True
# # counter = 0
# #
# # list = []
# #
# # while (loop == True):
# #     var = raw_input("Please enter something: ")
# #
# #     if var != "-1":
# #       print "you entered", var
# #       list.append(int(var))
# #     elif(var == "-1"):
# #         loop = False
# #
# #
# # for j in range(0, len(list)):
# #     min = 100000
# #     for i in range(j, len(list)):
# #         if list[i] < min:
# #             min = list[i]
# #             index = i
# #
# #     temp = list[j]
# #     list[j] = list[index]
# #     list[index] = temp
# #
# #
# #     print min
# #
# ########################################################################
#
# # # clasic sorting of array
# #
# # list = [5, 2, 3, 1, 4, 9, 6, 7, 10, 8]
# #
# # for j in range(0, len(list)):
# #     min = 100000
# #     for i in range(j, len(list)):
# #         if list[i] < min:
# #             min = list[i]
# #             index = i
# #
# #     temp = list[j]
# #     list[j] = list[index]
# #     list[index] = temp
# #
# #
# #     print min
#
# #########################################################################
#
# ########## Strings   ################
#
# #
# # string = "Python programming is easy"
# #
# # ##### show string
# # print string
# #
# # #### string.upper()
# # print string.upper()
# #
# # ##### string.lower()
# # print string.lower()
# #
# # ##### String.replace("easy", "powerful")
# # print string.replace("easy", "powerful")
# #
# # ##### Slice
# # print string[0:6]
# # print string[2:6]
# # print string[:5]
# # print string[4:]
# #
# # #####  lenght
# # print len(string)
#
# #####       count       ####
#
# # text = "happy birthday"
# #
# # print text.count("a")
# #
# # print text.islower()
# # print text.isupper()
# #
# # text = "tomer"
# # print text.isalpha()
# #
# # text = "13579"
# # print text.isdigit()
# #
# # text = "happy birthday to you"
# # print text.find("t")
# #
# # text = "tomer  "
# # print text.strip()    ### remove space
# #
# # word = "happybirthdaytoyou"
# #
# # print word.index("bir")
# # print word[word.index("bir"):]
# # print word[word.index("hap"):word.index("bir")]
# #
# # ###______________________________________________________________________
# #
# # # get user eamil address
# # email = raw_input("what is you email? ").strip()
# #
# # #slice out user name
# # username = email[:email.index("@")]
# #
# # #slice domain name
# # domain = email[email.index("@")+1 :]
# #
# # #format message
# # output = "Your username is {} and your domain name is {}".format(username,domain)
# # print output
# ##############################################################################
#
# # def helloWorld():
# #     print "Hello, World!"
# #
# # helloWorld()
# #
# #
# # print "________________________________________________________________"
# #
# #
# # def findMaximum (numberOne, numberTwo):
# #     if numberOne > numberTwo:
# #         return numberOne
# #     else:
# #         return numberTwo
# #
# # numberOne = 10
# # numberTwo = 20
# #
# # greaterNumber = findMaximum(numberOne, numberTwo)
# #
# # print greaterNumber
# #
# #
# # print "________________________________________________________________"
# #
# #
# # # Define a function that adds two numbers and returns the result
#
# # def returnSum(numberOne, numberTwo):
# #     return(numberOne + numberTwo)
# #
# # # Declare two numbers
# # numberOne = 10
# # numberTwo = 20
# # # Declare a variable that would store the result of the returned function
# # additionResult = returnSum(numberOne, numberTwo)
# # print(additionResult)
# #
# #
# # print "________________________________________________________________"
# #
# #
# # # Define a function to return the type of triangle
# # def typeOfTriangle(sideOne, sideTwo, sideThree):
# #     # Check if both sideOne and sideTwo are equal or sideOne and sideThree are equal
# #     if sideOne == sideTwo or sideOne == sideThree:
# #         # Now that either sideOne is equal to sideTwo or sideOne = sideThree, we can make an equilateral triangle check by checking if sideTwo and sideThree are equal too
# #         if sideTwo == sideThree:
# #             # Since all the 3 sides are equal, the triangle is an equilateral triangle
# #             return('Equilateral triangle')
# #         else:
# #             # Not all 3 sides are equal, but 2 sides are equal and hence the triangle is an Isosceles triangle
# #             return('Isosceles triangle')
# #     elif sideTwo == sideThree:
# #             # This executes if sideOne is not equal to both sideTwo and sideThree. Here, if sideTwo and sideThree are equal, the triangle is an Isosceles triangle since two sides are equal
# #         return('Isosceles triangle')
# #     else:
# #         # If no sides are equal, the triangle is a Scalene triangle
# #         return('Scalene triangle')
# #
# # # Declare three sides of a triangle
# # sideOne = 10
# # sideTwo = 20
# # sideThree = 20
# # # Declare a variable to store the type of the triangle returned
# # triangle = typeOfTriangle(sideOne, sideTwo, sideThree)
# # print(triangle)
# #
# # # Output => Isosceles triangle
# #
# # ___________________________________________________________________________________________________
#
# # def add(x,y):
# #     return x+y
# #
# # sum = add(5,3)
# # print sum
#
# #________________________________________________________________________________________
#
# # # function that reverse string:
# #
# # def rev(word):
# #     return word[::-1]
# #
# # reverse = rev("1234")
# # print reverse
# #
# # reverse = rev("tomer")
# # print reverse
# #
# #_______________________________________________________________________________________
# # #####################   IF   ###################
# #
# # distance = 100
# #
# # if distance == 100:
# #     print('Distance is 100')
# #
# #
# # #################  IF-Else  #############
# #
# # distance = 200
# #
# # if distance <= 100:
# #     print('Distance is less than or equal to 100')
# # else:
# #     print('Distance is greater than 100')
# #
# #
# # ######################  If-Elif-Else   ##########################
# #
# # distance = 400
# #
# # if distance <= 100:
# #     print('Distance is less than or equal to 100')
# # elif distance <= 200:
# #     print('Distance is less than or equal to 200')
# # elif distance <= 300:
# #     print('Distance is 300')
# # else:
# #     print('Distance is greater than 300')
# #
# # ########    Nested If   ##############
# #
# # distance = 50
# #
# # if distance < 100:
# #     if distance == 50:
# #         print 'Distance is 50'
# #
# #
# # #   Write a program to check if a given number is odd or even
# # #   Even numbers are numbers that are divisible by 2. If the number is not divisible by 2, that's an odd number
# #
# number = 11
#
# if number % 2 is 0:              # if number % 2 = 0 so the number is even(zugi)
#     print('Even number')
# else:
#     print('Odd number')
#
# # Output => Odd number
# #
# #
# #
# # '''
# # Write a program to check if a number is divisible by both 10 as well as 50. If it is
# # divisible by 30 as well, print 'This number is divisible by 10, 50 and 30'. If not, print
# # This number divisible by 10 and 50 but not 30
# # '''
# #
# number = 150
# if number % 10 is 0 and number % 50 is 0:
#     if number % 30 is 0:
#         print('This number is divisible by 10, 50 and 30')
#     else:
#         print('This number is divisible by 10 and 50 but not 30')
#
# ###################################################################################################
# #
# # # Write a program that get 10 positive numbers from the user and prints the largest one
# #
# max_number = 0
#
# for i in range(9):
#     print "Please Enter a number: "
#     num = int(raw_input())
#     if num > max_number:
#         max_number = num
#
# print "max number = %d"% max_number
# ##############################################################################################
#
# # # Write a program that randomize 7 numbers and prints their sum total
# # # if the sum divided by 7, also print the word "boom"
# #
# import random
# sum = 0
#
# for x in range(7):
#   num = random.randint(1,100)
#   print num
#   sum = sum + num
#
# print sum
#
# if sum % 7 == 0:
#     print "BOOM!"
# #########################################################################################
#
# # Write a program that randomizes a number and prints the sum total of its digits.
# # For example if the number was : 2345, the result should be: 14
# # -----------
# # Option 1:
# # -----------
# #
# import random
#
# num = random.randint(100, 100000)
# print num
#
# sum = 0
# num_i = num
#
# while num_i !=0:
#     digit = num_i % 10
#     sum += digit
#     num_i /= 10
#
# print "Total sum of digits =", sum
#
# # #-----------
# # # Option 2:
# # #-----------
# #
# import random
#
# num = random.randint(100, 100000)
# print num
#
# num_str = str(num)          # convert int to string
# total = 0
#
# for digit in num_str:
#     total += int(digit)     # convert back to int for calculate the number
#
# print "Total = ", total
#
# ##############################################################################
# #
# # # Write program that get lines from user until empty line is inserted
# # # After the user typed in an empty line. print all previously
# # # inserted lines in reverse order (from last to first)
# #
# text = ""
#
# while True:
#     print "Insert a line: "
#     line = raw_input()
#     text = line + "\n" + text
#
#     if len(line) == 0: break
#
# print text
#
# ###################################################################################
#
# # Write a program that randomizes integer in a loop until
# # it finds a number that is divided by: 7, 13 and 15
#
# # option 1:
# #----------
#
# import random
# bingo = ""
# num = 0
#
# while bingo != "end":
#     num = random.randint(100, 10000)
#     print num
#     if num % 7 == 0 and num % 13 == 0 and num % 15 == 0:
#         bingo = "end"
#
# print "The number is: " , num
#
#
# # option 2:
# #----------
#
# import random
#
# while True:
#     cand = random.randint(100, 10000)
#
#     if cand % 7 != 0: continue
#     if cand % 13 != 0: continue
#     if cand % 15 != 0: continue
#
#     print "Number is : ", cand
#     break
#
# ##############################################################
# #
# # # Write a program that randomizes 2 numbers and calculate their least
# # # common multiplier, that is the smallest number that is divisable by both.
# # # for example: if the numbers were 4 and 6, program should print 12
#
# import random
#
# num1 = random.randint(1, 10)
# num2 = random.randint(1, 10)
#
# print num1, num2
#
#
# for i in range(1, 10000):
#     if i % num1 is 0 and i % num2 is 0:
#         print "The number is:", i
#         break
#
#
# ##################################################################################
# #
# #
# # Write a program that takes two strings from the user and checks if they represent
# # a valid user name.
# #
# # Valid users and passwords:
# #     apple => red
# #     lettuce => green
# #     lemon => yellow
# #     orange => orange
#
#
# ## Dictionary:
# pwd = {
#     'apple'   : 'red',
#     'lettuce' : 'green',
#     'lemon'   : 'yellow',
#     'orange'  : 'orange',
# }
#
# name = raw_input("Please type in your name: ")
#
# password = raw_input("What's the password? ")
#
# if pwd.has_key(name) and pwd[name] == password:
#     print "Welcome,", name , " !!!"
# else:
#     print "ALERT !!!!!"
#
# print "The items are:\n", pwd.items()
# print "The keys are:\n", pwd.keys()
# print "The values are:\n" , pwd.values()
#
# #############################################################################
#
#
# #Define a list of 20 grades and print only the grades that are above average
#
# grades = [99, 90, 15, 28, 38, 44, 50, 81, 79, 60, 99, 90, 15, 28, 38, 44, 50]
#
# sum_grades = sum(grades)
#
# avg = sum_grades / len(grades)
#
# print "Average is: %d" % avg
#
# for i in grades:
#     if i > avg: print i
#
# ################################################################################
#
#
# # A file named hosts holds hostnames and IP addresses
# # in format: hostname=ip
# # Write a program that reads the file and takes
# # a list of hostnames in sys.argv
# # Program should print the IP addresses of the hosts requested
#
# import sys
#
# hosts = {}
#
# with open("C:\TEST\hosts.txt", "r") as f:
#     for line in f:
#         if not "=" in line: continue
#         (hostname, ip) = line.rstrip().split('=')
#         hosts[hostname] = ip
#
# for hostname in sys.argv[1:]:
#     if hosts.has_key("work"):
#         print "Found: %s => %s" % (hostname, hosts[hostname])
#     else:
#         print "No IP found for %s" % hostname
#
# ##############################################################################
#
# # Use range() and list comprehension to get
# # the list of all lowercase english letters
# # Hint: look for chr() and ord()
#
#
# print [chr(x) for x in range(ord('a'), ord('z')+1)]
#
# #############################################################################
#
# ## Sort array
#
# arr = [3,5,1,9,7]
#
# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#
#         if arr[i] > arr[j]:
#             arr[i], arr[j] = arr[j], arr[i]
#
# print arr
# ##########################################################################
#
# print("Hello !!!")
# num = input("please enter number:")
# if num > 0:
#     print "The number is greater than 0"
# elif num ==0:
#     print "The num is 0"
# else:
#     print "the numer is negative"
#
# ________________________________________________________________________________
# num1 = input ("Enter number 1:")
# num2 = input ("Enter number 2:")
# num3 = input ("Enter number 3:")
#
# print "your numbers are:" + str(num1) + " "  + str(num2) + " " +  str(num3)
#
# ______________________________________________________________________________
#
# value = "abrakadabra"
# print(len(value))
# ________________________________________________________________________________
# a=0
# while a<10:
#     a = a+1
#     print a
# __________________________________________________________________________________
# words = ['pu', 'window', 'dog']
# for word in words:
#     print word, len(word)
# _____________________________________________________________________________________
# word1 = raw_input ("Enter first word :")
# word2 = raw_input ("Enter second word :")
# word3 = raw_input ("Enter third word :")
#
# print "all the words together:" + str(word1) + " " + str(word2) + " " + str(word3)
# ______________________________________________________________________________________
#
#
# def sum(num1, num2):
#     return num1+num2
#
# x = input ("Enter first number:")
# y = input ("Enter second number:")
#
# result = sum(x,y)
# print "The result is=" + str(result)
# ________________________________________________________________________________________
#
# def sum(num1, num2):
#     return num1+num2
#
# def min(num1, num2):
#     return num1-num2
#
# def mult(num1, num2):
#     return num1*num2
#
# def div(num1, num2):
#     return num1/num2
#
# num1 = input ("Please enter the first number:")
# num2 = input ("Please enter your second number:")
# act = raw_input ("please choose your action:sum, min, mult, div : ")
#
# if str(act) == 'sum':
#     result = sum(num1,num2)
#     print "The result is: " + str(result)
# elif str(act) == 'min':
#     result = min(num1,num2)
#     print "The result is: " + str(result)
# elif str(act) == 'mult':
#     result = mult(num1,num2)
#     print "The result is :" + str(result)
# elif str(act) == 'div':
#     result = div(num1,num2)
#     print "The result is: " + str(result)
# ______________________________________________________________________________________
#
# num = input ("Please enter number:")
# for i in range (1,num):
#     for j in range (num,0):
#         print (" ")
#             for h in range (1,i):
#                   print ("X")
#                       for g in range (i,h):
#                              print ("X")
#                              print '\n'
# ______________________________________________________________________________________
#
# size = int(raw_input("Enter the size: "))
# char = raw_input("Enter the character to draw: ")
# for i in range(1, size+1):
#     print char*i
# ______________________________________________________________________________________
#
#
# size = input("Enter the size: ")
# for i in range(1, size+1):
#     print " " * (size+1) + "X" * i
#
# size = int(raw_input("Enter the size: "))
# temp = size-1
# for i in range(1, size+1):
#     print (" " * temp) + ("X" * (i*2 -1))
#     temp = temp-1
#
# ______________________________________________________________________________________
#
# size = int(raw_input("Enter the size: "))
# temp = size-1
# for i in range(1, size+1):
#     print (" " * temp) + ("X" * (i*2 -1))
#     temp = temp-1
# ______________________________________________________________________________________
#
# size = int(raw_input("Enter the size: "))
# temp = size-1
# for i in range(1, size+1):
#     print (" " * temp) + ("X" * (i*2 -1))
#     temp = temp-1
#         for i in range(size+1, 1):
#              print (" " * temp) + ("X" * (j*2 -1))
#              temp = temp-1
# _______________________________________________________________________________________________________________
# a = [5, 2, 3, 1, 4]
# a.sort()
# print a
# ________________________________________________________________________________________________________________
#
# list = [5, 2, 3, 1, 4, 9, 6]
# small = list[0]
# big = list[0]
#
# for i in range(1,len(list)):
#
#  if (list[i] > big):
#     big = list[i]
#  elif (list[i] < small):
#     small = list[i]
# print "The small number is: " + str(small)
# print "The big number is: " + str(big)
# ___________________________________________________________________________________________________________________
#
# list = [5, 2, 3, 1, 4, 9, 6, 7, 10, 8]
#
# for j in range(0, len(list)):
#     min = 100000
#     for i in range(j, len(list)):
#         if list[i] < min:
#             min = list[i]
#             index = i
#
#     temp = list[j]
#     list[j] = list[index]
#     list[index] = temp
#
#
#     print min
#
# loop = True
# counter = 0
#
# list = []
#
# while (loop == True):
#     var = raw_input("Please enter something: ")
#
#     if var != "-1":
#       print "you entered", var
#       list.append(int(var))
#     elif(var == "-1"):
#         loop = False
#
#
# for j in range(0, len(list)):
#     min = 100000
#     for i in range(j, len(list)):
#         if list[i] < min:
#             min = list[i]
#             index = i
#
#     temp = list[j]
#     list[j] = list[index]
#     list[index] = temp
#
#
#     print min
#
#
#
# f = open("textfile.txt","w")
#
# str = f.write("This is line for test")
#
# f = open("textfile.txt","r")
#
# contents = f.read()
#
# print contents
#
# print contents.replace("T","3")
#
#
#
# str = raw_input("Please enter string: ")
#
# for i in range((len(str)-1), -1, -1):
#
#      print  (str[i]),
# ______________________________________________________________________________________

