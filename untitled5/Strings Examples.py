########## Strings   ################


string = "Python programming is easy"

##### show string
print string

#### string.upper()
print string.upper()

##### string.lower()
print string.lower()

##### String.replace("easy", "powerful")
print string.replace("easy", "powerful")

##### Slice
print string[0:6]
print string[2:6]
print string[:5]
print string[4:]

#####  lenght
print len(string)

#####       count       ####

text = "happy birthday"

print text.count("a")

print text.islower()
print text.isupper()

text = "tomer"
print text.isalpha()

text = "13579"
print text.isdigit()

text = "happy birthday to you"
print text.find("t")

text = "tomer  "
print text.strip()    ### remove space

word = "happybirthdaytoyou"

print word.index("bir")
print word[word.index("bir"):]
print word[word.index("hap"):word.index("bir")]

###______________________________________________________________________

# get user eamil address
email = raw_input("what is you email? ").strip()

#slice out user name
username = email[:email.index("@")]

#slice domain name
domain = email[email.index("@")+1 :]

#format message
output = "Your username is {} and your domain name is {}".format(username,domain)
print output

###########################################################

# # Program to check if a string is palindrome or not
#
# my_str = []
#
# my_str = raw_input("Enter a string: ")
#
# rev_str = reversed(my_str)
#
# if list(my_str) == list(rev_str):
#    print("It is palindrome")
# else:
#    print("It is not palindrome")