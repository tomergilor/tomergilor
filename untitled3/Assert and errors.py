"""
x = 2
y = -1

def power(x,y):

    assert x > 0, 'x must be a pos number not {0}'.format(x)
    assert y > 0, 'y must be a pos number not {0}'.format(y)

    return x**y

print power(x,y)


------------------------------------------------------------------------------

def get_age(age):
    assert age > 0, "Age can't be negative"
    print "ok your age is:",age

get_age(-1)
------------------------------------------------------------------------------


### Check if input is integer or not:

try:
    num = int(raw_input("Please enter integer number: "))
    print "your number is integer"
except ValueError:
    print " your number is not integer !"
________________________________________________________________________________


def my_div(num1, num2):
    return float (num1) /  float (num2)

assert
--------------------------------------------------------------------------------
"""



