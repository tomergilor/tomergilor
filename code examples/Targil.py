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
    print "incorrect data !"




