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

########    Nested If   ##############

distance = 50

if distance < 100:
    if distance == 50:
        print 'Distance is 50'


#   Write a program to check if a given number is odd or even
#   Even numbers are numbers that are divisible by 2. If the number is not divisible by 2, that's an odd number

number = 11

if number % 2 is 0:              # if number % 2 = 0 so the number is even(zugi)
    print('Even number')
else:
    print('Odd number')

# Output => Odd number



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


