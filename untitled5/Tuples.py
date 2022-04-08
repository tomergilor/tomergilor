"""
 What is a tuple ?
A tuple is a container that holds many objects under a
single name. A tuple is immutable which means, a tuple once
defined cannot be modified.
"""

dateOfBirth = ('01-01-1900', '31-12-2016')

print dateOfBirth
print dateOfBirth[1]

#### Delete tuple
del(dateOfBirth)


####____________________________________________________________####

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
print(convertedLeapYearTuple)               # Output => (2020, 2024, 2028)
