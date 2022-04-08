"""

def sum_two_or_more_numbers(num1, num2, *args):     #args meaning is that we don't know how many parameters will be recived.
    result = num1 + num2
    for other_num in args:
        result += other_num
    return result

print sum_two_or_more_numbers(1, 2)

print sum_two_or_more_numbers(1, 2, 3, 4, 5)

-------------------------------------------------------------------------------------------------------------------------

def func_with_defaults(x, y=5, z=17):
    return x, y, z


print func_with_defaults(1)

print func_with_defaults(1, 4)

print func_with_defaults(9, 8, 5)
______________________________________________________________________________________________________________________


def book_hotel_room(floor=1, beds=2, **kwargs):
    print 'You ordered a room on floor #%d, with:' % (floor, )
    print ' %d beds' % (beds, )
    for key, value in kwargs.items():
        print ' %d %s' % (value, key)

book_hotel_room(ashtrays=3, toilets=8, windows=2)
-------------------------------------------------------------------------------------

#####   **kwargs     #####

def together(a, b, c=0, *args, **kwargs):
    print a, b, c, args, kwargs


together(1, 2)
together(1, 2, 3)
together(*range(10))
together(1, 2, c=3, d=4, e=5)
together(1, 2, 3, 4, 5, f=6, z=7)7

-------------------------------------------------------------------------------------



def table_things(**kwargs):
    for name, value in kwargs.items():
        print( '{0} = {1}'.format(name, value))

table_things(Apple = 'fruit', Cabbage = 'vegetable', Banana = 'fruit')
________________________________________________________________________________________


def echo_args(*args):
    for arg in args:
        print arg

echo_args(1,2,3)

=========================================================================================


def display_stuff(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print key, '==>', value

display_stuff(name='jetbird', passion='development', language='python')


# output:
# passion ==> development
# name ==> jetbird
# language ==> python

========================================================================================

def one(*args):
    print args

one()                          #output: ()

one(1, 2, 3)                   #output: (1, 2, 3)


def two(x, y, *args):
    print x, y, args

two('a', 'b', 'c')              #output: a b ('c',)

-------------------------------------------------------------------------------------------


def foo(**kwargs):
    print kwargs
foo()                        # output: {}
foo(x=1, y=2, z=3)           # output: {'y': 2, 'x': 1, 'z': 3}

"""
