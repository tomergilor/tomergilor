print "#######             LOOPS           ########"

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print ( str(number) + "  "),


print " "
print " "

print "##############       While Loop        ############ "

length = 1

while length <= 3:
    print "Value of length = ", length
    length = length + 1


print  "_______________________________________________________"

outerLoopValue = 1
innerLoopValue = 1

while outerLoopValue <= 2:      ### This inner loop runs three times for every iteration of the outer loop

    while innerLoopValue <=3:
        print ("Outer loop value = " , outerLoopValue)
        print ("Inner loop value = " , innerLoopValue)

        innerLoopValue = innerLoopValue + 1
        outerLoopValue = outerLoopValue + 1

print "______________________________________________________________________________________________"
print "          break:   A break statement is used to stop a loop from further execution."
print ""

length = 1

while length > 0:
    if length == 3:
        break
    print ("Length = ", length)
    length = length + 1

print "______________________________________________________________________________________________"
print "       Continue:  Continue statement is used to skip a particular iteration of the loop."
print ""

length = 1
while length <= 4:
    if length == 2:
        length = length + 1
        continue
    print ("Length = ", length)
    length = length + 1

print "______________________________________________________________________________________________"
print "       ################          ELSE  in loops       ##################                          "
print ""

length = 1
while length <= 3:
    if length == 5:
        break
    print ("Length = ", length)
    length = length + 1
else:
    print "Break statement was not executed"


print "__________________________________________________________________________________"

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


