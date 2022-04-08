"""

############################        Modules     ######################

_______________________________________________________________________
import random

x = random.randint(0, 10)
y = random.randint(0, 10)

print "I have %d dollars and %d cents" % (x,y)


______________________________________________________________________
from random import randint

x = randint(0, 10)
y = randint(0, 10)

print "I have %d dollars and %d cents" % (x,y)
______________________________________________________________________

##########################      Files       #####################

#######     Read from file:     #######

fin = open("C:\\Users\\Tomer\\Documents\\test\\Docs test\\test text.txt","r")

for line in fin:
    print line

____________________________________________________________________________________


### Last example is an option but the following example is much better and correct:


import sys

with open("C:\\Users\\Tomer\\Documents\\test\\Docs test\\test text.txt", 'r') as f:
    for line in f:
        sys.stdout.write(line)

# No need to close the file because 'with' doing it.
___________________________________________________________________________________


#####  Write to a file    ####

with open("C:\\Users\\Tomer\\Documents\\test\\Docs test\\test text.txt", 'w') as fout:
    fout.write("The End!")
_________________________________________________________________________________________

######  Copy from one file to pther one   #####

with open("C:\\Users\\Tomer\\Documents\\test\\Docs test\\test text.txt", 'r') as fin:
    with open("C:\\Users\\Tomer\\Documents\\test\\Docs test\\test new.txt", 'w') as fout:
        for line in fin:
            fout.write(line)

_________________________________________________________________________________________
###### The glob option return files or folders that match the glob value
###### good to search folders or files from any specific type

import glob
from os import path

with open("C:\\Users\\Tomer\\Documents\\test\\Docs test\\test text.txt", 'r'):
    text_file = glob.glob("*.txt")
    print text_file

_________________________________________________________________________________________


## Write a program that takes 2 files name and append the first file's content to the end of the  second file.

import sys

with open ("C:\\Users\\Tomer\\PycharmProjects\\untitled2\\file1.txt","r") as fin:
    with open("C:\\Users\\Tomer\\PycharmProjects\\untitled2\\file2.txt","a")as fout:
        for line in fin:
            fout.write(line)
______________________________________________________________________________________________________________


## write a program that takes 3 names. The first wto are existing file names and the
## the last is a new file name. program should write the lines from the first two
## files interwinded into the output file.


import itertools
import sys

with open ("C:\\Users\\Tomer\\PycharmProjects\\untitled2\\file1.txt","w") as fin1:
    with open("C:\\Users\\Tomer\\PycharmProjects\\untitled2\\file2.txt","a")as fin2:
        with open("C:\\Users\\Tomer\\PycharmProjects\\untitled2\\file3.txt","r+") as fout:
            for (l1,l2) in itertools.izip_longest(fin1,fin2,fillvalue=""):
                fout.write(l1+l2)

____________________________________________________________________________________________

# search for a string for one file and if exist copy from this word to onoter file

f = open("C:\\Users\\Tomer\\PycharmProjects\\untitled2\\file1.txt")
f1 = open("C:\\Users\\Tomer\\PycharmProjects\\untitled2\\file2.txt","a")

doIHaveToCopyTheLine=False

for line in f.readlines():
  if "If you" in line:
    doIHaveToCopyTheLine=True
  if doIHaveToCopyTheLine:
    f1.write(line)
f1.close()
f.close()

"""
######################################################################
# ## enter port number and find if it appears in the file (text.file.txt) with all the ports and if existing print it
# text_file = open ("test.txt","r")
# print text_file.read()
# port = raw_input("For find specific port, Please enter the port number:")
#
# for i in text_file:
#     if port in str(i):
#         print i
#     else:
#         print "Can't find the specific port "
#         break
# text_file.close()
#######################################################
