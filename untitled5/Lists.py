####    How to define a list
####    Syntax to define a list is as follows:
####    listName = [object1, object2, object3]

bestFriends = ['Mark', 'Mary', 'Maria', 'John']

print bestFriends

####  How to access the values in a list ?

print bestFriends[0]        # Mark
print bestFriends[0:2]      #['Mark', 'Mary']

#### Add new element to the list:

bestFriends.append('Febin')
print bestFriends           # ['Mark', 'Mary', 'Maria', 'John', 'Febin']


####    Insert operation is used to add a new element at a specified index and shift
####    the other elements to the right.

bestFriends.insert(1, 'Ben')
print bestFriends               #   ['Mark', 'Ben', 'Mary', 'Maria', 'John', 'Febin']

####    Remove element from list

bestFriends.remove('Mary')
print bestFriends               #   ['Mark', 'Ben', 'Maria', 'John', 'Febin']

####    Sort list
bestFriends.sort()
print bestFriends               #   ['Ben', 'Febin', 'John', 'Maria', 'Mark']

####    Reverse List
bestFriends.reverse()
print bestFriends               #   ['Mark', 'Maria', 'John', 'Febin', 'Ben']

####    Pop - Pop operation is used to return an element at the specified index and remove
####    it from the list.

bestFriends.pop(2)
print bestFriends

